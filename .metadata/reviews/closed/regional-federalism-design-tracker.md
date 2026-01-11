# Regional Federalism Design Review Tracker

## Meta

- **Topic:** regional-federalism-design
- **Target:** plans/regional-federalism/02-design/
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
- **Input:** plans/regional-federalism/02-design/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_design_review_2026_01_11.md
- **Summary:** Reviewed design docs for alignment with the constitution; flagged conflicts in elections and armed-forces rules, plus gaps on judicial timelines and federal lawmaking procedure.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_design_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-design-review/01-reply_to_regional_federalism_design_review_2026_01_11.md
- **Summary:** Agreed with all 4 findings; proposed implement for all: update elections/armed-forces design docs to match constitution, add explicit judicial timelines to Article XI, add federal lawmaking procedure to Article IV and institutions doc.
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-design-review/01-reply_to_regional_federalism_design_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-design-review/02-response_to_claude_design_reply_2026_01_11.md
- **Summary:** Confirmed implement for issues 01-03; requested ISSUE-04 refinements (define Senate delay trigger, explicit veto override) and a brief Article XII timing reference in armed-forces design.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-design-review/02-response_to_claude_design_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_design_review_implementation_2026_01_11.md
- **Summary:** Implemented all 4 issues: aligned elections with NPV (ISSUE-01), aligned armed-forces with Article XII keyholders (ISSUE-02), added 30/30/30 timelines to Article XI (ISSUE-03), added federal lawmaking Section 5 to Article IV with veto override and anti-expansion clause (ISSUE-04).
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_design_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-design-review/03-verify_design_implementation_2026_01_11.md
- **Summary:** Verified issues 01-04 were implemented as agreed, including ISSUE-04 refinements and ISSUE-02 timing reference; no new issues.
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | high | Presidential selection method conflicts with constitution | resolved | Verified NPV alignment and design note in 02-elections.md |
| ISSUE-02 | high | Two-key authorization combinations conflict with Article XII | resolved | Verified Article XII keyholders + timing reference in 06-armed-forces.md |
| ISSUE-03 | medium | Judicial timelines defined in design but not in constitution | resolved | Verified explicit 30/30/30 timelines in Article XI Section 2 |
| ISSUE-04 | medium | Federal lawmaking procedure unclear with narrowed Senate role | resolved | Verified Article IV Section 5 + institutions mirror with delay designation + anti-expansion |

## Agreements Log

Key positions agreed between LLMs:

- Elections design should conform to the constitution's national popular vote requirement.
- Armed-forces design should mirror Article XII keyholders and fallback (with timing referenced).
- Judicial deadlines should be constitutionalized rather than left implicit.
- Federal lawmaking procedure should be explicit with a House-led path and narrowly scoped Senate delay.

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-design-tracker.md

Your current task is step 05 with status "planned". Verify Claude's implementation by:

1. Reading the changelog at .metadata/changelog/claude_codex_regional_federalism_design_review_implementation_2026_01_11.md
2. Spot-checking the modified files:
   - plans/regional-federalism/02-design/02-elections.md (Section 9.2 NPV alignment)
   - plans/regional-federalism/02-design/06-armed-forces.md (Section 9.1 Article XII keyholders)
   - plans/regional-federalism/02-design/09-constitution.md (Article XI.2 timelines, Article IV.5 lawmaking)
   - plans/regional-federalism/02-design/03-institutions.md (Section 5.3a lawmaking explanation)
3. Confirming each issue was addressed as agreed, including:
   - ISSUE-04 refinements: veto override (House 2/3), statutory designation for delay categories, anti-expansion clause
   - ISSUE-02 refinement: Article XII timing/expiry reference
4. Creating your verification response file
5. Updating the tracker (close if complete, or add next step if issues found)

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-design-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
