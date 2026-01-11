# Regional Federalism Implementation Review Tracker

## Meta

- **Topic:** regional-federalism-implementation
- **Target:** plans/regional-federalism/05-implementation/
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
- **Input:** plans/regional-federalism/05-implementation/
- **Output:** .metadata/reviews/llms/codex/regional_federalism_implementation_review_2026_01_11.md
- **Summary:** Reviewed implementation acts for constitutional alignment; flagged transition-act supremacy conflicts, mandatory-jurisdiction delays, election deadline and majority-method mismatches, plus region-formation and state-certification ambiguities.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/regional_federalism_implementation_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/regional-federalism-implementation-review/01-reply_to_regional_federalism_implementation_review_2026_01_11.md
- **Summary:** Agreed with all 6 issues; proposed constitutional transition clause (Article XV), judicial capacity clause (Article XI), deadline corrections (14/21 days), single national RCV, Schedule A for initial boundaries, ministerial state role clarification; posed 4 open questions.
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/regional-federalism-implementation-review/01-reply_to_regional_federalism_implementation_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-implementation-review/02-response_to_claude_implementation_reply_2026_01_11.md
- **Summary:** Confirmed all six fixes; selected Article XV transition clause, Schedule A boundaries, single national RCV, and Article XI capacity clause; reaffirmed 14/21-day deadlines and ministerial state compilation.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/regional-federalism-implementation-review/02-response_to_claude_implementation_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_regional_federalism_implementation_review_2026_01_11.md
- **Summary:** Implemented all 6 issues: added Article XV transition authorization (Sections 2-4), Article XI capacity clause (Section 5), Schedule A with 7 initial regions; revised Transition Act Section 2.2 and 9.3; aligned Elections Act to 14/21-day deadlines, uniform RCV, and ministerial state role.
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_regional_federalism_implementation_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/regional-federalism-implementation-review/03-verify_implementation_changes_2026_01_11.md
- **Summary:** Verified issues 01-06 implemented as agreed; deadlines, RCV, Schedule A, transition and capacity clauses all align with constitutional requirements.
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | high | Transition Act delays constitutional effectiveness contrary to Article XV | resolved | Verified Article XV transition authorization + Transition Act alignment |
| ISSUE-02 | high | Transition Act delays mandatory jurisdiction via phase/GAO gating | resolved | Verified Article XI capacity clause + no GAO gating |
| ISSUE-03 | high | Elections Act certification deadlines conflict with Article VI | resolved | Verified 14/21-day deadlines in Elections Act |
| ISSUE-04 | high | Elections Act allows non-uniform majority mechanisms + RCV tabulation mismatch | resolved | Verified uniform national RCV method |
| ISSUE-05 | medium | Region formation by statute conflicts with constitutional establishment | resolved | Verified Schedule A + Transition Act Phase II reference |
| ISSUE-06 | medium | State certification step risks reintroducing state chokepoints | resolved | Verified ministerial state role + transmission-only language |

## Agreements Log

Key positions agreed between LLMs:

- All 6 issues represent genuine constitutional/statutory conflicts requiring resolution\n- Transition authorization should be in Article XV\n- Initial regional boundaries should be enumerated in Schedule A\n- Presidential majority method should be a single national RCV\n- Judicial capacity clause belongs in Article XI\n- Election deadlines must align with 14/21 days and state role remains ministerial

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-implementation-tracker.md

Your current task is step 05 with status "planned". Verify the implementation documented in:
.metadata/changelog/claude_codex_regional_federalism_implementation_review_2026_01_11.md

Check the modified files for all 6 issues:
- ISSUE-01: Article XV Sections 2-4 (transition authorization) + Transition Act Section 2.2
- ISSUE-02: Article XI Section 5 (judicial capacity) + Transition Act Section 9.3
- ISSUE-03: Elections Act Section 7.1 (14/21 day deadlines)
- ISSUE-04: Elections Act Sections 5.4-5.6 (uniform national RCV)
- ISSUE-05: Schedule A (initial regional boundaries) + Transition Act Phase II
- ISSUE-06: Elections Act Sections 2.3, 7.1 (ministerial state role)

Files to verify:
- plans/regional-federalism/02-design/09-constitution.md
- plans/regional-federalism/05-implementation/02-transition-act.md
- plans/regional-federalism/05-implementation/05-elections-implementation-act.md

Create your verification file, then update the tracker per the protocol.

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/regional-federalism-implementation-tracker.md

Your current task is step {N} with status "planned". Read the input file, perform the action described, create your output file, then update the tracker:
1. Change step {N} status to "done"
2. Fill in the Output and Summary fields
3. Add the next step entry with status "planned"
4. Update "Current State" section with next actor and action
5. Update Issues table if you identify or resolve issues
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
