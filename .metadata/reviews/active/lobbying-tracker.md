# Lobbying Analysis Review Tracker

## Meta

- **Topic:** lobbying
- **Target:** analysis/political/lobbying/
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
- **Next action:** Initial review of lobbying analysis documents
- **Prompt for next actor:** See Handoff Prompts section below

## Steps

### 01

- **Actor:** codex
- **Status:** planned
- **Action:** review
- **Input:** analysis/political/lobbying/
- **Output:** (pending)
- **Summary:** (pending)
- **Next:** claude

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-XX | - | (no issues yet) | - | - |

## Agreements Log

Key positions agreed between LLMs:

- (none yet)

## Handoff Prompts

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/lobbying-tracker.md

Your current task is step 01 with status "planned". Review the target documents in analysis/political/lobbying/ (files 01-overview.md through 11-legislation.md).

Create your review file at .metadata/reviews/llms/codex/lobbying_review_2026_01_11.md, then update the tracker per the protocol.

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/lobbying-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker per the protocol.

Protocol: .metadata/protocols/llm-review-protocol.md
```
