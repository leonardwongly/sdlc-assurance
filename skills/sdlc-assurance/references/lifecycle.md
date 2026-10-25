# Lifecycle gates and design decisions

Read the sections relevant to the authorized task. Every gate is a decision about a specific scope, candidate, and conditions. A gate cannot expand permission to edit, deploy, message others, spend money, or delete data.

## G0 — Scope

Establish requested mode, user outcome, repository/worktree, baseline state, affected surfaces, constraints, risk tier, exclusions, acceptance owner, and target claim. Inspect existing tests and delivery workflows before proposing replacements. Record consequential unknowns and investigate cheap, reversible uncertainties.

Ground these decisions in project context: users and domain, workflows/content, maturity and current behavior, architecture and dependencies, design system/brand, supported devices and accessibility needs, deployment/operational model, sensitive data, team capacity, budget, and applicable standards. Read the sources that establish these facts; label assumptions and missing context. Scale discovery to the change. A prototype, a maintained internal tool, and a regulated service need different validation, but none may misstate what was observed. For a whole-project audit, inventory all requested surfaces and distinguish reviewed, sampled, excluded, and unreviewed areas.

**Evidence:** Short scope statement; starting revision plus dirty-state description when relevant; affected dependencies/platforms; risk rationale; planned gates. Use an existing issue or design document when possible.

**Advance:** The task can proceed within authority and material ambiguity is resolved or explicitly bounded. Unknowns with reversible experiments may remain as owned investigation tasks. Hold the dependent activity if behavior, data ownership, public contract, or authorization cannot be resolved safely.

## G1 — Intent

Describe observable outcomes before implementation details. For consequential behavior record:

- Requirement ID and acceptance owner; input/preconditions; output and persisted side effects.
- Examples of success, denial/failure, boundary values, and recovery.
- Invariants and forbidden effects: what must never happen, including after partial failure.
- Quality targets with measurement conditions: latency percentile/workload, availability interval, recovery time/data-loss limit, accessibility/platform requirements.
- Risk ID, plausible failure/abuse scenario, consequence, affected users/data, existing controls, uncertainty, and verification method.

Avoid invented universal thresholds. Confirm domain rules and acceptable tradeoffs with an authorized stakeholder when needed. An acceptance rule may itself be wrong; review it independently for H changes.

**Evidence:** Requirement–risk–check mapping, reviewed examples, measurable quality targets, unresolved decisions with owners.

**Advance:** Every in-scope acceptance criterion, consequential risk/control, and mandatory assurance activity has applicable REQUIRED check coverage with an oracle or a valid exception. A planned optional method cannot close a mandatory obligation. Missing coverage/requirements trigger clarification or investigation, not more tests against guessed behavior. Retain approval and rationale when changing agreed coverage or thresholds.

## G2 — Design

Choose the simplest design that satisfies the accepted requirements in the actual project context. Reuse suitable implementation patterns. For UI creation/redesign, read [Custom UI design](custom-ui-design.md) and perform project-specific reimagination of the affected interface; do not use premade page templates or substitute cosmetic restyling for design. Existing accessible components, native controls, design-system tokens, and purposeful product conventions may be reused. Preserve scope: a backend change or typo does not authorize redesigning unrelated UI. For each affected surface, answer the relevant questions and link the answer to a risk/control/check:

