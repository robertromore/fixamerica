# Israel-Palestine Managed Coexistence Framework Review Tracker

## Meta

- **Topic:** israel-palestine-coexistence
- **Target:** plans/international/israel-palestine/managed-coexistence-framework
- **Created:** 2026-01-31
- **Last updated:** 2026-01-31
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
- **Next action:** Initial review of target documents
- **Prompt for next actor:** See Handoff Prompts section

## Steps

### 01

- **Actor:** codex
- **Status:** planned
- **Action:** review
- **Input:** plans/international/israel-palestine/managed-coexistence-framework
- **Output:** .metadata/reviews/llms/codex/israel_palestine_coexistence_review_2026_01_31.md
- **Summary:**
- **Next:** claude

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|

## Agreements Log

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/israel-palestine-coexistence-tracker.md

Your current task is the step with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change the current step status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update the Issues table if applicable

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/israel-palestine-coexistence-tracker.md

Your current task is the step with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change the current step status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned" (or set tracker status to "closed" if complete)
4. Update "Current State" section with next actor and action
5. If you identify new issues, add them to the Issues table. If all issues are resolved, consider closing the review.

Protocol: .metadata/protocols/llm-review-protocol.md
```
