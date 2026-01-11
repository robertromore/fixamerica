# {Topic} Review Tracker

## Meta

- **Topic:** {topic_name}
- **Target:** {path/to/target/}
- **Created:** {YYYY-MM-DD}
- **Last updated:** {YYYY-MM-DD}
- **Status:** in_progress
- **Participants:** {llm_a} (reviewer), {llm_b} (implementer)

## Protocol

- Full protocol: `.metadata/protocols/llm-review-protocol.md`
- Each step is append-only with a unique ID
- Statuses: planned | in_progress | done | blocked | no_action
- Include file paths for all referenced artifacts
- Tracker is the single source of truth
- LLMs do not edit each other's output files

## Current State

- **Next actor:** {llm_name}
- **Next action:** {description of next action}
- **Prompt for next actor:** See Handoff Prompts section below

## Steps

### 01

- **Actor:** {llm_name}
- **Status:** planned
- **Action:** review
- **Input:** {target_path}
- **Output:** (pending)
- **Summary:** (pending)
- **Next:** {other_llm}

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-XX | - | (no issues yet) | - | - |

## Agreements Log

Key positions agreed between LLMs:

- (none yet)

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For {llm_a} (when next actor is {llm_a})

```text
Read the review tracker at .metadata/reviews/active/{topic}-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For {llm_b} (when next actor is {llm_b})

```text
Read the review tracker at .metadata/reviews/active/{topic}-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
