#!/usr/bin/env python3
"""Validate the distribution and optionally compare an actual installed skill.

This checks packaging, not the correctness of decisions made using the skill.
Requires Python 3.10+; no third-party dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


class GuideLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: list[str] = []
        self.remote_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get('id'):
            self.ids.append(values['id'])
        if tag == 'a' and values.get('href'):
            self.links.append(values['href'])
        if tag in {'script', 'link', 'img', 'iframe'}:
            source = values.get('src') or values.get('href') or ''
            if source.startswith(('https:', 'http:', '//')):
                self.remote_assets.append(source)


def files_and_hashes(folder: Path) -> dict[str, str]:
    return {
        str(path.relative_to(folder)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(folder.rglob('*')) if path.is_file()
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed', type=Path, help='Actual installed sdlc-assurance directory')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    skill = root / 'skills' / 'sdlc-assurance'
    errors: list[str] = []
    required = [
        'SKILL.md', 'agents/openai.yaml', 'references/lifecycle.md',
        'references/custom-ui-design.md', 'references/testing-and-test-assurance.md',
        'references/evidence-and-gates.md', 'references/worked-example.md',
        'references/sources.md', 'assets/assurance-record.md', 'assets/lifecycle-guide.html',
    ]
    for name in required:
        if not (skill / name).is_file():
            errors.append(f'Missing skill file: {name}')
    for name in ['README.md', 'LICENSE']:
        if not (root / name).is_file():
            errors.append(f'Missing repository file: {name}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', entry, re.S)
    if not front or not re.search(r'^name: sdlc-assurance\s*$', front[1], re.M):
        errors.append('Missing or incorrect skill name in frontmatter')
    if not front or not re.search(r'^description: \S.+$', front[1], re.M):
        errors.append('Missing nonempty skill description')

    count = 0

    def check_link(path: Path, target: str) -> None:
        nonlocal count
        parts = urlsplit(target)
        if parts.scheme or target.startswith(('#', '//')):
            return
        count += 1
        resolved = (path.parent / unquote(parts.path)).resolve()
        if not resolved.is_relative_to(root):
            errors.append(f'{path.relative_to(root)} links outside the package: {target}')
        elif not resolved.exists():
            errors.append(f'{path.relative_to(root)} has missing link: {target}')

    markdown = [root / 'README.md', *skill.rglob('*.md')]
    for path in markdown:
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
            check_link(path, target)
        if re.search(r'(?:/Users/|/home/|[A-Z]:\\Users\\)', content):
            errors.append(f'{path.relative_to(root)} contains a machine-specific home path')
    guide = skill / 'assets/lifecycle-guide.html'
    html = GuideLinks()
    html.feed(guide.read_text(encoding='utf-8'))
    for link in html.links:
        check_link(guide, link)
    if len(html.ids) != len(set(html.ids)):
        errors.append('Guide has duplicate static element IDs')
    if html.remote_assets:
        errors.append('Offline guide contains external runtime assets')
    if args.installed:
        installed = args.installed.resolve()
        if not installed.is_dir():
            errors.append(f'Installed skill directory not found: {installed}')
        else:
            expected, actual = files_and_hashes(skill), files_and_hashes(installed)
            missing = sorted(set(expected) - set(actual))
            changed = sorted(name for name in expected.keys() & actual.keys() if expected[name] != actual[name])
            if missing or changed:
                errors.append(f'Installed content mismatch; missing={missing}, changed={changed}')
            else:
                print(f'Installed skill matches all {len(expected)} source files')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Package valid: {len(required)} required skill files, {count} local links')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
