# Principle-Driven Interaction Reviews

## Locate the user's difficulty

The execution/evaluation cycle covers goal formation, intention, action specification, execution, perception, interpretation, and outcome evaluation. The gulf of execution concerns knowing how to act; the gulf of evaluation concerns understanding what happened. Translations between user intent, input, system state, and output can locate failures without requiring a complete model for every issue.

Discuss usability for specified users, tasks, and contexts. Efficiency, success, safety, learnability, memorability, utility, and satisfaction can involve tradeoffs. Designer preference does not establish enjoyment; speed is not every product's only goal.

## Principles and inspection questions

| Principle | Inspect within the task |
| --- | --- |
| Visible status | Can people interpret progress and outcomes? |
| User concepts | Are terminology, mappings, and sequence understandable? |
| Control and freedom | Are exit, cancel, back, and recovery appropriate? |
| Consistency and conventions | Does shared meaning produce consistent behavior? |
| Error prevention | Are costly slips and ambiguous inputs reduced? |
| Recognition | Is necessary information available at the point of use? |
| Flexibility and efficiency | Are suitable shortcuts available for frequent tasks? |
| Simplicity and emphasis | Does irrelevant material obscure the task? |
| Error diagnosis and recovery | Is the problem explained with an actionable next step? |
| Help | Is guidance available within the task? |

The eight golden rules add a check for consistency, universal usability, informative feedback, closure, error prevention, reversal, user control, and memory load. Closure does not require a dialog. The frameworks overlap without a mandatory one-to-one mapping; neither is a universal scoring scale.

## Review methods

For heuristic evaluation, understand the main tasks before inspecting paths and local states. Independent reviewers may combine findings afterward. Repeated AI self-review is not independent expert agreement. Expert concerns require appropriate validation rather than being presented as inevitable user failures.

For cognitive walkthroughs, specify a first-time user's knowledge and goal. At each step ask whether the user would pursue the right subgoal, notice the action, relate it to the goal, and interpret progress. Record the basis for judgments instead of substituting expert knowledge.

## Accessible interactions

Prefer suitable native semantics and reliable existing components. Inspect keyboard sequence, visible focus, labels, and error associations. Custom interactions need behavior as well as semantics; ARIA attributes alone cannot supply missing interaction.

A modal moves focus inside, contains Tab navigation, offers a close action and Escape handling, then restores focus to its trigger or a logical continuation. Choose initial focus for content and consequences rather than always choosing the first button.

Relevant status messages should be perceivable by assistive technology without unnecessary focus movement; avoid making every update interruptive. Check whether sticky content obscures keyboard focus. A minimum requirement against complete obscuring differs from a stricter requirement against partial obscuring.

For a WCAG 2.2 AA target, criterion 2.5.8 specifies 24×24 CSS px minimum targets, with spacing, equivalent-control, inline, user-agent, and essential-presentation exceptions. This is not a universal recommended touch size or a complete conformance test. Check exceptions against the selected baseline.

Automated scans find only some issues. Verify keyboard operation, actual states, and the target assistive technology. Screenshot review cannot establish an accessibility audit.

## Findings and priorities

Record location or step, evidence type, observed or potential behavior, task impact, principle, severity with rationale, recommendation, and verification. A severity scale may use 0 non-issue, 1 cosmetic, 2 minor, 3 major, and 4 catastrophic. Keep this distinct from P0/P1 engineering priority. Mark unknown frequency as unknown.

Prioritize using task blockage, reach, consequences, recovery, and implementation cost. For example, a visible save button with unclear feedback is a risk from a static image. Reproducing absent feedback and observing repeated clicks provides stronger evidence.

After changes, verify behavior and affected regression paths; the presence of a CSS class or a specific message alone does not establish a fix.
