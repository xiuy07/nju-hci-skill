# Controlled Experiments and Data Analysis

## Define the estimand

State the decision, primary outcome, comparison direction, and smallest meaningful difference. Define H0/H1, independent and dependent variables, controls, and assignment units. When success, errors, time, and workload coexist, identify primary outcomes and guardrails before inspecting results.

Experiments typically combine intervention and random assignment; quasi-experiments intervene without complete randomization; observational studies primarily observe. Group count and repeated measurement alone do not establish the category. Do not claim randomization without evidence or infer causation from association alone.

## Design structure

- Between-subjects designs expose different participants to conditions and avoid within-person transfer while requiring attention to individual differences.
- Within-subjects designs preserve pairing and require attention to learning, fatigue, and carryover. AB/BA, random order, and Latin squares address different effects without guaranteeing complete elimination.
- Matched participants are different people paired on relevant characteristics. Matching controls only those characteristics and is not the same as repeated measurement of one person.
- Factorial designs retain factors and interactions. Mixed designs include between- and within-subject factors. A strict split-plot design also involves randomization levels, so analyze the actual structure.

Plan sample size using a target effect or precision, variability, design, primary outcome, and attrition. Pilots inform feasibility and variability but small pilot effect estimates are unstable. Fixed counts do not guarantee power; observed post-hoc power does not resolve uncertainty.

For online experiments, distinguish assignment, exposure, and return visits. Check unexpected assignment ratios, contamination, and logging changes. Set analysis windows and stopping rules; repeatedly checking ordinary p-values and stopping at significance is inappropriate. Use a corresponding design for sequential analysis.

## Data contract and quality

Prefer a suitable long format. Candidate fields are `participant_id, condition, task_id, trial, order, success, time_ms, error_count, assistance, app_version, device, exclusion_reason`. Adapt to actual data without requesting unrelated personal information.

Reconstruct assignment, observation, and inference units. Thirty trials from one participant do not create thirty independent participants. Preserve A/B pairing within people. When both people and tasks repeat, justify aggregation or use a model expressing dependence.

Keep raw data unchanged and save cleaning and derived results separately. Check keys, duplicates, units, impossible times, mislabeled conditions, missingness, failure, attrition, and software changes. Do not remove observations to obtain significance. Before combining instrument or schema versions, establish semantic and scoring compatibility.

## Describe before inferring

Show participants, trials, successes, failures, missingness, and denominators by condition. Examine timing distributions and anomalies. Provide suitable quantiles or explain transformations for skewed times. Successful-attempt timing is conditional; report success and inclusion scope alongside it.

Use plots that reveal paired changes, distributions, and intervals. A large number of trial points must not imply a large independent sample. Aggregate and estimate uncertainty at the appropriate level.

| Question and structure | Candidate methods | Conditions to examine |
| --- | --- | --- |
| Independent continuous means | Welch t, appropriate robust or resampling methods | Independent units, distribution, outliers, target quantity |
| Paired continuous outcomes | Paired differences, paired t, suitable nonparametric or resampling methods | Difference structure and independence across people; Wilcoxon also has assumptions |
| Independent binary outcomes | Proportion differences and intervals, Fisher/chi-square, suitable regression | Denominators, sparse cells, clustering |
| Paired binary outcomes | Paired methods such as McNemar | Construct the table from within-person discordance |
| Multiple factors or repeated observations | Design-appropriate models, repeated-measures analysis, mixed models | Interactions, participant/task dependence, fit |
| Counts, rates, or bounded outcomes | Response-distribution-appropriate models | Exposure, overdispersion, boundaries, excess zeros |

The table guides selection rather than requiring every test. A significant normality test alone should not mechanically determine the method. Examine the estimand and assumptions. Linear mixed models do not automatically suit binary outcomes; use an appropriate generalized model.

Bootstrap independent or clustered units appropriately and resample paired observations together. Record interval method, resample count, seed, and software versions. Very small samples and degenerate distributions can limit reliability. Check installed APIs before implementation instead of silently upgrading from online documentation.

## Interpret for the design decision

Report directional differences or ratios with units, a suitable effect measure, uncertainty intervals, and assumptions. Distinguish percentage points from relative percentages. Define the denominator for standardized paired effects. A p-value is not the probability that a design is better; failure to reject H0 does not establish equivalence.

Declare multiplicity handling or exploratory status for multiple outcomes or comparisons. Equivalence and non-inferiority require defensible prespecified margins and suitable analysis. Insufficient information remains uncertain even after trying another test.

Connect results to design: faster performance with more errors requires a tradeoff; an overall improvement can hide a subgroup regression. Treat underpowered subgroup findings as exploratory. Deliver reproducible code or calculation records, cleaning rules, descriptions, effects and intervals, limitations, and further validation at the length the user needs.
