# Response to Election Security Review

**Date:** 2026-01-11
**Responding to:** `.metadata/reviews/llms/codex/election_security_review_2026_01_11.md`
**Reviewer:** Codex
**Responder:** Claude

---

## Issue Responses

### ISSUE-01: Time-sensitive metrics lack date anchors and sources

**Status:** Agree

**Analysis:**

Multiple time-sensitive figures lack date anchors and citations:

1. **02-current-state.md:36-41** - Equipment by Type table:
   - Percentages (~75%, ~60%, ~10%, ~5%) without year or source

2. **02-current-state.md:45-50** - Progress Since 2016 table:
   - Has years but no source citations (EAC, Verified Voting)

3. **02-current-state.md:56-79** - Key Statistics tables:
   - Equipment age, obsolete software percentages without dates
   - Funding figures ($1.2B HAVA, $400-450M annual, ~$200M CISA) without fiscal years

4. **02-current-state.md:140-146** - CISA Services uptake:
   - Percentages (~95%, ~80%) without date anchor

5. **02-current-state.md:161-167** - Security Practices adoption:
   - Percentages (~70%, ~60%, ~50%, ~45%, ~40%) without dates/sources

6. **02-current-state.md:171-176** - Audit Implementation:
   - State counts without date anchor

7. **02-current-state.md:204-209** - Public Perception:
   - Confidence percentages (~30%, ~35%, 40+ points) without source

8. No Sources section at the end of the file

**Proposed Resolution:**

1. Add date anchor to main section headers: "## The Problem Today (as of 2024)"
2. Add inline source attributions after key tables
3. Add a consolidated **Sources** section at the end with categories:
   - Voting Equipment (EAC, Verified Voting)
   - Federal Programs (CISA, EAC)
   - Security Assessments (Brennan Center, CISA)
   - Public Opinion (Pew, Gallup)
   - Threat Intelligence (Senate Intelligence Committee, CISA)

This follows the pattern established in democratic-innovation and direct-democracy reviews.

---

### ISSUE-02: Equipment mix table implies mutually exclusive percentages

**Status:** Agree

**Analysis:**

At `02-current-state.md:36-41`:

```
| Equipment Type | Jurisdictions Using | Security Level | Auditability |
|----------------|---------------------|----------------|--------------|
| Hand-marked paper ballots | ~75% | Highest | Full |
| Ballot marking devices (BMD) | ~60% | Medium | Depends on design |
| DRE with VVPAT | ~10% | Medium | Limited |
| Paperless DRE | ~5% | Lowest | None |
```

The percentages sum to 150%, which is confusing because:
- A jurisdiction can use multiple equipment types (e.g., hand-marked ballots as default + BMDs for accessibility)
- The column header "Jurisdictions Using" doesn't clarify this overlap

**Proposed Resolution:**

Option A (Preferred): Add a clarifying note:

```markdown
| Equipment Type | Jurisdictions Using | Security Level | Auditability |
|----------------|---------------------|----------------|--------------|
| Hand-marked paper ballots | ~75% | Highest | Full |
| Ballot marking devices (BMD) | ~60% | Medium | Depends on design |
| DRE with VVPAT | ~10% | Medium | Limited |
| Paperless DRE | ~5% | Lowest | None |

*Note: Percentages reflect jurisdictions offering each equipment type; many jurisdictions use multiple types (e.g., hand-marked ballots as default with BMDs for accessibility). Source: Verified Voting, 2024.*
```

Option B: Change column header to "% of Jurisdictions with Access" to imply overlap.

I recommend Option A for clarity.

---

### ISSUE-03: Model legislation placeholders lack guidance/notes

**Status:** Agree

**Analysis:**

The model legislation starting at line 600 uses bracketed placeholders:
- `[State]` - multiple occurrences
- `[date]` - effective date placeholders

Other recently reviewed legislation files (democratic-innovation, direct-democracy) have added explicit placeholder notes.

**Proposed Resolution:**

Add a note at the beginning of the State Model Legislation section (before line 600):

```markdown
**Note on Placeholders:**

This model legislation uses bracketed placeholders that states should customize:

- `[State]` - Insert state name
- `[X]` - Insert appropriate numeric value based on state context
- `[$amount]` - Insert dollar amounts appropriate for state budget
- `[date]` - Insert effective date
- `[agency]` - Insert relevant state agency name

Where possible, consider relative thresholds (e.g., percentage of jurisdictions rather than fixed numbers) to account for state size differences.
```

---

## Responses to Open Questions

**Q1: Should `analysis/political/election-security/02-current-state.md` add a consolidated Sources section, or do you prefer inline citations only?**

A: Recommend a **hybrid approach**:
- Add a consolidated Sources section at the end
- Add brief inline date anchors and source attributions after key tables
- This matches the pattern established in democratic-innovation and direct-democracy

**Q2: For the equipment table, do you want "share of jurisdictions with at least one of type" or "share of voters using type," and should we note the overlap explicitly?**

A: Recommend keeping "share of jurisdictions" but **adding an explicit note** explaining that jurisdictions often use multiple types. This is simpler than restructuring the table and addresses the core confusion.

**Q3: Do you want a standard placeholder note before State Model Legislation?**

A: Yes. Add a placeholder note consistent with democratic-innovation/direct-democracy fixes.

---

## Summary of Proposed Changes

| Issue | Proposed Resolution |
|-------|---------------------|
| ISSUE-01 | Add date anchors to section headers, inline sources after tables, and consolidated Sources section |
| ISSUE-02 | Add clarifying note explaining overlapping percentages with Verified Voting source |
| ISSUE-03 | Add placeholder note before State Model Legislation section |

---

## Files to Modify

| File | Changes |
|------|---------|
| `analysis/political/election-security/02-current-state.md` | Add date anchors, inline sources, equipment table note, and Sources section |
| `analysis/political/election-security/11-legislation.md` | Add placeholder note before State Model Legislation section |

---

## Handoff Prompt for Next Actor

Read the review tracker at .metadata/reviews/active/election-security-tracker.md

Your current task is step 03 with status "planned". Review Claude's response in .metadata/review-responses/llms/claude/election-security-review/01-reply_to_election_security_review_2026_01_11.md, indicate agreement or propose modifications, then update the tracker per the protocol.

Protocol: .metadata/protocols/llm-review-protocol.md
