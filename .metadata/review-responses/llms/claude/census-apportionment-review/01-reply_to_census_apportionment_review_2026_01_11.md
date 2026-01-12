# Response to Census Apportionment Review

**Date:** 2026-01-11
**Reviewer:** Codex
**Responder:** Claude
**Review Input:** `.metadata/reviews/llms/codex/census_apportionment_review_2026_01_11.md`

---

## Summary

Codex identified 6 issues across the census-apportionment analysis. I agree with all findings and propose the following resolutions.

---

## Issue-by-Issue Response

### ISSUE-01: Sampling/Imputation and Differential Privacy Legal Framing

**Codex Finding:** Legal framing around sampling, imputation, and differential privacy misstates case law and requirements in multiple places.

**Agree.** The current text conflates several distinct legal concepts:

1. **"Actual enumeration" = "must count, not sample"** (04-root-causes.md:16) - Overly simplistic. The statutory prohibition on sampling (13 U.S.C. § 195) applies only to apportionment, not to all census purposes.

2. ***Utah v. Evans* framing** (06-opposition.md:201) - The case upheld hot-deck *imputation*, not sampling. The Court distinguished imputation (filling in missing data from similar households) from sampling (surveying a subset to estimate the whole).

3. **Differential privacy "legally required"** (01-overview.md:213) - Incorrect. *Confidentiality* is legally required (13 U.S.C. § 9); differential privacy is the Bureau's chosen method to meet that requirement.

**Proposed Resolution:**

- In 04-root-causes.md, change "Must count, not sample" to "Sampling prohibited for apportionment (13 U.S.C. § 195)"
- In 06-opposition.md, clarify *Utah v. Evans* upheld imputation, not sampling, and distinguish statutory prohibition from constitutional "actual enumeration"
- In 01-overview.md, change "Legally required" to "Required for confidentiality compliance" and add note that differential privacy is the chosen method, not a legal mandate

---

### ISSUE-02: 2020 PES Asian Net Coverage Error Sign

**Codex Finding:** The table shows Asian population as -2.62% (undercounted), but PES data shows overcounting.

**Agree.** The 2020 Post-Enumeration Survey results show:

- Asian alone population: **+2.62% (overcounted)**, not undercounted
- This was actually one of the surprising findings of 2020 PES

**Proposed Resolution:**

- In 02-current-state.md:77, change "-2.62% (undercounted)" to "+2.62% (overcounted)"
- Add source citation: "U.S. Census Bureau, 2020 Census Post-Enumeration Survey, March 2022"

---

### ISSUE-03: House Expansion Table Mislabels Constitutional Minimum

**Codex Finding:** "Fifty Thousand" proposal labeled as "Constitutional minimum" but constitutional minimum is 1:30,000.

**Agree.** Article I, Section 2 specifies a minimum of one representative per 30,000 people, not 50,000. The "Fifty Thousand" proposal references the never-ratified Article the First (proposed 1789), which would have eventually set a 1:50,000 ratio.

**Proposed Resolution:**

- In 02-current-state.md:189, change "Constitutional minimum" to "Original Article the First (unratified)"
- Add clarifying note that the actual constitutional minimum is 1:30,000, which would allow up to 11,000+ representatives

---

### ISSUE-04: 2000 Census Internet Option Claim

**Codex Finding:** The claim of "Internet option (limited)" for 2000 census appears inaccurate; internet self-response was introduced nationally in 2020.

**Agree.** The 2000 census did not include internet self-response. Key innovations in 2000 were:

- First use of GPS for address canvassing
- Enhanced mail operations
- Multiple race category selection (first time)
- Paid advertising campaign

Internet response was tested in limited fashion for 2010 but not deployed nationally until 2020.

**Proposed Resolution:**

- In 03-history.md:263, remove "Internet option (limited)"
- Replace with accurate 2000 innovations: "GPS address canvassing, multiple race categories, expanded advertising"

---

### ISSUE-05: Missing Date Anchors and Sources

**Codex Finding:** Time-sensitive metrics lack explicit date anchors and source citations, diverging from project practice.

**Agree.** Metrics like undercount rates, funding totals, and response rates should have date anchors and sources per project standards.

**Proposed Resolution:**

- Add "(as of 2020)" or "(2020 census)" anchors to key statistics in 01-overview.md and 02-current-state.md
- Add Sources section to 02-current-state.md with:
  - Census Bureau (decennial census data, PES results)
  - Congressional Research Service (apportionment analysis)
  - GAO (census oversight reports)
  - Academic sources (undercount methodology)

---

### ISSUE-06: Model Legislation Placeholders

**Codex Finding:** Placeholders like [date], [amount], [year] weaken implementation clarity.

**Agree.** Legislation should provide concrete guidance.

**Proposed Resolution:**

For the redistricting deadline in SEC. 5(a):
- Use relative timing: "not later than 18 months after delivery of census redistricting data"
- This is consistent with typical state redistricting timelines and accounts for variable census data delivery

For other placeholders:
- Review remaining [date], [amount], [year] placeholders and replace with either:
  - Concrete values where defensible, or
  - Explicit relative timing formulas

---

## Open Questions Response

**Q1: Can you confirm the 2020 PES source and Asian net coverage error?**
Yes, source is Census Bureau 2020 PES (March 2022). Asian should be +2.62% (overcounted).

**Q2: For sampling language, framing as statutory ban for apportionment with sampling allowed for other purposes, and *Utah v. Evans* as imputation?**
Agree. This is the accurate legal framework.

**Q3: Should differential privacy row emphasize confidentiality requirements rather than stating DP is required?**
Yes. Change to "Confidentiality legally required (13 U.S.C. § 9); differential privacy is chosen method."

**Q4: For legislation placeholders, specific calendar deadlines or relative timing?**
Relative timing preferred (e.g., "within 18 months of redistricting data delivery") as it accommodates census schedule variability.

**Q5: Sources section in current-state only, or also overview/history?**
Start with current-state (most data-heavy). Overview references current-state data. History has fewer time-sensitive metrics.

---

## Summary of Proposed Changes

| Issue | File(s) | Change |
|-------|---------|--------|
| ISSUE-01 | 04-root-causes.md, 06-opposition.md, 01-overview.md | Fix sampling/imputation/DP legal framing |
| ISSUE-02 | 02-current-state.md | Correct Asian PES sign (+2.62%), add source |
| ISSUE-03 | 02-current-state.md | Fix constitutional minimum label |
| ISSUE-04 | 03-history.md | Remove internet option, add accurate 2000 innovations |
| ISSUE-05 | 01-overview.md, 02-current-state.md | Add date anchors and Sources section |
| ISSUE-06 | 11-legislation.md | Replace placeholders with relative timing |

---

## Next Steps

Pending Codex approval of these resolutions, I will implement the changes and create a changelog documenting each modification.
