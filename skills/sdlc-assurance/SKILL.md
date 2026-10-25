---
name: sdlc-assurance
description: Guide software changes through requirements, design, implementation, risk-based testing, validation of test quality, and evidence-based completion. Use for end-to-end development, substantial fixes, design reviews, validation plans, and release-readiness assessments; scale the workflow to the authorized scope and consequence of failure.
---

# SDLC assurance

Produce software and review conclusions whose claims are supported by relevant, reproducible evidence. Work in small increments. Treat requirements, design, test quality, release qualification, and observed operation as distinct sources of confidence. This skill is not a certification or a guarantee of defect-free software.

## Scope and project context

1. Identify the requested outcome and mode: **plan/design**, **audit/review**, **implement/fix**, **qualify release**, **deploy**, or **operate/retire**. Combine modes only within authorization. A request to review does not authorize editing; a request to implement does not authorize production deployment.
2. Inspect applicable instructions, project documentation, existing architecture, tests, CI, and worktree state using available repository tools. Establish users/domain, critical journeys, product maturity, supported platforms, deployment model, data sensitivity, design system, team/tool constraints, and existing acceptance/operational requirements relevant to the change. Distinguish observed facts from assumptions; do not infer production readiness from a prototype or transfer one project's thresholds/tooling to another. Preserve unrelated changes and reuse appropriate implementation conventions and evidence artifacts.
3. Record scope, explicit exclusions, acceptance criteria, environment, owner, and strongest completion claim being pursued. Resolve material ambiguity about behavior, security, data, or authorization; otherwise state a reasonable assumption and proceed.
4. Classify risk from the highest credible consequence, affected boundaries, reversibility, exposure, and uncertainty. A one-line change can be high risk. Unknown consequential behavior needs investigation, not an invented low rating.
5. Select applicable gates and required checks before implementation. For a trivial reversible edit, an inline scope statement and targeted inspection may suffice. Do not generate a dossier or new tests without a meaningful risk to address.

For whole-project reviews, inventory requested surfaces and mark reviewed, sampled, excluded, and unreviewed coverage. A changed-file review cannot establish an entire-system audit. Record limits of available context; ask only when a missing fact changes material behavior, design, risk, or authority.

## Route to the needed detail

| Need | Resource | When to read |
|---|---|---|
| Plan, design, build, release, operate, retire | [Lifecycle](references/lifecycle.md) | At the first relevant stage; use the applicable sections |
| Create or redesign a user interface | [Custom UI design](references/custom-ui-design.md) | Required for UI creation/redesign; derive the design from project context, never a premade page template |
| Choose tests and test their reliability | [Testing and test assurance](references/testing-and-test-assurance.md) | For changed behavior or validation/test-quality work |
| Decide gates, exceptions, evidence validity, completion language | [Evidence and gates](references/evidence-and-gates.md) | Before evaluating a gate or claiming completion |
| Capture traceability without inventing a new format | [Assurance record](assets/assurance-record.md) | Copy only needed sections into an existing issue/doc or task-owned file |
| Understand a complete concrete example | [Worked example](references/worked-example.md) | When translating requirements into evidence is unclear |
| See stages, risk depth, and claim boundaries | [Visual guide](assets/lifecycle-guide.html) | Open for the user when explaining or planning the workflow |
| Check grounding and domain-specific limits | [Sources](references/sources.md) | When selecting authoritative standards or refreshing guidance |

The visual guide is a reference, not live project status. Do not interpret its selected stage, risk tier, or checklist as execution evidence.

## Risk-based validation depth

| Tier | Typical consequence | Minimum approach |
|---|---|---|
| **L — low** | Reversible presentation/docs change with no business-rule, persistent-data, security, or external-contract impact | Inspect the actual output and affected rendering/build path where relevant; explain why broader checks do not apply |
| **M — standard** | Bounded business behavior, data handling, or API change | Trace acceptance and failures to checks; exercise meaningful real boundaries and a representative journey; assess test quality and regressions |
| **H — high** | Authorization, privacy, payments, destructive migrations, consequential concurrency, infrastructure trust, broad exposure, or difficult recovery | Add independent challenge of requirements/design, relevant adversarial/failure/recovery checks, demonstrated detector sensitivity, and candidate-bound release evidence if release is in scope |

