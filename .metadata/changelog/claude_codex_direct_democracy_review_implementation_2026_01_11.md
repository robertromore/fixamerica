# Changelog: Direct Democracy Review Implementation

**Date:** 2026-01-11
**Implementer:** Claude
**Reviewer:** Codex
**Review Tracker:** `.metadata/reviews/active/direct-democracy-tracker.md`

---

## Summary

Implemented 4 agreed changes from the Codex review of the direct democracy analysis files.

## Changes Made

### ISSUE-01: Time-sensitive counts and percentages lack date anchors/sources

**Status:** Resolved

**Files Modified:**
- `analysis/political/direct-democracy/02-current-state.md`

**Changes:**
1. Added date anchor to section header: "## State Ballot Initiative Systems (as of 2024)"
2. Added date anchor to popular referendum section: "Twenty-three states allow citizens to challenge enacted laws (as of 2024)"
3. Added date anchor to recall section: "Nineteen states allow recall of state officials (as of 2024)"
4. Added date anchor to participatory budgeting section header and figures
5. Added inline source: "*Source: Participatory Budgeting Project, 2023.*"
6. Added date anchor to NPV section: "## National Popular Vote Interstate Compact (as of 2024)"
7. Added inline source after NPV table: "*Source: National Popular Vote Interstate Compact, 2024.*"
8. Added consolidated **Sources** section with categories:
   - Initiative, Referendum, and Recall (NCSL, Ballotpedia)
   - Participatory Budgeting (PB Project, NYC Civic Engagement)
   - National Popular Vote (NPVIC)
   - Democratic Innovation (OECD, Ireland Citizens' Assembly)
   - Trust and Engagement (Pew, Gallup, Census Bureau)

---

### ISSUE-02: Initiative-state table implies full list but includes only 10 states

**Status:** Resolved

**Files Modified:**
- `analysis/political/direct-democracy/02-current-state.md`

**Changes:**
1. Changed table introduction from:
   ```
   Twenty-four states allow citizen-initiated ballot measures:
   ```
   To:
   ```
   Twenty-four states allow citizen-initiated ballot measures. Examples of major initiative states:
   ```

2. Added note after table:
   ```
   *Table shows 10 major initiative states. See NCSL for the complete list of all 24 states.*
   ```

---

### ISSUE-03: Ireland Constitutional Convention count omits independent chair

**Status:** Resolved

**Files Modified:**
- `analysis/political/direct-democracy/02-current-state.md`

**Changes:**
1. Updated line 185 from:
   ```
   - 2012-2014: Constitutional Convention (66 citizens + 33 politicians)
   ```
   To:
   ```
   - 2012-2014: Constitutional Convention (100 members: 66 citizens + 33 politicians + 1 independent chair)
   ```

---

### ISSUE-04: Model legislation placeholders lack guidance/notes

**Status:** Resolved

**Files Modified:**
- `analysis/political/direct-democracy/11-legislation.md`

**Changes:**
1. Added placeholder note before State Model Legislation section (after line 414):

```markdown
**Note on Placeholders:**

This model legislation uses bracketed placeholders that states should customize:

- `[State]` - Insert state name
- `[X]` - Insert appropriate numeric value based on state context
- `[$amount]` - Insert dollar amounts appropriate for state cost of living
- `[date]` - Insert effective date
- `[House/Assembly]` - Insert chamber name per state constitution
- `[agency]` - Insert relevant state agency name

Where possible, consider relative thresholds (e.g., percentage of eligible voters rather than fixed numbers) to account for state population differences.
```

---

## Files Modified

| File | Changes |
|------|---------|
| `analysis/political/direct-democracy/02-current-state.md` | Added date anchors, relabeled initiative table as examples, fixed Ireland count, added Sources section |
| `analysis/political/direct-democracy/11-legislation.md` | Added placeholder note before State Model Legislation |

---

## Verification Checklist

- [x] Date anchors added to time-sensitive sections
- [x] Inline sources added for key figures
- [x] Consolidated Sources section added
- [x] Initiative-state table relabeled as examples with NCSL reference
- [x] Ireland Constitutional Convention count corrected to 100
- [x] Placeholder note added to model legislation section
