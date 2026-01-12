# Census Apportionment Review Implementation Changelog

**Date:** 2026-01-11
**Reviewer:** Codex
**Implementer:** Claude
**Review Input:** `.metadata/review-responses/llms/codex/census-apportionment-review/02-response_to_claude_census_apportionment_reply_2026_01_11.md`

---

## Summary

Implemented 6 issues identified in the census-apportionment review. Changes include legal framing corrections, data fixes, date anchors, sources, and legislation placeholder resolutions.

---

## Changes by Issue

### ISSUE-01: Sampling/Imputation and Differential Privacy Legal Framing

**Files Modified:**
- `analysis/political/census-apportionment/01-overview.md`
- `analysis/political/census-apportionment/04-root-causes.md`
- `analysis/political/census-apportionment/06-opposition.md`
- `analysis/political/census-apportionment/09-resources.md`

**Changes:**

**01-overview.md (Line 213):**
- Changed "Legally required" to "Meets confidentiality requirements (13 U.S.C. § 9)"
- Clarifies that confidentiality is required but differential privacy is the chosen method

**04-root-causes.md (Line 16):**
- Changed "Must count, not sample | Expensive, inaccurate for mobile populations" to "Sampling prohibited for apportionment (13 U.S.C. § 195) | Expensive, limits statistical methods"
- Accurately cites the statutory prohibition and its scope

**06-opposition.md (Line 201):**
- Changed "*Utah v. Evans* allowed sampling for some purposes" to "*Utah v. Evans* upheld imputation (distinct from sampling); 13 U.S.C. § 195 prohibits sampling for apportionment"
- Correctly distinguishes imputation from sampling

**09-resources.md (Line 109):**
- Changed "*Utah v. Evans* | 2002 | Imputation for overseas military | Allowed" to "*Utah v. Evans* | 2002 | Hot-deck imputation for missing household data | Upheld (distinct from sampling)"
- Accurately describes the case holding

---

### ISSUE-02: Asian PES Sign Correction

**File:** `analysis/political/census-apportionment/02-current-state.md`

**Changes:**
- Line 77: Changed "Asian | -2.62% (undercounted)" to "Asian | +2.62% (overcounted)"
- Added source citation: "U.S. Census Bureau, 2020 Post-Enumeration Survey, March 2022"

**Before:**
```markdown
| Asian | -2.62% (undercounted) |
```

**After:**
```markdown
| Asian | +2.62% (overcounted) |

*Source: U.S. Census Bureau, 2020 Post-Enumeration Survey, March 2022.*
```

---

### ISSUE-03: Constitutional Minimum Label Fix

**File:** `analysis/political/census-apportionment/02-current-state.md`

**Changes:**
- Line 191: Changed "Fifty Thousand | 6,600+ | Constitutional minimum" to "Fifty Thousand | 6,600+ | Original Article the First (unratified)"
- Added clarifying note about actual constitutional minimum (1:30,000)

**Before:**
```markdown
| Fifty Thousand | 6,600+ | Constitutional minimum |
```

**After:**
```markdown
| Fifty Thousand | 6,600+ | Original Article the First (unratified) |

*Note: The constitutional minimum is 1 representative per 30,000 people (Article I, Section 2), which would allow up to 11,000+ representatives. The "Fifty Thousand" proposal references the original unratified Article the First from 1789.*
```

---

### ISSUE-04: 2000 Census Internet Option Removal

**File:** `analysis/political/census-apportionment/03-history.md`

**Changes:**
- Lines 263-264: Removed incorrect "Internet option (limited)" and replaced with accurate 2000 innovations

**Before:**
```markdown
| Internet option (limited) | Technology modernization |
| Multiple race categories | First time allowed |
```

**After:**
```markdown
| GPS for address canvassing | Improved geographic accuracy |
| Multiple race categories | First time respondents could select multiple races |
```

---

### ISSUE-05: Date Anchors and Sources Section

**Files Modified:**
- `analysis/political/census-apportionment/01-overview.md`
- `analysis/political/census-apportionment/02-current-state.md`

**Changes:**

**01-overview.md:**
- Line 120: Changed "## By the Numbers" to "## By the Numbers (2020 Census)"

**02-current-state.md:**
- Line 120: Changed "## Key Statistics" to "## Key Statistics (2020 Census)"
- Lines 376-403: Added comprehensive Sources section with:
  - Census Bureau (census results, PES, apportionment)
  - Congressional Research Service (apportionment analysis)
  - Government Accountability Office (census oversight reports)
  - Academic Sources (Balinski & Young, National Academies)
  - Legal Sources (key Supreme Court cases)

---

### ISSUE-06: Legislation Placeholder Resolution

**File:** `analysis/political/census-apportionment/11-legislation.md`

**Changes:**

**Federal Legislation:**
- Line 247: Changed "[date]" to "18 months after delivery of decennial census redistricting data" (redistricting deadline)

**State Model Legislation:**
- Line 463: Added note explaining that bracketed fields are state-specific parameters
- Line 508: Changed "[date]" to "60 days following delivery of decennial census redistricting data" (data transmission)
- Line 524: Changed "[date]" to "90 days following delivery of decennial census redistricting data" (database availability)
- Line 616: Changed "[date]" to "18 months following Census Day" (final report)
- Line 622: Changed "[date following completion of census cycle]" to "24 months following delivery of decennial census redistricting data" (sunset)

**Note added:**
> *In model legislation below, bracketed fields such as [State], [Department of Corrections], [Secretary of State], and $[amount] are state-specific parameters to be filled by enacting legislatures. Timing provisions use relative dates tied to census milestones.*

---

## Files Modified

| File | Changes |
|------|---------|
| `analysis/political/census-apportionment/01-overview.md` | DP legal framing, date anchor |
| `analysis/political/census-apportionment/02-current-state.md` | Asian PES sign, constitutional minimum label, date anchor, Sources section |
| `analysis/political/census-apportionment/03-history.md` | 2000 census innovations |
| `analysis/political/census-apportionment/04-root-causes.md` | Sampling/enumeration legal framing |
| `analysis/political/census-apportionment/06-opposition.md` | Utah v. Evans framing |
| `analysis/political/census-apportionment/09-resources.md` | Utah v. Evans case description |
| `analysis/political/census-apportionment/11-legislation.md` | Placeholder resolutions, state model note |

---

## Verification Checklist

- [x] Differential privacy framed as confidentiality compliance method, not legal requirement
- [x] Sampling prohibition correctly cited as 13 U.S.C. § 195 for apportionment only
- [x] *Utah v. Evans* correctly described as hot-deck imputation (not sampling, not overseas military)
- [x] Asian PES corrected to +2.62% (overcounted) with source citation
- [x] "Fifty Thousand" relabeled as Article the First (unratified) with 1:30,000 minimum note
- [x] 2000 census internet option removed; GPS canvassing added
- [x] Date anchors added to statistics headers in overview and current-state
- [x] Sources section added to current-state with Census Bureau, CRS, GAO, academic, legal sources
- [x] Federal legislation placeholders replaced with relative timing
- [x] State model legislation note added explaining bracketed parameters
- [x] State model timing placeholders replaced with census-milestone-relative dates

---

## References

- `.metadata/reviews/llms/codex/census_apportionment_review_2026_01_11.md`
- `.metadata/review-responses/llms/claude/census-apportionment-review/01-reply_to_census_apportionment_review_2026_01_11.md`
- `.metadata/review-responses/llms/codex/census-apportionment-review/02-response_to_claude_census_apportionment_reply_2026_01_11.md`
