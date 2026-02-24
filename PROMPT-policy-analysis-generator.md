# Prompt for Generating Comprehensive Policy Analysis Content

You are a policy analyst creating comprehensive, evidence-based analysis for the FixAmerica policy project. Your task is to generate detailed policy analysis content for a specified domain and subtopic.

## Content Structure Required

Create the following 12 core files plus 1 README (13 total files):

1. **README.md** - Domain/subdomain overview with file listing
2. **01-overview.md** - Executive summary, scope, key facts, core tensions
3. **02-current-state.md** - Present-day conditions with specific data and statistics
4. **03-history.md** - Historical evolution and key policy milestones
5. **04-root-causes.md** - Systemic analysis of underlying problems
6. **05-stakeholders.md** - Who is affected, who has power, interests and conflicts
7. **06-opposition.md** - Who opposes reform, their arguments, and rebuttals
8. **07-solutions.md** - Proposed reforms and policy interventions
9. **08-roadmap.md** - Implementation timeline, phases, and milestones
10. **09-resources.md** - Further reading, citations, and data sources
11. **10-actions.md** - What individual citizens can do
12. **11-legislation.md** - Draft legislative text and model bills
13. **12-perspectives.md** - Analysis through distinct political perspectives

---

## File Templates and Requirements

### README.md

```markdown
# [Topic Title]

[One-sentence description of the topic]

## Overview

[2-3 paragraph overview explaining what this topic covers, why it matters, and key challenges]

Related topics covered elsewhere:
- **[Related Topic 1]**: See [Link](../related-folder/)
- **[Related Topic 2]**: See [Link](../related-folder/)

## Scope

This analysis covers:

- **[Category 1]**: [Description]
- **[Category 2]**: [Description]
- **[Category 3]**: [Description]

## Files

| File | Description |
|------|-------------|
| [01-overview.md](01-overview.md) | Executive summary and scope |
| [02-current-state.md](02-current-state.md) | Present-day conditions and data |
| [03-history.md](03-history.md) | Historical context and evolution |
| [04-root-causes.md](04-root-causes.md) | Systemic analysis of why problems exist |
| [05-stakeholders.md](05-stakeholders.md) | Who is affected and who has power |
| [06-opposition.md](06-opposition.md) | Who opposes reform and why |
| [07-solutions.md](07-solutions.md) | Proposed reforms and interventions |
| [08-roadmap.md](08-roadmap.md) | Implementation timeline and sequencing |
| [09-resources.md](09-resources.md) | Further reading and citations |
| [10-actions.md](10-actions.md) | What citizens can do |
| [11-legislation.md](11-legislation.md) | Draft legal text and model legislation |
| [12-perspectives.md](12-perspectives.md) | Political perspectives analysis |

---

*[Back to [Domain] Overview](../README.md)*
```

### 01-overview.md

```markdown
# [Topic Title]: Overview

## Overview

[3-4 paragraphs providing:
- What this policy area is and why it matters
- Current state and major challenges
- Strategic significance
- Unique aspects or emerging issues]

## Scope

This analysis covers:

- **[Area 1]**: [Brief description]
- **[Area 2]**: [Brief description]
- **[Area 3]**: [Brief description]
- **[Area 4]**: [Brief description]

## Key Facts

| Metric | Value | Source |
|---|---|---|
| [Key statistic 1] | [Specific value with units] | [Organization, Year] |
| [Key statistic 2] | [Specific value with units] | [Organization, Year] |
| [Key statistic 3] | [Specific value with units] | [Organization, Year] |
| [Key program/law] | [Description] | [Citation] |

**CRITICAL**: Include 6-10 key facts with:
- Specific, current statistics with source citations
- Fiscal years for budget figures (e.g., "FY2024", "FY2025")
- Full source attribution (e.g., "DoD Comptroller, 2024", "SIPRI, March 2024")

## Core Tensions and Tradeoffs

- **[Tension 1]**: [Description of the tradeoff]
- **[Tension 2]**: [Description of the tradeoff]
- **[Tension 3]**: [Description of the tradeoff]
- **[Tension 4]**: [Description of the tradeoff]

## Key Questions

1. [Fundamental question 1]
2. [Fundamental question 2]
3. [Fundamental question 3]
4. [Fundamental question 4]

## Vision of Success

A successful [topic] policy would:

- **[Characteristic 1]**: [Description]
- **[Characteristic 2]**: [Description]
- **[Characteristic 3]**: [Description]
- **[Characteristic 4]**: [Description]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Next: [Current State](02-current-state.md)
```

