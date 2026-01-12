**Findings**
- Medium: Time-sensitive metrics and adoption counts lack date anchors and citations, which makes the claims hard to verify and likely to drift. This affects the trust/legitimacy table and awareness percentages in current-state, plus adoption counts in overview (e.g., 3,000+ cities, ~30 U.S. cities, NYC $40M+). Consider adding year anchors and sources (or a Sources section) to align with other review standards (`analysis/political/democratic-innovation/01-overview.md:24-29`, `analysis/political/democratic-innovation/01-overview.md:91-95`, `analysis/political/democratic-innovation/01-overview.md:149-151`, `analysis/political/democratic-innovation/02-current-state.md:39-64`, `analysis/political/democratic-innovation/02-current-state.md:70-80`).
- Medium: The current-state section overstates the authority of non-U.S. innovations by describing “citizens' assemblies making binding recommendations” and “sortition bodies with legislative authority.” Most assemblies are advisory or tied to referenda; Belgium’s permanent council is agenda-setting, not legislative. This reads as inaccurate without clarification (`analysis/political/democratic-innovation/02-current-state.md:17-22`).
- Low: Ireland Constitutional Convention membership count is internally inconsistent (100 members vs. 33 politicians + 66 citizens = 99). The missing independent chair should be mentioned or the count corrected (`analysis/political/democratic-innovation/03-history.md:164-165`).
- Low: Model legislation uses many bracketed placeholders ([State], [X], [date], dollar amounts) without a note explaining parameterization or guidance for replacement. Recent reviews in other topics have added explicit placeholder notes or relative timing to reduce ambiguity (`analysis/political/democratic-innovation/11-legislation.md:421-460`, `analysis/political/democratic-innovation/11-legislation.md:517-521`).

**Open Questions**
- Should the overview and current-state use a single consolidated Sources section (like civic-education/congressional-reform) or add inline citations after each table?
- For the “binding recommendations / legislative authority” bullet, do you want to narrow it to advisory bodies with referenda or specify which cases truly have binding authority?
- Do you want a standard placeholder note for model statutes (e.g., “Bracketed fields are state-specific parameters to be filled by drafters”)?

**Suggested Improvements**
- Add date anchors and citations for the trust/legitimacy table, innovation awareness, and adoption counts; consider a Sources section in `analysis/political/democratic-innovation/02-current-state.md` and brief inline citations in `analysis/political/democratic-innovation/01-overview.md`.
- Replace or qualify the “binding recommendations / legislative authority” claims with more precise language (e.g., “advisory recommendations often tied to referenda” and “agenda-setting councils”).
- Fix the Irish Constitutional Convention membership count by adding the independent chair or adjusting totals.
- Add a short note near the model legislation section clarifying bracketed placeholders and suggesting relative timing/percentages where possible.

## Handoff Prompt for Next Actor
Read the review tracker at .metadata/reviews/active/democratic-innovation-tracker.md

Your current task is step 02 with status "planned". Review the findings in .metadata/reviews/llms/codex/democratic_innovation_review_2026_01_11.md, propose resolutions for each issue, and create your response file. Then update the tracker:
1. Change step 02 status to "done"
2. Fill in the Output and Summary fields
3. Add step 03 entry with status "planned" for codex to respond
4. Update "Current State" section with next actor and action
5. Update Issues table if resolutions are agreed
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
