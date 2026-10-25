# Testing and test assurance

Use this reference to select evidence for a specific change, requirement, and risk.
It is a method-selection guide, not a mandate to run every technique or tool.
Testing can establish observed behavior under stated conditions; it cannot prove the absence of all defects.

## 1. Establish the claim before selecting tests

1. Name the authorized task mode: review, design, implementation, qualification, or operation.
2. Bind the proposed assertion to a requirement, acceptance example, or invariant.
3. Identify the highest credible consequence, affected boundaries, uncertainty, and reversibility.
4. Record tier L, M, or H and the reason; a small diff may be H.
5. Identify what could falsify the assertion, including plausible defects and environmental failures.
6. Choose the least costly method that exposes that failure at the relevant boundary.
7. Define the expected result and evidence before execution where practical.

Use existing repository workflows and tests before introducing new infrastructure.
For a trivial reversible change, a concise observation can be sufficient evidence.
Do not add tests that merely restate implementation or inflate a coverage number.
When a requirement is ambiguous, resolve the expected behavior instead of encoding an accidental result.

## 2. Plan checks and applicability

Create a row for every required check; unresolved and unsuccessful rows must remain visible.
A row should name: requirement/risk, assertion, method, environment, oracle, candidate identity,
required/optional status, applicability reason, owner, result state, and evidence location.
For lightweight work, these fields may be one concise note rather than a separate document.

Reconcile the check inventory against all in-scope acceptance criteria, consequential risks/controls,
and mandatory assurance activities. Each needs applicable REQUIRED evidence or a valid exception.
Do not label a check optional when it is the only planned evidence for an acceptance obligation.
Select environments, scenarios, workload, and quality thresholds from observed project context rather
than importing a generic stack checklist. Scope/criteria reductions need the relevant explicit approval.

- `PASS`: observed evidence supports the named assertion for the candidate and conditions.
- `FAIL`: observed behavior violates the expected result or required check.
- `BLOCKED`: a prerequisite, permission, dependency, or environment prevents execution.
- `NOT_RUN`: applicable work has not been executed.
- `NOT_APPLICABLE`: a documented scope or design reason removes this check's relevance.

Unavailable infrastructure is `BLOCKED`, never `NOT_APPLICABLE`.
Unresolved applicability makes the gate `NOT_READY` unless an unresolved `FAIL` or `BLOCKED` takes precedence.
Keep raw results when evidence becomes stale or mismatched; the gate is `NOT_READY` until revalidated unless an unresolved `FAIL` or `BLOCKED` takes precedence.
Optional methods need not be added mechanically. Any credible in-scope acceptance/invariant violation
found by optional, manual, or exploratory checks is an unresolved FAIL in the gate record, even if the risk
was already known. Consequential unresolved signals need triage and prevent the affected PASS claim.
Checks beyond authorized scope belong to an `OUT_OF_SCOPE` phase, not an invented check state.
Do not infer product assurance from a gate containing only `NOT_APPLICABLE` rows.
An in-scope gate with no applicable required checks is NOT_READY; mark a genuinely excluded phase
OUT_OF_SCOPE instead of assigning a scope-only PASS. Required upstream decisions also enter aggregation.

## 3. Minimum sufficiency by risk tier

These are minimum recommendations to tailor and record, not automatic release guarantees.
An applicable organizational or domain requirement can require more evidence.

| Tier | Typical scope | Minimum evidence to plan |
| --- | --- | --- |
| L | Reversible change without logic, data, or security-boundary impact | Inspect the exact change; validate the affected visible or static result; check an adjacent failure mode if credible. Run existing mandatory checks. Record why broader methods add no relevant evidence. |
| M | Bounded behavior, data, or API change | Trace acceptance examples to focused behavior checks, boundary/negative cases, and regression evidence. Exercise relevant changed boundaries and the affected journey. Assess key detector sensitivity and demonstrate rejection of a plausible defect where consequential behavior warrants it. Assess recovery and nonfunctional applicability. |
| H | Auth/authz, privacy, payments, destructive data, concurrency, infrastructure trust, cross-service behavior, or difficult rollback | Add independent challenge of requirements/design and key oracles; adversarial and failure/recovery checks at affected real boundaries; fault sensitivity of critical checks; candidate-bound release evidence when qualification is in scope. Select relevant concurrency, security, migration, performance, and operational evidence. |

