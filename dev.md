# Development and release notes

The public title is **Strategist Assistant**. The internal runtime folder remains `maa_war_planner` so existing script identities and campaign data keep their names.

## Source and publication copy

Runtime files are under `mod/maa_war_planner/`. The portable launcher descriptor is `maa_war_planner.mod`. The English publication description is projected to `publishing/description.en.md`; README and store variants are generated from the release author's canonical description. Change that canonical source and rerender rather than maintaining separate feature descriptions.

The mod is a standalone implementation. War Planner was inspected during initial research; no dependency or copied third-party source was established by that review. No open-source licence has been selected. Repository availability alone must not be represented as an MIT or other permissive licence.

## Verification

Use `python -B tools/verify_runtime.py` for the exported runtime inventory and `python -B -m unittest discover -s tests` for the portable package checks. These static checks do not replace CK3 runtime verification.

Gameplay acceptance belongs to the tested DEV source. The public export inherits that evidence only after a file comparison with its explicit packaging changes. Localization acceptance checks all target-game languages, referenced keys, syntax and substitutions statically; a separate game launch for each language is not required.

Native scenarios cover selected governments, purchases, resource budgets, transaction recovery and interface callbacks. They do not establish universal compatibility with other mods, every campaign state or all future game patches. The final in-game save checks reported by the owner are **USER_REPORTED**; their exact sequence was not enumerated, and they are separate from automated native evidence. Calendar accrual in the most recent income investigation was **NOT_VERIFIED** after a native event interrupted the probe; the release does not claim that probe passed.

## Contributions and reports

For gameplay changes, describe the affected mechanic, retain unrelated changes, and test the relevant behavior in an isolated CK3 profile. Report the exact source revision and remaining limitations. Avoid introducing unverified resource conversions or treating a static check as engine acceptance.

For bug reports, provide the game version, active mod list, ruler/government, upkeep mode and a reproducible save when possible. Use the [GitHub issue tracker](https://github.com/G4VV4KH/-CK3-Strategist-Assistant/issues), or email **g4vv4kh@gmail.com**.
