# Cognitive Foundations and Predictive Models

## Choose a suitable question

The Model Human Processor describes interactions among perception, cognition, action, and memory, with limited coverage of collaboration, emotion, and complex environments. Proximity, similarity, continuity, and closure can support organization but must serve task meaning; color alone is insufficient.

Reduce unaided recall and cross-screen memory demands. Neither 7±2 nor fixed memory durations parameterize every person or limit visible menus. Chunking should improve understandable structure rather than reach a prescribed count.

HTA describes task structure; GOMS describes methods and selection; KLM predicts skilled, error-free operation time; Fitts models pointing movement. Learning, error recovery, and subjective experience need other evidence.

## GOMS

Specify Goals, Operators, Methods, and Selection rules. Different methods may achieve one goal. Selection depends on knowledge, equipment, and starting state rather than arbitrarily choosing the fastest path.

Closing a window may involve pointing and clicking or using a shortcut. Establish hand position, shortcut knowledge, and whether unsaved changes produce a dialog. Excluding that dialog means the prediction is not complete closing time.

## KLM: sequences and parameters

State task boundaries, focus, hand position, window state, known input, skill, and device. Define an operator dictionary, list the sequence, and sum the terms.

| Symbol | Action | Illustrative parameter (s) |
| --- | --- | --- |
| K | One keystroke | 0.28; skill-dependent, not universal |
| P | Pointing | 1.10 as an example; a calibrated pointing model may replace it |
| B | Mouse-button action | 0.20; define press, release, or complete-click conventions |
| H | Homing between devices | 0.40 |
| M | Mental preparation | 1.35, placed by cognitive unit |
| R | Blocking response time | Given or measured for the task |
| D | Drawing | Do not invent missing parameters |

Some conventions include button actions in K, others separate B. This package uses B to distinguish it from pointing. Never count one click twice. A shortcut label is not automatically one K; define physical-key and modeling conventions.

Place M at genuine preparation or choice. Skilled continuous entry and a natural click after pointing usually do not need M before every element. Explain confirmation after variable entry. Avoid double-counting concurrent waiting or combining a fixed P with a Fitts estimate of the same movement.

Example: known command, correct focus, and hands on keyboard. `ipconfig` has eight characters plus Enter, or nine K. Under `M+9K`, `1.35+9×0.28=3.87 s`. Opening the terminal, changing focus, and waiting for output are excluded.

Report whether parameters are given, illustrative, or measured, with sequence, total, and omissions. Use justified ranges or sensitivity analysis when parameters are uncertain instead of false numerical precision. Validate actual efficiency with target users.

## Fitts: form, units, and limits

Distance A and width W along the movement direction use matching units, with W>0. Distinguish visible geometry from the actionable target.

- Original form: `ID=log2(2A/W)`.
- Shannon form: `ID=log2(A/W+1)`.
- `MT=a+b×ID`, with a in time and b in time/bit.

State the selected form. Coefficients must match its calibration, device, and task. For A=200 px and W=40 px, original ID≈3.322. Assuming a=50 ms and b=150 ms/bit gives MT≈548.3 ms. Shannon ID≈2.585; coefficients fitted to the other form cannot simply be reused as calibrated values.

`IP=ID/MT` has units bit/s when MT is seconds. Formal throughput generally uses repeated trials and effective-width treatment. A single predicted ratio is not measured device performance.

Larger targets and shorter required movements often aid pointing, balanced against accidental activation, occlusion, and discovery. Edge advantages depend on pointer constraints and cannot be assumed for touch, multiple displays, or window edges. Fitts models movement rather than all visual search and decision time.
