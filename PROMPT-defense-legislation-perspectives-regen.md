# Prompt: Regenerate Defense 11-legislation.md and 12-perspectives.md Files

You are regenerating the `11-legislation.md` and `12-perspectives.md` files for the FixAmerica defense policy analysis. The existing files are skeleton stubs (48-80 lines each) that lack the required template structure. You must replace them with comprehensive, detailed versions.

**Today's date is 2026-01-30.**

---

## Scope

You must regenerate **14 files total**:

### Parent-Level (2 files)

- `analysis/defense/11-legislation.md` (currently 75 lines -- needs to be 600-900 lines)
- `analysis/defense/12-perspectives.md` (currently 48 lines -- needs to be 800-1000 lines)

**Note**: The current parent-level 11-legislation.md is titled "Defense Industrial Base: Model Legislation" and covers only industrial base issues. The regenerated version must cover the **entire defense domain** with 3-4 major federal bills spanning multiple defense reform areas (budget/procurement, personnel, alliances, technology, oversight).

### Subtopic-Level (12 files -- 6 subtopics x 2 files each)

Each subtopic's `11-legislation.md` (currently 68-80 lines -- needs to be 500-700 lines) and `12-perspectives.md` (currently 48-54 lines -- needs to be 800-1000 lines):

| Subtopic Directory | Description |
|---|---|
| `alliances-treaties` | NATO burden-sharing, Indo-Pacific bilateral treaties, AUKUS/Quad, adapting Cold War-era alliances to cyber/space threats |
| `arms-sales` | Foreign Military Sales, Arms Export Control Act, human rights conditions, AI/autonomous systems transfer controls |
| `budget-and-procurement` | PPBE system reform, acquisition process, cost overruns, defense industrial base competition, DoD audit failures |
| `civil-military-relations` | Civilian control of the military, civil-military gap, politicization, oversight of AI/autonomous/cyber capabilities |
| `counterterrorism` | Post-9/11 CT strategy, "over-the-horizon" operations, 2001 AUMF reform, AI for intelligence, drone warfare oversight |
| `cyber-warfare` | USCYBERCOM/NSA, "defend forward" doctrine, critical infrastructure defense, Cyber National Guard, international norms |

### NOT in Scope

The following 15 subtopics have **only README stubs** and lack the supporting files (01-overview through 10-actions) needed for context. They are **not** part of this regeneration task:

`defense-budget`, `defense-technology`, `drone-warfare`, `force-structure`, `foreign-interventions`, `intelligence-oversight`, `maritime-security`, `military-bases`, `military-industrial-complex`, `military-justice`, `military-personnel`, `nuclear-policy`, `space-defense`, `special-operations`, `war-powers`

These require their 01-10 files to be written first, which is a separate task.

---

## Why Regeneration Is Needed

### Current 11-legislation.md Deficiencies (all 7 files)

The existing legislation files are bare draft bills with no surrounding analytical framework. They contain only:
- A title heading
- `SEC.` numbered sections with 1-2 sentence provisions
- A `Document Navigation` footer

They are **missing all of these required sections** (0 of 7 files have them):
- `## Overview` (legislative approach and theory of change)
- `## Constitutional Amendments` (or explanation of why none needed)
- `## Federal Legislation` header (with full bill structure)
- `SEC. DEFINITIONS` (in bill text)
- `## State Model Legislation`
- `## Regulatory Framework`
- `## Legal Considerations`
- `## Loopholes, Shortcomings, and Rectification`
- `## References`

Example of what's currently there (BAD -- this is the entire cyber-warfare legislation file):

