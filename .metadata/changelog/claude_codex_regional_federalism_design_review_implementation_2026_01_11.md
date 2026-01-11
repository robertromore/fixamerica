# Changelog: Claude-Codex Regional Federalism Design Review Implementation

**Date:** 2026-01-11
**Reviewers:** Codex (reviewer), Claude (implementer)
**Tracker:** `.metadata/reviews/active/regional-federalism-design-tracker.md`

---

## Summary

This changelog documents changes to the Regional Federalism design documents and constitution following a review cycle between Codex and Claude. The review identified cross-document conflicts (elections, armed-forces) and mechanism gaps (judicial timelines, federal lawmaking procedure).

**Review Chain:**
1. `.metadata/reviews/llms/codex/regional_federalism_design_review_2026_01_11.md`
2. `.metadata/review-responses/llms/claude/regional-federalism-design-review/01-reply_to_regional_federalism_design_review_2026_01_11.md`
3. `.metadata/review-responses/llms/codex/regional-federalism-design-review/02-response_to_claude_design_reply_2026_01_11.md`

---

## Changes Implemented

### ISSUE-01: Presidential Selection Method Aligned with Constitution

**File:** `plans/regional-federalism/02-design/02-elections.md`
**Location:** Section 9.2

**Change:** Updated presidential selection mechanism to match constitution's national popular vote requirement.

**Content changed:**
- Replaced "national popular vote or proportional regional vote (per design)" with "national popular vote (as mandated by Article VI, Section 2)"
- Added design note explaining proportional regional vote was explored but not adopted
- Added forward link to Article VI, Section 2(c)

---

### ISSUE-02: Two-Key Authorization Aligned with Article XII

**File:** `plans/regional-federalism/02-design/06-armed-forces.md`
**Location:** Section 9.1

**Change:** Updated two-key authorization to mirror exact constitutional keyholders and fallback.

**Content changed:**
- Replaced list of "possible combinations" with constitutional keyholders:
  - Key 1: President (or Chief Justice if President is party to crisis)
  - Key 2: Supermajority (2/3) of Regional Governors
- Added timing/expiry reference to Article XII, Section 2 (48-hour window, 30-day expiration, 72-hour disclosure)
- Added design note explaining alternative combinations were explored but not adopted

---

### ISSUE-03: Judicial Timelines Added to Constitution

**File:** `plans/regional-federalism/02-design/09-constitution.md`
**Location:** Article XI, Section 2

**Change:** Added explicit 30/30/30 day timelines for mandatory jurisdiction cases.

**Content added:**
- (a) Specific timeframes: trial 30 days, appellate 30 days, Supreme Court 30 days
- (b) Extension cap: 15 additional days per level, only for cause, in writing
- (c) Default trigger: failure to decide within time limit triggers self-executing defaults of Section 4

---

### ISSUE-04: Federal Lawmaking Procedure Added

**File:** `plans/regional-federalism/02-design/09-constitution.md`
**Location:** Article IV, Section 5 (new)

**Change:** Added explicit federal lawmaking procedure under narrowed Senate powers.

**Content added:**
- (a) Bills introduced in House within enumerated federal powers
- (b) House passage leads to presidential presentation
- (c) Presidential veto override: House two-thirds vote
- (d) Senate has no veto over ordinary legislation
- (e) Interregional coordination bills: Senate may delay 60 days; designation must be by prior statute, no retroactive expansion
- (f) Anti-expansion clause: only Congress can define delay categories

**File:** `plans/regional-federalism/02-design/03-institutions.md`
**Location:** Section 5.3a (new)

**Change:** Added corresponding explanation of federal lawmaking under narrowed Senate powers.

**Content added:**
- Step-by-step lawmaking path (House → President → signature/override)
- Enumeration of Senate's limited powers
- Explanation of 60-day interregional coordination delay
- Forward link to Article IV, Section 5

---

## Agreements Reached

- Elections design conforms to constitution's national popular vote requirement
- Armed-forces design mirrors Article XII keyholders and fallback with timing referenced
- Judicial deadlines are constitutional (explicit 30/30/30 + limited extensions)
- Federal lawmaking is explicit: House-led path, House two-thirds override, tightly scoped Senate delay with anti-expansion clause

---

## Files Modified

| File | Changes |
|------|---------|
| `plans/regional-federalism/02-design/02-elections.md` | Updated Section 9.2 with NPV mandate and design note |
| `plans/regional-federalism/02-design/06-armed-forces.md` | Updated Section 9.1 with constitutional keyholders and timing reference |
| `plans/regional-federalism/02-design/09-constitution.md` | Added Article XI Section 2 timelines; added Article IV Section 5 federal lawmaking |
| `plans/regional-federalism/02-design/03-institutions.md` | Added Section 5.3a federal lawmaking explanation |
