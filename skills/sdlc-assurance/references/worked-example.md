# Worked examples — illustrative, not executed evidence

These examples show decisions to make. No repository, test, deployment, or approval was actually exercised by this document. Expected results below are plans, never PASS evidence.

## High risk: editing a tenant-owned record

**Request:** Implement an endpoint allowing editors to rename records in their own tenant. Production deployment is not requested.

**G0:** Implement/fix mode. Risk H because authorization and tenant isolation are affected. Target local and real-database integration verification. G5–G7 are outside the assignment; no production action is implied.

**G1 rules:** An authenticated editor may rename a record in the editor's current tenant. Viewers and other tenants cannot rename it. Denied requests must not alter the record or emit a successful-update event. Define whether permission changes racing with an update must take effect at transaction authorization time; the example chooses this explicit rule and requires domain review. Error behavior must follow the agreed contract without unnecessary existence disclosure.

**G2 design:** Determine tenant and role from trusted identity, never an untrusted request tenant field. Resolve authorization and update within the required transaction/control boundary. Scope the write by tenant and record; define expected behavior for missing or concurrently changed records. Use the existing event/audit mechanism and ensure denied requests cannot emit success. Design test fixtures with tenants A/B, editor/viewer identities, independently stored records, and deterministic coordination for permission races.

| Rule/risk | Planned check and oracle | Expected effects | Evidence needed |
|---|---|---|---|
| Own-tenant editor succeeds | API integration against real test DB; reviewed permission matrix | Only target name changes; contract-correct success/event | Request/response, independent DB readback, event observation |
| Cross-tenant access denied | Identity in A submits record ID from B, including forged tenant field | Contract-correct denial; B's record unchanged; no success event | Before/after snapshot and event check |
| Viewer denied | Viewer submits direct API request bypassing UI | No write or success event | Direct request and persisted-effect readback |
| Permission race handled | Coordinated revocation/update interleaving under agreed transaction-time rule | Behavior matches the explicit race policy; no unauthorized write | Interleaving barriers/trace plus final DB state |
| Retry and failure safe | Repeat request; interrupt relevant write/event boundary | Agreed idempotency/consistency behavior | Record/event reconciliation and failure trace |
| User journey works | UI editor renames and reloads; viewer cannot complete equivalent operation | Visible result matches persisted result | Actions, UI/accessibility capture, reload/readback |

**Validate the tests:** Derive expected permission results from the reviewed matrix, not the production authorization helper. In isolated local state, remove the tenant predicate or seed a representative authorization fault; the cross-tenant detector should fail for the prohibited write. Restore the clean implementation and rerun relevant checks. A high mutation score on string formatting would not establish authorization sensitivity.

**Possible gate outcomes:** If real DB setup is unavailable, the integration check is BLOCKED even if mocked tests pass. G4 is BLOCKED; report “implementation finished; real-database validation blocked.” If the required checks actually run successfully with credible evidence, a bounded INTEGRATION_VERIFIED claim can be made for those behaviors. This still is not a release or deployment claim.

## Evidence mismatch: green results on the wrong candidate

**Facts supplied:** Suite passed on artifact A. A dependency/configuration change produces artifact B. No impact analysis or B results exist.

Preserve A's PASS records. Mark their validity for B unresolved/invalid and G5 NOT_READY until impact analysis and necessary revalidation bind evidence to B. Do not change the timestamps, copy the green badge, or call B release qualified.

## Accepted exception: qualification remains conditional

**Facts supplied:** A required physical-device check is BLOCKED. An authorized release owner explicitly accepts that named gap for candidate B with a bounded rollout, monitoring, expiry, and approval evidence. All other applicable required checks have valid PASS evidence; no policy hard stop applies.

The device check remains BLOCKED. The gate is CONDITIONAL. State “conditionally approved to proceed under exception EX-1; physical-device behavior remains unverified,” not “all tests passed” or unqualified RELEASE_QUALIFIED. Production deployment still needs authorization for its target and action.

