**Findings**
- Medium: The legal/methodology framing around sampling and disclosure avoidance is inaccurate in several places. "Actual enumeration" is presented as "must count, not sample," the opposition section cites *Utah v. Evans* as allowing sampling, and the resources table describes *Utah v. Evans* as "imputation for overseas military." Differential privacy is labeled "legally required" rather than confidentiality being required with differential privacy as the chosen method. These statements misstate constitutional/statutory constraints and case holdings (`analysis/political/census-apportionment/04-root-causes.md:15-17`, `analysis/political/census-apportionment/06-opposition.md:198-202`, `analysis/political/census-apportionment/09-resources.md:105-110`, `analysis/political/census-apportionment/01-overview.md:209-214`).
- Medium: The 2020 Post-Enumeration Survey table lists Asian net coverage error as -2.62% (undercounted). PES reporting indicates Asian populations were overcounted in 2020; the sign looks inverted and should be verified/corrected with a source (`analysis/political/census-apportionment/02-current-state.md:69-79`).
- Medium: The House expansion proposals table labels "Fifty Thousand" as the "Constitutional minimum." The constitutional minimum is 1 representative per 30,000 people, so this label is incorrect (`analysis/political/census-apportionment/02-current-state.md:185-190`).
- Low: The 2000 Census "Internet option (limited)" claim appears inaccurate; internet self-response was introduced nationally in 2020. The 2000 innovations should be revised to mail/phone operations and other documented changes (`analysis/political/census-apportionment/03-history.md:259-264`).
- Low: Time-sensitive metrics (funding totals, response rates, undercount rates, ACS stats) lack explicit date anchors and source citations in the overview/current-state narrative sections, which diverges from recent project practice on dated metrics and sources (`analysis/political/census-apportionment/01-overview.md:1-118`, `analysis/political/census-apportionment/02-current-state.md:1-170`).
- Low: The model legislation leaves unresolved placeholders (e.g., [date], [amount], [year]) including the federal redistricting deadline, which weakens implementation clarity. These should be replaced with concrete statutory deadlines or clear relative timing guidance (`analysis/political/census-apportionment/11-legislation.md:246-248`, `analysis/political/census-apportionment/11-legislation.md:508-524`, `analysis/political/census-apportionment/11-legislation.md:592-616`).

**Open Questions**
- Can you confirm the intended source for the 2020 Post-Enumeration Survey table (Census Bureau PES release) and whether the Asian net coverage error should be an overcount (+2.62%)?
- For sampling language, do you want it framed as a statutory ban for apportionment (13 U.S.C. 195) with sampling allowed for other purposes, and *Utah v. Evans* described as imputation rather than sampling?
- Should the differential privacy row be rewritten to emphasize legal confidentiality requirements rather than stating differential privacy itself is required?
- For the legislation placeholders, do you prefer specific calendar deadlines (e.g., redistricting completed by Dec 31, 2031) or relative timing (e.g., within 6 months of census data delivery)?
- Do you want a Sources section added to current-state only, or also to overview (and possibly history) for the most-cited metrics?

**Suggested Improvements**
- Correct the sampling/imputation and case law references, and tighten the differential privacy framing to match statutory requirements and Supreme Court holdings.
- Verify and fix the 2020 PES table (Asian net coverage error), with a citation to the Census Bureau PES release.
- Replace the "Constitutional minimum" label in the House expansion proposals table with an accurate description (or change the proposal to reflect the 30,000 ratio if that is intended).
- Update the 2000 Census innovations list to remove the internet option and use documented modernization steps.
- Add date anchors and a Sources section for key metrics in overview/current-state, aligned with project standards.
- Resolve model-legislation placeholders with concrete or relative timing guidance, especially for the federal House expansion redistricting deadline.

## Handoff Prompt for Next Actor
Read the review tracker at .metadata/reviews/active/census-apportionment-tracker.md

Your current task is step 02 with status "planned". Review the findings in .metadata/reviews/llms/codex/census_apportionment_review_2026_01_11.md, propose resolutions for each issue, and create your response file. Then update the tracker:
1. Change step 02 status to "done"
2. Fill in the Output and Summary fields
3. Add step 03 entry with status "planned" for codex to respond
4. Update "Current State" section with next actor and action
5. Update Issues table if resolutions are agreed
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
