# Version and Platform Compatibility

## Separate four kinds of version

Track skill, project/platform, standard/pattern, and study/data versions independently. Updating the skill does not prove a project is compatible. Examine only dimensions relevant to the decision.

This skill is version 2.0.0. Chinese and English packages share an invocation name and capability boundary; install one language package. Markdown instructions are the core. Client UI metadata support may vary. Do not claim an unverified minimum client, model, or operating-system version.

## Adapt an actual project

1. Read configuration, lockfiles, runtime information, and user constraints to establish versions. Prefer code and observed behavior to guesses. Mark unavailable versions unknown.
2. Locate behavior affected by differences: dialog focus, routing history, validation, announcements, or statistical API arguments. Do not force an upgrade without a relevant difference.
3. Consult official documentation for the applicable version. Distinguish normative requirements, recommended patterns, and component implementations. Latest documentation does not prove an older version supports a feature.
4. Choose the smallest viable approach: existing component behavior, local compatibility handling, fallback, or a proposed upgrade requiring a project decision. Preserve the stack and avoid silent major dependency changes.
5. Verify relevant tasks and input methods in the target environment. Label results tested, documentation-only, unverified, or not applicable. Intended compatibility is not demonstrated support.

Use a short matrix only when useful:

| Environment/version | Behavior | Approach | Evidence/status |
| --- | --- | --- | --- |
| Locked component library | Focus restoration after dialog close | Prefer existing callback; supplement if needed | Record actual runtime outcome |
| Target browser/screen-reader pair | Status perception | Appropriate semantics and verification | Explicitly pending if untested |
| Installed statistics library | Parameters and result fields | Use supported interfaces | Run the relevant minimal calculation |

## Platforms and standards

Web CSS pixels are not interchangeable with native points or density units. Mobile testing includes keyboards, touch, and lifecycle; desktop testing includes keyboard access and multiple windows. Hybrid apps follow actual embedded behavior. Similar-looking components may have different input conventions.

WCAG 2.2 may be an explicitly selected Web baseline; it does not impose a universal project conformance level. Conformance is a complete-scope claim. Pattern guidance and automated scanning cannot replace the standard. When migrating an older baseline, identify changed, additional, and untested requirements. A candidate newer standard is not automatically an adopted requirement.

Language switching also affects expansion, date and number formats, time zones, sorting, input methods, and terminology. Reports follow the user's language regardless of the installed package language.

## Research and analysis versions

Record product build, prototype, task wording, instrument language/version, event definitions, assignment logic, data schema, and analysis software. If builds change between conditions, do not attribute every difference to the target design.

Before merging data, map units, events, and categories and retain conversion rules. Translation does not automatically establish instrument measurement equivalence; report separately without adequate comparability. Preserve cleaning, seed, and software details. If an older library lacks an interface, use an appropriate equivalent or report the limitation.

## Upgrade and rollback

The invocation remains `$hci-design-research`. Back up the installed directory and inspect local customizations before upgrading. Replace the complete package to avoid mixed-language or obsolete files. Version 2 separates experimental analysis and adds compatibility and AI interaction; source attribution lives in repository README files.

Switch languages by installing one complete package into the same destination, not two discoverable packages with the same name. Restore a complete backup or known old commit for rollback. A version string on disk does not prove a client reloaded it; confirm through subsequent actual reads.