**Quality Requirements for 01-overview.md**:
- Professional, accessible writing
- Specific examples and data points
- Clear articulation of policy tensions
- Concrete vision of success
- 8-10 well-sourced key facts in table format

### 02-current-state.md

```markdown
---
freshness:
  last-reviewed: [YYYY-MM-DD]
  data-year: [YYYY]
  review-cycle: 6
  sections: []
notes: []
sources:
  count: 0
  verified: [YYYY-MM-DD]
  broken: 0
---

# [Topic Title]: Current State

## [Major Topic Area 1]

[Description of current conditions]

### [Subtopic 1.1]

[Detailed analysis with data]

| Metric | Value | Trend | Source |
|---|---|---|---|
| [Metric 1] | [Value] | [Increasing/Decreasing/Stable] | [Citation] |
| [Metric 2] | [Value] | [Trend] | [Citation] |

### [Subtopic 1.2]

[Analysis]

## [Major Topic Area 2]

[Continue with additional major areas...]

### Key Data Tables

Use tables extensively for:
- Budget breakdowns
- Program statistics
- Performance metrics
- Comparative data

## [Regulatory/Legal Framework if applicable]

### Key Laws and Regulations

| Law/Regulation | Purpose |
|---|---|
| **[Law name]** | [Description] |
| **[Regulation name]** | [Description] |

## [Process Description if applicable]

### The [Process Name]

1. **[Step 1]**: [Description]
2. **[Step 2]**: [Description]
3. **[Step 3]**: [Description]

[Explain timeline, challenges, participants]

## [Emerging Issues/Challenges]

[Discussion of new developments, technological changes, or evolving challenges]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
```

