# Requirements, Tasks, and Interaction Design

## Connect goals to acceptance

Distinguish user goals, business goals, features, and constraints. Knowing whether registration succeeded is a user goal; increasing conversion is a business goal; adding a status page is a proposed solution. Establish the problem before committing to the solution.

Capture enough task context: relevant user differences, environment and interruptions, input devices, frequency, failure cost, and evidence. Personas should represent observed behavior and motivation. Label unsupported personas as hypotheses; fictional biographies do not establish research. Cover the primary path and infrequent tasks with substantial consequences.

Scenarios describe triggers, goals, preconditions, actions, and outcomes without prematurely prescribing controls. Keep evidence or assumptions connected to decisions and acceptance:

| Need | Decision | Observable acceptance |
| --- | --- | --- |
| Confirm registration on a weak connection | Distinguish progress, success, failure, and unknown outcome | Refresh or retry can recover the real status without claiming false success |
| Continue after an input error | Explain errors locally and preserve valid input | Correcting the affected item is sufficient to continue |
| Recover an accidental deletion | Choose undo or a recovery area according to consequences | Recovery has an explicit scope; explain irreversible consequences beforehand |

## HTA and information architecture

Number goals and subtasks, then add a plan specifying order, branches, loops, and termination. A task tree alone does not explain execution.

```text
0 Complete registration
  1 Find an event
  2 Check eligibility and capacity
  3 Enter and review information
  4 Submit
  5 Confirm the outcome
Plan 0: 1→2; if eligible, 3→4→5; otherwise stop.
Retry recoverable failures at 4. For an unknown outcome, query status first.
```

Decompose only as far as the current decision requires. Understand objects and task relationships before choosing navigation, views, and controls. Open card sorting explores categories and labels; closed sorting examines predefined categories; tree testing examines findability without visual presentation. Each provides different evidence and requires interpretation.

## Describe behavior through states

Select relevant states: initial, loading, empty, editing, validating, submitting, success, recoverable error, unknown outcome, unauthorized, and canceled. For key states, specify entry, available actions, feedback, retained data, exit, and recovery.

In asynchronous flows, sending a request and completing a business operation are distinct. Canceling a wait may not reverse a server transaction; a timeout does not establish failure. Frontend click prevention cannot replace server idempotency where duplicate operations matter. Introduce implementation requirements only when relevant to the task.

Optimistic updates suit operations with appropriate consequences and reliable rollback. Restore the real state and explain failures. Autosave should distinguish local changes, saving, synchronization, and conflict; a transient notification cannot resolve a persistent conflict.

## Prototypes and iteration

Fidelity and functional depth are separate dimensions. Low fidelity supports structure and workflow decisions; high fidelity supports detailed behavior. Horizontal prototypes cover many functions superficially; vertical prototypes implement selected paths deeply. Explain simulated or Wizard-of-Oz capabilities. High fidelity does not establish production readiness.

Choose a prototype inexpensive enough to revise and capable of testing the current uncertainty. Use observation and test findings to guide iterations rather than treating personas, frameworks, or prototypes as final outputs.

## Simplification and tradeoffs

- Remove low-value duplication while retaining necessary infrequent tasks; click frequency alone is insufficient.
- Organize around user concepts with meaningful hierarchy, proximity, and alignment. Visible menus have no universal seven-item limit.
- Reveal advanced functionality progressively while preserving discoverable access, essential status, and recovery.
- When moving work to another device or collaborator, include switching, synchronization, and recovery costs.

Responsive design changes task presentation as well as size. Check narrow-screen order, on-screen keyboards, zoom, and interruption. Internationalization must accommodate text expansion, date and number formats, time zones, and writing direction. Keep translated meanings aligned without assuming fixed text lengths.

Deliver the requested flow, state table, wireframe, prototype, or implementation. Mark unverified behavior and connect important tradeoffs to user impact and verification; theory annotations for every control are unnecessary.