Critical or regulated systems add applicable domain assurance, specialist review, and formal methods where warranted to H. Do not claim compliance without the required domain evidence. Tiers are routing conventions, not numerical probabilities or substitutes for judgment. Select methods by the risks present; H does not mean run every available test type.

## Work through applicable gates

| Gate | Outcome that must be supported |
|---|---|
| **G0 Scope** | Authorized task, initial state, risk tier, unknowns, and intended claim are explicit |
| **G1 Intent** | Requirements, acceptance examples, invariants, and failure risks map to verification methods |
| **G2 Design** | Interfaces, data/state, trust boundaries, failure/recovery, and testability address the identified risks |
| **G3 Build** | Implementation and relevant review/static/component checks support the specified behavior |
| **G4 Validate** | Real-boundary/user-journey checks and risk-selected quality checks support integration; the validation itself is credible |
| **G5 Qualify release** | Evidence binds to the candidate; relevant migration/recovery, rollout, monitoring, and risk disposition are ready |
| **G6 Observe deployment** | An authorized rollout actually occurred and artifact/configuration plus user/business outcomes were observed |
| **G7 Operate/evolve/retire** | Monitoring, restoration, incident learning, reassessment, or authorized retirement is evidenced within a stated interval/scope |

These are iterative decision points, not a waterfall mandate. Several activities can overlap; downstream evidence may reopen an upstream gate. A changed requirement, design, dependency, build, configuration, or data assumption triggers impact analysis and revalidation of affected checks. Preserve original results; do not relabel them as current proof.

Scope gates to the work: a design can be complete at G2; implementation can be complete with scoped G3/G4 evidence while deployment remains out of scope. In a readiness audit, assess relevant gates without implementing or pretending they passed. Mark excluded phases **OUT_OF_SCOPE** at phase level with a reason; this is not a test result.

## Requirements and evidence coverage

For each consequential requirement, maintain:

**Need → requirement ID → risk ID → design control → check ID → observed evidence → bounded claim → operational signal (when relevant).**

Every in-scope acceptance criterion, consequential risk/control, and mandatory repository/domain/skill activity needs applicable REQUIRED check coverage or a valid authorized exception. Keep unmet rows and evidence gaps visible. Specify the oracle (how correctness is determined), expected behavior, forbidden effects, environment, pass threshold, and evidence before execution. Any credible in-scope violation is a gate finding even if discovered by an optional/manual check. Do not downgrade checks, remove requested coverage, or weaken acceptance thresholds without the relevant owner's explicit approval or a valid exception. Technique selection remains proportional; acceptance obligations cannot disappear.

For UI creation/redesign, perform the custom UI reimagination process in the linked reference: derive flows and composition from actual users, content, domain, platform, and existing product constraints. Do not start from premade page/dashboard/landing templates or present restyling one as custom design. Reuse suitable native/accessible components, design tokens, and existing purposeful conventions; custom does not mean rebuilding primitives or changing unrelated screens. The reusable evidence-record template is documentation, not a UI template. Do not claim a named tool ran when this process was performed manually.

Use available specialists or subagents only when authorized and useful. Give them disjoint ownership or an independent challenge with minimal raw context. Independent reviewers should derive expectations from requirements and evidence, not be prompted to agree with the implementer. Multiple agents sharing one mistaken assumption do not constitute independent proof.

## Validate the validation

Before relying on the suite for an affected consequential behavior, check:

