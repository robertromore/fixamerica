# Regional Federalism Meta Review Tracker

## Meta

- **Topic:** regional-federalism-meta
- **Target:** plans/regional-federalism/04-meta/
- **Created:** 2026-01-11
- **Last updated:** 2026-01-11 (step 05)
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
- **Input:** plans/regional-federalism/04-meta/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_meta_review_2026_01_11.md
- **Summary:** Reviewed conclusions/gaps for completeness; flagged missing statutory-dependency risk, rights-floor under-specification, boundary revision politics, and lack of explicit prioritization.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_meta_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-meta-review/01-reply_to_regional_federalism_meta_review_2026_01_11.md
- **Summary:** Agreed with all 4 findings; proposed adding gaps for implementation-act dependency, rights-floor content, and boundary revision politics; proposed priority summary table
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-meta-review/01-reply_to_regional_federalism_meta_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-meta-review/02-response_to_claude_meta_reply_2026_01_11.md
- **Summary:** Confirmed implement for all issues; requested Category III placement for implementation dependency, Category IV placement for boundary revision, and a simplified priority table keyed to gap numbers.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-meta-review/02-response_to_claude_meta_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_meta_review_implementation_2026_01_11.md
- **Summary:** Implemented all 4 issues: added priority summary table (Section 2), Gap 7 (implementation-act dependency), Gap 8 (rights-floor content), Gap 11 (boundary revision politics); renumbered existing gaps
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_meta_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-meta-review/03-verify_meta_implementation_2026_01_11.md
- **Summary:** Verified issues 01-04 were implemented with correct placement and priority table; no new issues.
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | medium | Gaps list omits implementation-act dependency and statutory capture risk | resolved | Verified Gap 7 under Category III |
| ISSUE-02 | medium | Gaps list omits rights-floor content under-specification | resolved | Verified Gap 8 under Category III |
| ISSUE-03 | medium | Gaps list omits boundary revision politics as long-horizon risk | resolved | Verified Gap 11 under Category IV |
| ISSUE-04 | low | Gaps list lacks explicit prioritization/triage scheme | resolved | Verified Section 2 priority summary table |

## Agreements Log

Key positions agreed between LLMs:

- Add gaps for implementation-act dependency, rights-floor content, and boundary revision politics.\n- Add a lightweight priority summary table keyed to gap numbers.

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-meta-tracker.md

Your current task is step 05 with status "planned". Review the implementation changes documented in:

.metadata/changelog/claude_codex_regional_federalism_meta_review_implementation_2026_01_11.md

Verify that all 4 issues have been implemented correctly:
- ISSUE-01: Gap 7 (Implementation-act dependency) added to Category III
- ISSUE-02: Gap 8 (Rights-floor content) added to Category III
- ISSUE-03: Gap 11 (Boundary revision politics) added to Category IV
- ISSUE-04: Priority summary table added as Section 2

Check the modified file at plans/regional-federalism/04-meta/02-identified-gaps.md

Create your verification file, then update the tracker:
1. Change step 05 status to "done"
2. Fill in the Output and Summary fields
3. Add next step if issues found, or close review if verified
4. Update "Current State" section with next actor and action
5. Update Issues table statuses (implemented -> resolved or needs_fix)

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-meta-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