```text
# Cyber Warfare: Model Legislation

## DRAFT: The Cyber Resilience and Deterrence Act of 2026

An Act to enhance the cybersecurity...

### SECTION 1. SHORT TITLE.
This Act may be cited as the "Cyber Resilience and Deterrence Act of 2026".

### SECTION 2. FINDINGS.
Congress finds that:
(1) Cyberspace is a critical domain for national security and economic prosperity.
...
[4 bare findings, no statistics or sources]

### TITLE I — NATIONAL CYBER DETERRENCE POLICY
SEC. 101. DECLARATORY POLICY ON RESPONSE TO CYBERATTACKS.
(a) It is the policy of the United States to deter significant cyberattacks...
[2-sentence provision, no subsections]
...

## Document Navigation
```

This is unacceptable. Each bill needs **full legislative text** with Findings (including specific statistics and source citations), Definitions (3+ key terms), multiple substantive sections with subsections, Reporting Requirements, and Authorization of Appropriations. Each file also needs the full surrounding framework: overview, state model legislation, regulatory framework, legal considerations, loopholes analysis, and references.

### Current 12-perspectives.md Deficiencies (all 7 files)

The existing perspectives files use a **completely wrong format**. Instead of the required 9 political perspectives (Conservative, Liberal, Progressive, Libertarian, Constitutionalist, Populist, Centrist, Religious Right, Democratic Socialist), they use 5-6 ad-hoc policy perspectives (e.g., "The National Security / Industrial Policy View," "The Free Market / Libertarian View," "The Persistent Engagement / Hawk View").

They are missing **all** required sections:
- YAML front matter
- Perspective Definitions table
- Scoring Framework
- All 9 standard perspectives with Engagement Consistency, Position Scores, Solution Evaluations, Legislation Evaluations, Alternative Proposals, Coalition Potential
- Summary Tables (Master Comparison, Solution Support Matrix, Legislation Support Matrix, Engagement Consistency Distribution, Common Ground Synthesis)
- Compromise Proposals with Concern Mapping and Concessions tables
- Strategic Implications

---

## Instructions

For each subtopic:

1. **Read the existing files** in that subtopic directory (01-overview through 10-actions) to understand the topic context, key statistics, proposed solutions, and stakeholder landscape
2. **Read the existing 11-legislation.md** to understand what bills are proposed (keep the same bill concepts and names but expand them into the full template structure)
3. **Read the existing 12-perspectives.md** to understand the topic framing (discard the non-standard format entirely; regenerate using the 9 standard political perspectives)
4. **Write the new 11-legislation.md** following the template below
5. **Write the new 12-perspectives.md** following the template below

For the parent level:

1. Read `analysis/defense/01-overview.md` through `10-actions.md` for domain-wide context
2. Write parent-level `11-legislation.md` covering the **full defense domain** (3-4 major federal bills spanning budget/procurement, personnel/workforce, alliances/security, and technology/oversight)
3. Write parent-level `12-perspectives.md` covering the full defense domain

### Topic-Specific Guidance

**Defense legislation differs from domestic policy** in important ways:
- Many provisions amend Title 10 (Armed Forces) or Title 50 (War and National Defense) of the U.S. Code
- The National Defense Authorization Act (NDAA) is the primary legislative vehicle; bills should be structured as standalone acts that could be incorporated into an NDAA
- War powers and executive authority issues require careful constitutional analysis (Article II Commander-in-Chief vs. Article I congressional authority)
- International agreements and treaty obligations constrain legislation
- Classification and intelligence oversight add complexity
- State model legislation is less common for defense topics; substitute with "Congressional Oversight and Reporting Mechanisms" where state legislation doesn't apply, or use state-level cybersecurity, National Guard, or economic development frameworks where relevant

---

## 11-legislation.md Template and Requirements

Each file must include ALL of the following sections. Target length: **500-900 lines**.

