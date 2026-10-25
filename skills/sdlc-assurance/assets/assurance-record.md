# Assurance record — copy only applicable sections

Template only. No result is implied by a blank field or example label. Replace brackets with observed information. Prefer linking existing issue/CI/design artifacts over duplicating them.

## Scope and decision

- Task/mode: [plan, review, implement, qualify, deploy, operate/retire]
- Authorized outcome and target claim: [behavior and environment]
- Starting state: [revision; dirty/untracked changes affecting task]
- Included/excluded surfaces and gates: [reason for each excluded phase]
- Risk tier and rationale: [L/M/H; consequence, exposure, reversibility, uncertainty]
- Owners: [implementation; requirements; independent review; release/risk authority]
- Assumptions/unknowns and resolution: [investigation or explicit bounded assumption]
- Project context: [users/domain, journeys/content, maturity, architecture, platforms, design system, data/operations, constraints; sources vs assumptions]
- Review coverage when relevant: [requested surfaces; reviewed/sampled/excluded/unreviewed; rationale and evidence]

## Requirements, risks, and design

| Requirement ID / acceptance rule | Risk ID / failure and consequence | Design control / decision | Check IDs | Operational signal if relevant |
|---|---|---|---|---|
| [REQ-…] | [RISK-…] | [control and design reference] | [CHK-…] | [signal or justified omission] |

Record examples, invariants, forbidden effects, contracts/state/data/trust boundaries, quality targets with workload/conditions, alternatives and tradeoffs. Attach diagrams only where they clarify a real decision.

For UI creation/redesign, follow references/custom-ui-design.md. Record context and brief, custom task flow/composition rationale, reused accessible primitives/conventions, required states/platforms, and prototype/interaction observations. Do not use premade page templates. This document is an evidence-record template, not a product UI template.

## Planned checks and applicability

Keep unmet checks in this table. Applicability is a design/scope decision; unavailable prerequisites are BLOCKED. Mark required/optional before execution. Record hard stops from governing policy. Every in-scope acceptance criterion, consequential risk/control, and mandatory activity needs REQUIRED coverage or a valid exception. Reconcile the requirement/risk denominator before declaring the plan complete. Record scope/criteria changes and their approval; do not remove failures through reclassification.

| Check ID / gate | Required? / hard stop? | Requirement/risk IDs | Method and oracle | Expected outcome / forbidden effects / threshold | Environment and inputs | Applicability rationale |
|---|---|---|---|---|---|---|
| [CHK-… / G…] | [yes/no; policy] | [IDs] | [independent expected result source] | [measurable criterion] | [candidate and conditions] | [applicable, unresolved, or concrete N/A reason] |

- Coverage reconciliation: [all obligations covered? uncovered IDs and missing conditions]
- Required upstream gate dependencies: [scope and IDs; existing conditions/exceptions]
- Scope/criteria changes: [before/after, reason, explicit owner approval where required]

## Candidate and evidence identity

- Source revision and dirty snapshot: [identity of actual tested source]
- Build/artifact digest: [if applicable]
- Test revision/configuration: [identity]
- Dependencies/runtime/platform/schema/configuration: [versions or manifest links]
- Fixtures/data/seed/concurrency/workload/time assumptions: [reproducible conditions]
- Runner and execution timestamps: [identity and interval]
- Environment fidelity and mock boundaries: [differences and claim limits]
- Evidence storage/access/redaction/retention: [appropriate location and limits]

## Execution record

| Check ID / attempt / purpose | State | Actual observation vs expected | Evidence reference | Valid for current claim? / reason | Cleanup and remaining effects |
|---|---|---|---|---|---|
| [CHK-… / attempt … / candidate, detector experiment, or historical] | [PASS/FAIL/BLOCKED/NOT_RUN/NOT_APPLICABLE] | [observed result or prerequisite] | [raw log/report/record] | [yes/no/unresolved] | [owned resources and result] |

Record discovered/executed/skipped counts when relevant. Preserve initial failures and retries. Do not fill PASS until execution and observation support it.

## Findings and current assessment

| Finding / affected obligation | Discovery source, including optional/manual | Current unresolved state | Resolution/disposition evidence | Candidate and clean revalidation | Owner |
|---|---|---|---|---|---|
| [FIND-… / REQ-…] | [check/agent/artifact] | [actual current state] | [cause, fix or demonstrated invalidity; preserve original] | [identity and observed result, or pending] | [owner] |

A later pass alone cannot close a finding. Expected detector failures belong to their experiment; require verified clean restoration. Include consequential cleanup gaps and credible acceptance violations even if found outside scheduled required tests. Inspect underlying result artifacts rather than treating another agent's summary as proof.

## Validation of validation

| Aspect | Observation/evidence | Gap or disposition |
|---|---|---|
| Oracle correctness and independence | [reviewed examples/reference method] | [risk of shared mistaken assumptions] |
| Detector sensitivity where warranted | [before-fix failure/mutation/negative control/fault injection] | [limitations, restored clean candidate] |
| Assertion strength | [outputs, persisted effects, forbidden effects] | [weak or mock-only assertions] |
| Harness reliability | [discovery, isolation, seeds/clocks, failures/retries/skips] | [flakiness or setup limitations] |
| Environment fidelity | [real boundaries exercised] | [unproven environments/providers] |
| Evidence provenance | [artifact/configuration match and retained raw results] | [staleness/mismatch] |

## Gate decisions

Apply references/evidence-and-gates.md, including obligation coverage, current findings, required upstream gates, precedence, and exception validity. Record OUT_OF_SCOPE only at phase level. An empty in-scope gate is NOT_READY. Do not erase known failures when another failure has higher precedence.

| Gate | Scope / required check IDs | Decision | All unresolved items / evidence links | Owner / next action |
|---|---|---|---|---|
| [G…] | [scope and denominator] | [PASS/FAIL/BLOCKED/NOT_READY/CONDITIONAL or phase OUT_OF_SCOPE] | [all gaps] | [concrete next step] |

## Exception, only if explicitly accepted

- Exception ID and authorized decision maker: [name/role/authority]
- Approval evidence: [actual recorded approval]
- Requirement/risk/check and underlying state: [exact gap]
- Candidate/environment, scope, permitted action: [bounds]
- Remaining consequence/uncertainty: [specific]
- Compensating controls and evidence: [or explicit acceptance of none]
- Expiry/revisit trigger and follow-up owner: [specific]
- Hard-stop/policy and authorization compatibility: [cannot override]
- Valid at point of use: [authority/scope/candidate/expiry rechecked; each condition/control actually satisfied with evidence]

## Rollout, recovery, operation — only within scope

- Target, owner, authorization, artifact/configuration: [actual facts]
- Migration/upgrade and recovery proof: [test conditions and results]
- Rollout steps, observation window/workload, stop thresholds: [predefined criteria]
- User/business monitoring and response: [signals/runbook/owner]
- Deployment observations: [execution ID, state, outcomes, interval]
- Maintenance/retirement: [reassessment or authorized decommission criteria/evidence]

## Final bounded claim

- Outcome: [what is actually complete; scoped claim label and any condition]
- Completion coverage: [all requested deliverables, integration/wiring, required validation, consequential cleanup/handoff; remaining obligations]
- Evidence: [short actual-check summary and links]
- Gaps and limits: [remaining states, environments, exceptions]
- Next step: [only if necessary; owner and exact missing prerequisite]
