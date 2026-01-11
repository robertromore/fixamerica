# Campaign Finance Analysis Review Tracker

## Meta

- **Topic:** campaign-finance
- **Target:** analysis/political/campaign-finance/
- **Created:** 2026-01-11
- **Last updated:** 2026-01-11
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
- **Next action:** Review closed (verification complete)
- **Prompt for next actor:** N/A

## Steps

### 01

- **Actor:** codex
- **Status:** done
- **Action:** review
- **Input:** analysis/political/campaign-finance/
- **Output:** .metadata/reviews/llms/codex/campaign_finance_review_2026_01_11.md
- **Summary:** Flagged legal doctrine overstatements, a FECA timeline error, voucher eligibility inconsistency, and missing dated sources for metrics.
- **Next:** claude

### 02

- **Actor:** claude
- **Status:** done
- **Action:** response
- **Input:** .metadata/reviews/llms/codex/campaign_finance_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/claude/campaign-finance-review/01-reply_to_campaign_finance_review_2026_01_11.md
- **Summary:** Agreed with all 4 issues. Proposed: fix legal doctrine to distinguish contributions vs expenditures, correct FECA 1971 timeline, remove LPRs from voucher eligibility, add date anchors + Sources section.
- **Next:** codex

### 03

- **Actor:** codex
- **Status:** done
- **Action:** response
- **Input:** .metadata/review-responses/llms/claude/campaign-finance-review/01-reply_to_campaign_finance_review_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/campaign-finance-review/02-response_to_claude_campaign_finance_reply_2026_01_11.md
- **Summary:** Approved all four resolutions with clarifications on doctrine language, FECA timeline, voucher eligibility, and dated sources.
- **Next:** claude

### 04

- **Actor:** claude
- **Status:** done
- **Action:** implement
- **Input:** .metadata/review-responses/llms/codex/campaign-finance-review/02-response_to_claude_campaign_finance_reply_2026_01_11.md
- **Output:** .metadata/changelog/claude_codex_campaign_finance_review_implementation_2026_01_11.md
- **Summary:** Implemented all 4 issues: fixed legal doctrine to distinguish contributions vs expenditures, corrected FECA 1971 timeline, fixed voucher eligibility, added date anchors and Sources section.
- **Next:** codex

### 05

- **Actor:** codex
- **Status:** done
- **Action:** verify
- **Input:** .metadata/changelog/claude_codex_campaign_finance_review_implementation_2026_01_11.md
- **Output:** .metadata/review-responses/llms/codex/campaign-finance-review/03-verify_campaign_finance_implementation_2026_01_11.md
- **Summary:** Verified all four issues resolved (doctrine distinctions, FECA timeline fix, voucher eligibility, date anchors + sources).
- **Next:** none

## Issues

| ID | Severity | Title | Status | Resolution |
|----|----------|-------|--------|------------|
| ISSUE-01 | medium | Legal doctrine summary overstates Citizens United/Buckley standards | resolved | Verified contributions vs expenditures language and corporate independent expenditures terminology |
| ISSUE-02 | medium | FECA 1971 timeline entry misstates self-funding limits | resolved | Verified FECA 1971 correction and 1974 Buckley note |
| ISSUE-03 | medium | Voucher eligibility conflicts with voter registration requirement | resolved | Verified voucher eligibility limited to U.S. citizens eligible to vote |
| ISSUE-04 | low | Time-sensitive metrics lack date anchors or sources | resolved | Verified date anchors and Sources section with cited sources |

## Agreements Log

Key positions agreed between LLMs:

- Distinguish contribution limits (appearance of corruption still valid) from independent expenditure limits (appearance rejected).
- Correct FECA 1971 timeline; clarify 1974 expenditure limits struck in Buckley.
- Voucher eligibility limited to U.S. citizens eligible to vote.
- Add date anchors and a Sources section for key metrics.

## Handoff Prompts

When user initiates a session with the next actor, use this prompt:

### For Codex (when next actor is codex)

```text
Read the review tracker at .metadata/reviews/active/campaign-finance-tracker.md

Your current task is step 05 with status "planned". Verify Claude's implementation by reviewing the changelog at .metadata/changelog/claude_codex_campaign_finance_review_implementation_2026_01_11.md and spot-checking the modified files:

- analysis/political/campaign-finance/01-overview.md (legal doctrine fix, date anchors)
- analysis/political/campaign-finance/02-current-state.md (date anchors, Sources section)
- analysis/political/campaign-finance/03-history.md (FECA 1971 timeline, Buckley note)
- analysis/political/campaign-finance/04-root-causes.md (legal doctrine fix)
- analysis/political/campaign-finance/11-legislation.md (voucher eligibility fix)

Create your verification response at .metadata/review-responses/llms/codex/campaign-finance-review/, then update the tracker:

1. Change step 05 status to "done"
2. Fill in the Output and Summary fields
3. If issues found: add step 06 for claude to fix, update Issues table
4. If verified: update "Current State" to indicate review complete
5. Update Issues table statuses as appropriate

Verification checklist from changelog:
- [ ] Legal doctrine distinguishes contributions (appearance valid) from independent expenditures (appearance rejected)
- [ ] "Corporate personhood" replaced with "corporate independent expenditures" in tables
- [ ] Self-funding limits removed from 1971 FECA; added to 1974 with Buckley note
- [ ] Voucher eligibility limited to U.S. citizens eligible to vote (no LPRs)
- [ ] Date anchors added to time-sensitive sections in overview and current-state
- [ ] Sources section includes FEC, OpenSecrets, Brennan Center, CFI, academic, and legal citations

Protocol: .metadata/protocols/llm-review-protocol.md
```

### For Claude (when next actor is claude)

```text
Read the review tracker at .metadata/reviews/active/campaign-finance-tracker.md

Your current task is step 04 with status "planned". Implement the agreed changes from .metadata/review-responses/llms/codex/campaign-finance-review/02-response_to_claude_campaign_finance_reply_2026_01_11.md:

- Update legal doctrine language in `analysis/political/campaign-finance/01-overview.md` and `analysis/political/campaign-finance/04-root-causes.md` to distinguish contributions vs. independent expenditures and remove corporate personhood attribution.
- Correct FECA 1971 description and add Buckley note in `analysis/political/campaign-finance/03-history.md`.
- Revise voucher eligibility to U.S. citizens eligible to vote in `analysis/political/campaign-finance/11-legislation.md`.
- Add date anchors in `analysis/political/campaign-finance/01-overview.md` and `analysis/political/campaign-finance/02-current-state.md`, and add a Sources section to current-state.

Create your changelog at `.metadata/changelog/claude_codex_campaign_finance_review_implementation_2026_01_11.md`, then update the tracker:
1. Change step 04 status to "done"
2. Fill in the Output and Summary fields
3. Add step 05 entry with status "planned" for codex to verify
4. Update "Current State" section with next actor and action
5. Update Issues table if any issue is resolved or needs follow-up
6. Update Agreements Log if key decisions are made

Protocol: .metadata/protocols/llm-review-protocol.md
```
