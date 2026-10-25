#!/usr/bin/env python3
"""Build the hosted guide without changing the installable offline source."""
import argparse
from html import escape
from pathlib import Path
import re


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    skill = root / 'skills' / 'sdlc-assurance'
    guide = skill / 'assets' / 'lifecycle-guide.html'
    source_base = 'https://github.com/leonardwongly/sdlc-assurance/blob/main/skills/sdlc-assurance/'

    def hosted_reference(match: re.Match) -> str:
        target = (guide.parent / match[1]).resolve()
        if not target.is_relative_to(skill) or not target.is_file():
            raise ValueError(f'Invalid reference: {match[1]}')
        return 'href="' + escape(source_base + target.relative_to(skill).as_posix(), quote=True) + '"'

    html = re.sub(r'href="(\.\./[^"]+)"', hosted_reference, guide.read_text(encoding='utf-8'))
    # Require a fresh destination so unrelated files cannot enter the Pages artifact.
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / 'index.html').write_text(html, encoding='utf-8')
    print('Built index.html from the skill guide with hosted reference links')


if __name__ == '__main__':
    main()
