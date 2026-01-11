# Political Analysis Review Tracker

## Meta

- **Topic:** political-analysis
- **Target:** analysis/political/ (top-level files only)
- **Created:** 2026-01-11
- **Last updated:** 2026-01-11
- **Status:** in_progress
- **Participants:** codex (reviewer), claude (implementer)

## Protocol

- Full protocol: `.metadata/protocols/llm-review-protocol.md`
- Each step is append-only with a unique ID
- Statuses: planned | in_progress | done | blocked | no_action
- Include file paths for all referenced artifacts
- Tracker is the single source of truth
- LLMs do not edit each other's output files

## Current State

- **Next actor:** codex
- **Next action:** Verify implementation of political analysis changes
- **Prompt for next actor:** See Handoff Prompts section below

## Steps

### 01

- **Actor:** codex
- **Status:** done
- **Action:** review
- **Input:** analysis/political/ (top-level files only: 01-overview.md through 11-legislation.md)
- **Output:** .metadata/reviews/llms/codex/political_analysis_review_2026_01_11.md
- **Summary:** Flagged missing citations/time-stamps, incomplete synthesis of non-electoral subtopics, and a constitutional feasibility issue in the legislation list.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/political_analysis_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/political-analysis-review/01-reply_to_political_analysis_review_2026_01_11.md
- **Summary:** Agreed with all 3 issues. Proposed: correct Alaska RCV date, add date anchors + Sources section, add cross-link tables for subtopics, add amendment caveat for National Referendum Act.
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/political-analysis-review/01-reply_to_political_analysis_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/political-analysis-review/02-response_to_claude_political_analysis_reply_2026_01_11.md
- **Summary:** Approved all three resolutions with clarifications on date anchors, subtopic link targets, and amendment caveat language.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/political-analysis-review/02-response_to_claude_political_analysis_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_political_analysis_review_implementation_2026_01_11.md
- **Summary:** Implemented all 3 issues: corrected Alaska RCV year, added date anchors and Sources section, added cross-link tables to solutions/roadmap/actions, added amendment caveat for National Referendum Act.
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** planned
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_political_analysis_review_implementation_2026_01_11.md
- **Output:** (pending)
- **Summary:** (pending)
- **Next:** claude

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | medium | Time-sensitive statistics lack citations; Alaska RCV adoption year appears incorrect | implemented | Corrected Alaska RCV year to 2020; added date anchors to all statistics tables; added Sources section |
| ISSUE-02 | medium | Solutions/roadmap omit synthesis or cross-links for several scoped subtopics | implemented | Added cross-link tables to 07-solutions.md, 08-roadmap.md, and 10-actions.md |
| ISSUE-03 | medium | National Referendum Act listed as federal legislation without amendment caveat | implemented | Added asterisk and footnote explaining constitutional amendment requirement |

## Agreements Log

Key positions agreed between LLMs:

- Use dated stats plus a consolidated Sources section for current-state metrics.
- Add cross-link tables instead of expanding top-level synthesis for missing subtopics.
- Keep National Referendum Act listed with an explicit amendment-required caveat.

## Notes

This review covers only the top-level files in `analysis/political/`. Separate reviews should be created for each of the 27 subtopic directories:

- administrative-reform
- budget-process
- campaign-finance
- census-apportionment
- civic-education
- congressional-reform
- constitutional-amendment-process
- democratic-innovation
- direct-democracy
- election-security
- electoral-college
- electoral-reform
- ethics-accountability
- executive-reform
- federalism-reform
- government-transparency
- judicial-reform
- lobbying
- local-democracy
- media-and-information
- party-systems
- political-violence
- primary-reform
- redistricting
- statehood-representation
- voting-rights
- war-powers

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/political-analysis-tracker.md

Your current task is step 05 with status "planned". Verify Claude's implementation by reviewing the changelog at .metadata/changelog/claude_codex_political_analysis_review_implementation_2026_01_11.md and spot-checking the modified files:

- analysis/political/02-current-state.md (date anchors + Sources section)
- analysis/political/03-history.md (Alaska RCV year correction)
- analysis/political/07-solutions.md (cross-link table)
- analysis/political/08-roadmap.md (cross-link table)
- analysis/political/10-actions.md (cross-link table)
- analysis/political/11-legislation.md (National Referendum Act amendment caveat)

Create your verification response, then update the tracker:

1. Change step 05 status to "done"
2. Fill in the Output and Summary fields
3. If issues found, add step 06 for Claude to fix; if verified, mark review complete
4. Update "Current State" section
5. Update Issues table status to "resolved" if verified

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/political-analysis-tracker.md

Your current task is step 06 with status "planned". Address any issues identified by Codex during verification. Review the verification response and fix any problems found.

Update the tracker after completing fixes:
1. Change step 06 status to "done"
2. Fill in the Output and Summary fields
3. Add step 07 for Codex to re-verify if needed
4. Update "Current State" section

Protocol: .metadata/protocols/llm-review-protocol.md
```
