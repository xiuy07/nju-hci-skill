# Interaction Design and Experimental Analysis · v2.0.0

[中文](README.md) · [English skill](locales/en/skills/hci-design-research/SKILL.md) · [Chinese skill](skills/hci-design-research/SKILL.md)

`hci-design-research` supports practical interaction projects: implementing principles in interfaces and flows, reviewing usability, planning research and controlled experiments, analyzing data, and explaining design implications. Its primary purpose is design and research work.

## What's new

- Complete Chinese and English packages, each with an entry point, UI metadata, and seven reference documents, sharing capabilities and invocation name.
- Version 2.0.0 with upgrade, rollback, language switching, and project, platform, standard, instrument, and data compatibility guidance.
- Expanded asynchronous states, unknown outcomes, recovery, information architecture, accessible behavior, remote studies, data quality, repeated measurement, effects, and uncertainty.
- Optional human-AI interaction guidance covering expectations, control, correction, and end-to-end usefulness.
- Source attribution, external references, and editorial corrections are centralized in README files.

## Use cases

| Task | Typical input | Expected outcome |
| --- | --- | --- |
| Interface or feature design | Requirements, goals, existing stack | Tasks, states, concrete design or implementation, acceptance |
| Workflow improvement | Interface, screenshots, reproduction steps | Evidence-based findings, impact, tradeoffs, repairs and verification |
| User research | Product decision and target population | Methods, recruitment criteria, tasks, protocol and measures |
| Comparative experiments | Alternatives, variables, constraints | Assignment, sample planning, controls, outcomes and analysis plan |
| Data analysis | Raw data, fields, study description | Quality review, correct inference units, effects and uncertainty |
| Efficiency prediction | Task, starting state, device | GOMS/KLM/Fitts sequences, parameters, calculations and limits |
| Compatibility | Lockfiles, platform versions, baseline | Behavioral differences, minimal adaptation and verification status |

Use for Web, mobile, desktop, and AI-enabled systems while respecting the actual platform. Pure visual styling and coding without interaction decisions do not need the skill. Screenshots, expert inference, predictions, and user measurements provide different evidence. This package does not certify accessibility or industry compliance.

## Install one language

| Package | Repository path | Invocation |
| --- | --- | --- |
| Chinese, default | `skills/hci-design-research` | `$hci-design-research` |
| English | `locales/en/skills/hci-design-research` | `$hci-design-research` |

Copy one complete directory into `$CODEX_HOME/skills/hci-design-research`, usually `~/.codex/skills/hci-design-research` when that variable is unset. Do not install both same-name packages into discovery paths. The installed language does not constrain response language.

Alternatively, ask an installation tool:

```text
Install locales/en/skills/hci-design-research from xiuy07/nju-hci-skill.
```

The private repository requires existing read access. Try invocation on the next turn; reopen the chat or restart the client if discovery has not refreshed. The method package requires no additional runtime or particular model. Analysis and implementation use available environment tools.

## Versioning and migration

`VERSION` and `manifest.json` record release, language entries, and layout. This project's version convention uses major releases for incompatible layout/workflow changes, minor releases for capabilities, and patches for compatible corrections. It does not implement automatic updating.

Back up an existing v1 installation and retain local customizations, then replace it with a complete v2 package. Invocation is unchanged. Experimental analysis is now separate, compatibility and AI interaction are new, and `references/provenance.md` is no longer installed. Confirm a backup before removing obsolete files after an overlay. Roll back using the complete backup or known v1 commit `4e21c59b919d1ebad61ba732494b159705639c6e`.

| Layer | Approach | Verification boundary |
| --- | --- | --- |
| Skill client | Markdown and relative resources; optional `agents/openai.yaml` | Locally checked structure; no universal client/model guarantee |
| Operating system | No OS-specific skill execution scripts | Checked locally on Windows; other systems not run |
| Framework/platform | Inspect project versions and environment | No invented minimum browser/framework and no silent upgrades |
| Accessibility | Explicit WCAG 2.2 baseline when selected | No complete conformance audit; patterns are not normative criteria |
| Statistics software | Method guidance independent of a specific library | No real study analysis or all-version validation performed |
| Research/data | Record builds, protocols, instruments and schemas | Establish comparability before pooling |

External material was accessed on 2026-10-17. A dated WCAG 2.2 Recommendation provides an identifiable baseline. The visited SciPy documentation displayed 1.18.0 and statsmodels displayed 0.15.0. These are documentation snapshots, not installation requirements or a claim of universal testing.

## Contents

Both packages contain identically named references:

- `requirements-design.md`: goals, HTA, information architecture, states, prototypes and tradeoffs.
- `principles-review.md`: principles, walkthroughs, heuristic evaluation, accessible interaction and prioritization.
- `research-evaluation.md`: observation, interviews, surveys, task testing and measures.
- `experimental-analysis.md`: experimental design, data contracts, quality, method selection and interpretation.
- `interaction-models.md`: cognitive foundations, GOMS, KLM, Fitts and parameter limits.
- `compatibility.md`: skill, project, standard, study and data version adaptation.
- `ai-interaction.md`: expectations, control, correction and utility, read only when applicable.

## Examples

```text
Use $hci-design-research to design registration, including weak connections and unknown outcomes.
Use $hci-design-research to review this prototype and separate visible evidence from untested behavior.
Use $hci-design-research to plan a within-subject navigation experiment and analysis.
Use $hci-design-research to analyze these data while preserving pairing and reporting uncertainty.
Use $hci-design-research to fix dialog focus behavior for the installed component version.
```

## Validation and maintenance

Run `python scripts/validate_package.py` to check both layouts, version consistency, internal references, language file parity, and source placement. The skill-creator `quick_validate.py` can also validate each skill directory. Structural checks do not establish user outcomes, translated instrument equivalence, or universal compatibility.

Keep meanings and versions synchronized, check official documentation affected by a change, and rerun checks. Verify actual behavior after changes. See [CHANGELOG.md](CHANGELOG.md).

## Attribution and sources

The foundational material is **organized from the Nanjing University Human-Computer Interaction Systems course**. This is an unofficial adaptation without university or instructor endorsement. The 33-page source PDF, extracted text, and screenshots are not included.

The foundation covers interaction principles, personas and scenarios, requirements and prototypes, HTA, evaluation, experimental design, cognition, GOMS/KLM/Fitts, and UCD. Editorial corrections address participant/expert counts, memory-number overgeneralization, usability/UX simplification, prototype assumptions, study categories, and model notation. Examples, templates, compatibility procedures, and engineering recommendations are synthesized rather than represented as verbatim course or paper content.

The [source register in the Chinese README](README.md#来源与参考) lists primary references, checked on 2026-10-17: Nielsen and Shneiderman, W3C WCAG and APG, GOV.UK user research, Google Research HEART, MacKenzie's modeling work, SciPy and statsmodels method documentation, and Microsoft Research human-AI interaction. Scope and applicability differ across standards, patterns, and methods; this is not a comprehensive academic review. No open-source license is asserted for the original course or third-party materials, and no redistribution rights to those materials are granted.