| Surface | Design questions | Useful challenge |
|---|---|---|
| Architecture | Where does each rule live? Who owns state? Which dependencies and failure domains are introduced? | Trace one success and one failed operation across boundaries |
| Interfaces | Are types, errors, versioning, compatibility, cancellation, pagination, and idempotency explicit? | Consumer/provider examples and incompatible-version scenarios |
| Data | Which invariants require constraints/transactions? How do precision, time, nulls, retention, and migration work? | Partial writes, duplicates, rollback/roll-forward, old-data examples |
| State/concurrency | Which transitions are allowed? What happens on races, retries, stale callbacks, and restart? | State table, interleaving walkthrough, lost-update/replay scenario |
| Security/privacy | What is trusted? Where are authentication and per-object/tenant authorization enforced? What data may leave or be logged? | Threat model, deny-path walkthrough, confused-deputy and leakage scenarios |
| Failure/recovery | What happens when a dependency times out, a process dies, or resources are exhausted? | Bounded retries/queues, cancellation, degraded behavior, restore procedure |
| UX/accessibility | Can users understand progress, failure, denial, and recovery? Does the task work with required input/assistive modes? | Prototype of actual journey and non-happy-path states |
| Performance/cost | What is the expected workload and limiting resource? Which budgets and growth assumptions matter? | Representative baseline or targeted spike, not speculative optimization |
| Operations | Which user outcomes indicate correctness? Who responds? Can rollout be stopped and state recovered? | Monitoring/runbook walkthrough tied to failure scenarios |
| Testability | Can time/randomness/dependencies be controlled without bypassing production controls? Can effects be observed and fixtures isolated? | Sketch a real-boundary test and a detector sensitivity check |

Record consequential decisions, alternatives considered, chosen tradeoffs, and revisit triggers. Avoid diagrams that only name technologies; show ownership, trust/data flow, state changes, and failure handling. Prototype an uncertain integration before committing to the architecture when execution is within scope; otherwise document the proposed experiment and unvalidated assumption. For critical algorithms/protocols, consider a small executable model or formal analysis; document model assumptions and limitations.

**Evidence:** Relevant contracts/schema/state model, concise architecture or sequence diagram, decision notes, threat/failure scenarios, testability and operational plan. Not every change needs every artifact.

For UI work, also retain the context/brief, chosen task flow and content hierarchy, rationale for custom composition, required state/platform/accessibility coverage, and actual prototype/render observations. A screenshot can demonstrate appearance; it cannot establish functional interaction, persistence, or user acceptance. Do not label unobserved user acceptance as approved.

**Advance:** Identified risks have design controls and feasible validation. A prototype validates only the tested assumption; it does not qualify the implementation for release.

## G3 — Build

Implement focused increments. Preserve unrelated work and compatibility constraints. Use types, constraints, established libraries, clear naming/control flow, and secure defaults. Do not mix unrelated refactoring into a sensitive behavior change. Update relevant documentation with the change.

Run applicable existing formatter/type checker/compiler and static/dependency/secret checks, including mandatory repository checks. Do not require irrelevant build tools for a static-text-only change. Review for correctness, ownership, security boundaries, failure behavior, maintainability, and tests. Match test scope to behavior: isolated rules merit unit/component checks; a data-store behavior requires the real data-store boundary somewhere in the evidence.

For meaningful fixes, retain the original reproduction and demonstrate the regression detector against the defective behavior when practical. Do not introduce a deliberate defect into shared or production state. High-impact logic needs independent challenge; passing build/static checks alone is not runtime proof.

**Evidence:** Cohesive diff, review findings/disposition, executed checks and logs, relevant regression result, dependency/config changes, unresolved issues.

**Advance:** Implementation is integrated within the intended source scope; required G3 checks are credible. Do not call a stub, mock, unconnected module, or written-but-unrun test complete implementation of the feature.

## G4 — Validate

Read [Testing and test assurance](testing-and-test-assurance.md). Execute the selected checks against real boundaries and representative journeys. Include failure and prohibited-effect assertions. Verify the test harness and check the oracle, sensitivity, fidelity, and provenance of critical evidence.

For a user journey, retain preconditions, action sequence, visible result when there is a UI, independent persisted-effect readback where relevant, and safe cleanup. For a service or batch job use requests, records, events, and reconciliation rather than forcing a UI test. Protect test data and secrets.

**Evidence:** Requirement-linked test results, environment/fixture details, observed effects, relevant screenshots/accessibility snapshots or machine-readable records, harness and sensitivity observations, logs/replay seeds, exclusions and failures.

**Advance:** Required checks and dependencies have PASS evidence, or a valid CONDITIONAL decision explicitly permits the dependent action. Reporting a failed/blocked decision does not itself permit progression. Include unresolved acceptance violations discovered by any check and gaps in required coverage. Mocks cannot close a required real-provider check. Missing hardware or credentials remains BLOCKED. Restore baseline only for resources owned by this task; retain evidence before cleanup and treat consequential cleanup failure as an unmet obligation.

