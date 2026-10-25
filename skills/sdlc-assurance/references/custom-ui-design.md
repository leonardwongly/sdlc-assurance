# Custom UI design process

Use this process whenever creating or redesigning a UI within the authorized task. Rethink the affected interface for its users, content, and workflows. Do not use premade page, dashboard, or landing-page templates, or treat changing a template's colors, fonts, or copy as custom design. This is a design method, not a claim to have invoked a particular tool.

Reuse native controls, tested accessible components, design-system tokens, and sound implementation patterns when appropriate. Preserve required product behavior, brand constraints, and platform conventions. Reusable evidence-record formats are allowed; they do not prescribe the product's layout. A typo correction, backend-only change, or narrow repair does not authorize a wholesale UI redesign. Apply the process to the actual design decisions in scope.

## 1. Establish the design brief

Record the project's domain, affected users, primary tasks, actual content and data, task frequency, workflow context, and decisions users need to make. Identify devices, viewport/text-size constraints, input and assistive modes, permission boundaries, content variability, existing requirements, and observed friction. Establish whether this is a new product or an established interface, the existing brand/design system and native platform conventions, architecture/component boundaries, accessibility requirements and support matrix, delivery budget, and authorized scope. Use available project evidence; distinguish observed facts from assumptions and resolve consequential uncertainty before dependent decisions.

For an existing interface, inspect its current behavior and content before proposing a replacement. Retain purposeful interaction conventions, components, and requirements deliberately; change only relevant screens. Custom design means a considered fit to this project, not novelty or unnecessary rewrites. Do not invent analytics, user research, or stakeholder approval.

## 2. Develop and select a product-specific structure

Design the information architecture, task flow, hierarchy, layout, typography, navigation, and state behavior from the brief. Let the content and workflow determine the composition. Generic card grids or hero sections are not defaults; any chosen structure must serve the task.

Explore materially different suitable structures when the design decision warrants it. Exploration can be private reasoning, sketches, or runnable alternatives; expose concrete alternatives when needed to resolve a consequential tradeoff or obtain meaningful review. Do not manufacture a fixed number of variants for a straightforward change. Retain a concise rationale for the selected approach and any material rejected alternative, including accessibility, consistency, usability, and implementation tradeoffs.

## 3. Specify behavior and build a reviewable prototype

Map the important user journey and its relevant states: loading, empty, long/variable content, success, validation error, denied access, partial failure, cancellation, retry, and recovery. Identify what the user can do next, what is persisted, and how progress or failure is communicated. Include responsive/adaptive behavior and applicable keyboard, focus, screen-reader, reduced-motion, and text-scaling requirements.

Render a sketch, prototype, or implementation at a fidelity sufficient to review the affected decisions. Use representative content and data. Label simulated actions and synthetic data. A static screenshot can demonstrate composition, but it cannot establish interaction behavior or persisted effects. A prototype does not qualify the implemented product for release.

## 4. Validate the design and implemented experience

Map every in-scope UI acceptance criterion and mandatory design activity to a required check or valid accepted exception under [Evidence and gates](evidence-and-gates.md). Before execution, identify the expected result, relevant states, environment, and evidence to retain.

For design-only work, validate the decisions and prototype behavior at the agreed fidelity; specify implementation/integration checks as future requirements outside this execution scope. Do not run unapproved product mutations or require implemented persistence to deliver a design proposal. Keep any consequential unvalidated design assumptions provisional. For implementation work, the actual connected product journey needs its own evidence; prototype behavior cannot substitute for it.

Inspect the rendered candidate at representative device/viewport sizes and relevant themes, zoom/text sizes, and content extremes. Exercise the primary journey and relevant error/denial/recovery paths. Check focus order and visibility, keyboard operation, control names and semantics, contrast/readability, overflow, state transitions, and applicable assistive technology behavior. Verify persisted effects independently when the UI changes stored data. Select checks by requirements and risk; do not claim universal accessibility from a screenshot or an automated scan alone.

Retain enough evidence to review the outcome:

- Brief, requirement mapping, selected approach, and material tradeoffs.
- Flow/state specification and prototype or rendered candidate.
- Candidate/environment identity, reproducible actions, observed results, and relevant screenshots/accessibility evidence.
- Required-check states, unresolved findings, limitations, and any accepted exception.

Design deliverables are complete only when their required review and validation are finished. Implementation completion also requires connected behavior, required functional/accessibility checks, and relevant cleanup. A blocked device, browser, or assistive-technology check remains blocked; it is not satisfied by a different environment without an approved change to the requirement. Report the exact scope supported by the evidence.
