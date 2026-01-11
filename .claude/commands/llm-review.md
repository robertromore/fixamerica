# LLM Review Collaboration

This skill manages LLM-to-LLM document review cycles using the project's formal collaboration protocol.

## Usage

- `/llm-review` - Show options (start new or continue existing)
- `/llm-review start {topic}` - Start a new review for the given topic
- `/llm-review continue` - Continue an existing review where you are the next actor
- `/llm-review status` - Show status of all active reviews
- `/llm-review close {topic}` - Close a completed review and commit changes

## Instructions

When this skill is invoked:

### If no arguments or "status"

1. List all active reviews by reading files in `.metadata/reviews/active/`
2. Optionally list recent closed reviews from `.metadata/reviews/closed/`
3. For each tracker, show: Topic, Status, Next Actor, Next Action
4. If the user is the next actor on any review, highlight that

### If "start" with topic or user wants to start a new review

1. Ask the user for:
   - **Topic name**: Short identifier (e.g., `campaign-finance`, `healthcare-analysis`)
   - **Target path**: What documents to review (e.g., `analysis/healthcare/`, `plans/regional-federalism/`)
   - **Participants**: Which LLMs will participate and their roles (reviewer vs implementer)

2. Copy the template:
   ```bash
   cp .metadata/templates/review-tracker-template.md .metadata/reviews/active/{topic}-tracker.md
   ```

3. Fill in the tracker's Meta section:
   - Topic: {topic_name}
   - Target: {target_path}
   - Created: {today's date in YYYY-MM-DD}
   - Last updated: {today's date in YYYY-MM-DD}
   - Status: in_progress
   - Participants: {llm_a} (reviewer), {llm_b} (implementer)

4. Update Current State:
   - Next actor: {reviewer}
   - Next action: Initial review of target documents
   - Prompt for next actor: See Handoff Prompts section

5. Update step 01:
   - Actor: {reviewer}
   - Status: planned
   - Action: review
   - Input: {target_path}
   - Output: (pending)
   - Summary: (pending)
   - Next: {implementer}

6. Update the Handoff Prompts section with correct LLM names

7. Provide the handoff prompt for the reviewer:
   ```
   Read the review tracker at .metadata/reviews/active/{topic}-tracker.md

   Your current task is step 01 with status "planned". Review the target documents,
   create your review file, then update the tracker per the protocol.

   Protocol: .metadata/protocols/llm-review-protocol.md
   ```

### If "continue" or user wants to continue an existing review

1. List active reviews where status is `in_progress`
2. If multiple reviews exist, ask user which one to continue
3. Read the selected tracker file
4. Find the step with status `planned`
5. Check if this LLM (Claude) is the actor for that step
6. If yes, execute the protocol:
   - Read the input file specified in the step
   - Perform the action (review, response, implement, verify, or fix)
   - Write output file to appropriate location
   - **Include a "Handoff Prompt for Next Actor" section at the end of the output file**
   - Update the tracker:
     - Mark step as `done` with Output and Summary filled in
     - Add next step with status `planned`
     - Update Current State section
     - Update Issues table and Agreements Log as needed
     - Update `Last updated` date in Meta section
     - Update Handoff Prompts section with the prompt from your output file
7. If no, provide the handoff prompt for the correct actor

### If "close" with topic or user wants to close a completed review

1. Read the tracker at `.metadata/reviews/active/{topic}-tracker.md`
2. Verify the review is ready to close:
   - All issues have status `resolved` or `wontfix`
   - Final verification step has status `done`
   - Meta status is `closed`
3. If not ready, explain what's still pending
4. If ready, perform the closing steps:
   - Move tracker from `active/` to `closed/`
   - Stage all files from the review cycle:
     - Modified source files (from changelogs)
     - Changelog files
     - Review and response files
     - The closed tracker
   - Create commit with message format shown below
5. Report the commit hash and summary

Commit message format:

```text
{topic} review: {brief summary}

- ISSUE-XX: {resolution summary}
- ISSUE-YY: {resolution summary}

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Codex <noreply@openai.com>
```

### Output File Handoff Requirement

Every output file (reviews, responses, changelogs, verification files) MUST end with:

```markdown
---

## Handoff Prompt for Next Actor

[Complete prompt that the user can copy-paste to the next LLM, including:
- Tracker path
- Step number and action
- Key context from this step
- Any decisions made or issues identified]
```

This ensures seamless handoff without requiring the user to construct prompts manually.

## Protocol Reference

Full protocol: `.metadata/protocols/llm-review-protocol.md`

### Core Rules

1. **Single source of truth**: The tracker file is authoritative
2. **Append-only outputs**: Do not edit other LLM's output files
3. **Ownership rule**: Only mark your own steps as `done`
4. **Date format**: Use `YYYY_MM_DD` in file names (snake_case)
5. **Single actor handoff**: `Next` field must specify exactly one actor
6. **Cite locations**: Reference specific file paths and line numbers

### Action Types

| Action | Description |
|--------|-------------|
| review | Initial analysis of target documents |
| response | Reply to review or counter-response |
| implement | Make agreed changes to source files |
| verify | Check implementation for correctness |
| fix | Address issues found in verification |

### Issue Severity Levels

- **critical**: Blocks functionality or creates contradictions
- **high**: Significant ambiguity or operational gap
- **medium**: Missing detail that could cause problems
- **low**: Enhancement or clarification

### File Naming Conventions

- Reviews: `{topic}_review_{YYYY_MM_DD}.md`
- Claude responses: `{NN}-reply_to_{original_file}.md`
- Codex responses: `{NN}-response_to_claude_{file}.md`
- Changelogs: `{llm1}_{llm2}_{topic}_{description}_{YYYY_MM_DD}.md`

### Output Locations

- Active trackers: `.metadata/reviews/active/`
- Closed trackers: `.metadata/reviews/closed/`
- Initial reviews: `.metadata/reviews/llms/{reviewer}/`
- Response files: `.metadata/review-responses/llms/{llm}/{topic}-review/`
- Changelogs: `.metadata/changelog/`

## Example Session

**Starting a new review:**
```
User: /llm-review start healthcare-legislation
Claude: I'll set up a new review for healthcare-legislation.

What is the target path for this review? (e.g., analysis/healthcare/)
User: analysis/healthcare/11-legislation.md
Claude: Who will be the participants?
User: codex as reviewer, claude as implementer
Claude: Created tracker at .metadata/reviews/active/healthcare-legislation-tracker.md

Handoff prompt for codex:
---
Read the review tracker at .metadata/reviews/active/healthcare-legislation-tracker.md
...
```

**Continuing an existing review:**
```
User: /llm-review continue
Claude: Active reviews:
- regional-federalism: closed
- healthcare-legislation: in_progress (next: claude, action: implement)

You are the next actor on healthcare-legislation. Reading tracker...

[Claude reads input file, performs implementation, updates tracker]
```
