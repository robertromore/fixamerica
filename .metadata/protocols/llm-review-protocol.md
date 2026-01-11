# LLM Review Collaboration Protocol

## Overview

This protocol enables structured collaboration between LLMs for document review, response, and implementation cycles.

## Core Rules

1. **Single source of truth**: The tracker file is authoritative. All other files (reviews, responses, changelogs) are referenced from it.
2. **Append-only outputs**: LLMs do not edit each other's output files. Corrections are made in new response files.
3. **Ownership rule**: Only the actor assigned to a step can mark it `done`.
4. **Date format**: Use `YYYY_MM_DD` in all file names (snake_case).
5. **Single actor handoff**: The `Next` field must specify exactly one actor to avoid ambiguity.
6. **Cite locations**: Verification and fix steps must cite specific file paths and section/line numbers when relevant.

## Roles

Roles are assigned per review in the tracker's Meta section:

- **Reviewer**: Analyzes documents, identifies issues, proposes improvements
- **Implementer**: Responds to reviews, makes changes, documents work

Either LLM can take either role. Roles are set when the review is created and remain fixed for that review.

## Action Types

| Action | Description | Expected Output |
|--------|-------------|-----------------|
| review | Initial analysis of target documents | Findings, open questions, suggestions |
| response | Reply to review or counter-response | Agreements, disagreements, proposals |
| implement | Make agreed changes to source files | Changelog entry + modified files |
| verify | Check implementation for correctness | Acknowledgement or issue list |
| fix | Address issues found in verification | Updated changelog + fixes |

## Tracker Structure

Each tracker contains these sections:

### Meta

Basic information about the review (update `Last updated` on every tracker edit):

```markdown
## Meta
- **Topic:** {topic_name}
- **Target:** {path/to/target/}
- **Created:** {YYYY-MM-DD}
- **Last updated:** {YYYY-MM-DD}
- **Status:** {in_progress|closed}
- **Participants:** {llm_a} (reviewer), {llm_b} (implementer)
```

### Current State

The active handoff information:

```markdown
## Current State
- **Next actor:** {llm_name}
- **Next action:** {description}
- **Prompt for next actor:** See Handoff Prompts section below
```

### Steps

Append-only log of all actions taken:

```markdown
### {NN}
- **Actor:** {llm_name}
- **Status:** {planned|in_progress|done|blocked|no_action}
- **Action:** {action_type}
- **Input:** {file_path}
- **Output:** {file_path}
- **Summary:** {brief description}
- **Next:** {next_llm_name}
```

### Issues

Table tracking all identified problems. Use unique IDs (e.g., `ISSUE-01`) so responses and changelogs can reference them unambiguously:

```markdown
## Issues
| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | critical | Example issue | resolved | How it was fixed |
```

Issue statuses: `open` | `resolved` | `wontfix` | `escalate`

### Agreements Log

Record of key decisions made during the review:

```markdown
## Agreements Log
Key positions agreed between LLMs:
- {Decision 1} - {which LLM's position was adopted}
- [DISPUTED] {Decision 2} - {escalated to user, resolved as X}
```

### Handoff Prompts

Pre-written prompts for each LLM to continue the review.

## Handoff Procedure

When completing a step:

1. Write your output file to the appropriate location
2. **Include a handoff prompt at the end of your output file** (see Output File Requirements below)
3. Update the tracker:
   - Change your step's status to `done`
   - Fill in Output and Summary fields
   - Add the next step with status `planned`
   - Update Current State section with next actor and action
   - Update Issues table if issues were resolved or identified
   - Update Agreements Log if key decisions were made
   - Update Handoff Prompts section with the prompt from your output file
4. The next LLM reads the tracker to know their task

## Output File Requirements

**Every output file MUST end with a handoff prompt section.** This ensures the next actor can continue without requiring the user to construct a prompt.

The section should be titled `## Handoff Prompt for Next Actor` and contain a complete prompt that the user can copy-paste to the next LLM.

The handoff prompt should include:

- The tracker path
- The step number and expected action
- Specific context from the current step that the next actor needs
- Any decisions that were made or issues that were resolved/identified

## Issue Severity Levels

- **Critical**: Blocks functionality or creates contradictions
- **High**: Significant ambiguity or operational gap
- **Medium**: Missing detail that could cause problems
- **Low**: Enhancement or clarification

## File Naming Conventions

All file names use snake_case with dates as `YYYY_MM_DD`:

- **Reviews**: `.metadata/reviews/llms/{llm}/{topic}_review_{YYYY_MM_DD}.md`
- **Responses**: `.metadata/review-responses/llms/{llm}/{topic}-review/{NN}_{action}_to_{other_llm}_{description}_{YYYY_MM_DD}.md`
- **Changelogs**: `.metadata/changelog/{llm1}_{llm2}_{topic}_{description}_{YYYY_MM_DD}.md`
- **Trackers (active)**: `.metadata/reviews/active/{topic}-tracker.md`
- **Trackers (closed)**: `.metadata/reviews/closed/{topic}-tracker.md`
- **Step Archives**: `.metadata/reviews/active/{topic}-tracker-archive.md`

## Conflict Resolution

If LLMs disagree after 2 rounds of back-and-forth on the same issue:

1. Document both positions in Agreements Log with prefix `[DISPUTED]`
2. Set issue status to `escalate`
3. User makes final decision
4. Update Agreements Log with resolution and remove `[DISPUTED]` prefix

## Session Initiation

User initiates each LLM session by:

1. Opening the tracker file
2. Providing the handoff prompt from the tracker's Handoff Prompts section
3. LLM reads tracker, performs task, updates tracker

## Completion Criteria

Review is complete when:

- All issues have status `resolved` or `wontfix`
- Final verification step has status `done`
- Both LLMs have no pending concerns
- Tracker Meta status is set to `closed`
- Tracker is moved from `.metadata/reviews/active/` to `.metadata/reviews/closed/`
- Changes are committed to git (see Closing a Review below)

## Closing a Review

When a review is verified complete:

1. Set tracker Meta status to `closed`
2. Set Current State next actor to `none`
3. Move tracker from `active/` to `closed/`
4. Commit all changes from the review cycle:
   - Modified source files
   - Changelog files
   - Review/response files
   - The closed tracker
5. Use commit message format: `{topic} review: {brief summary of changes}`

Example commit message:

```text
regional-federalism-design review: align design docs with constitution

- ISSUE-01: Updated elections design for NPV
- ISSUE-02: Updated armed-forces two-key authorization
- ISSUE-03: Added judicial timelines to Article XI
- ISSUE-04: Added federal lawmaking procedure to Article IV

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Codex <noreply@openai.com>
```

## Archive Policy

When step count exceeds 20:

1. Move steps 01-10 to archive file at `.metadata/reviews/active/{topic}-tracker-archive.md`
2. Renumber remaining steps in main tracker starting from 01
3. Keep Issues table and Agreements Log in main tracker (do not archive)
4. Add note at top of Steps section: `Note: Steps 01-10 archived to {topic}-tracker-archive.md`

## Starting a New Review

1. Copy `.metadata/templates/review-tracker-template.md` to `.metadata/reviews/active/{topic}-tracker.md`
2. Fill in the Meta section with topic, target, participants, and roles
3. Update Current State with the first actor and action
4. Create step 01 entry for the reviewer with status `planned`
5. Provide the tracker path to the reviewer LLM with the handoff prompt
