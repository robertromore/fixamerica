# Regional Federalism Foundation Review Tracker

## Meta

- **Topic:** regional-federalism-foundation
- **Target:** plans/regional-federalism/01-foundation/
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
- **Input:** plans/regional-federalism/01-foundation/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_foundation_review_2026_01_11.md
- **Summary:** Reviewed core idea and design axioms; flagged gaps around region formation rules, DC/territory status, overlay model ambiguity, MV transfer scope, and enforcement-axiom tensions.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_foundation_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-foundation-review/01-reply_to_regional_federalism_foundation_review_2026_01_11.md
- **Summary:** Most issues already resolved in constitution/implementation from prior review cycle; proposed minor_update for ISSUE-02/03/04 (forward refs), implement for ISSUE-05 (axiom reconciliation note), no_action for ISSUE-01
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-foundation-review/01-reply_to_regional_federalism_foundation_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-foundation-review/01-response_to_claude_foundation_reply_2026_01_11.md
- **Summary:** Confirmed minor updates for ISSUE-02/03, modified ISSUE-01/04 to add forward-reference and de-duplication signal, and requested a brief axiom-reconciliation design note for ISSUE-05.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-foundation-review/01-response_to_claude_foundation_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_foundation_review_implementation_2026_01_11.md
- **Summary:** Implemented all 5 issues: added Section 5.4 forward-ref (ISSUE-01), non-state entity note (ISSUE-02), Option C non-adopted label (ISSUE-03), MV-RF de-duplication paragraph (ISSUE-04), axiom reconciliation design note (ISSUE-05)
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_foundation_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-foundation-review/02-verify_foundation_implementation_2026_01_11.md
- **Summary:** Verified updates for ISSUE-01 through ISSUE-05; all resolutions match agreed scope, no new issues.
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | high | Region formation and revision process undefined | resolved | Added Section 5.4 in 01-core-idea.md with forward-ref to Art I.4 |
| ISSUE-02 | medium | DC/territory/tribal status conflicts with region definition | resolved | Added blockquote note in Section 6 with forward-ref to Art XVI |
| ISSUE-03 | medium | Functional overlay regions conflict with single-tier framing | resolved | Added design note labeling Option C as non-adopted |
| ISSUE-04 | medium | MV-RF transfer scope unclear, risks additive bureaucracy | resolved | Added de-duplication paragraph in Section 13 with forward-ref to Allocation Framework Act |
| ISSUE-05 | medium | Enforcement axioms need trigger/executor clarity | resolved | Added axiom reconciliation design note after Axiom 8 in 02-design-axioms.md |

## Agreements Log

Key positions agreed between LLMs:

- Foundation documents remain problem-framing but include concise forward references and explicit labels where design choices are settled.
- Option C (functional overlays) is labeled as a conceptual alternative not adopted in the constitutional design.
- ISSUE-05 warrants a brief axiom-reconciliation design note, with deeper detail deferred to judiciary/armed-forces docs.

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-foundation-tracker.md

Your current task is step 05 with status "planned". Verify Claude's implementation by:

1. Reading the changelog at .metadata/changelog/claude_codex_regional_federalism_foundation_review_implementation_2026_01_11.md
2. Spot-checking the modified files:
   - plans/regional-federalism/01-foundation/01-core-idea.md (Section 5.4, Section 6 note, Option C label, Section 13 de-duplication)
   - plans/regional-federalism/01-foundation/02-design-axioms.md (design note after Axiom 8)
3. Confirming each issue was addressed as agreed
4. Creating your verification response file
5. Updating the tracker (close if complete, or add next step if issues found)

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
