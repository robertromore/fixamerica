# Prompt for Generating Comprehensive Policy Analysis Content

You are a policy analyst creating comprehensive, evidence-based analysis for the FixAmerica policy project. Your task is to generate detailed policy analysis content for a specified domain and subtopic following a standardized 13-file structure.

## Task Overview

Generate a complete policy analysis subdirectory containing:
- **1 README.md** - Subdomain overview with file listing
- **12 standard analysis files** (01-overview.md through 12-perspectives.md)

**Total deliverable**: 13 markdown files with comprehensive, internally consistent policy analysis.

---

## File-by-File Templates and Requirements

### README.md

**Purpose**: Provide overview of the subdomain and navigation to all analysis files

**Template**:
```markdown
# [Subtopic Title]

This subdirectory provides a detailed analysis of [brief description of what this covers].

## Overview

[2-3 paragraphs explaining:
- What this policy area encompasses
- Why it matters and current challenges
- Key aspects covered in the analysis]

This analysis examines [specific aspects], including [key areas]. It explores [major themes] and proposes [approach to solutions].

## File Listing

- **[01-overview.md](01-overview.md):** Executive summary of [subtopic]
- **[02-current-state.md](02-current-state.md):** Detailed data on [key aspects]
- **[03-history.md](03-history.md):** The evolution of [topic] from [era] to present
- **[04-root-causes.md](04-root-causes.md):** Systemic analysis of [core problems]
- **[05-stakeholders.md](05-stakeholders.md):** The roles of [key actors]
- **[06-opposition.md](06-opposition.md):** Arguments against reforms
- **[07-solutions.md](07-solutions.md):** Proposals for [type of reform]
- **[08-roadmap.md](08-roadmap.md):** Phased implementation plan
- **[09-resources.md](09-resources.md):** Key [research/reports/analysis]
- **[10-actions.md](10-actions.md):** How citizens can [engage/help/advocate]
- **[11-legislation.md](11-legislation.md):** Draft text for [legislative approach]
- **[12-perspectives.md](12-perspectives.md):** Differing views on [core questions]
```

**Quality Standards**:
- Clear, concise overview (2-3 paragraphs)
- File listing with specific, descriptive summaries (not generic boilerplate)
- Customized descriptions that reflect actual content
- Professional tone

---

### 01-overview.md

**Purpose**: Executive summary providing scope, key facts, core tensions, and vision

**Template**:
```markdown
# [Subtopic Title]: Overview

## Overview

[3-4 substantive paragraphs covering:
1. What this policy area is and its significance
2. Current state and major challenges
3. Strategic importance or emerging issues
4. Core tensions or unique complexities]

## Scope

This analysis covers the key aspects of [topic]:

- **[Area 1]**: [Description]
- **[Area 2]**: [Description]
- **[Area 3]**: [Description]
- **[Area 4]**: [Description]
- **[Area 5]**: [Description]

## Key Facts

| Metric | Value | Source |
|---|---|---|
| [Statistic 1] | [Specific value with units] | [Organization, Year] |
| [Statistic 2] | [Specific value with units] | [Organization, Year] |
| [Statistic 3] | [Specific value with units] | [Organization, Year] |
| [Statistic 4] | [Specific value with units] | [Organization, Year] |
| [Statistic 5] | [Specific value with units] | [Organization, Year] |
| [Statistic 6] | [Specific value with units] | [Organization, Year] |
| [Key Law/Program] | [Description] | [Citation] |
| [Key Law/Program] | [Description] | [Citation] |

## Core Tensions and Tradeoffs

- **[Tension 1 Name]**: [Description of the fundamental tradeoff or dilemma]
- **[Tension 2 Name]**: [Description of the fundamental tradeoff or dilemma]
- **[Tension 3 Name]**: [Description of the fundamental tradeoff or dilemma]
- **[Tension 4 Name]**: [Description of the fundamental tradeoff or dilemma]
- **[Tension 5 Name]**: [Description of the fundamental tradeoff or dilemma]

## Key Questions

1. [Fundamental question about the topic]
2. [Question about policy approach or tradeoffs]
3. [Question about implementation or oversight]
4. [Question about future challenges or adaptations]

## Vision of Success

A successful [topic] policy in the 21st century would feature:

- **[Characteristic 1]**: [Description of desired outcome]
- **[Characteristic 2]**: [Description of desired outcome]
- **[Characteristic 3]**: [Description of desired outcome]
- **[Characteristic 4]**: [Description of desired outcome]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Next: [Current State](02-current-state.md)
```

**Quality Standards**:
- **CRITICAL**: Include 8-10 specific key facts with precise numbers and sources
- Fiscal years MUST be specified for all budget figures (e.g., "FY2024", "FY2025")
- Core tensions should present genuine dilemmas, not easy choices
- Vision should be concrete and measurable
- Professional, engaging prose

---

### 02-current-state.md

**Purpose**: Comprehensive present-day data, conditions, and trends

**Template**:
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

# [Subtopic Title]: Current State

## [Major Topic Area 1]

[Description of current conditions in this area]

### [Subtopic 1.1]

[Detailed analysis with specific data]

| Metric | Value | Trend | Source |
|---|---|---|---|
| [Metric 1] | [Value] | [↑/↓/Stable] | [Citation, Year] |
| [Metric 2] | [Value] | [Trend] | [Citation, Year] |

### [Subtopic 1.2]

[Analysis of another aspect]

## [Major Topic Area 2]

[Continue with 3-5 major topic areas...]

### Key Indicators Table

| Indicator | Current Value | 5-Year Trend | Note |
|---|---|---|---|
| [Indicator 1] | [Value] | [Description] | [Context] |
| [Indicator 2] | [Value] | [Description] | [Context] |

## [Regulatory/Legal Framework if applicable]

### Key Laws and Regulations

| Law/Regulation | Year | Purpose |
|---|---|---|
| **[Law Name]** | [Year] | [What it does] |
| **[Regulation]** | [Year] | [What it governs] |

## [Process/System Description if applicable]

### The [Process Name]

1. **[Step 1]**: [Description, timeline, responsible parties]
2. **[Step 2]**: [Description, timeline, responsible parties]
3. **[Step 3]**: [Description, timeline, responsible parties]

