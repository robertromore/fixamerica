# Regional Federalism Analysis Review Tracker

## Meta

- **Topic:** regional-federalism-analysis
- **Target:** plans/regional-federalism/03-analysis/
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
- **Input:** plans/regional-federalism/03-analysis/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_analysis_review_2026_01_11.md
- **Summary:** Reviewed analysis set for rigor and alignment; flagged undefined rights floors, unsupported economic enforcement assumptions, unanchored fiscal-continuation mitigation, and a dangling appendix reference.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_analysis_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-analysis-review/01-reply_to_regional_federalism_analysis_review_2026_01_11.md
- **Summary:** Agreed with all 4 findings; proposed minor_update for ISSUE-01/02 (add implementation notes), implement for ISSUE-03 (add fiscal continuation to Article XVII - Option A recommended), implement for ISSUE-04 (remove dangling Appendix A reference).
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-analysis-review/01-reply_to_regional_federalism_analysis_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-analysis-review/02-response_to_claude_analysis_reply_2026_01_11.md
- **Summary:** Confirmed minor updates for rights-floor and economic enforcement notes, selected Option A for fiscal continuation with guardrails, and approved fixing the Appendix A reference.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-analysis-review/02-response_to_claude_analysis_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_analysis_review_implementation_2026_01_11.md
- **Summary:** Implemented all 4 issues: added rights-floor notes to policy stress test, anti-dumping notes to economic stress test, fiscal continuation default to Article XVII, fixed Appendix A reference
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_analysis_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-analysis-review/03-verify_analysis_implementation_2026_01_11.md
- **Summary:** Verified issues 01-04 were implemented with requested guardrails; no new issues.
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | medium | Rights-floor assumptions in analysis are undefined in design | resolved | Verified implementation notes in policy stress test |
| ISSUE-02 | medium | Anti-dumping penalties/remote-work equalization fees lack formal mechanism | resolved | Verified implementation notes in economic stress test |
| ISSUE-03 | medium | Automatic fiscal continuation not anchored in design defaults | resolved | Verified Article XVII fiscal continuation default with guardrails |
| ISSUE-04 | low | Missing Appendix A reference in authoritarian scenario | resolved | Verified link to armed-forces design document |

## Agreements Log

Key positions agreed between LLMs:

- Analysis assumptions should be flagged as implementation requirements where mechanisms are not yet codified.\n- Fiscal continuation should be constitutionalized with a narrow default (no new programs).

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-analysis-tracker.md

Your current task is step 05 with status "planned". Review the implementation changes documented in:

.metadata/changelog/claude_codex_regional_federalism_analysis_review_implementation_2026_01_11.md

Verify that all 4 issues have been implemented correctly:
- ISSUE-01: Rights-floor implementation notes in plans/regional-federalism/03-analysis/01-stress-testing-policy.md
- ISSUE-02: Anti-dumping implementation notes in plans/regional-federalism/03-analysis/02-stress-testing-economic.md
- ISSUE-03: Fiscal continuation default in Article XVII, Section 2(d) of plans/regional-federalism/02-design/09-constitution.md
- ISSUE-04: Appendix A reference fixed in plans/regional-federalism/03-analysis/05-authoritarian-scenario.md

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
Read the review tracker at .metadata/reviews/active/regional-federalism-analysis-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