Critical/high-assurance systems extend H with applicable domain rules and qualified expert review.
Determine whether hazard analysis, formal methods, independence requirements, traceability, or prescribed
validation environments apply; do not substitute this skill for certification or regulated approval.
If credible catastrophic consequences remain poorly understood, escalate the uncertainty before claiming readiness.
H selects methods relevant to the risk; it does not require every technique below.

## 4. Choose methods by the failure they can reveal

| Risk or question | Suitable method | Evidence that supports the assertion |
| --- | --- | --- |
| Local deterministic decision logic | Unit tests with independently derived examples; property tests for invariants | Inputs, expected outputs/invariants, candidate, run output, and a demonstrated failing counterexample when faulted |
| Component behavior and state transitions | Component tests over public behavior | Initial state, action sequence, emitted result and persisted effects, including rejected transitions |
| Producer/consumer compatibility | Contract checks plus real integration where behavior depends on transport/runtime | Versioned contract, accepted/rejected payloads, consumer/provider versions, and observed exchange |
| User-visible correctness across layers | Representative end-to-end journey | Actions, visible states, durable effects, access context, boundary identities, and cleanup outcome |
| Broad input space or parsing | Property-based testing or bounded fuzzing | Generator/corpus, constraints, seeds where supported, runtime budget, crashes/counterexamples and minimized reproductions |
| Complex output with useful alternatives | Differential or metamorphic testing | Independent comparator or justified relation, known limitations, discrepancies and adjudication |
| Races, retries, ordering, distributed failures | Controlled interleavings, fault injection, integration stress | Schedule/fault placement, concurrent identities, observed histories, invariant checks, and recovery result |
| Sensitive trust boundary | Threat-informed abuse and authorization tests | Actor/resource/action matrix, denied and permitted outcomes, side effects, and data/log exposure checks |
| Operational capacity or responsiveness | Controlled benchmark/load/soak test | Workload, environment, raw measurements, repetitions, resource/error data, and comparison method |
| Data change, rollback, restore | Rehearsal using representative isolated data | Before/after invariants, transformation results, interruption/restart behavior, restore and reconciliation evidence |

Static analysis, types, linting, dependency checks, and review complement execution.
Record their configuration, scope, suppressions, versions, and findings; a clean scan is bounded by its rules.
Use formal analysis when a critical invariant and tractable model justify it; state model assumptions and
the connection between model and implementation. A proof about the model is not a deployment observation.

## 5. Design the case space

Select dimensions from the affected risk surface instead of mechanically crossing every combination:

- Normal, empty, minimal, maximum, just-below/at/above boundary, malformed, and unexpected input.
- Missing, null, duplicate, stale, reordered, conflicting, and partially valid data.
- Authorized, unauthorized, expired, revoked, cross-user, cross-tenant, and elevated identities.
- First use, repeat use, restart, upgrade, cancellation, timeout, partial completion, retry, and recovery.
- Sequential and concurrent actions; replay, duplicate delivery, lost acknowledgement, and out-of-order events.
- Dependency success, slow response, malformed response, unavailability, and partial failure.
- Time zones, clock changes, locale, encoding, precision, schema/version compatibility, and accessibility.
- Realistic volume, skew, growth, resource limits, backpressure, and degraded operation.

Prioritize combinations that interact: a retry after a committed payment is different from an ordinary retry.
Use equivalence classes, boundary analysis, decision tables, or state models to justify sampled cases.
For combinatorial sampling, state which interactions it covers and which critical combinations need explicit tests.
For regressions, reproduce the old failure when feasible and show the corrected candidate satisfies the requirement.

## 6. Establish trustworthy oracles

An oracle determines whether a result is correct; successful execution alone is not an oracle.
Prefer acceptance examples, domain invariants, approved reference data, independent calculations,
or separately implemented reference behavior over expected values copied from the production algorithm.

- Assert externally meaningful outcomes, including persisted effects and forbidden side effects.
- Derive expected values separately; shared parser, formatter, or business logic can create correlated errors.
- Review snapshots for meaning and scope; automatic snapshot acceptance is not independent validation.
- A second model or service is a comparator, not ground truth; adjudicate disagreements.
- Validate metamorphic relations themselves and avoid relations that also hold for broken constant outputs.
- Make tolerances explicit and justified by the domain or measurement precision.
- For visual/accessibility assertions, combine relevant programmatic checks with observed interaction.

Preserve oracle provenance, assumptions, reviewer decisions, and known blind spots in proportion to risk.

## 7. Test the tests and the harness