**Quality Requirements for 02-current-state.md**:
- YAML front matter with freshness metadata
- Extensive use of data tables
- Specific, current statistics with sources
- Fiscal years specified for all budget data
- Trend analysis (what's improving/worsening)
- Geographic or demographic breakdowns where relevant
- Process descriptions with specific steps and timelines

### 03-history.md

```markdown
# [Topic Title]: History

## Historical Development

### Early History ([Time Period])

[Origins and foundational developments]

### The [Era Name] ([Years])

[Key developments during this period]

### Key Turning Points

| Year | Event | Significance |
|------|-------|--------------|
| [Year] | [Event description] | [Why it mattered] |
| [Year] | [Event description] | [Why it mattered] |

### Modern Era ([Recent Period])

[Recent historical context leading to current state]

## Evolution of [Key Aspect]

[Timeline showing how specific element changed over time]

## Lessons from History

[What history teaches us about this issue]

### Pattern 1: [Description]

[Historical pattern and its implications]

### Pattern 2: [Description]

[Historical pattern and its implications]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Current State](02-current-state.md)
- Next: [Root Causes](04-root-causes.md)
```

**Quality Requirements**:
- Chronological organization
- Key turning points table
- Connection to present-day issues
- Lessons learned section

### 04-root-causes.md

```markdown
# [Topic Title]: Root Causes

## Systemic Analysis

Why does this problem persist?

## Structural Causes

### [Structural Cause 1]

[Explanation of how system structure creates the problem]

**Evidence**: [Data or examples]

### [Structural Cause 2]

[Continue...]

## Institutional Causes

### [Institutional Cause 1]

[How institutions perpetuate the problem]

### [Institutional Cause 2]

[Continue...]

## Political Economy

### Who Benefits from the Status Quo

| Actor | Benefit | Incentive to Block Reform |
|-------|---------|---------------------------|
| [Actor 1] | [What they gain] | [Why they resist change] |
| [Actor 2] | [What they gain] | [Why they resist change] |

### Perverse Incentives

[Description of misaligned incentives]

## Cultural and Behavioral Factors

[How culture, norms, or behavior patterns contribute]

## Causal Relationships

[Description of how causes interact and reinforce each other]

## Why Reform Has Failed

[Analysis of past reform attempts and why they didn't succeed]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
```

**Quality Requirements**:
- Multiple levels of causation (structural, institutional, political economy)
- Specific examples and evidence
- Political economy analysis identifying beneficiaries
- Explanation of why problems persist despite reform attempts

### 05-stakeholders.md

```markdown
# [Topic Title]: Stakeholders

## Who Is Affected

### Primary Stakeholders

| Group | Impact | Size | Key Interests |
|-------|--------|------|---------------|
| [Group 1] | [How affected] | [Number] | [What they want] |
| [Group 2] | [How affected] | [Number] | [What they want] |

### Secondary Stakeholders

[Groups indirectly affected]

## Who Has Power

### Decision Makers

| Actor | Role | Authority | Influence Level |
|-------|------|-----------|-----------------|
| [Actor 1] | [Position] | [Powers] | High/Medium/Low |

### Key Organizations and Institutions

- **[Organization 1]**: [Their role and influence]
- **[Organization 2]**: [Their role and influence]

## Stakeholder Interests and Alignment

### Aligned Interests (Potential Coalition Partners)

[Groups whose interests align for reform]

### Conflicting Interests

[Where stakeholder interests clash]

### The "Iron Triangle" or Power Structure

[Description of entrenched power relationships, if applicable]

## Influence Mechanisms

How stakeholders exert influence:
- **Lobbying**: [Details]
- **Campaign Contributions**: [Details]
- **Revolving Door**: [Details if applicable]
- **Public Advocacy**: [Details]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Root Causes](04-root-causes.md)
- Next: [Opposition](06-opposition.md)
```

**Quality Requirements**:
- Comprehensive stakeholder tables
- Specific numbers for affected populations
- Power analysis identifying decision-makers
- Coalition mapping

### 06-opposition.md

```markdown
# [Topic Title]: Opposition Analysis

## Who Opposes Reform

### Organized Opposition

| Actor | Interest | Resources | Tactics |
|-------|----------|-----------|---------|
| [Actor 1] | [Why they oppose] | [Financial, political resources] | [How they fight reform] |

### Ideological Opposition

[Principled objections to reform from various political perspectives]

## Opposition Arguments and Rebuttals

### Argument 1: [Claim Title]

**Claim**: [What opponents say]

**Evidence Cited**: [What data they reference]

**Reality**: [Evidence-based response]

**Rebuttal**: [Counter-argument]

### Argument 2: [Claim Title]

**Claim**: [What opponents say]

**Evidence Cited**: [What data they reference]

**Reality**: [Evidence-based response]

**Rebuttal**: [Counter-argument]

[Continue with 4-6 major opposition arguments]

## Historical Patterns of Opposition

[How opposition has evolved over time]

## Counter-Strategies

### Political Strategies

[How to build coalitions and overcome opposition]

### Communication Strategies

[How to frame reform positively]

### Policy Design Strategies

[How to design reforms that reduce opposition]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Stakeholders](05-stakeholders.md)
- Next: [Solutions](07-solutions.md)
```

**Quality Requirements**:
- Comprehensive opposition arguments
- Evidence-based rebuttals
- Fair presentation of opposing views
- Strategic analysis of how to overcome opposition

### 07-solutions.md

```markdown
# [Topic Title]: Solutions

## Reform Framework

### Guiding Principles

- [Principle 1]
- [Principle 2]
- [Principle 3]

### Theory of Change

[How reforms will create desired outcomes]

## Proposed Solutions

### Solution 1: [Title]

**Description**: [What it does and how it works]

**Evidence Base**: [Why we believe this will work - studies, pilot programs, international examples]

**Implementation**: [Specific steps to implement]

**Cost/Resources**: [Budget estimates if applicable]

**Timeline**: [How long to implement]

**Challenges**: [Implementation barriers and how to address them]

**Impact Metrics**: [How to measure success]

### Solution 2: [Title]

[Continue with same structure...]

[Include 5-8 major solutions]

## International Models

### [Country 1]: [Program Name]

**Description**: [What they do]

**Results**: [Outcomes achieved]

**Applicability to U.S.**: [What we can learn/adapt]

### [Country 2]: [Program Name]

[Continue...]

## Pilot Programs and Demonstrations

[Successful pilot programs that could be scaled]

## Sequencing and Prioritization

### Quick Wins (0-2 years)

- [Action that can show early results]

### Medium-term Reforms (2-5 years)

- [More complex changes requiring legislation or institutional reform]

### Long-term Transformation (5-10 years)

- [Fundamental systemic changes]

## Complementary Policies

[Other policy changes needed to support main reforms]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
```

**Quality Requirements**:
- 5-8 detailed, specific solutions
- Evidence base for each proposal
- International examples
- Implementation details including costs and timelines
- Clear sequencing strategy

### 08-roadmap.md

```markdown
---
freshness:
  last-reviewed: [YYYY-MM-DD]
  data-year: [YYYY]
  review-cycle: 12
  sections: []
notes: []
sources:
  count: 0
  verified: [YYYY-MM-DD]
  broken: 0
---

# [Topic Title]: Implementation Roadmap

## Strategic Approach

[Overall strategy for achieving reform - theory of change]

## Phase 1: Foundation (Years 1-2)

### Objectives

- [Objective 1]
- [Objective 2]

### Key Actions

| Action | Lead Actor | Timeline | Resources | Success Metric |
|--------|-----------|----------|-----------|----------------|
| [Action 1] | [Who] | [When] | [What needed] | [How measured] |

### Legislative Requirements

- [Bill or authorization needed]

### Expected Outcomes

[What Phase 1 should achieve]

## Phase 2: Building Momentum (Years 3-5)

### Objectives

- [Objective 1]
- [Objective 2]

### Key Actions

[Same table structure as Phase 1]

### Expected Outcomes

[What Phase 2 should achieve]

## Phase 3: Major Reform (Years 6-10)

### Objectives

- [Objective 1]
- [Objective 2]

### Key Actions

[Same table structure]

### Expected Outcomes

[What Phase 3 should achieve]

## Success Metrics and Milestones

| Milestone | Target Date | Metric | Baseline | Year 3 Target | Year 5 Target | Year 10 Target |
|-----------|-------------|--------|----------|---------------|---------------|----------------|
| [Milestone 1] | [Date] | [Measurement] | [Current] | [Target] | [Target] | [Target] |

## Governance and Oversight

[Who oversees implementation, reporting requirements, accountability mechanisms]

## Risk Mitigation

### Risk 1: [Description]

**Likelihood**: High/Medium/Low

**Impact**: High/Medium/Low

**Mitigation Strategy**: [How to address]

### Risk 2: [Description]

[Continue...]

## Resource Requirements

### Funding

| Phase | Estimated Cost | Funding Source |
|-------|----------------|----------------|
| Phase 1 | [Amount] | [Source] |
| Phase 2 | [Amount] | [Source] |
| Phase 3 | [Amount] | [Source] |
| **Total** | **[Total]** | |

### Personnel

[Staffing needs]

### Infrastructure

[Technology, systems, or facilities needed]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Solutions](07-solutions.md)
- Next: [Resources](09-resources.md)
```

**Quality Requirements**:
- YAML front matter
- 3-phase implementation plan
- Detailed action tables with timelines
- Specific, measurable success metrics
- Risk analysis with mitigation strategies
- Resource estimates

### 09-resources.md

```markdown
# [Topic Title]: Resources

## Academic Research

### Peer-Reviewed Studies

- Author, A. "Title of Study." *Journal Name* vol.# no.# (Year): pages. DOI or URL.
- Author, B., & Author, C. "Title." *Journal* (Year). URL.

### Working Papers

- Organization. "Title." Working Paper Series. Year. URL.

## Government Reports and Data

### Federal Agencies

- [Agency Name]. "Report Title." Year. <URL>
- [Agency Name]. [Dataset Name]. Updated [Date]. <URL>

### Congressional Reports

- Congressional Research Service. "[Title]." Report R##### (Year). <URL>
- Government Accountability Office. "[Title]." GAO-##-### (Year). <URL>

## Books

- Author, A. *Title of Book*. Publisher, Year.
- Author, B., & Author, C. *Title*. Publisher, Year.

## Think Tank Analysis

- [Organization]. "[Report Title]." Year. <URL>
- [Organization]. "[Brief Title]." Year. <URL>

## Organizations and Advocacy Groups

| Organization | Focus | Website | Type |
|--------------|-------|---------|------|
| [Org 1] | [What they do] | [URL] | Research/Advocacy/Trade Assoc. |
| [Org 2] | [What they do] | [URL] | [Type] |

## Data Sources

| Dataset | Provider | Update Frequency | URL |
|---------|----------|------------------|-----|
| [Dataset 1] | [Organization] | [Frequency] | [URL] |

## News and Journalism

### Investigative Reports

- Publication. "Article Title." Date. URL.

### Ongoing Coverage

- Publication. [Topic] coverage. URL.

## International Sources

- [Organization]. "[Title]." Year. <URL>

## Legal Resources

- Case citations
- Statutory references
- Regulatory documents

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Roadmap](08-roadmap.md)
- Next: [Actions](10-actions.md)
```

**Quality Requirements**:
- Comprehensive source list across multiple categories
- Proper citation formatting
- URLs for digital resources
- Mix of academic, government, and policy sources
- Data sources clearly identified

### 10-actions.md

```markdown
# [Topic Title]: Citizen Actions

## What You Can Do

### Individual Actions

#### Learn and Stay Informed

- [Specific action 1]
- [Specific action 2]

#### Make Personal Changes

- [Action 1]
- [Action 2]

#### Use Your Voice

- [Action 1]
- [Action 2]

### Community Actions

#### Organize Locally

- [Action 1]
- [Action 2]

#### Build Coalitions

- [Action 1]
- [Action 2]

### Political Actions

#### Contact Elected Officials

**Template Email/Letter**:

```
Subject: [Topic]

Dear [Representative/Senator],

[Template text]
```

#### Support Legislation

- [Specific bill or initiative to support]
- How to advocate for it

#### Electoral Engagement

- [Voting guide considerations]
- [Candidate question templates]

### Professional Actions

[If applicable - actions people can take in their professional capacity]

## Organizations to Support

| Organization | Focus | How to Help | Website |
|--------------|-------|-------------|---------|
| [Org 1] | [Mission] | Donate/Volunteer/Advocate | [URL] |
| [Org 2] | [Mission] | [Ways to contribute] | [URL] |

## Staying Informed

### Newsletters and Updates

- [Newsletter 1]: [Description and signup URL]
- [Newsletter 2]: [Description and signup URL]

### Social Media

- Follow: [@handle] for [type of content]

### Podcasts and Media

- [Podcast name]: [Description]

## Advocacy Toolkit

### Key Talking Points

1. [Talking point 1]
2. [Talking point 2]

### Common Misconceptions to Counter

| Misconception | Reality |
|---------------|---------|
| [Myth] | [Fact] |

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Resources](09-resources.md)
- Next: [Legislation](11-legislation.md)
```

**Quality Requirements**:
- Specific, actionable items (not vague generalities)
- Template letters/emails
- Concrete organizations with clear actions
- Talking points for advocacy

### 11-legislation.md

```markdown
# [Topic Title]: Legislation

## Overview

[Legislative approach for this topic - comprehensive vs. incremental reform, federal vs. state focus]

## Constitutional Amendments

[If needed, provide draft text and justification]

OR

*No constitutional amendments required for this reform.*

## Federal Legislation

### The [Name] Act

**Purpose**: [What this law accomplishes]

**Key Provisions**:
1. [Major provision 1]
2. [Major provision 2]
3. [Major provision 3]

**Draft Text**:

```text
[CONGRESS AND SESSION]

AN ACT
To [brief purpose statement]

Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,

SECTION 1. SHORT TITLE.

This Act may be cited as the "[Full Name] Act of [Year]".

SEC. 2. FINDINGS.

Congress finds the following:
(1) [Finding with supporting data]
(2) [Finding with supporting data]
(3) [Continue...]

SEC. 3. DEFINITIONS.

In this Act:
(1) [TERM].—The term "[term]" means [definition].
(2) [Continue...]

SEC. 4. [MAIN SUBSTANTIVE PROVISION].

(a) IN GENERAL.—[Main requirement or program]
(b) [SPECIFIC REQUIREMENTS].—
    (1) [Requirement 1]
    (2) [Requirement 2]
(c) AUTHORIZATION OF APPROPRIATIONS.—There are authorized to be appropriated to carry out this section—
    (1) $[amount] for fiscal year [year];
    (2) $[amount] for fiscal year [year]; and
    (3) such sums as may be necessary for each fiscal year thereafter.

[Continue with additional sections...]

SEC. ##. EFFECTIVE DATE.

This Act shall take effect on the date that is [timeframe] after the date of enactment of this Act.
```

**Explanation of Key Provisions**:

- **Section X: [Title]**: [What it does and how it works]
- **Section Y: [Title]**: [What it does and how it works]

**Implementation Timeline**: [When provisions take effect]

**Regulatory Authority**: [Which agency implements]

**Challenges**: [Legal or implementation barriers]

**Refinements**: [Possible improvements to address challenges]

## State Model Legislation

### Model [State Topic] Act

**Purpose**: [What this accomplishes at state level]

**Adaptability Notes**: [How states should customize]

**Draft Text**: [Similar structure to federal legislation]

## Regulatory Framework

### Administrative Implementation

**Primary Agency**: [Which agency]

**Rulemaking Required**:
1. [Regulation 1]: [What it covers]
2. [Regulation 2]: [What it covers]

**Enforcement Mechanisms**: [How compliance is ensured]

## Legal Considerations

### Constitutional Issues

[Analysis of constitutional questions - Commerce Clause, federalism, etc.]

### Preemption

[Federal preemption of state law issues]

### Enforcement

[Civil vs. criminal penalties, private right of action, agency authority]

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity | Proposed Fix |
|----------|-------------|----------|--------------|
| [Loophole 1] | [How it could be exploited] | High/Med/Low | [How to close it] |

### Known Shortcomings

| Issue | Impact | Root Cause | Mitigation |
|-------|--------|------------|------------|
| [Issue 1] | [Effect] | [Why it exists] | [How to address] |

### Rectification Procedures

1. **[Fix 1]**: [Specific legislative or regulatory change]
2. **[Fix 2]**: [Specific change]

### Sunset and Review Provisions

[Mechanisms for evaluating and updating the law]

## References

### Statutory References

- [Existing law citations]

### Case Law

- [Relevant court decisions]

### Academic Sources

- [Legal scholarship]

## Related Topics

- [Cross-references to related legislation in other subtopics]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
```

**Quality Requirements**:
- Actual draft bill text in proper format
- Findings section with current data
- Specific appropriations amounts
- Detailed explanation of provisions
- Loopholes and shortcomings analysis
- Cross-references to related legislation

### 12-perspectives.md

```markdown
# [Topic Title]: Political Perspectives Analysis

## Overview

[Topic] touches on fundamental questions about [core questions related to government role, individual responsibility, market vs. state, etc.]. Different political traditions offer distinct visions for how to approach these challenges.

This analysis examines [topic] through [6-9] distinct political perspectives, exploring how each tradition approaches the core questions and proposed solutions.

## Perspectives Analyzed

### 1. [Perspective Name] (e.g., Progressive, Conservative, Libertarian, etc.)

**Core View**: [Fundamental philosophical position on this issue]

**Stance on Status Quo**: [Whether they see current situation as acceptable]

**Key Priorities**:
- [Priority 1]
- [Priority 2]

**Policy Preferences**:
- [Specific policy position 1]
- [Specific policy position 2]

**Objections to Other Approaches**: [What they oppose and why]

**Key Phrase**: "[Memorable quote capturing this perspective]"

### 2. [Perspective Name]

[Same structure as above]

[Continue for 6-9 perspectives total]

### Recommended Perspectives to Include:

- **Progressive / Social Democrat**
- **Conservative / Traditional**
- **Libertarian / Classical Liberal**
- **Socialist / Democratic Socialist**
- **Populist** (left or right)
- **Pragmatic Centrist / Evidence-Based**
- **Realist** (for foreign policy topics)
- **Idealist / Liberal Internationalist** (for foreign policy)
- **Technocratic / Expert-Driven**

[Choose 6-9 that are most relevant to your specific topic]

## Areas of Agreement

[Surprisingly, where do different perspectives find common ground?]

## Fundamental Disagreements

[Irreconcilable differences in values or priorities]

## Potential Compromises

[Policy approaches that might bridge some divides]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Legislation](11-legislation.md)
```

**Quality Requirements**:
- 6-9 distinct, well-developed perspectives
- Fair representation of each viewpoint
- Specific policy positions, not vague generalities
- Memorable key phrases for each
- Analysis of areas of agreement and fundamental disagreements

---

## Critical Quality Standards

### Data Consistency Requirements

**MANDATORY RULES**:

1. **Use specific, current statistics** with source citations
   - ✓ Good: "Total RDT&E budget: $143.2 billion (FY2025)" with source "DoD Comptroller, FY2025"
   - ✗ Bad: "Over $140 billion" or "around $145 billion"

2. **Cite fiscal years** for ALL budget figures
   - ✓ Good: "$113 billion (FY2023)"
   - ✗ Bad: "$113 billion"

3. **Maintain identical figures** across all files where the same statistic appears
   - If 01-overview says "~$238 billion", 02-current-state can say "$238.4 billion" ONLY if the "~" symbol is used in overview
   - Otherwise, use EXACTLY the same number everywhere

4. **Use precise numbers consistently**
   - If citing "58.1 years" in one place, use "58.1 years" everywhere, not "58 years" or "nearly 58"

5. **Distinguish between different metrics clearly**
   - Example: "44 million experiencing food insecurity" vs "41 million SNAP participants" - these are different metrics and should never be conflated

6. **Specify timeframes**
   - ✓ Good: "2019-2023 average"
   - ✗ Bad: "recent years"

### Writing Quality Standards

1. **Professional, clear prose** - avoid jargon unless necessary and defined
2. **Evidence-based claims** - every major assertion should have a citation
3. **Balanced perspectives** - present multiple viewpoints fairly
4. **Specific examples** - use concrete cases, not just abstractions
5. **Action-oriented** - focus on implementable solutions

### Structural Requirements

1. **Front matter**: Include YAML metadata in 02-current-state.md and 08-roadmap.md
2. **Navigation**: Every file ends with Previous/Next/Up links
3. **Cross-references**: Link to related content within the domain
4. **Tables**: Use markdown tables for comparative data
5. **Consistent formatting**: Follow markdown best practices

### Content Depth Guidelines

**01-overview.md should include**:
- 3-4 paragraph overview
- Scope definition
- 8-10 key facts with specific statistics
- 4-6 core tensions
- 3-4 key questions
- Vision of success

**02-current-state.md should include**:
- Comprehensive data tables with current statistics
- Trend analysis
- Geographic or demographic breakdowns
- Multiple metrics for each major topic area
- Source citations for all data
- Process descriptions with specific steps where applicable

**07-solutions.md should include**:
- 5-8 specific, detailed policy proposals
- Evidence base for each (studies, pilots, international examples)
- Cost estimates where applicable
- Implementation mechanisms
- Timeline for each solution
- Anticipated impacts and outcomes

**11-legislation.md should include**:
- Actual draft bill language
- "Findings" sections with current data
- Specific appropriation amounts
- Detailed explanation of how provisions work
- Legal considerations
- Loopholes and shortcomings analysis with proposed fixes

---

## Examples of Quality Standards

### GOOD Examples:

✓ "Foreign Military Sales (FMS): $80.9 billion (FY2023)" - specific, sourced, fiscal year noted
✓ "NATO members meeting 2% GDP target: 23 of 32 (2024)" - precise, current, sourced
✓ "Average cost overrun for major defense programs: 30-40% (GAO)" - range with source

### BAD Examples to Avoid:

✗ "FMS is about $80 billion" - vague, no fiscal year
✗ "Most NATO members don't meet the target" - imprecise
✗ "Programs often go over budget" - no specific data

---

## Tone and Approach

- **Non-partisan but not neutral** - analyze policies based on evidence and outcomes
- **Solution-focused** - emphasize what can be done, not just problems
- **Comprehensive** - cover the full spectrum of issues within the topic
- **Accessible** - write for informed citizens, not just policy experts
- **Realistic** - acknowledge political constraints and tradeoffs

---

## Citations and Sources

### Use authoritative sources:
- Government agencies (Census Bureau, CBO, GAO, agency reports)
- Academic research and peer-reviewed studies
- Congressional Budget Office and GAO reports
- Think tanks across the political spectrum
- Official program data
- Peer-reviewed journals

### Format citations:
- In tables: `(Organization, Year)` or `(Organization Name YYYY)`
- In text: Inline with hyperlinks where available
- Full citations in 09-resources.md

---

## Validation Checklist

Before submitting, verify:

- [ ] All 13 files created (README + 12 standard files)
- [ ] All statistics appear identically wherever cited
- [ ] All fiscal years are specified for budget figures
- [ ] All sources are properly attributed
- [ ] Navigation links work correctly (Previous/Next/Up)
- [ ] YAML front matter present in 02 and 08
- [ ] Tables are properly formatted
- [ ] No typos or grammatical errors
- [ ] All major claims have citations
- [ ] Cross-references between files are accurate
- [ ] File titles match the topic consistently

---

## Domain-Specific Guidance

When creating content, consider the domain context. For example:

### Defense Domain:
- Include data on budget levels, force structure, personnel, equipment
- Reference specific weapons programs, treaties, or operations
- Address strategic threats and geopolitical context
- Consider civil-military relations and oversight issues

### Economic Domain:
- Include data on employment, wages, GDP impacts, business statistics
- Reference specific industries, sectors, and market structures
- Address distributional impacts and equity concerns
- Consider macroeconomic effects

### Social Policy Domain:
- Include demographic data, benefit levels, participation rates
- Reference specific programs and eligibility criteria
- Address equity and access issues
- Consider administrative implementation challenges

[Adapt this section based on the specific domain you're working in]

---

## Deliverable

Provide a complete folder structure with:
- 1 README.md
- 12 core analysis files (01-overview.md through 12-perspectives.md)

**Expected total**: 13 markdown files with comprehensive, internally consistent policy analysis.
