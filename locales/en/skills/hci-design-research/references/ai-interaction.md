# Human-AI Interaction

Read only for recommendation, prediction, generation, or automation features. Ordinary deterministic controls do not require this extension.

## Expectations and control

Communicate capabilities and likely failure. People should be able to invoke, dismiss, and correct assistance and understand important behavior. Updates or preference changes should preserve understandable workflows.

Make uncertain output inspectable. Depending on the feature, provide editing, retry, comparison, undo, or human escalation. An explanation panel is useful only when it serves a user decision.

## Turn principles into states and tasks

These are synthesized project recommendations rather than a fixed interface template:

| Situation | Design and verification |
| --- | --- |
| Generation is incomplete | Distinguish progress, partial output, completion, and failure; explain what survives stopping |
| A suggestion can be applied | Separate preview, selection, and actual commitment |
| Output is incorrect | Support editing and regeneration without recreating all context |
| Automation has external consequences | Make action, scope, and outcome visible; match controls to authorization and consequences |
| Models or configuration change | Compare quality, latency, and task performance under matching conditions and record configuration |

Avoid unsupported confidence percentages and do not treat fluent language as correctness. Supporting material must substantiate the particular claim rather than merely look credible.

## Evaluate end-to-end utility

Define task and failure consequences, then measure correct completion, error detection, correction effort, time, and appropriate reliance. Acceptance rate is not quality; frequent acceptance can conceal unnoticed errors. Record model/system versions, prompts or configuration, input data, and repetition strategy.

Stochastic systems may produce different results for identical input. Plan repetitions and sampling for the research question and preserve reproducible conditions. One successful demonstration does not establish stable capability. Distinguish live outputs from fixed or manually simulated research stimuli.