[Explain challenges, bottlenecks, or inefficiencies]

## Geographic Variation

[Regional differences if applicable - can be table or prose]

## Recent Trends

[Changes in the last 5-10 years with specific data points]

## Emerging Challenges

[New developments, technological changes, or evolving issues]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
```

**Quality Standards**:
- **MANDATORY**: YAML front matter at top
- Extensive use of data tables (at least 3-5 tables)
- ALL statistics must have sources and years
- Trend analysis showing what's improving/worsening
- Process descriptions with specific steps and timelines
- Geographic or demographic breakdowns where relevant
- Recent trends section with 5-10 year perspective

---

### 03-history.md

**Purpose**: Historical evolution providing context for current state

**Template**:
```markdown
# [Subtopic Title]: History

## Historical Development

The [topic] has evolved significantly over time, shaped by [key forces].

---

### [Early Period Name] ([Years]): [Brief Description]

- **[Key Aspect]**: [Description of how things were]
- **[Major Development]**: [What happened and why it mattered]
- **[Important Context]**: [Additional relevant information]

---

### [Middle Period Name] ([Years]): [Brief Description]

- **[Major Change 1]**: [Description]
- **[Major Change 2]**: [Description]
- **[Landmark Event/Law]**: [What happened, why it was significant]

---

### [Modern Period Name] ([Years]): [Brief Description]

- **[Development 1]**: [Description leading to current state]
- **[Development 2]**: [Description]
- **[Recent Changes]**: [Events in last 10-20 years]

---

## Key Turning Points

| Year | Event | Significance |
|------|-------|--------------|
| [Year] | [Event description] | [Why it was a turning point, what changed] |
| [Year] | [Event description] | [Why it was a turning point, what changed] |
| [Year] | [Event description] | [Why it was a turning point, what changed] |

## Lessons from History

[What history teaches us about this issue]

### Pattern 1: [Description]

[Historical pattern and its implications for current policy]

### Pattern 2: [Description]

[Another pattern and what it suggests]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Current State](02-current-state.md)
- Next: [Root Causes](04-root-causes.md)
```

**Quality Standards**:
- Clear chronological organization with era divisions
- Horizontal rules (---) between major eras for visual separation
- Key turning points table with specific years
- Connection between historical events and present-day issues
- "Lessons from History" section analyzing patterns
- Specific dates, legislation names, and key figures

---

### 04-root-causes.md

**Purpose**: Systemic analysis of why problems persist

**Template**:
```markdown
# [Subtopic Title]: Root Causes

## Systemic Analysis

The current challenges in [topic] are not the result of a single failure but of several long-term, interlocking trends. These include [preview of major causes].

## [Major Root Cause Category 1]

### [Specific Cause 1.1]

[Detailed explanation of how this creates or perpetuates the problem]

**Evidence**: [Data, examples, or studies demonstrating this cause]

### [Specific Cause 1.2]

[Continue...]

## [Major Root Cause Category 2]

### [Specific Cause 2.1]

[How this factor contributes to the problem]

**Evidence**: [Supporting data or examples]

### [Specific Cause 2.2]

[Continue...]

## Political Economy

### Who Benefits from the Status Quo

| Actor | Benefit | Economic Value | Incentive to Block Reform |
|-------|---------|----------------|---------------------------|
| [Actor 1] | [What they gain] | [$ or scale if quantifiable] | [Why they resist change] |
| [Actor 2] | [What they gain] | [$ or scale] | [Why they resist change] |

### Perverse Incentives

[Description of how current system creates misaligned incentives]

## [Cultural/Behavioral/Institutional Factors if applicable]

[How culture, norms, institutions, or behavioral patterns contribute]

## Causal Chain

[Description or simple diagram showing how causes interact and reinforce each other]

```text
[Cause A] Creates [Condition B]
    ↓
[Condition B] Leads to [Problem C]
    ↓
[Problem C] Reinforces [Cause A]
```

## Why Reform Has Failed