```markdown
# [Subtopic Title]: Legislation

## Overview

[2-3 paragraphs describing the legislative approach: what existing law provides the foundation (cite specific statutes like Title 10, the Goldwater-Nichols Act, the War Powers Resolution, the Arms Export Control Act, etc.), why new legislation is needed, and the theory of change. For defense topics, address the relationship between legislative reform and executive authority.]

---

## Constitutional Amendments

*No constitutional amendments are required for [topic]. [Brief explanation of existing constitutional authority -- Article I Section 8 (raise armies, declare war, regulate commerce), Article II (Commander-in-Chief), treaty power, etc. Note any constitutional tensions between congressional and executive authority.]*

---

## Federal Legislation

### The [Full Name] Act

**Purpose**: [1-2 sentences]

**Key Provisions**:

1. [Major provision 1]
2. [Major provision 2]
3. [Major provision 3]
4. [Major provision 4]
5. [Major provision 5]

**Draft Text**:

IMPORTANT: Draft text must include ALL of these sections with substantive content:
- Congress designation and session
- "AN ACT" purpose statement
- SEC. 1. SHORT TITLE
- SEC. 2. FINDINGS (5-8 findings with SPECIFIC statistics and source citations -- e.g., "GAO has identified $XXX billion in cost overruns across major defense acquisition programs (GAO-24-XXX)")
- SEC. 3. DEFINITIONS (define 3+ key terms used in the Act)
- SEC. 4-8. SUBSTANTIVE PROVISIONS (multiple sections with subsections (a), (b), (c) and numbered paragraphs (1), (2), (3))
- SEC. X. REPORTING REQUIREMENTS (what must be reported, to whom, how often)
- SEC. Y. AUTHORIZATION OF APPROPRIATIONS (specific dollar amounts per fiscal year)
- SEC. Z. EFFECTIVE DATE

Each substantive section should have 3-5 subsections. The entire draft text block should be 80-150 lines per bill.

**Explanation of Key Provisions**: [Bullet list explaining WHY each major section matters -- not just what it does, but the problem it solves]

**Implementation Timeline**: [Table with Milestone | Deadline | Responsible Party]

**Challenges**: [2-3 specific implementation challenges]

**Refinements**: [2-3 possible improvements]

---

[Repeat for 2-4 federal bills total]

---

## State Model Legislation

For defense subtopics where state legislation is relevant (cyber-warfare, civil-military relations/National Guard, budget-and-procurement/economic development):

### Model [State Name] Act

**Purpose**: [What this accomplishes at state level]

**Adaptability Notes**: [How states should customize]

**Draft Text**: [Full draft text with SECTION 1 through at least SECTION 4]

For subtopics where state legislation is not applicable (alliances-treaties, counterterrorism, arms-sales), use this alternative:

### Congressional Oversight Mechanisms

[Description of enhanced oversight procedures, reporting requirements, and institutional reforms that don't require new legislation but improve congressional control]

---

## Regulatory Framework

### Administrative Implementation

**Primary Agency**: [DoD, State Department, CISA, etc.]

**Rulemaking Required**:

1. **[Regulation 1]**: [What it covers, statutory deadline]
2. **[Regulation 2]**: [What it governs]
3. **[Regulation 3]**: [What it establishes]

**Enforcement Mechanisms**:

- **Civil Penalties**: [Range, triggers]
- **Administrative Actions**: [Agency tools -- debarment, suspension, etc.]
- **Congressional Review**: [Oversight mechanisms specific to defense]

---

## Legal Considerations

### Constitutional Issues

[Analysis of constitutional basis with relevant case law. For defense topics, always address:
- Article I vs. Article II tensions
- Commander-in-Chief authority limits
- *Youngstown Sheet & Tube Co. v. Sawyer* framework (Jackson concurrence categories)
- *Hamdi v. Rumsfeld*, *Boumediene v. Bush* for detention/counterterrorism topics
- Treaty power and executive agreements
- State secrets and classification issues]

### Preemption

[Federal-state preemption analysis; for defense, focus on federal supremacy in military affairs, National Guard dual status, state cybersecurity frameworks]

### Enforcement and Compliance

[How compliance is ensured -- IG oversight, GAO audits, congressional reporting]

---

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | How It Could Be Exploited | Severity | Proposed Fix |
|----------|---------------------------|----------|--------------|
| [Loophole 1] | [Specific exploitation scenario] | High/Med/Low | [Legislative fix] |
| [Loophole 2] | [Scenario] | [Severity] | [Fix] |
| [Loophole 3] | [Scenario] | [Severity] | [Fix] |
| [Loophole 4] | [Scenario] | [Severity] | [Fix] |
| [Loophole 5] | [Scenario] | [Severity] | [Fix] |

### Known Shortcomings

| Issue | Impact | Root Cause | Mitigation |
|-------|--------|------------|------------|
| [Shortcoming 1] | [Impact] | [Cause] | [Mitigation] |
| [Shortcoming 2] | [Impact] | [Cause] | [Mitigation] |
| [Shortcoming 3] | [Impact] | [Cause] | [Mitigation] |

### Rectification Procedures

1. **[Fix 1]**: [Specific amendment or regulatory language]
2. **[Fix 2]**: [Specific change]
3. **[Fix 3]**: [Specific change]
4. **[Fix 4]**: [Specific change]

### Sunset and Review Provisions

[Reauthorization timeline, required evaluations, GAO reviews]

---

## References

### Statutory References

- [U.S. Code citation] - [What it governs]
- [Public Law citation] - [What it does]

### Case Law

- *[Case Name]*, [Citation] (Court Year) - [What it established]

### Academic and Legal Sources

- [Author]. "[Title]." *Journal* (Year).

---

## Related Topics

- [Related Topic](../related-topic/11-legislation.md) - [How they connect]

---

## Document Navigation

- Up: [Defense](../01-overview.md)
- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
```

