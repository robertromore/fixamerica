# Regional Federalism Review Tracker

## Meta

- **Topic:** regional-federalism
- **Target:** plans/regional-federalism/
- **Created:** 2026-01-11
- **Last updated:** 2026-01-11 (step 09)
- **Status:** closed
- **Participants:** codex (reviewer), claude (implementer)

## Protocol

- Full protocol: `.metadata/protocols/llm-review-protocol.md`
- Each step is append-only with a unique ID
- Statuses: planned | in_progress | done | blocked | no_action
- Include file paths for all referenced artifacts
- Tracker is the single source of truth
- LLMs do not edit each other's output files

## Current State

- **Next actor:** none
- **Next action:** Review closed (all issues resolved, verification complete)
- **Prompt for next actor:** N/A

## Steps

### 01

- **Actor:** codex
- **Status:** done
- **Action:** review
- **Input:** plans/regional-federalism/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_plan_review_2026_01_11.md
- **Summary:** Initial review: 6 findings (2 critical, 4 medium), 4 open questions, 4 suggested improvements
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_plan_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-review/01-reply_to_regional_federalism_plan_review_2026_01_11.md
- **Summary:** Accepted most findings; split constitutional vs statutory; proposed specific implementations
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-review/01-reply_to_regional_federalism_plan_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-review/01-response_to_claude_reply_to_regional_federalism_plan_review_2026_01_11.md
- **Summary:** Agreed with Claude adjustments; resolved disagreements on turnout thresholds, two-key authorization, boundary criteria, presidential selection, malapportionment caps
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-review/01-response_to_claude_reply_to_regional_federalism_plan_review_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_review_implementation_2026_01_11.md
- **Summary:** Implemented 9 major changes: boundary revision (Art I.4), presidential selection (Art VI), amendment thresholds (Art X), two-key authorization (Art XII.2), DC/territories/tribal (Art XVI), congressional defaults (Art XVII), fiscal council anti-capture (Sec 11.4), court capacity (Sec 9.3)
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-review/02-response_to_claude_claude_codex_regional_federalism_review_implementation_2026_01_11.md
- **Summary:** Found 4 issues: boundary blackout permanent, election default conflicts with NPV, DC double representation, default equalization incentive
- **Next:** claude

### 06

- **Actor:** claude
- **Status:** done
- **Action:** fix
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-review/02-response_to_claude_claude_codex_regional_federalism_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-review/02-reply_to_codex_response_to_implementation_2026_01_11.md
- **Summary:** Fixed all 4 issues: changed blackout to 18-month window, explicitly superseded Electoral College, separated DC provisions, added declining equalization rate
- **Next:** codex

### 07

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-review/02-reply_to_codex_response_to_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-review/03-response_to_claude_02_reply_to_codex_response_to_implementation_2026_01_11.md
- **Summary:** Acknowledged all 4 fixes; flagged 1 remaining gap: default majority-winner mechanism unspecified
- **Next:** claude

### 08

- **Actor:** claude
- **Status:** done
- **Action:** fix
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-review/03-response_to_claude_02_reply_to_codex_response_to_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-review/03-reply_to_codex_response_to_implementation_followup_2026_01_11.md
- **Summary:** Added default runoff mechanism to Art XVII.2(c): 21-day runoff between top two if no majority; Congress can supersede with RCV or other mechanism
- **Next:** codex

### 09

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-review/03-reply_to_codex_response_to_implementation_followup_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-review/04-verify_default_majority_winner_fix_2026_01_11.md
- **Summary:** Verified Article XVII.2(c) adds default 21-day runoff for majority requirement; no new issues
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | critical | Regional boundaries constitutionally frozen | resolved | Article I.4 boundary revision mechanism |
| ISSUE-02 | high | Presidential selection ambiguous | resolved | Article VI national popular vote + majority requirement |
| ISSUE-03 | high | Amendment thresholds vague ("supermajority") | resolved | Article X numeric thresholds (2/3, 3/4, 7-year window) |
| ISSUE-04 | high | Two-key authorization keyholders undefined | resolved | Article XII.2 President + Regional Governors supermajority |
| ISSUE-05 | medium | DC/territories/tribal nations unaddressed | resolved | Article XVI non-state entities |
| ISSUE-06 | medium | No congressional default rules | resolved | Article XVII self-executing defaults |
| ISSUE-07 | medium | Fiscal council capture risk | resolved | Section 11.4 anti-capture provisions |
| ISSUE-08 | medium | Court capacity during transition | resolved | Section 9.3 staffing and funding provisions |
| ISSUE-09 | low | Boundary blackout was permanent (4-year cycle) | resolved | Changed to 1 year before / 6 months after elections |
| ISSUE-10 | low | Election default referenced Electoral College | resolved | Explicitly superseded Electoral College |
| ISSUE-11 | low | DC double representation (congress + region) | resolved | Separated congressional/presidential/regional provisions |
| ISSUE-12 | low | Default equalization could incentivize inaction | resolved | Declining rate 5% -> 2% floor starting year 6 |
| ISSUE-13 | low | Default majority-winner mechanism unspecified | resolved | Art XVII.2(c) default runoff within 21 days |

## Agreements Log

Key positions agreed between LLMs:

- No turnout thresholds for amendments (prevents boycott incentive) - Codex position adopted
- Two-key authorization uses Regional Governors, not Congress - Claude position accepted
- Boundary criteria statutory, not constitutional - Codex position adopted
- Presidential selection method (RCV vs other) left to statute - Codex position adopted
- Hard malapportionment caps avoided where principles suffice - Codex position adopted
- Declining defaults create pressure for Congress to act - Codex position adopted

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-tracker.md

Your current task is step 08 with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step 08 status to "done"
2. Fill in the Output and Summary fields
3. Add step 09 entry with status "planned"
4. Update "Current State" section with next actor and action
5. If this resolves ISSUE-13, update the Issues table

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-tracker.md

Your current task is step 09 with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step 09 status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned" (or set tracker status to "closed" if complete)
4. Update "Current State" section with next actor and action
5. If you identify new issues, add them to the Issues table. If all issues are resolved, consider closing the review.

Protocol: .metadata/protocols/llm-review-protocol.md
```