Check that critical assertions can detect the failures they claim to prevent.
Choose a targeted mutation, injected fault, known-bad input/output, or deliberate negative control.
Examples: remove an ownership guard, suppress a durable write, corrupt a checksum, return stale data,
force a dependency timeout, or substitute an incorrect result that still has the expected shape.
Run these experiments only in authorized isolated copies/environments and restore the baseline afterward.

Record the defect introduced, expected detecting check, observed failure, and restored baseline result.
A test that remains green requires investigation: the fault may be irrelevant, unreachable, equivalent,
masked by a mock, or outside the assertions. Explain the finding; do not silently discard it.
For broad mutation runs, inspect meaningful survivors and exclusions; a mutation percentage alone proves little.
Keep faulted executions separate from candidate validation so expected failures cannot be misreported as regressions.
Label the purpose before execution. An expected product failure in a detector experiment can be a PASS
for the detector's stated criterion, never a PASS for the faulted product. Restore and revalidate the clean
candidate; unexpected outcomes and failed restoration remain gaps. Do not retroactively relabel failures.

Validate harness fundamentals before relying on a green summary:

- Discovery: expected checks ran; no empty suite, unintended filter, skipped critical path, or stale test bundle.
- Execution: awaits and child processes complete; failures propagate to the runner and CI exit status.
- Assertions: the intended oracle executes; exceptions and asynchronous rejections cannot be swallowed.
- Fixtures: setup represents the stated preconditions and does not bypass the behavior under test.
- Isolation: state, ports, clocks, caches, credentials, and random sources do not leak across tests.
- Dependency fidelity: mocks enforce relevant contracts and failures; integrate where mocks omit the risk.
- Provenance: results match source, artifact, config, dependency, fixture, and environment identities.
- Cleanup: created data/resources are accounted for; cleanup failure is recorded separately from test success.

Evidence may be a controlled failing run, discovery report, trace, recorded observation, or reviewed harness code.
Scale the audit to the claim; do not require mutation infrastructure for a text-only L change.

## 8. Handle flakiness without hiding uncertainty

Preserve the first failure and every retry, with inputs, seed, timing, order, worker count, and logs where useful.
A retry passing does not erase a failure or establish its cause.
Separate immutable attempt results from the current assessment. Resolve a prior failure with a linked
cause/disposition, fix or demonstrated invalidity, current candidate, and appropriate clean revalidation.
A fixed failure stays in history without permanently forcing FAIL. A proven harness failure invalidates
that attempt as product evidence but leaves the product obligation unmet until a valid run. Test renaming,
new candidate labels, snapshot updates, or arbitrary numbers of green retries do not establish resolution.
Reproduce with controlled order, isolation, clocks, and concurrency; distinguish product races from harness defects.
Use waiting on observable conditions instead of arbitrary delays, while retaining bounded timeouts.
Do not fix flakiness by weakening the assertion or increasing timeouts without a justified behavior contract.
Quarantine requires an owner, underlying result state, impact, replacement evidence, and a revisit trigger.
An accepted exception follows the skill's exception rules; quarantined critical evidence cannot silently disappear.

## 9. Bind environment fidelity to claim limits

Identify which boundaries are real, emulated, mocked, synthetic, disabled, or unobserved.
Local, synthetic, emulator, simulator, device, browser, hosted CI, provider, staging, and production
evidence support different claims; never promote one merely because the same test name ran.
Record runtime/platform versions, topology, permissions, flags, dependencies, dataset, and network assumptions.
Use the actual boundary when correctness depends on platform APIs, persistence, identity enforcement,
provider semantics, deployment configuration, or cross-service interaction.
If access is unavailable, retain a `BLOCKED` row and state the strongest narrower result actually demonstrated.
Production tests need explicit authorization, bounded impact, safe data, stop conditions, and observed cleanup.
Release qualification establishes a candidate's readiness; only an authorized observed rollout supports `DEPLOYED_OBSERVED`.

Integration evidence must identify the exact boundary. An SDK mock, replayed webhook, provider sandbox,
and live payment each establish different facts. For asynchronous operations verify terminal business
effects and forbidden duplicates, not just acknowledgement or queue acceptance; observe failures/retries
and reconciliation where relevant. For migrations verify logical content and recovery state rather than
row counts alone. A deployment/CI request accepted for execution remains pending until its result is observed.

## 10. Performance and resource evidence