---

## 12-perspectives.md Template and Requirements

Each file must include ALL of the following sections. Target length: **800-1000 lines**.

The file MUST use the **full template** from `docs/templates/12-perspectives.md`. The 9 perspectives are: **Conservative, Liberal, Progressive, Libertarian, Constitutionalist, Populist, Centrist, Religious Right, Democratic Socialist**.

**CRITICAL**: Do NOT use the existing ad-hoc perspectives (e.g., "Realist," "Hawk," "Huntingtonian," "Free Market View"). These must be replaced entirely with the 9 standard political perspectives listed above.

### Defense-Specific Guidance for Perspectives

Defense policy creates unusual political coalitions. Keep these dynamics in mind:

- **Conservative**: Generally favors high defense spending, strong military, robust deterrence. May split between defense hawks (more spending) and fiscal hawks (budget discipline).
- **Liberal**: Favors diplomatic solutions, alliance-strengthening, oversight of military spending. Supports defense but questions scale and scope.
- **Progressive**: Skeptical of military spending, prioritizes domestic investment. Favors significant defense cuts, opposes military interventions, emphasizes human rights conditions.
- **Libertarian**: Favors non-interventionism, reduced global military footprint, homeland defense only. Opposes foreign bases and alliances that create entangling commitments.
- **Constitutionalist**: Focuses on proper constitutional authority -- Congress's war powers, Senate treaty ratification, strict interpretation of Commander-in-Chief authority. Critical of executive overreach.
- **Populist**: Anti-establishment, skeptical of "forever wars" and defense contractor profits. May support strong military but opposes interventionism and elite-driven foreign policy.
- **Centrist**: Pragmatic, supports bipartisan defense consensus. Favors measured spending increases, alliance maintenance, and careful reforms.
- **Religious Right**: Supports strong national defense as moral duty, may emphasize religious freedom in military, traditional military culture, and support for Israel.
- **Democratic Socialist**: Favors dramatic defense spending cuts, opposes arms exports, supports conversion of military spending to social programs. Skeptical of military-industrial complex.