## Low risk: correcting a static help-text typo

**Request:** Correct one word in a static help panel. No logic, layout contract, data, or security behavior changes.

Risk L after confirming the actual diff. Inspect the changed text in context and affected rendering/build path as relevant. Check nearby layout/accessibility only if the edit could affect them. An inline record is sufficient. Do not require a threat-model document, mutation testing, load testing, deployment, or a new test that asserts the exact sentence. If the string is executable markup or changes a security instruction, revisit the risk assessment.

## Review only: assess a data migration plan

**Request:** Review this migration for data-loss risk; do not edit or run it.

Read schema/plan and relevant evidence. Map hazards such as partial writes, duplicates, interruption, compatibility, and restore gaps. Distinguish source-confirmed concerns from reproduced failures. Propose concrete tests and acceptance thresholds, but mark them NOT_RUN or BLOCKED as appropriate. Deliver the completed review with findings and unknowns. Do not execute the migration, create a new implementation, or label proposed tests as proof.

## Stochastic output: useful samples are not a population guarantee

**Request:** Assess an AI-assisted classifier before expanding its use.

Define the decision population, error costs, held-out labeled dataset, slices, human-label agreement, leakage controls, repeated-run protocol, uncertainty, and minimum acceptance criteria before evaluation. Keep model/prompt/data/tool versions in provenance. A handful of attractive outputs or agreement between two similar models is not an independent oracle. Report observed rates and uncertainty by slice; do not promise deterministic correctness or generalize to unrepresented groups. See the testing reference for details.

## Optional test discovers a real acceptance violation

**Facts supplied:** A payment feature requires at most one charge per logical order. Required happy-path tests pass. An exploratory retry test proves two charges for one order; it was labelled optional.

Record the invariant violation as unresolved FAIL in the relevant gate. The optional scheduling label cannot remove it. If no required test covered duplicate prevention, also record the coverage gap. Fix and revalidate the defect, or retain a valid permitted exception with its condition; do not report the entire payment behavior verified because the required-test list is green.

## Failure history and detector experiments

**Facts supplied:** Candidate A fails a regression. The cause is identified and fixed in B; the relevant clean tests run on B with valid evidence. A separate isolated experiment deliberately removes the guard, observes the detector fail as expected, then restores and revalidates B.

Keep A's FAIL and its linked resolution. Its resolved history does not make B permanently FAIL. The experiment's detector criterion can PASS because it detected the seeded defect; that is not candidate correctness evidence for the faulted build. B's current assessment uses its clean, restored, relevant evidence and all other required obligations. An unexplained passing retry would not provide the same resolution.

## Custom UI in an existing product

**Request:** Redesign an internal dispatch screen for operators handling urgent work, preserving the existing native platform and design system.

Use the actual task frequency, content, role permissions, existing workflow and accessibility needs to reimagine the affected screen. Compare an appropriate queue-first arrangement with a case-detail-first arrangement if that resolves a real design choice. Choose and explain the layout in that context; do not recolor a premade dashboard. Reuse the product's accessible buttons, tables, focus conventions, and tokens where suitable. Prototype the real content density and loading/empty/denied/error states; verify the critical operator journey and responsive/accessibility behavior when implementation is in scope. A screenshot supports appearance, not correct assignment persistence. A design-only request can deliver reviewed design evidence without claiming the application was implemented.

## Full-repository audit with partial inspection

**Facts supplied:** The user requested a whole-repository audit. Only changed frontend files were reviewed; backend authorization, CI configuration, and migration code were not inspected.

Report findings for the inspected frontend scope and retain the unreviewed surfaces in a repository-wide inventory. The audit is incomplete for the original request until those surfaces are reviewed, appropriately sampled with disclosed limits, or an explicit scope reduction is accepted. Do not call the repository defect-free or the entire audit complete from the changed-file evidence.