Define the user/business operation, acceptable latency/throughput/resource behavior, and expected workload first.
Select representative distributions: payload size, cardinality, skew, cache hit rate, concurrency, session length,
read/write mix, dependency latency, and realistic failure rates. Include growth or saturation only when relevant.
Distinguish microbenchmarks, component capacity tests, end-to-end load, stress, and soak claims.
Record hardware/runtime/config, warmup policy, cold/warm behavior, sample size, repetitions, and raw results.
Control background load and major confounders; measure both baseline and candidate under comparable conditions.
Report distributions and tail behavior where relevant, errors/timeouts, throughput, and resource use together.
Check that the load generator is not the bottleneck and that offered load differs visibly from completed work.
Explain variability and limitations; do not present a single noisy run as a precise improvement.
Avoid asserting performance from code shape alone or extrapolating a tiny synthetic workload to production capacity.

## 11. Security, migration, and recovery

Derive abuse cases from assets, actors, trust boundaries, and attacker-controlled inputs.
Test denial and allowed behavior; denial must prevent durable side effects and sensitive output/log leakage.
Where applicable, exercise privilege changes, object ownership, tenant isolation, replay, injection,
untrusted file/path/URL handling, secrets exposure, exhaustion, and dependency/supply-chain controls.
Use isolated adversarial fixtures; do not attack external services outside authorized scope.

For schema/data changes, exercise compatibility across mixed versions and representative legacy records.
Verify invariants, counts and meaningful content reconciliation; counts alone can hide corruption.
Interrupt a representative migration and test restart/idempotency, partial-state handling, and rollback or roll-forward.
When rollback cannot restore correctness, demonstrate the supported recovery path and state its limitations.
For backups, verify restoration and application usability; a successful backup command is insufficient.
Capture actual recovery duration and recovered data boundaries when recovery objectives are part of acceptance.

## 12. Data, ML, and stochastic outputs when applicable

Check input quality, provenance, leakage, missingness, distribution shifts, and representative subgroups.
Separate training/tuning examples from held-out evaluation; protect the evaluation set from adaptation.
Use requirement-specific rubrics, independent labels/review, baseline comparisons, and explicit unacceptable outcomes.
For stochastic systems, record model/config/prompt/data versions, repetitions, sample selection, and seeds when available.
Report uncertainty and variation; a fixed seed improves reproduction but does not establish broad reliability.
Validate evaluators with known-good, known-bad, borderline, and adversarial cases; investigate reviewer disagreements.
Assess privacy, unsafe outputs, prompt injection/tool authorization, and abstention/fallback behavior where relevant.
No average score overrides a required invariant or conceals a critical subgroup failure.
Define held-out sample/slice sufficiency, repeated-run protocol and uncertainty-based acceptance before
evaluation. Do not stop early after favorable samples, repeatedly tune against the held-out set, or silently
drop failed slices. Insufficient observations make the claim NOT_READY, not proof of a target error rate.

## 13. Place checks in delivery and operations

Put fast deterministic affected checks on local/pre-merge paths; run required real-boundary checks before their gate.
Use scheduled runs for costly breadth, fuzzing, soak, compatibility matrices, and drift/dependency reassessment.
Scheduling a required check later does not satisfy today's gate; use a valid exception or keep the gate unmet.
Recheck candidate identity and applicable evidence at G5; observe actual rollout and smoke/business outcomes at G6.
At G7, connect monitors to failure modes and exercise alert/response paths where authorized.
An alert configured in code is not evidence that delivery, diagnosis, or recovery works.
Revisit upstream gates after relevant code, config, data, dependency, environment, or assumption changes.

## 14. Report what the evidence permits

Use [Evidence and gates](evidence-and-gates.md) as the single decision authority. Include requirement/risk
coverage, all current in-scope findings, evidence validity, and required upstream dependencies. Apply
non-excepted FAIL, then BLOCKED, then missing/invalid/empty/unresolved obligations as NOT_READY;
otherwise a valid satisfied exception or upstream CONDITIONAL yields CONDITIONAL. PASS requires
complete applicable coverage, valid passing checks/dependencies, and no unresolved in-scope finding.
Exceptions preserve the underlying result and require an authorized decision maker, explicit approval evidence,
affected requirement/risk/check, compensating controls and evidence, expiry/revisit trigger, and bounded scope.
Recheck exception conditions and scope at use; an approved but unfulfilled compensating control is not sufficient.
The agent cannot self-approve; hard stops, authorization, and claim boundaries cannot be waived by this skill.
Report the strongest supported completion label and material gaps, including observed failures and retries.
In review-only work, complete the review with evidence-backed findings and proposed checks; do not mutate
the product, run unauthorized disruptive experiments, or describe unexecuted validation as passing.