```markdown
---
freshness:
  last-reviewed: 2026-01-30
  data-year: 2024
  review-cycle: 12
  sections:
    - name: "Legislation Evaluations"
      data-year: 2024
    - name: "Engagement Consistency Assessment"
      data-year: 2024
notes:
  - Revisit after relevant congressional votes to update legislation status.
  - Flag any new Supreme Court rulings on this topic for reassessment.
  - Update after elections to reflect any changed party positions.
sources:
  count: [NUMBER]
  verified: 2026-01-30
  broken: 0
---

# [Subtopic Title]: Political Perspectives Analysis

## Overview

[Opening paragraph on what fundamental questions this topic raises for different political perspectives]

## Perspective Definitions

| Perspective | Core Values | Policy Orientation |
|-------------|-------------|-------------------|
| Conservative | Tradition, limited government, individual responsibility | Incremental change, fiscal restraint, market solutions |
| Liberal | Progress, equality, social responsibility | Government as problem-solver, regulation, safety nets |
| Progressive | Systemic change, economic justice, structural reform | Transformative reform, wealth redistribution, worker power |
| Libertarian | Individual liberty, minimal state, free markets | Deregulation, privatization, voluntary association |
| Constitutionalist | Original intent, enumerated powers, federalism | Strict constitutional limits, states' rights |
| Populist | Anti-elite, pro-worker, economic nationalism | Trade protection, anti-monopoly, immigration restriction |
| Centrist | Pragmatism, compromise, incremental progress | Bipartisan solutions, evidence-based policy |
| Religious Right | Faith-based values, traditional morality | Social conservatism, religious liberty |
| Democratic Socialist | Worker ownership, public goods, democratic control | Public investment, labor rights, universal programs |

## Scoring Framework

### Position Scores (1-10)

| Score | Meaning |
|-------|---------|
| 10 | Full agreement with project analysis |
| 7-9 | Substantial to strong agreement |
| 5-6 | Mixed/moderate agreement |
| 3-4 | Substantial disagreement |
| 1-2 | Strong opposition |

### Engagement Consistency (1-5)

| Level | Label | Indicators |
|-------|-------|------------|
| 5 | Highly Consistent | Stated positions reflect underlying principles; positions stable when concerns addressed |
| 4 | Mostly Consistent | Principles generally align with positions; minor strategic flexibility |
| 3 | Mixed Consistency | Some positions principled, others reflect coalition pressures |
| 2 | Low Consistency | Positions shift frequently; stated concerns differ from underlying priorities |
| 1 | Unpredictable | Positions driven primarily by opposition dynamics |

### Legislation Status Reference (as of January 2026)

| Bill/Amendment | Type | Current Status | Last Action |
|----------------|------|----------------|-------------|
| [Bill from 11-legislation] | Federal | Proposed | [Status] |

---

## Perspective Analyses

[FOR EACH of the 9 perspectives, include ALL of the following subsections:]

### [Perspective Name] Perspective

#### Engagement Consistency Assessment

**Score: [X]/5 - [Label]**

| Indicator | Assessment |
|-----------|------------|
| Stated vs actual motivations | [Analysis] |
| Principle consistency | [Analysis] |
| Goalpost stability | [Analysis] |
| Zero-sum behavior | [Analysis] |

**Justification:** [Explanation]

**Evidence for assessment:**

- [Specific vote, statement, or action]
- [Platform position or policy document citation]
- [Historical pattern with source]

#### Position Scores

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Current State Assessment | [X]/10 | [Why] |
| Root Cause Agreement | [X]/10 | [Why] |

**Source references:**

- [Think tank or official source]
- [Academic or journalistic source]

#### Solution Evaluations

| Solution | Score | Stated Position | Underlying Concerns |
|----------|-------|-----------------|---------------------|
| [Solution 1 from 07-solutions] | [X]/10 | [What they say] | [Actual motivations] |
| [Solution 2] | [X]/10 | [What they say] | [Actual motivations] |

#### Legislation Evaluations

| Bill | Score | Stated Position | Underlying Concerns |
|------|-------|-----------------|---------------------|
| [Bill 1 from 11-legislation] | [X]/10 | [What they say] | [Actual motivations] |
| [Bill 2] | [X]/10 | [What they say] | [Actual motivations] |

#### Alternative Proposals

[What reforms this perspective would support instead -- 2-4 bullet points]

#### Coalition Potential

- **Natural allies:** [Other perspectives]
- **Potential bridges:** [Perspectives that could be brought on board]
- **Unlikely partners:** [Perspectives with fundamental conflicts]

---

[REPEAT FOR ALL 9 PERSPECTIVES]

---

## Summary Tables

### Master Comparison

| Perspective | Consistency | Current State | Root Causes | Solutions Avg | Legislation Avg |
|-------------|-------------|---------------|-------------|---------------|-----------------|
| Conservative | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Liberal | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Progressive | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Libertarian | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Constitutionalist | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Populist | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Centrist | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Religious Right | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |
| Democratic Socialist | [X]/5 | [X]/10 | [X]/10 | [X]/10 | [X]/10 |

### Solution Support Matrix

| Solution | Con | Lib | Prog | Libt | Const | Pop | Cent | RelR | DemSoc |
|----------|-----|-----|------|------|-------|-----|------|------|--------|
| [Solution 1] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| [Solution 2] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] |

### Legislation Support Matrix

| Bill | Con | Lib | Prog | Libt | Const | Pop | Cent | RelR | DemSoc |
|------|-----|-----|------|------|-------|-----|------|------|--------|
| [Bill 1] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] |
| [Bill 2] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] | [X] |

### Engagement Consistency Distribution

| Level | Count | Perspectives |
|-------|-------|--------------|
| 5 - Highly Consistent | [N] | [List] |
| 4 - Mostly Consistent | [N] | [List] |
| 3 - Mixed Consistency | [N] | [List] |
| 2 - Low Consistency | [N] | [List] |
| 1 - Unpredictable | [N] | [List] |

### Common Ground Synthesis

| Reform Category | Broad Support (5+) | Narrow Support (3-4) | Structural Opposition |
|-----------------|-------------------|---------------------|----------------------|
| [Reform 1] | [Perspectives] | [Perspectives] | [Perspectives] |

---

## Compromise Proposals

### Compromise 1: [Title]

**Bridges:** [Which perspectives]

**Core Agreement:** [Shared values]

**Policy Description:** [Specific proposal]

**Concern Mapping:**

| Perspective | How This Addresses Their Concerns |
|-------------|-----------------------------------|
| [Perspective] | [Appeal] |

**Concessions:**

| Perspective | What They Give Up |
|-------------|-------------------|
| [Perspective] | [Concession] |

**Viability Assessment:**

- **Coalition Size:** [X]/9
- **High Consistency Ratio:** [X]/[X]
- **Durability:** [Assessment]
- **Implementation Path:** [How enacted]

[Include 2-3 compromise proposals]

---

## Strategic Implications

### Most Viable Coalition

[Analysis]

### Key Obstacles

[What prevents agreement]

### Low Consistency Partners

[How to manage unpredictable perspectives]

### Recommended Approach

[Strategic recommendation for advancing reform]

---

## Document Navigation

- Previous: [Legislation](11-legislation.md)
- Up: [Defense](../01-overview.md)
```

