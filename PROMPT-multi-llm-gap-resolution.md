# Multi-LLM Gap Resolution Protocol

Prompt for resolving "Requires Development" gaps in the Regional Federalism constitutional design through multi-LLM review. Established during the Gap 170 (Fiscal Cliff Hostage) resolution on 2026-01-31.

## Context

The Regional Federalism project (`plans/constitutional-amendments/comprehensive/regional-federalism/`) contains a constitutional design with an identified gaps tracking system. Gaps represent known vulnerabilities, attack vectors, or under-specified domains in the constitutional text. Each gap has a status:

- **Requires Development** — No constitutional text exists; needs drafting
- **Partially Mitigated** — Some mechanisms exist but are insufficient
- **Mitigated** — Constitutional text drafted and integrated but not formally verified
- **Resolved** — Constitutional text verified against gaming vectors with date stamp

**Key directories:**

- `02-design/constitution/` — Authoritative constitutional text (numbered article files)
- `04-meta/gaps/` — Gap detail files organized by theme (numbered 01-19)
- `04-meta/gaps/00-index.md` — Master index of all gaps with status
- `04-meta/02-identified-gaps.md` — Summary statistics

## Overview

A coordinating LLM (with codebase access) prepares a self-contained briefing for a gap, sends it to two external LLMs for independent review, synthesizes the reviews, surfaces design decisions for the human, sends decisions back for a second round of review, and iterates until all three reviewers converge. Once consensus is reached, integration proceeds.

**Roles:**

- **Coordinator** (Claude or equivalent with codebase access) — Reads files, generates briefings, verifies claims, synthesizes reviews, performs integration
- **Reviewer A** (external LLM without codebase access) — Independent review from briefing
- **Reviewer B** (different external LLM without codebase access) — Independent review from briefing
- **Human** — Makes design decisions when reviewers surface options

---

## Step 1: Select Gap, Read Context, and Perform Overlap Analysis

Read the gap entry from its detail file (e.g., `04-meta/gaps/07-fiscal-equalization.md`). Identify:

- The gap's proposed resolution text (if any)
- All constitutional design files the resolution references or should be placed in
- Any related resolved gaps that might conflict or overlap

Read the relevant constitutional design files to understand what already exists. Pay special attention to:

- The article/section where the new text would be placed
- Adjacent sections that might interact
- Any existing provisions that cover similar ground (potential conflicts)
- Already-resolved gaps that address related attack vectors

### 1a. Placement Verification

**Every proposal has placement errors.** In 16 of 16 resolved gaps, the original proposal targeted an incorrect location. Verify before proceeding:

- Does the target Article/Section exist? (e.g., "Article XIV-RF, Section 9" — Article XIV-RF ends at Section 5)
- Is the target section already occupied? (e.g., "Article XVII, Section 8" — already Habeas Corpus)
- Is there an RF supplement for this Article, or is it standalone only? (e.g., Article VII has no VII-RF)
- What is the next available section number?
- Is the target article the correct home? (e.g., national injunction rules belong in standalone Article XIV, not RF-specific XIV-RF)

### 1b. Institution Verification

Verify all institutions named in the proposal against the constitutional text:

- Does the named institution exist? (e.g., "National Electoral Commission" does not exist; the text has IEC and NEC)
- Is the institution's jurisdiction correct for the proposed role?
- Are there naming conflicts? (e.g., NEC = National Election Court, not National Electoral Commission)

### 1c. Overlap Analysis

**This is the most important analytical step.** Before generating the briefing, build a coverage table:

| Proposal Element | Existing Coverage | Location | Overlap % |
|---|---|---|---|
| Subsection (a) | [What exists] | [Article/Section] | [0-100%] |
| Subsection (b) | [What exists] | [Article/Section] | [0-100%] |
| ... | ... | ... | ... |

Compute overall overlap percentage. In practice, proposals range from 30% to 80% overlap with existing provisions. The genuinely additive elements (the remaining %) are what the resolution should focus on.