## G5 — Qualify release

Bind evidence to a source snapshot, artifact digest, test version, dependencies, configuration, migration state, and relevant environment. Revalidate affected checks after changes. Use the same artifact downstream when the platform permits; otherwise establish and document the build relationship and required rechecks.

Where applicable, verify upgrade from supported prior versions, realistic data migration, interrupted migration, backups and restoration, old/new compatibility, rollout controls, and recovery. Code rollback does not automatically undo writes or schema changes; choose and rehearse a safe rollback or roll-forward strategy.

Define deployment owner, prerequisites, authorization, rollout population/steps, stop thresholds, observation duration, business outcome signals, and incident response. Record residual risks and any authorized exceptions. Apply relevant domain or organizational requirements; this skill does not replace them.

**Evidence:** Candidate manifest, applicable gate record, approved exception records, migration/recovery results, rollout and monitoring/runbook plan.

**Advance:** Applicable G0–G5 obligations and dependencies have valid PASS evidence for the candidate and declared scope. Only this supports unqualified RELEASE_QUALIFIED. An unresolved prerequisite exception makes qualification CONDITIONAL even if candidate tests passed; recheck its conditions before any permitted action. Neither decision is deployment execution or deployment authority. If the request ends at local work, do not run this phase merely to expand the assignment.

## G6 — Observe deployment

Proceed only with deployment authorization for the actual target. Verify target environment, configuration, identity/privileges, artifact digest/version, and migration status. Execute the approved rollout. Observe critical journeys and business outcomes alongside infrastructure health. Use representative canary/control traffic and observation periods when applicable; no traffic is not a successful canary.

Stop or recover according to the agreed conditions. Production fault injection, destructive tests, and synthetic user actions with external effects require their own appropriate authorization. Record changes made during deployment; if they alter assumptions, reopen qualification checks.

**Evidence:** Execution/deployment identifier, target and timestamps, deployed artifact/config identity, smoke/outcome observations, rollout/rollback events, exposure and observation window.

**Advance:** DEPLOYED_OBSERVED is supported only for the named environment, behaviors, and interval. Successful command exit or a deployment dashboard is insufficient to establish user-level success.

## G7 — Operate, evolve, retire

Maintain service objectives, actionable alerts, synthetic journeys, independent reconciliation when needed, ownership, restore drills, and runbooks. Investigate incidents and near misses; identify the missing requirement/control/detector and add the smallest effective regression or structural fix. Reassess dependencies, configuration drift, data shape/scale, permissions, and stale assumptions.

Treat maintenance changes as new increments through applicable gates. Periodically retire unused flags, dead code, obsolete dependencies, and stale exceptions within authorization.

For retirement, identify consumers, retained data and obligations, replacement paths, notifications, credentials/integrations, reversibility, and evidence retention. Migrate and verify consumers first; obtain required authorization before deletion, credential revocation, or external messages. Verify the decommissioned endpoint/job no longer runs and required data remains accessible. Do not delete audit evidence accidentally.

**Evidence:** Operational interval and outcomes, incident actions and verification, restore/reassessment records, or authorized retirement plan and execution evidence.

**Advance:** Report the assessed interval or completed retirement scope. Continuous operation has no permanent PASS asserting future safety.

## Iteration and scheduling

- Front-load uncertain architecture, security, data-loss, and integration risks with small experiments.
- Keep fast deterministic checks on changes. Run more expensive relevant suites at integration/release boundaries or scheduled intervals with explicit freshness rules.
- A scheduled check required for a candidate must still have applicable current evidence before its gate passes.
- Parallelize independent checks when environments and fixtures are isolated. Serialize changes to shared state or allocate separate resources.
- Do not broaden/repeat successful checks without a changed candidate, failure, required gate, or unresolved risk that justifies it.
- Capture evidence incrementally. A final checklist assembled from memory is weaker than execution-linked records.