---

## Formatting and Style Rules

1. **No emojis** in any file
2. **ATX-style headers** (`#`, `##`, `###`)
3. **Dash-style lists** (`-`)
4. **Single space after list markers** (`1. ` not `1.  `; `- ` not `-   `)
5. **Horizontal rules** (`---`) between major sections
6. **Fenced code blocks** with backticks for draft legislative text
7. **Document navigation** at the bottom of every file
8. **Specific statistics with sources** -- never use vague language like "significant" or "many"
9. **Fiscal years for all budget figures** -- e.g., "$5 billion (FY2027)"
10. Use **2026** for `last-reviewed` and `verified` dates in YAML front matter
11. Use **2024** for `data-year` in YAML front matter (most recent data year available)

---

## Session Management and Batching

**CRITICAL**: This task produces thousands of lines of output across multiple files. A single session **will** exceed output limits if you try to generate all files at once. You MUST split the work into batches.

### Completed Batches (DO NOT REGENERATE)

The following files have already been generated and should NOT be rewritten:

- ~~**Batch 1** (COMPLETE): `budget-and-procurement/11-legislation.md`, `budget-and-procurement/12-perspectives.md`, `arms-sales/11-legislation.md`, `arms-sales/12-perspectives.md`~~
- ~~**Batch 2** (COMPLETE): `civil-military-relations/11-legislation.md`, `civil-military-relations/12-perspectives.md`, `cyber-warfare/11-legislation.md`, `cyber-warfare/12-perspectives.md`~~
- ~~**Batch 3 partial** (COMPLETE): `counterterrorism/11-legislation.md`~~