**Red flags during overlap analysis:**

- Proposal claims "not addressed" but existing provision partially covers it → reviewer will catch, reduces credibility
- Proposal duplicates an already-resolved gap → check 00-index.md for status
- Proposal targets a section that was recently modified by another gap resolution → read the current text, not the gap entry's stale version

---

## Step 2: Generate Briefing Prompt for External LLMs

Write a self-contained briefing that another LLM can act on without access to the codebase. The briefing must include enough context for the reviewer to identify conflicts with existing provisions.

**Required sections:**

### 2a. Context

What the constitutional system is, where design files live, where gap files live. Include the specific Article/Section numbers and file names relevant to this gap.

### 2b. The Problem

What the gap is, why it matters, the specific attack vector. Include the step-by-step attack sequence from the gap entry.

### 2c. Why This Is Worse in This System

How the regional federal structure amplifies the risk compared to the current US system. This helps reviewers understand the stakes and evaluate whether the proposed resolution is proportionate.

### 2d. The Proposed Resolution

Full draft constitutional text from the gap entry. Include the complete text, not a summary.

### 2e. Key Design Principles

What the resolution is trying to achieve and how each subsection serves that goal. This helps reviewers evaluate whether alternative approaches might work better.

### 2f. What Resolution Looks Like

The specific files that would be modified and the integration steps. This helps reviewers flag cross-reference issues.

### 2g. Gaming Vectors to Verify Against

Second-order attacks the reviewer should check for. These are the ways the proposed resolution itself could be exploited or circumvented.

### 2h. Overlap Analysis Results

Include the coverage table from Step 1c. This is the most valuable section for reviewers — it lets them focus on genuinely additive elements rather than re-discovering existing coverage. Include:

- The coverage table (proposal element / existing coverage / location / overlap %)
- Overall overlap percentage
- List of genuinely additive elements with explanation of why each is not covered

### 2i. Placement Verification Results

State the placement correction and rationale:

- Original proposal target (and why it's wrong)
- Corrected placement (with section number and file)
- Why this location is the correct home

### 2j. Design Questions (D1-Dn)

Frame specific design decisions the reviewer should address. Use the Dn format with concrete options:

```text
D1: [Question]
- Option A: [description + tradeoff]
- Option B: [description + tradeoff]
- Option C: [description + tradeoff]
```

This format ensures reviewers give actionable recommendations rather than open-ended commentary. In practice, 3-8 design decisions per gap is typical.

### 2k. Verification Questions

Include 2-4 specific factual questions the reviewer can help verify:

- Cross-reference accuracy (does Section X actually say Y?)
- Scope questions (does §Z cover scenario W?)
- Institutional jurisdiction questions

### 2l. Related Resolved Gaps

Any already-resolved gaps that might conflict or interact. Include the Article/Section where they were integrated and a one-line summary. This is critical for catching conflicts (e.g., Gap 170's debt limit suspension conflicted with Gap 260's debt limit abolition).

**Example briefing structure (from Gap 170):**

```text
## Gap 170 -- Fiscal Cliff Hostage (Weaponized Shutdowns)

### Context
You are working on a proposed Regional Federal Constitution that
reorganizes the US into ~6-8 Regions between federal and state levels.
Constitutional design files: `02-design/constitution/`
Gap tracking files: `04-meta/gaps/`
This gap is Critical severity, status Requires Development.

### The Problem
The constitution requires appropriations by law but has no fallback
if Congress fails to pass a budget. In the proposed Regional Federal
system, a shutdown becomes an extinction-level event because...

[Full attack vector sequence]

### The Proposed Resolution
[Complete draft constitutional text from gap entry]

### Related Resolved Gaps
- Gap 260 (Debt Limit Suicide Vest): Resolved as Article I, Section 20.
  Abolishes the statutory debt limit entirely.
- Gap 241 (Unfunded Mandate): Resolved as Article X, Section 18.
  Prohibits unfunded federal mandates on Regions.

### Gaming Vectors to Verify Against
- Weaponized auto-CR (majority prefers cuts to negotiating)
- Selective appropriation (funding allies, starving opponents)
- Inflation erosion (nominal dollars during high inflation)
- Essential functions scope creep (reclassifying programs)
```

**Important**: Reference specific Article/Section numbers and file names. Reviewers cannot look things up; everything they need must be in the briefing.

---

## Step 3: Collect Reviews from Two External LLMs

Send the briefing to two different LLMs. Request each to produce:

1. **Findings** — Verify the proposed text against cited constitutional provisions. Identify conflicts with already-resolved gaps or existing articles. Identify gaming vectors not addressed by the proposal. Flag ambiguous or undefined terms. Assess integration readiness.
2. **Open Questions / Assumptions** — Questions that need design decisions before integration.

**Expected review format:**

```text
Findings

High -- [Description]. [file reference] [file reference]
Medium -- [Description]. [file reference] [file reference]
Low -- [Description]. [file reference]

Open Questions / Assumptions

[Questions that need design decisions before integration]
```

**Severity levels for findings:**

- **High** — Contradicts existing constitutional text or creates a new critical vulnerability
- **Medium** — Ambiguous, undefined, or potentially conflicting; needs clarification
- **Low** — Minor gaming risk or style issue

---

## Step 4: Synthesize Reviews and Verify Claims

The coordinating LLM reads both reviews and:

1. **Verifies every claimed conflict** by reading the cited constitutional files. Do not trust file/line references without checking. Reviewers working from briefings (not codebase access) may cite wrong locations.

2. **Identifies convergence**: Where both reviewers agree, the finding is likely valid.

3. **Identifies divergences**: Where reviewers disagree or one catches something the other missed, assess which is correct by reading source files.

4. **Surfaces design decisions**: Extract the open questions that require a human decision before integration can proceed. Frame as concrete options (Option A / Option B / Option C) with tradeoffs for each.

**Output format:**

```text
### Confirmed findings (both reviews agree)
1. [Finding] -- [verified against file:line]
2. [Finding] -- [verified against file:line]

### Divergences worth noting
| Issue | Review 1 | Review 2 |
|-------|----------|----------|
| [topic] | [position] | [position] |

### Design decisions required
Decision 1: [Question]
- Option A: [description + tradeoff]
- Option B: [description + tradeoff]
- Option C: [description + tradeoff]
```

Present this synthesis to the human for design decisions.

---

## Step 5: Second Review Round

Once design decisions are made, send the updated synthesis back to the two external LLMs for validation. Include:

- The specific decisions made (with rationale)
- The coordinating LLM's proposed integration approach
- Any revised constitutional text reflecting the decisions
- The coordinator's own review/synthesis of the first round

**Expect reviewers to catch in round 2:**

- Terminology mismatches between proposed text and existing provisions
- Circularity in definitions
- Silent deletion of features from superseded provisions
- Assumptions about terms being defined when they aren't

---

## Step 6: Iterate Until Convergence

Repeat Steps 4-5 until all three reviewers (two external + coordinating) agree on:

- The final constitutional text
- Which files need modification
- Which existing provisions need amendment or deletion
- That no unresolved conflicts remain

**Convergence criteria:**

- No reviewer raises a Medium or higher finding that others dispute
- All design decisions are resolved
- All cross-references to existing provisions are verified
- Gaming vectors are addressed or explicitly accepted

### Round expectations

The number of rounds depends on the gap's complexity and the quality of the overlap analysis in the briefing.

| Scenario | Typical Rounds | Examples |
|----------|---------------|----------|
| Thorough overlap analysis, narrow additive scope | 1 | Gaps 193, 195, 206 |
| Moderate overlap, several design decisions | 2 | Gaps 170, 194, 197, 202 |
| Complex conflicts, placement disputes, or reviewer errors | 3 | Gap 82 |

**Compressed workflow:** When the coordinator's overlap analysis is thorough (Step 1c), reviewers can focus on the genuinely additive elements and often converge in a single round. Of 16 resolved gaps, 10 converged in 1 round, 5 in 2 rounds, and 1 in 3 rounds. The key predictor of round count is the quality of the briefing, not the gap's inherent complexity.

---

## Step 7: Integrate

Once all reviewers converge, perform the integration. Use this checklist:

### Integration Checklist

1. **Constitutional design file** — Add the new Section/Article with the agreed text
    - e.g., `02-design/constitution/04-fiscal-system.md` or `02-design/single-topic/judicial-reform.md`
    - Use the next available Section number in the target article
    - Do not add gap number comments in constitutional text; gap references belong in gap files only

2. **Superseded provisions** — Amend or replace with forward references
    - e.g., replace Article XXI 2(d) with "the provisions of Article X, Section 19 shall apply"
    - Do not silently delete; always leave a forward reference or explicit removal note

3. **Cross-references in other design files** — Update any existing provisions that reference the new Section
    - e.g., Section 18(j)(2) adding "under Section 19" to its auto-CR reference

4. **Implementation Notes** — Update the target design file's Implementation Notes section
    - Add any implementing legislation required by the new provisions
    - e.g., "Injunctive Relief Scope Act (three-judge panel procedures, MDL consolidation standards)"

5. **Gap detail file** — Update status from REQUIRES DEVELOPMENT to RESOLVED:
    - Change status text to: `**RESOLVED.** Integrated as [Article/Section] in [file].`
    - Change severity line to: `**Severity:** [level] | **Mitigability:** Resolved`
    - Include placement correction if the original proposal targeted the wrong location
    - Include the design decision table (D1-Dn with choices and rationale)
    - Include gaming vectors addressed table
    - Date stamp: `Resolved YYYY-MM-DD.`

6. **Gap index** (`04-meta/gaps/00-index.md`) — Change the gap's Mitigation Status to `✅ Resolved`

7. **Master statistics** (`04-meta/02-identified-gaps.md`) — Decrement "Requires Development" count, increment "Resolved" count

8. **Article crosswalk** (`02-design/constitution/article-crosswalk.md`) — Add section-level citation
    - e.g., `Article XIV, Section 16 (Injunctive Relief Scope and Anti-Forum Shopping) — see single-topic/judicial-reform.md`

9. **Daily changelog** (`changelog/YYYY-MM-DD.md`) — Document the resolution:
    - Problem summary
    - Solution summary (subsection-by-subsection)
    - Design decisions table (all Dn choices with rationale)
    - Placement correction (if any)
    - Conflicts resolved
    - Statistics delta (old → new for both Requires Development and Resolved)
    - All files modified (grouped by Constitutional Text, Cross-References, Gap Documentation)

10. **Markdownlint verification** — Run `npx markdownlint-cli` on all modified design files
    - Fix any violations before committing

11. **Main changelog** (`CHANGELOG.md`) — Add summary entry with link to daily file (if maintained separately)

---

## Example: Gap 170 Resolution Timeline

| Round | Actor | Action | Key Output |
|-------|-------|--------|------------|
| 0 | Coordinator | Read gap + design files, generate briefing | Self-contained prompt with full context |
| 1 | Reviewer A | Independent review | 5 findings (1 High, 3 Medium, 1 Low) |
| 1 | Reviewer B | Independent review | 4 findings + integration path recommendation |
| 2 | Coordinator | Synthesize, verify, surface decisions | 3 confirmed findings, 3 design decisions |
| 2 | Human | Make design decisions | Option B / Yes / Option A |
| 3 | Reviewer A | Validate decisions + integration approach | 3 findings (3 Medium) on terminology and silent deletion |
| 3 | Reviewer B | Validate decisions + integration approach | Confirms all findings, adds inflation recommendation |
| 4 | Coordinator | Final synthesis, all agree | Integration proceeds |
| 5 | Coordinator | Integrate into 4 files, update 3 tracking files | Gap 170 Resolved |

**Key findings from Gap 170:**

- Article XXI 2(d) had an existing auto-continuation rule (CPI-U indexed) that conflicted with Gap 170's 98% nominal decline. Resolution: replace Article XXI 2(d) with forward reference to new Section 19.
- Gap 260 had already abolished the debt limit, making Gap 170's Subsection (6) (debt limit suspension) redundant. Resolution: remove Subsection (6).
- Section 20(a) triggers borrowing authority on "authorization by Congress to appropriate" but auto-CR is constitutional, not congressional. Resolution: add bridge clause deeming auto-CR appropriations as "authorized by Congress" for Section 20 purposes.
- "Discretionary programs" was undefined. Resolution: replace with fixed enumerated list of essential functions.
- CPI-U indexing decision: essential functions CPI-indexed, discretionary at 98% nominal (maximizes negotiation pressure while protecting union-critical arteries).

---

## Common Patterns (from 16 resolved gaps)

### Placement errors are universal

Every proposal targeted the wrong location. Common failure modes:

| Error Type | Example | Frequency |
|------------|---------|-----------|
| Non-existent section | "Article XIV-RF, Section 9" (ends at §5) | ~50% |
| Occupied section | "Article XVII, Section 8" (already Habeas Corpus) | ~20% |
| Wrong article | "Article I-RF, Section 13" for war powers (belongs in Article XI) | ~20% |
| Non-existent RF supplement | "Article VII-RF, Section 4" (Article VII is standalone) | ~15% |

**Fix**: Always verify placement in Step 1a before generating the briefing.

### Overlap ranges from 30% to 80%

No proposal is entirely new. Existing provisions always cover some of the problem:

| Overlap Range | Interpretation | Action |
|---------------|---------------|--------|
| 0-30% | Genuinely novel gap | Full draft needed; less conflict risk |
| 30-60% | Typical | Narrow to additive elements; amend existing sections |
| 60-80% | Mostly covered | Small surgical additions; risk of duplication |
| 80%+ | Consider "Accepted by Design" | May not need constitutional text |

### Institution naming confusion

Proposals frequently reference institutions by wrong or non-existent names:

| Proposal Names | Actual Institution | Location |
|---|---|---|
| "National Electoral Commission" | National Election Court (NEC) | Article VII §7 |
| "National Electoral Commission" | Independent Election Commission (IEC) | Article VII §4 |
| "Federal Pension Oversight Board" | IFC Pension Actuarial Division | Article X §20 |
| "Regional Chief Judges" | Chief Justices of Regional Supreme Courts | Article XIV-RF §5 |

### Self-executing > requiring human action

Provisions that operate "by operation of law" are stronger than provisions requiring an institution to act:

- Auto-certification (results deemed certified) > NEC steps in to certify
- Void ab initio (alternate slates have no effect) > court must invalidate
- Automatic stay upon filing > court must grant stay

Prefer self-executing mechanisms in constitutional text. Reserve institutional action for situations where judgment is required.

### Constitutional text vs. implementing legislation

The constitutional text should establish the principle, structure, and self-executing mechanisms. Details that require adaptation should be delegated:

| In Constitution | In Implementing Legislation |
|---|---|
| Three-judge panel requirement | Panel selection procedures |
| Criminal penalties mandatory | Sentencing guidelines |
| Removal from office (self-executing) | Specific felony classifications |
| "As provided by law" delegation | Detailed procedural rules |

### Phantom resolutions

Gaps may be marked "Resolved" with references to non-existent constitutional text. Gap 173 was marked "Resolved — integrated into Article III-RF, Section 13" but Article III-RF only runs through Section 12. Always verify that cited constitutional text actually exists before accepting a "Resolved" status.

### Design decision convergence patterns

| Decision Type | Typical Convergence | Example |
|---|---|---|
| Placement | Round 1 (reviewers almost always agree) | D1 in every gap |
| Scope | Round 1-2 | Functional definitions preferred over enumerated lists |
| Institutional home | Round 1 | Existing institutions preferred over new ones |
| Penalties | Round 1-2 | Hybrid (constitutional + statutory) most common |
| Overlap handling | Round 1 | Narrow additive integration preferred over replacement |

---

## Lessons Learned

### From Gap 170 (original protocol development)

- The coordinating LLM should **always verify reviewer claims** against source files. Reviewers working from briefings (not codebase access) may cite wrong Article/Section numbers.
- **Terminology precision matters**. Constitutional text creates legal meaning. A bridge clause using "congressional obligations" instead of "appropriations authorized by Congress" is a real defect, not a style issue. Use the exact vocabulary from the existing constitutional text.
- **Silent deletion is a finding**. When replacing one provision with another, explicitly account for every feature of the old provision. Either port it, reject it with rationale, or note it as a design decision for the human.
- **Gaming vectors compound**. A provision that is individually sound may create new attack surfaces when combined with other provisions. Reviewers should check cross-gap interactions.
- **Include related resolved gaps in the briefing**. The most important findings in the Gap 170 review were conflicts with already-resolved provisions. Without those cross-references, reviewers cannot catch conflicts.
- **Frame decisions as options, not questions**. "Should we use CPI indexing?" is less useful than "Option A: CPI-index everything. Option B: CPI-index essential functions only. Option C: No CPI indexing anywhere. Tradeoffs: [specific]."

### From Gaps 173-189 (process refinements)

- **Overlap analysis is the key step.** The quality of the overlap analysis determines how many review rounds are needed. A thorough coverage table with specific section citations allows reviewers to focus on genuinely additive elements.
- **Scope narrowing is the most common reviewer finding.** Proposals routinely overstate what they cover. Reviewers consistently identify that existing provisions are scoped narrower than initially assessed (e.g., Gap 173: "§3(e) covers only Regional courts + Federal Floor cases" reduced overlap from 50-60% to 30-35%).
- **Two-tier designs resolve scope conflicts.** When a new provision overlaps with an existing one for some case types but not others, a two-tier design (existing provision handles its cases; new provision handles the rest) avoids both duplication and gaps (e.g., Gap 173 §16(c): automatic stay for non-§4 cases only).
- **The "void ab initio" pattern is powerful.** For prohibitions, declaring the prohibited act void from inception is stronger than requiring a court to invalidate it. Used in Gap 189 §7(n) for alternate certifications.
- **Functional definitions beat enumerated lists for scope.** "No legislature, executive, political party, or other person or body" catches more actors than "No legislature" (Gap 189). "Any instrument, regardless of whether created, issued, or sponsored by a Region" catches adoption-vs-issuance games (Gap 195).
- **Cross-reference savings clauses prevent unintended conflicts.** When adding procedural requirements (like scope limitations on injunctive relief), include an explicit savings clause preserving substantive rights under other provisions (e.g., Gap 173 §16(e) preserving Effective Remedies under §6).
- **Default-to-operation-of-law closes inaction gaps.** When an official can paralyze a process by doing nothing, add a default that triggers automatically (e.g., Gap 189 §7(m): results deemed certified if no option executed within timeframe).

### From the full 16-gap corpus (statistical observations)

- **Placement errors: 16/16 proposals.** Always verify in Step 1a.
- **Institution naming errors: ~6/16 proposals.** Always verify in Step 1b.
- **Overlap range: 30-80%.** Average ~55%. The genuinely additive portion is typically 3-5 subsections.
- **Rounds to convergence: median 1, mean 1.6.** Thorough briefings compress the process.
- **Design decisions per gap: median 6, range 3-8.** Most resolve in a single round when framed as concrete options.
- **Files modified per resolution: median 5-6.** Constitutional text (1-2), crosswalk (1), gap file (1), index (1), stats (1), changelog (1).