[Analysis of past reform attempts and why they haven't succeeded]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
```

**Quality Standards**:
- Multiple levels of causation (structural, institutional, political economy, cultural)
- Specific examples and evidence for each cause
- Political economy analysis identifying who benefits from status quo
- Causal chain showing how problems reinforce each other
- Analysis of why past reforms failed
- Evidence-based, not merely speculative

---

### 05-stakeholders.md

**Purpose**: Identify who is affected and who has power to change things

**Template**:
```markdown
# [Subtopic Title]: Stakeholders

The [topic] is shaped by the interactions of several key groups, each with its own [interests/power/resources].

## Who Is Affected

### Primary Stakeholders

| Group | Impact | Size | Key Interests |
|-------|--------|------|---------------|
| [Group 1] | [How they're affected] | [Number of people/entities] | [What they want] |
| [Group 2] | [How they're affected] | [Number] | [What they want] |
| [Group 3] | [How they're affected] | [Number] | [What they want] |

### Secondary Stakeholders

[Groups indirectly affected]

- **[Group 1]**: [How they're affected, size if known]
- **[Group 2]**: [How they're affected]

## Who Has Power

### Decision Makers

| Actor | Role | Authority | Resources | Influence Level |
|-------|------|-----------|-----------|-----------------|
| [Actor 1] | [Position/role] | [Legal powers] | [Budget/staff] | High/Medium/Low |
| [Actor 2] | [Position/role] | [Legal powers] | [Budget/staff] | High/Medium/Low |

### Key Organizations and Institutions

- **[Organization 1]**: [Their role, influence mechanisms, and interests]
- **[Organization 2]**: [Their role, influence mechanisms, and interests]
- **[Organization 3]**: [Their role, influence mechanisms, and interests]

### Influencers

[Groups without formal authority but with significant influence]

- **[Group/Org 1]**: [How they influence - lobbying, public advocacy, expertise]
- **[Group/Org 2]**: [How they influence]

## Stakeholder Interests and Alignment

### Aligned Interests (Potential Coalition Partners)

[Which stakeholder groups share interests that could support reform]

| Coalition | Shared Interest | Strength |
|-----------|-----------------|----------|
| [Groups 1, 2, 3] | [What they all want] | [Strong/Moderate/Weak] |

### Conflicting Interests

[Where stakeholder interests clash]

- **[Conflict 1]**: [Group A] wants [X] but [Group B] wants [Y]
- **[Conflict 2]**: [Description of tension]

### The [Power Structure/Iron Triangle if applicable]

[Description of entrenched power relationships]

## Influence Mechanisms

How stakeholders exert influence on policy:

- **Lobbying**: [Specific details - spending, access, key firms]
- **Campaign Contributions**: [Data if available]
- **Revolving Door**: [Examples if applicable]
- **Public Advocacy**: [Campaigns, media, grassroots]
- **Expertise/Information**: [Control of data, technical knowledge]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Root Causes](04-root-causes.md)
- Next: [Opposition](06-opposition.md)
```

**Quality Standards**:
- Comprehensive stakeholder tables with specific numbers
- Clear distinction between affected parties and power holders
- Coalition mapping showing potential alliances
- Specific influence mechanisms with examples
- Quantitative data where available (population sizes, spending amounts)

---

### 06-opposition.md

**Purpose**: Analyze who opposes reform and their arguments

**Template**:
```markdown
# [Subtopic Title]: Opposition to Reform

Proposals to reform [topic] often face resistance from those who believe [summary of opposition stance].

---

## Who Opposes Reform

### Organized Opposition

| Actor | Interest | Resources | Tactics |
|-------|----------|-----------|---------|
| [Actor 1] | [Why they oppose] | [Financial resources, political access] | [Lobbying, ads, etc.] |
| [Actor 2] | [Why they oppose] | [Resources they command] | [How they fight reform] |

### Ideological Opposition

[Principled objections from various political perspectives]

- **[Perspective 1 - e.g., Conservative]**: [Their objection based on values/principles]
- **[Perspective 2 - e.g., Libertarian]**: [Their objection]
- **[Perspective 3]**: [Their objection]

---

## Opposition Arguments and Rebuttals

### Argument 1: [Title of Claim]

**Claim**: [What opponents say in their own words]

**Evidence Cited**: [What data or examples they reference]

**Reality**: [Evidence-based response to the claim]

**Rebuttal**: [Counter-argument addressing their concerns]

### Argument 2: [Title of Claim]

**Claim**: [What opponents say]

**Evidence Cited**: [What they cite]

**Reality**: [Evidence-based response]

**Rebuttal**: [Counter-argument]

### Argument 3: [Title of Claim]

[Continue with same structure for 4-6 major opposition arguments]

---

## Historical Patterns of Opposition

[How opposition has evolved or remained consistent over time]

## Counter-Strategies

### Political Strategies

[How to build coalitions, leverage public support, navigate opposition]

### Communication Strategies

[How to frame reform positively, address concerns, win public opinion]

### Policy Design Strategies

[How to design reforms to reduce legitimate concerns and split opposition]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Stakeholders](05-stakeholders.md)
- Next: [Solutions](07-solutions.md)
```

**Quality Standards**:
- Fair, accurate representation of opposition arguments
- Evidence-based rebuttals (not dismissive or strawmanning)
- 4-6 major arguments comprehensively addressed
- Specific examples of organized opposition
- Strategic analysis of how to overcome opposition
- Horizontal rules separating major sections

---

### 07-solutions.md

**Purpose**: Propose specific, evidence-based reforms

**Template**:
```markdown
# [Subtopic Title]: Solutions

[Topic] requires a multi-faceted approach that aims to [goals].

---

## Reform Framework

### Guiding Principles

- [Principle 1 - what should guide reform efforts]
- [Principle 2]
- [Principle 3]
- [Principle 4]

### Theory of Change

[How the proposed reforms will create desired outcomes - the logical pathway from actions to results]

---

## Proposed Solutions

### Solution 1: [Descriptive Title]

**Description**: [What it does and how it works - 2-3 paragraphs]

**Evidence Base**: [Why we believe this will work - cite studies, pilot programs, international examples, or theoretical foundations]

**Implementation**: [Specific steps required to put this in place]

**Cost/Resources**: [Budget estimates, personnel needs, or "minimal cost" if applicable]

**Timeline**: [How long to design, pass, and implement]

**Challenges**: [Implementation barriers and how to address them]

**Impact Metrics**: [How to measure whether this is working - specific indicators]

### Solution 2: [Descriptive Title]

[Follow same structure as Solution 1]

### Solution 3: [Descriptive Title]

[Continue for 5-8 major solutions total]

---

## International Models

### [Country 1]: [Program/Policy Name]

**Description**: [What they do differently]

**Results**: [Outcomes they've achieved with data]

**Applicability to U.S.**: [What we can learn, what would need adaptation, what barriers exist]

### [Country 2]: [Program/Policy Name]

[Continue with 2-4 international examples]

---

## Pilot Programs and Demonstrations

[Successful pilot programs in the U.S. that could be scaled, with results]

## Sequencing and Prioritization

### Quick Wins (0-2 years)

- [Action that can show early results and build momentum]
- [Another quick action]

### Medium-term Reforms (2-5 years)

- [More complex changes requiring legislation or institutional change]
- [Another medium-term reform]

### Long-term Transformation (5-10 years)

- [Fundamental systemic changes requiring sustained effort]
- [Another long-term transformation]

## Complementary Policies

[Other policy changes in related areas needed to support main reforms]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
```

**Quality Standards**:
- 5-8 specific, detailed solutions (not vague aspirations)
- Evidence base for EACH proposal (studies, examples, theory)
- Implementation details including costs and realistic timelines
- International examples with actual data on results
- Clear sequencing showing what comes first and why
- Horizontal rules between major sections

---

### 08-roadmap.md

**Purpose**: Phased implementation plan with timelines and metrics

**Template**:
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

# [Subtopic Title]: Implementation Roadmap

## Strategic Approach

[Overall strategy for achieving reform - how phases build on each other, theory of change]

---

## Phase 1: [Phase Name] (Years 1-2)

### Objectives

- [Objective 1 - what this phase aims to accomplish]
- [Objective 2]
- [Objective 3]

### Key Actions

| Action | Lead Actor | Timeline | Resources Needed | Success Metric |
|--------|-----------|----------|------------------|----------------|
| [Action 1] | [Agency/Congress/etc.] | [Specific months] | [Budget, staff, authority] | [How to measure] |
| [Action 2] | [Who leads] | [When] | [What's needed] | [Metric] |
| [Action 3] | [Who leads] | [When] | [What's needed] | [Metric] |

### Legislative Requirements

- [Specific bill or authorization needed, with timeline]
- [Another legislative action required]

### Expected Outcomes

[What Phase 1 should achieve - concrete deliverables and changes]

---

## Phase 2: [Phase Name] (Years 3-5)

### Objectives

- [Objective 1]
- [Objective 2]
- [Objective 3]

### Key Actions

[Same table structure as Phase 1]

### Legislative Requirements

[What new laws or authorizations are needed]

### Expected Outcomes

[What Phase 2 should achieve, building on Phase 1]

---

## Phase 3: [Phase Name] (Years 6-10)

### Objectives

- [Objective 1]
- [Objective 2]

### Key Actions

[Same table structure]

### Expected Outcomes

[What Phase 3 should achieve - the full vision realized]

---

## Success Metrics and Milestones

| Milestone | Target Date | Metric | Baseline (Current) | Year 3 Target | Year 5 Target | Year 10 Target |
|-----------|-------------|--------|-------------------|---------------|---------------|----------------|
| [Milestone 1] | [Date] | [What's measured] | [Current value] | [Target] | [Target] | [Target] |
| [Milestone 2] | [Date] | [What's measured] | [Baseline] | [Target] | [Target] | [Target] |
| [Milestone 3] | [Date] | [What's measured] | [Baseline] | [Target] | [Target] | [Target] |

## Governance and Oversight

[Who oversees implementation, reporting requirements, accountability mechanisms, evaluation process]

## Risk Mitigation

### Risk 1: [Specific Risk Description]

**Likelihood**: High/Medium/Low

**Impact**: High/Medium/Low

**Mitigation Strategy**: [Specific actions to reduce likelihood or impact]

**Contingency Plan**: [What to do if it occurs]

### Risk 2: [Description]

[Continue with 3-5 major risks]

## Resource Requirements

### Funding

| Phase | Estimated Cost | Funding Source | Notes |
|-------|----------------|----------------|-------|
| Phase 1 (Yrs 1-2) | [$X million/billion] | [Appropriation/existing authority] | [Context] |
| Phase 2 (Yrs 3-5) | [$X million/billion] | [Source] | [Context] |
| Phase 3 (Yrs 6-10) | [$X million/billion] | [Source] | [Context] |
| **Total (10 years)** | **[$X million/billion]** | | |

### Personnel

[Staffing needs by phase - FTEs, expertise required]

### Infrastructure

[Technology systems, facilities, or other infrastructure needed]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Solutions](07-solutions.md)
- Next: [Resources](09-resources.md)
```

**Quality Standards**:
- **MANDATORY**: YAML front matter at top
- 3-phase structure with clear progression
- Detailed action tables with specific timelines and responsibilities
- Measurable success metrics with baseline and targets
- Risk analysis with specific mitigation strategies
- Resource estimates with funding sources identified
- Horizontal rules between phases

---

### 09-resources.md

**Purpose**: Curated bibliography and resource list

**Template**:
```markdown
# [Subtopic Title]: Resources

This section provides a curated list of [key research/reports/sources] on [topic].

---

## Academic Research

### Peer-Reviewed Studies

- Author, A., & Author, B. "Title of Study." *Journal Name* vol.# no.# (Year): pages. DOI or URL.
- Author, C. "Title of Paper." *Journal* vol.# (Year): pages. <URL>

### Working Papers and White Papers

- Organization. "Title." Working Paper Series #. Year. <URL>
- Author, D. "Title." Institution Working Paper. Year. <URL>

---

## Government Reports and Data

### Federal Agencies

- [Agency Name]. "Report Title." Publication Date/Year. <URL>
- [Agency Name]. "[Dataset Name]." Updated [Frequency]. <URL>

### Congressional Reports

- Congressional Research Service. "[Title]." Report R##### (Date). <URL>
- Government Accountability Office. "[Title]." GAO-##-### (Date). <URL>

### Agency Data Portals

- [Agency]. [Database Name]. <URL> - [Description of what data is available]

---

## Books

- Author, A. *Title of Book*. Publisher, Year.
- Author, B., & Author, C. *Title*. Publisher, Year. - [Brief description of focus/argument]

---

## Think Tank Analysis

### Research Organizations

- [Organization]. "[Report Title]." Year. <URL> - [Brief description]
- [Organization]. "[Brief Title]." Year. <URL>

### Policy Briefs

- [Organization]. "[Title]." Year. <URL>

---

## Organizations and Advocacy Groups

| Organization | Focus | Type | Website |
|--------------|-------|------|---------|
| [Organization 1] | [What they research/advocate for] | Research/Advocacy/Trade Assoc. | <URL> |
| [Organization 2] | [Focus area] | [Type] | <URL> |
| [Organization 3] | [Focus area] | [Type] | <URL> |

---

## Data Sources

| Dataset | Provider | Update Frequency | URL | Description |
|---------|----------|------------------|-----|-------------|
| [Dataset 1] | [Organization] | [Annual/Quarterly/Monthly] | <URL> | [What data it contains] |
| [Dataset 2] | [Organization] | [Frequency] | <URL> | [What's included] |

---

## News and Journalism

### Investigative Reports

- Publication. "Article Title." Date. <URL> - [Brief note on what it covers]
- Publication. "Article Title." Date. <URL>

### Ongoing Coverage

- *[Publication Name]*. [Topic] coverage. <URL> - [Note about their reporting focus]

---

## International Sources

- OECD. "[Title]." Year. <URL>
- [International Organization]. "[Report]." Year. <URL>

---

## Legal Resources

### Case Law

- *Case Name*, [Citation] (Court Year). - [What the case established]

### Statutory References

- [U.S. Code citation] - [What it governs]
- [Public Law citation] - [What it does]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Roadmap](08-roadmap.md)
- Next: [Actions](10-actions.md)
```

**Quality Standards**:
- Comprehensive sources across multiple categories
- Proper citation formatting
- Working URLs for all digital resources
- Mix of academic, government, think tank, and journalistic sources
- Brief descriptions for major sources
- Organized by type for easy navigation
- Horizontal rules between major sections

---

### 10-actions.md

**Purpose**: Guide citizens on how to engage with the issue

**Template**:
```markdown
# [Subtopic Title]: What You Can Do

[Brief intro on why citizen engagement matters for this topic]

---

## Individual Actions

### Learn and Stay Informed

- [Specific action - e.g., "Subscribe to [Newsletter] for monthly updates on [topic]"]
- [Specific action - e.g., "Follow [Data source] to track [specific metrics]"]
- [Reading recommendation with specific title]

### Make Personal Changes

[If applicable - actions individuals can take in their own lives]

- [Specific, concrete action]
- [Another action]

### Use Your Voice

- **Contact Your Representatives**: [Specific guidance - when, about what issues]
- **Submit Public Comments**: [When opportunities arise, which agencies]
- **Write Letters to the Editor**: [About what specific issues]
- **Share Information**: [On which platforms, what messages]

---

## Community Actions

### Organize Locally

- [Specific organizing suggestion - e.g., "Form a local study group on [topic]"]
- [Action - e.g., "Host town halls with elected officials focused on [issue]"]
- [Action - e.g., "Partner with [type of organization] to [specific goal]"]

### Build Coalitions

- [Coalition-building suggestion]
- [Another specific action]

---

## Political Actions

### Contact Elected Officials

**When to Contact**:
- [Specific timing - e.g., "During budget season", "When X legislation is pending"]
- [Specific occasions]

**What to Say - Template Email**:

```
Subject: [Specific, clear subject line]

Dear [Representative/Senator] [Last Name],

[Opening paragraph - state who you are and why you care]

[Second paragraph - specific ask or position]

[Third paragraph - local impact or personal story if applicable]

Thank you for your service and consideration.

Sincerely,
[Your Name]
[Your City, State]
```

**What to Say - Phone Call Script**:

```
"Hello, my name is [Name] and I'm a constituent from [City]. I'm calling about [specific issue/bill]. I'd like the [Representative/Senator] to [specific ask]. Can you please note my position?"
```

### Support Legislation

Current or proposed legislation to support:

- **[Bill Name/Number]**: [What it does] - [How to advocate: contact committee members, etc.]
- **[Bill Name/Number]**: [What it does] - [How to help]

### Electoral Engagement

**Questions to Ask Candidates**:

1. "[Specific question about their position on X]"
2. "[Question about their plan for Y]"
3. "[Question about oversight/accountability for Z]"

**Voting Considerations**:
- [What to look for in candidate positions]
- [Key committees or positions that matter for this issue]

---

## Professional Actions

[If applicable - actions people can take in their professional roles]

- **[For Profession X]**: [Specific action]
- **[For Profession Y]**: [Specific action]

---

## Organizations to Support

| Organization | Focus | How to Help | Website |
|--------------|-------|-------------|---------|
| [Organization 1] | [Specific mission] | Donate/Volunteer/Spread the word | <URL> |
| [Organization 2] | [Mission] | [Ways to contribute] | <URL> |
| [Organization 3] | [Mission] | [Ways to help] | <URL> |

---

## Staying Informed

### Newsletters and Updates

- **[Newsletter Name]**: [What it covers, frequency] - <Signup URL>
- **[Newsletter Name]**: [Description] - <URL>

### Social Media Accounts to Follow

- [@handle] ([Platform]) - [Type of expert, what they cover]
- [@handle] ([Platform]) - [Description]

### Podcasts and Media

- **[Podcast Name]**: [Description of focus] - <URL>
- **[Media Source]**: [What they cover well] - <URL>

---

## Advocacy Toolkit

### Key Talking Points

When discussing [topic] with others, emphasize:

1. **[Talking Point 1]**: [Concise framing with key stat]
2. **[Talking Point 2]**: [Concise framing]
3. **[Talking Point 3]**: [Concise framing]

### Common Misconceptions to Counter

| Misconception | Reality | Source |
|---------------|---------|--------|
| "[Common myth]" | [Factual correction with data] | [Citation] |
| "[Another myth]" | [Reality] | [Source] |

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Resources](09-resources.md)
- Next: [Legislation](11-legislation.md)
```

**Quality Standards**:
- Specific, actionable items (not vague like "get involved")
- Template letters and phone scripts
- Concrete organizations with clear contribution paths
- Talking points that are concise and backed by data
- Multiple engagement levels (individual, community, political, professional)
- Horizontal rules between major sections

---

### 11-legislation.md

**Purpose**: Draft legislative text and implementation framework

**Template**:
```markdown
# [Subtopic Title]: Legislation

## Overview

[Legislative approach - comprehensive vs. incremental, federal vs. state focus, why legislation is needed]

---

## Constitutional Amendments

[If needed, provide draft text and justification]

**OR**

*No constitutional amendments required for this reform.*

---

## Federal Legislation

### The [Full Name] Act

**Purpose**: [What this law accomplishes in 1-2 sentences]

**Key Provisions**:

1. [Major provision 1 - brief description]
2. [Major provision 2 - brief description]
3. [Major provision 3 - brief description]
4. [Major provision 4 - brief description]

**Draft Text**:

```text
[118th CONGRESS, 1st Session] or [Current Congress and Session]

AN ACT

To [brief purpose statement - e.g., "establish a comprehensive framework for..."]

Be it enacted by the Senate and House of Representatives of the
United States of America in Congress assembled,

SECTION 1. SHORT TITLE.

This Act may be cited as the "[Full Name] Act of [Year]".

SEC. 2. FINDINGS.

Congress finds the following:

(1) [Finding with specific data - e.g., "According to [Source, Year], [statistic/fact]."]
(2) [Finding with data]
(3) [Finding with data]
(4) [Finding establishing problem or need]
(5) [Finding establishing Congressional authority or purpose]

SEC. 3. DEFINITIONS.

In this Act:

(1) [TERM].—The term "[term]" means [precise definition].
(2) [ANOTHER TERM].—The term "[term]" means [definition].
(3) [Continue with all key terms used in the Act]

SEC. 4. [MAIN SUBSTANTIVE PROVISION - e.g., "ESTABLISHMENT OF PROGRAM"].

(a) IN GENERAL.—[Main requirement or program establishment]

(b) [SPECIFIC REQUIREMENTS].—
    (1) [Requirement 1]
    (2) [Requirement 2]
    (3) [Requirement 3]

(c) [ANOTHER SUBSECTION - e.g., "ELIGIBLE ENTITIES"].—
    (1) IN GENERAL.—[Who can participate/benefit]
    (2) [Additional details]

(d) [ADMINISTRATION].—
    (1) DESIGNATED AGENCY.—The [Agency Name] shall administer the program established under subsection (a).
    (2) RESPONSIBILITIES.—In administering the program, the [Agency] shall—
        (A) [responsibility];
        (B) [responsibility]; and
        (C) [responsibility].

SEC. 5. [ANOTHER MAJOR PROVISION].

[Continue with substantive sections...]

SEC. X. REPORTING REQUIREMENTS.

(a) ANNUAL REPORTS.—Not later than [timeframe] after the date of enactment of this Act, and annually thereafter, the [Agency] shall submit to Congress a report that includes—
    (1) [what must be reported];
    (2) [data required];
    (3) [evaluation metrics]; and
    (4) [recommendations for improvements].

(b) PUBLIC AVAILABILITY.—The [Agency] shall make each report submitted under subsection (a) publicly available on the internet website of the [Agency].

SEC. Y. AUTHORIZATION OF APPROPRIATIONS.

There are authorized to be appropriated to carry out this Act—
    (1) $[specific amount] for fiscal year [year];
    (2) $[specific amount] for fiscal year [year+1];
    (3) $[specific amount] for fiscal year [year+2];
    (4) $[specific amount] for fiscal year [year+3]; and
    (5) $[specific amount] for fiscal year [year+4].

SEC. Z. EFFECTIVE DATE.

This Act shall take effect on the date that is [X days/months] after the date of enactment of this Act.
```

**Explanation of Key Provisions**:

- **Section 2 (Findings)**: [Why this section matters, what it establishes]
- **Section 4 ([Main Provision])**: [Detailed explanation of how this works, who it affects, what it requires]
- **Section X (Reporting)**: [Why transparency is required, what will be tracked]
- **Section Y (Appropriations)**: [Budget justification - why this amount, what it covers]

**Implementation Timeline**:

| Milestone | Deadline | Responsible Party |
|-----------|----------|-------------------|
| [Action 1 - e.g., "Agency publishes proposed rules"] | [X days after enactment] | [Agency] |
| [Action 2 - e.g., "Public comment period closes"] | [Timeline] | [Agency/Public] |
| [Action 3 - e.g., "Final rules published"] | [Timeline] | [Agency] |
| [Action 4 - e.g., "Program begins accepting applications"] | [Timeline] | [Agency] |

**Regulatory Authority**: [Which agency implements, what regulatory actions are required]

**Challenges**:

- **[Challenge 1]**: [Potential legal or implementation barrier]
- **[Challenge 2]**: [Another challenge]

**Refinements**:

- **[Refinement 1]**: [Possible improvement to address challenges]
- **[Refinement 2]**: [Another potential improvement]

---

## State Model Legislation

### Model [State Name/Topic] Act

**Purpose**: [What this accomplishes at state level]

**Adaptability Notes**: [How states should customize - population differences, existing law, fiscal capacity]

**Draft Text**:

```text
[Similar structure to federal legislation, adapted for state context]

SECTION 1. SHORT TITLE.

This Act shall be known and may be cited as the "[State Topic] Act of [Year]".

[Continue with findings, definitions, substantive provisions, appropriations, effective date]
```

---

## Regulatory Framework

### Administrative Implementation

**Primary Agency**: [Which federal/state agency has lead responsibility]

**Rulemaking Required**:

1. **[Regulation 1 Title]**: [What it must cover, statutory deadline]
2. **[Regulation 2 Title]**: [What it governs]
3. **[Regulation 3 Title]**: [What it establishes]

**Enforcement Mechanisms**:

- **Civil Penalties**: [Range, what triggers them]
- **Administrative Actions**: [Agency enforcement tools]
- **Private Right of Action**: [Whether individuals can sue, standing requirements]
- **Criminal Penalties**: [If applicable, for what violations]

---

## Legal Considerations

### Constitutional Issues

**[Issue 1 - e.g., Commerce Clause Authority]**: [Analysis of constitutional basis, relevant case law]

**[Issue 2 - e.g., Federalism Concerns]**: [How this respects or challenges federal-state balance]

**[Issue 3 if applicable]**: [Additional constitutional analysis]

### Preemption

[Whether and how federal law preempts state law, express vs. implied preemption, savings clauses]

### Enforcement and Compliance

[How compliance is ensured, inspection authority, penalties for violation]

---

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | How It Could Be Exploited | Severity | Proposed Fix |
|----------|---------------------------|----------|--------------|
| [Loophole 1] | [Specific scenario of how someone could get around the requirement] | High/Med/Low | [Legislative or regulatory language to close it] |
| [Loophole 2] | [Scenario] | [Severity] | [Fix] |

### Known Shortcomings

| Issue | Impact | Root Cause | Mitigation |
|-------|--------|------------|------------|
| [Shortcoming 1] | [What problem this creates] | [Why it exists - political compromise, technical limits, etc.] | [How to address through amendment or regulation] |
| [Shortcoming 2] | [Impact] | [Cause] | [Mitigation] |

### Rectification Procedures

1. **[Fix for Loophole/Shortcoming 1]**: [Specific legislative or regulatory amendment language]
2. **[Fix 2]**: [Specific change needed]
3. **[Fix 3]**: [Specific change needed]

### Sunset and Review Provisions

[If included: timeline for reauthorization, required evaluations, sunset date]

[If not included: argument for why a sunset clause should/shouldn't be added]

---

## References

### Statutory References

- [U.S. Code citation] - [What existing law this builds on or amends]
- [Public Law citation] - [Relevant precedent]

### Case Law

- *[Case Name]*, [Citation] (Court Year) - [What principle this case establishes]
- *[Case Name]*, [Citation] (Court Year) - [Relevance to this legislation]

### Academic and Legal Sources

- [Author]. "[Title]." *Journal* (Year). - [Why this scholarship is relevant]

---

## Related Topics

Cross-references to related legislation in other policy areas:

- [Related Topic 1](../related-topic/11-legislation.md) - [How they connect]
- [Related Topic 2](../related-topic/11-legislation.md) - [Relationship]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Actions](10-actions.md)
- Next: [Perspectives](12-perspectives.md)
```

**Quality Standards**:
- Actual draft bill text in proper legislative format
- Findings section with current, specific data
- Precise appropriations amounts with justification
- Detailed explanation of how provisions work
- Implementation timeline
- Comprehensive loopholes and shortcomings analysis
- Proposed fixes for identified weaknesses
- Proper legal citation format
- Horizontal rules between major sections

---

### 12-perspectives.md

**Purpose**: Analyze the issue through multiple political lenses

**Template**:
```markdown
# [Subtopic Title]: Political Perspectives Analysis

[Opening paragraph explaining what fundamental questions this topic raises about government's role, individual rights, market vs. state, etc.]

Different political traditions offer distinct visions for how to approach [topic]. This analysis examines the issue through [6-9] distinct political perspectives, exploring how each tradition approaches the core questions and proposed solutions.

---

## Perspectives Analyzed

### 1. [Perspective Name - e.g., "Progressive / Social Democrat"]

**Core Belief**: [Fundamental philosophical position - 1-2 sentences on their worldview]

**Stance on [Topic]**: [Their overall view - is current system acceptable, what needs changing]

**Key Priorities**:
- [Priority 1]
- [Priority 2]
- [Priority 3]

**Policy Preferences**:
- [Specific policy position 1]
- [Specific policy position 2]
- [Specific policy position 3]

**Objections to Other Approaches**: [What they oppose and why - e.g., "Rejects market-based solutions as inadequate..."]

**Key Phrase**: "[Memorable quote or slogan capturing this perspective]"

---

### 2. [Perspective Name - e.g., "Conservative / Traditional"]

**Core Belief**: [Philosophical foundation]

**Stance on [Topic]**: [View of current situation and change]

**Key Priorities**:
- [Priority 1]
- [Priority 2]
- [Priority 3]

**Policy Preferences**:
- [Position 1]
- [Position 2]
- [Position 3]

**Objections to Other Approaches**: [What they oppose]

**Key Phrase**: "[Quote]"

---

### 3. [Perspective Name - e.g., "Libertarian / Classical Liberal"]

[Follow same structure]

---

### 4. [Perspective Name - e.g., "Socialist / Democratic Socialist"]

[Follow same structure]

---

### 5. [Perspective Name - e.g., "Populist" (specify left or right)]

[Follow same structure]

---

### 6. [Perspective Name - e.g., "Pragmatic Centrist / Evidence-Based"]

[Follow same structure]

---

### [Additional Perspectives 7-9 as relevant - could include:]

- **Technocratic / Expert-Driven**
- **Realist** (especially for foreign policy)
- **Idealist / Liberal Internationalist** (for foreign policy)
- **Communitarian**
- **Neo-Liberal**
- **Nationalist** (specify economic or cultural focus)

[Choose 6-9 total perspectives most relevant to your specific topic]

---

## Areas of Agreement

Despite their differences, several perspectives find common ground on:

- **[Area 1]**: [What different groups surprisingly agree on and why]
- **[Area 2]**: [Another area of overlap]
- **[Area 3]**: [Third area of potential consensus]

---

## Fundamental Disagreements

Irreconcilable differences that reflect core value conflicts:

- **[Disagreement 1]**: [Progressive/Socialist view] vs [Conservative/Libertarian view] on [specific issue] - [why this is hard to bridge]
- **[Disagreement 2]**: [Perspective A] vs [Perspective B] on [issue]
- **[Disagreement 3]**: [Core values clash description]

---

## Potential Compromises

Policy approaches that might bridge some divides:

- **[Compromise 1]**: [Description of middle-ground approach that addresses concerns from multiple sides]
- **[Compromise 2]**: [Another potential bridge]
- **[Compromise 3]**: [Third possibility]

---

## Document Navigation

- Up: [[Domain]](../01-overview.md)
- Previous: [Legislation](11-legislation.md)
```

**Quality Standards**:
- 6-9 distinct, well-developed perspectives
- Fair, accurate representation of each viewpoint (not caricatures)
- Specific policy positions, not vague generalities
- Memorable "key phrase" for each perspective
- Substantive analysis of agreements and disagreements
- Realistic assessment of compromise possibilities
- Horizontal rules between perspectives for readability

---

## Critical Quality Standards

### Data Consistency Requirements

**MANDATORY RULES THAT MUST BE FOLLOWED**:

1. **Use specific, current statistics** with source citations
   - ✓ Good: "Total defense budget: $842 billion (FY2024)" with source "DoD Comptroller, FY2024"
   - ✗ Bad: "Over $800 billion" or "around $850 billion"

2. **Cite fiscal years for ALL budget figures**
   - ✓ Good: "$113 billion (FY2023)"
   - ✗ Bad: "$113 billion" without fiscal year

3. **Maintain identical figures across all files**
   - If 01-overview says "< 0.5% of population", every other file must use "< 0.5%", not "less than 1%"
   - Only use approximations (~) if CONSISTENTLY used everywhere for that stat

4. **Use precise numbers consistently**
   - If citing "58.1 years" in one place, use "58.1 years" everywhere, not "58 years" or "about 58"

5. **Distinguish between different metrics clearly**
   - Example: "44 million food insecure" vs "41 million SNAP participants" - these are different and should never be conflated

6. **Specify timeframes and years**
   - ✓ Good: "2019-2023 average", "2022 Census", "March 2024 report"
   - ✗ Bad: "recent years", "latest data", "modern era"

### Writing Quality Standards

1. **Professional, accessible prose** - Avoid jargon unless necessary and defined
2. **Evidence-based claims** - Every major assertion needs a citation
3. **Balanced perspectives** - Present multiple viewpoints fairly
4. **Specific examples** - Use concrete cases, not just abstractions
5. **Action-oriented** - Focus on implementable solutions
6. **No scope creep** - Stay within the defined topic boundaries

### Structural Requirements

1. **Front matter**: YAML metadata required in 02-current-state.md and 08-roadmap.md
2. **Navigation**: Every file must end with Previous/Next/Up links
3. **Cross-references**: Link to related content within domain
4. **Tables**: Use markdown tables for comparative data
5. **Formatting**: Horizontal rules (---) to separate major sections
6. **Consistency**: File titles must match topic across all files

### Content Depth Guidelines

**01-overview.md must include**:
- 3-4 paragraph substantive overview
- Clear scope definition with 4-6 areas
- 8-10 key facts with specific statistics
- 4-6 core tensions presenting real dilemmas
- 3-4 key questions
- Concrete vision of success

**02-current-state.md must include**:
- YAML front matter
- 3-5 comprehensive data tables
- Specific statistics with sources and years
- Trend analysis (what's improving/worsening)
- Process descriptions with specific steps where applicable
- Geographic or demographic breakdowns where relevant

**07-solutions.md must include**:
- 5-8 specific, detailed policy proposals
- Evidence base for EACH (studies, pilots, international examples)
- Cost estimates where applicable
- Implementation mechanisms and timelines
- Anticipated impacts and outcomes
- Clear sequencing (quick wins, medium-term, long-term)

**11-legislation.md must include**:
- Actual draft bill language in proper format
- "Findings" sections with current, specific data
- Specific appropriation amounts
- Detailed explanation of how provisions work
- Implementation timeline table
- Legal considerations
- Comprehensive loopholes/shortcomings analysis with proposed fixes

---

## Validation Checklist

Before considering the work complete, verify:

- [ ] All 13 files created (README + 12 standard files)
- [ ] All statistics appear identically wherever cited across files
- [ ] All fiscal years specified for budget figures
- [ ] All sources properly attributed with year
- [ ] Navigation links work correctly (Previous/Next/Up)
- [ ] YAML front matter present in files 02 and 08
- [ ] Tables properly formatted with alignment
- [ ] No typos or grammatical errors
- [ ] All major claims have citations
- [ ] Cross-references between files are accurate
- [ ] File titles consistent across all documents
- [ ] Scope stays within defined boundaries (no scope creep)
- [ ] Horizontal rules (---) used to separate major sections
- [ ] README file listing describes actual content, not generic descriptions

---

## Examples of Quality vs. Poor Execution

### GOOD Examples:

✓ **Statistic**: "Foreign Military Sales (FMS): $80.9 billion (FY2023)" - specific, sourced, fiscal year noted

✓ **Consistency**: If 01-overview says "~67 million beneficiaries", 02-current-state also says "~67 million", not "about 68 million"

✓ **Evidence**: "Studies in Denmark and Finland show that universal basic income pilots reduced poverty by 15-20% (OECD, 2023)" - specific, sourced

✓ **Navigation**: Clear Previous/Next/Up links at bottom of every file

✓ **README description**: "Detailed data on the civil-military gap, public trust, and technological challenges" - specific to actual content

### BAD Examples to Avoid:

✗ **Vague statistic**: "FMS is about $80 billion" - no fiscal year, imprecise

✗ **Inconsistency**: 01-overview says "< 0.5% of population" but 04-root-causes says "less than 1% of population"

✗ **No evidence**: "Programs often go over budget" - no specific data, source, or magnitude

✗ **Missing navigation**: File doesn't end with Previous/Next/Up links

✗ **Generic README**: "Current state and data" - could apply to any topic

---

## Tone and Approach

- **Non-partisan but not neutral** - Analyze policies based on evidence and outcomes
- **Solution-focused** - Emphasize what can be done, not just problems
- **Comprehensive** - Cover full spectrum within topic scope
- **Accessible** - Write for informed citizens, not just experts
- **Realistic** - Acknowledge political constraints and tradeoffs
- **Respectful** - Present opposing views fairly, even when critiquing them

---

## Domain-Specific Guidance Examples

### For Defense Topics:
- Include data on budgets, personnel, equipment, force structure
- Reference specific weapons programs, treaties, operations by name
- Address strategic threats and geopolitical context
- Consider civil-military relations and oversight mechanisms

### For Economic Topics:
- Include employment, wages, GDP impacts, business statistics
- Reference specific industries, sectors, market structures
- Address distributional impacts and equity
- Consider macroeconomic effects and fiscal implications

### For Social Policy Topics:
- Include demographic data, benefit levels, participation rates
- Reference specific programs with eligibility criteria
- Address equity, access, and adequacy issues
- Consider administrative implementation challenges

### For Environmental Topics:
- Include emissions data, resource consumption, impact metrics
- Reference specific regulations, targets, international agreements
- Address cost-benefit analysis and economic impacts
- Consider technological feasibility and timelines

[Adapt based on your specific domain]

---

## Final Deliverable

Provide complete folder structure containing:

**13 Total Files**:
- 1 README.md
- 12 core analysis files (01-overview.md through 12-perspectives.md)

**Expected characteristics**:
- Comprehensive (each file 200-800 lines depending on topic complexity)
- Internally consistent (statistics match across files)
- Evidence-based (every claim sourced)
- Professionally written (clear, accessible, action-oriented)
- Properly formatted (navigation, tables, front matter)
- Publication-ready

---

## Notes on Using This Prompt

When you receive a request to generate analysis for a specific domain/subtopic:

1. Ask clarifying questions if needed about:
   - Specific scope within the topic
   - Any particular emphasis areas
   - Existing related content to cross-reference

2. Research current data from authoritative sources:
   - Government agencies and official statistics
   - Congressional Budget Office, GAO reports
   - Academic research and think tanks
   - Official program data

3. Follow the templates precisely:
   - Use the exact structure provided
   - Include all required sections
   - Maintain formatting standards

4. Verify consistency before delivering:
   - Run through validation checklist
   - Cross-check all statistics across files
   - Ensure navigation links are correct

5. Deliver all 13 files as a complete package

**Remember**: Quality over speed. It's better to take time to research accurate data and craft well-evidenced analysis than to rush and produce superficial or inconsistent content.