### Remaining Work

**Start here.** Generate the following 5 files in 2 sessions:

**Session A** (3 files):

1. Read `counterterrorism/` files 01-10 and the already-written `counterterrorism/11-legislation.md`, then write `counterterrorism/12-perspectives.md`
2. Read `alliances-treaties/` files 01-10, then write its `11-legislation.md` and `12-perspectives.md`

**Session B** (2 files -- parent level):

1. Read `analysis/defense/` files 01-10, then write parent-level `11-legislation.md` and `12-perspectives.md`

### Within Each Session

- **Do not read files from other batches** -- only read the context files for the subtopics in your current session
- **Write each file completely** before moving to the next file -- do not leave partial files
- **After completing a session**, stop. The next session will be run separately
- If you are running low on output capacity mid-session, **finish the current file** and note which files remain

### Processing Order Within Each Session

For each subtopic in the session:

1. Read the existing files 01-10 in that subtopic directory
2. Read the existing 11-legislation.md (to preserve bill concepts and names, or to use as context if already complete)
3. Write the new 11-legislation.md (legislation first, since perspectives references it) -- **skip if already complete**
4. Write the new 12-perspectives.md

---

## Quality Checklist

Before considering each file complete, verify:

- [ ] File exceeds minimum line count (500+ for legislation, 800+ for perspectives)
- [ ] All template sections present (see section lists above)
- [ ] Draft legislative text includes SEC. FINDINGS with specific statistics and source citations
- [ ] Draft legislative text includes SEC. DEFINITIONS with 3+ key terms per bill
- [ ] Draft legislative text includes 4+ substantive sections with subsections
- [ ] Draft legislative text includes REPORTING REQUIREMENTS
- [ ] Draft legislative text includes AUTHORIZATION OF APPROPRIATIONS with per-FY amounts
- [ ] Loopholes table has 4+ entries with Proposed Fix column
- [ ] Shortcomings table has 3+ entries with Mitigation column
- [ ] Legal Considerations section addresses Article I vs Article II constitutional tensions
- [ ] References include statutory citations (Title 10, Title 50, specific public laws)
- [ ] References include relevant case law (Youngstown, Hamdi, etc. where applicable)
- [ ] All 9 standard perspectives included in perspectives files (Conservative through Democratic Socialist)
- [ ] YAML front matter present in perspectives files with correct dates (2026-01-30 for review/verified, 2024 for data-year)
- [ ] Each perspective has Engagement Consistency, Position Scores, Solution Evaluations, Legislation Evaluations, Alternative Proposals, and Coalition Potential
- [ ] Perspectives files include Summary Tables (Master Comparison, Solution Support Matrix, Legislation Support Matrix, Engagement Consistency Distribution, Common Ground Synthesis)
- [ ] Perspectives files include 2-3 Compromise Proposals with Concern Mapping and Concessions tables
- [ ] Perspectives files include Strategic Implications section
- [ ] Document Navigation present at bottom of every file
- [ ] No emojis anywhere
- [ ] Horizontal rules between all major sections
- [ ] Single space after list markers (no double-spacing)
