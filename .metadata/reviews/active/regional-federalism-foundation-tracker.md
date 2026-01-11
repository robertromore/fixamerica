# Regional Federalism Foundation Review Tracker

## Meta

- **Topic:** regional-federalism-foundation
- **Target:** plans/regional-federalism/01-foundation/
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
- **Next action:** Initial review of foundation documents (01-core-idea.md, 02-design-axioms.md)
- **Prompt for next actor:** See Handoff Prompts section below

## Steps

### 01

- **Actor:** codex
- **Status:** planned
- **Action:** review
- **Input:** plans/regional-federalism/01-foundation/
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

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-foundation-tracker.md

Your current task is step 01 with status "planned". Review the target documents in plans/regional-federalism/01-foundation/ (specifically 01-core-idea.md and 02-design-axioms.md), create your review file at .metadata/reviews/llms/codex/regional_federalism_foundation_review_2026_01_11.md, then update the tracker:

1. Change step 01 status to "done"
2. Fill in the Output and Summary fields
3. Add step 02 entry with status "planned" for claude to respond
4. Update "Current State" section with next actor and action
5. Add any issues identified to the Issues table with appropriate severity

Review focus: Examine the core idea and design axioms for internal consistency, completeness, clarity, and any gaps or ambiguities that need resolution.

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-foundation-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