- **Oracle:** Expected results come from reviewed rules/examples or a meaningfully independent method, not copied production logic.
- **Sensitivity:** Demonstrate a relevant detector catches a representative defect where warranted: regression fails before the fix, targeted mutation, negative control, or safe fault injection. Run deliberate defects only in isolated non-production state; restore and verify the clean candidate afterward.
- **Assertions:** Check meaningful outputs, persisted effects, events, and prohibited effects, not only return codes, mocked calls, snapshots, or absence of crashes.
- **Harness:** Required tests were discovered and ran; skips, retries, setup failures, time/randomness, isolation, and cleanup are visible. A retry does not erase an earlier failure. Resolve failures with causal/disposition evidence and current revalidation; retain attempt history separately from the current assessment. Deliberate detector experiments are labelled separately from candidate runs.
- **Fidelity:** Record which components are mocked and consequential differences in identity, data, concurrency, platform, permissions, network, and configuration.
- **Provenance:** Results identify the actual source/artifact, tests, environment, inputs, and execution. Preserve accessible raw evidence with sensitive information redacted appropriately.

For H changes, independently challenge critical oracles and demonstrate relevant detector sensitivity unless a valid authorized exception is recorded. If such evidence cannot be obtained, narrow the claim and expose the gap. For L, do not introduce mutation suites or regression tests for a harmless textual change.

## Gate evaluation

Check states are **PASS, FAIL, BLOCKED, NOT_RUN, NOT_APPLICABLE**. Use NOT_APPLICABLE only with a scope/design justification; missing credentials or infrastructure means BLOCKED. A PASS applies only to its observed conditions.

Gate decisions are **PASS, FAIL, BLOCKED, NOT_READY, CONDITIONAL**, with exact rules in [Evidence and gates](references/evidence-and-gates.md). Include missing requirement/risk coverage, all unresolved in-scope findings, evidence validity, and required upstream decisions. Zero applicable required checks cannot yield PASS for an in-scope gate. A prerequisite's CONDITIONAL decision propagates until its gap is resolved. Accepted exceptions retain underlying states, require explicit authorized approval and satisfied current conditions, and never establish a PASS. Hard stops, claim truthfulness, and permission boundaries cannot be waived.

Advance dependent work only on PASS or a valid CONDITIONAL decision within its approved conditions and existing authorization. FAIL, BLOCKED, or NOT_READY holds the dependent progression; continue useful independent authorized work. Gate inspection, safe investigation, and repair may proceed to resolve the unmet criteria.

Do not use test count, coverage percentage, mutation score, reviewer agreement, or a synthesized confidence score as a substitute for risk coverage and credible evidence. A running application is not a completed journey; a completed journey is not proof of every feature; staging is not production.

## Visual reporting

For substantial work, present a compact current-scope map or table using the same G0–G7 labels. Show required checks, unresolved gates, evidence links, and the strongest supported claim. Use explicit text states, arrow labels, and a legend; never rely on color alone. Label hypothetical examples clearly. Do not populate missing evidence with a green default.

Use the bundled visual guide for explanation. If adapting it to a live task, replace illustrative content with observed records and label the candidate/environment and timestamp. Keep the actual evidence record authoritative. A simple Mermaid flow or Markdown matrix is preferable when it fully explains the decision.

## Completion and handoff

Report the outcome, affected surfaces, observed validation, exact environment/candidate, unresolved risks, and next action only where needed. Inspect trusted candidate-bound result artifacts before relying on delegated success reports; queued jobs and green badges alone are not proof. Use plain descriptive language rather than slogans. Use the smallest useful response; link durable evidence when available.

Distinguish **PROPOSED**, **IMPLEMENTED**, **LOCALLY_VERIFIED**, **INTEGRATION_VERIFIED**, **RELEASE_QUALIFIED**, and **DEPLOYED_OBSERVED** according to the claim rules. Name the behaviors covered. Mark conditional outcomes explicitly. Report commits, pushes, merges, deployment, or production validation only if actually performed and verified.

An unqualified task-complete claim requires all requested deliverables, wiring/integration, required validation, and consequential cleanup/handoff obligations to be satisfied. Otherwise report implementation/design work delivered and the precise failed, blocked, pending, provisional, or conditional portion. A verified subset does not complete the larger requested behavior. If an external requirement is blocked, finish independent authorized work, retain the blocked check, and give the precise missing prerequisite. Never silently substitute a weaker environment or imply that an unexecuted plan is proof. Ongoing operation is assessed over a stated interval, never declared permanently safe or complete.
