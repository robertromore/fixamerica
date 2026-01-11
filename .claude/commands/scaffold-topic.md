# Scaffold Analysis Topic

Create a new analysis subtopic with all 11 standard files.

## Usage

```
/scaffold-topic <domain>/<subtopic>
```

Example: `/scaffold-topic economic/gig-economy`

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse the arguments** to extract `<domain>` and `<subtopic>`
   - If no arguments provided, ask: "Which domain and subtopic? (e.g., `economic/gig-economy`)"
   - Validate that domain exists in `analysis/` directory

2. **Create the subtopic directory** at `analysis/<domain>/<subtopic>/`

3. **Create all 11 standard files** with proper scaffolding:

### 01-overview.md
```markdown
# [Subtopic Title]

## Overview

*Brief description of this policy area.*

## Scope

This analysis covers:

- *Key area 1*
- *Key area 2*
- *Key area 3*

## Key Facts

- *Statistic or fact 1*
- *Statistic or fact 2*

## Why This Matters

*Explanation of significance.*

---

## Document Navigation

- Next: [Current State](02-current-state.md)
```

### 02-current-state.md
```markdown
# [Subtopic Title]: Current State

## Present Conditions

*Description of current situation.*

## Key Data

| Metric | Value | Source |
|--------|-------|--------|
| *Metric 1* | *Value* | *Citation* |

## Geographic Variation

*Regional differences if applicable.*

## Recent Trends

*Changes in the last 5-10 years.*

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
```

### 03-history.md
```markdown
# [Subtopic Title]: History

## Historical Development

### Early History

*Origins and early development.*

### Key Turning Points

- **[Year]**: *Event and significance*
- **[Year]**: *Event and significance*

### Modern Era

*Recent historical context.*

## Lessons from History

*What history teaches us about this issue.*

---

## Document Navigation

- Previous: [Current State](02-current-state.md)
- Next: [Root Causes](04-root-causes.md)
```

### 04-root-causes.md
```markdown
# [Subtopic Title]: Root Causes

## Systemic Analysis

Why does this problem persist?

### Structural Causes

- *Cause 1*
- *Cause 2*

### Institutional Causes

- *Cause 1*
- *Cause 2*

### Political Economy

*Who benefits from the status quo?*

## Causal Diagram

*Description of how causes interact.*

---

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
```

### 05-stakeholders.md
```markdown
# [Subtopic Title]: Stakeholders

## Who Is Affected

### Primary Stakeholders

| Group | Impact | Size |
|-------|--------|------|
| *Group 1* | *How affected* | *Number* |

### Secondary Stakeholders

*Groups indirectly affected.*

## Who Has Power

### Decision Makers

- *Actor 1*: *Their role and influence*

### Influencers

- *Organization/group*: *Their influence*

## Stakeholder Interests

*Matrix of stakeholder positions.*

---

## Document Navigation

- Previous: [Root Causes](04-root-causes.md)
- Next: [Opposition](06-opposition.md)
```

### 06-opposition.md
```markdown
# [Subtopic Title]: Opposition Analysis

## Who Opposes Reform

### Organized Opposition

| Actor | Interest | Resources | Tactics |
|-------|----------|-----------|---------|
| *Actor 1* | *Why they oppose* | *What they have* | *How they fight* |

### Ideological Opposition

*Principled objections to reform.*

## Opposition Arguments

### Argument 1: *[Title]*

**Claim**: *What they say*

**Reality**: *Evidence-based response*

## Counter-Strategies

*How to address opposition.*

---

## Document Navigation

- Previous: [Stakeholders](05-stakeholders.md)
- Next: [Solutions](07-solutions.md)
```

### 07-solutions.md
```markdown
# [Subtopic Title]: Solutions

## Reform Framework

### Principles

- *Guiding principle 1*
- *Guiding principle 2*

## Proposed Solutions

### Solution 1: *[Title]*

**Description**: *What it does*

**Evidence**: *Why it works*

**Challenges**: *Implementation barriers*

### Solution 2: *[Title]*

**Description**: *What it does*

**Evidence**: *Why it works*

**Challenges**: *Implementation barriers*

## International Models

*Examples from other countries.*

## Sequencing

*Which reforms should come first?*

---

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Next: [Roadmap](08-roadmap.md)
```

### 08-roadmap.md
```markdown
# [Subtopic Title]: Implementation Roadmap

## Strategic Approach

*Overall strategy for achieving reform.*

## Phase 1: Foundation

- *Action item 1*
- *Action item 2*

## Phase 2: Building Momentum

- *Action item 1*
- *Action item 2*

## Phase 3: Major Reform

- *Action item 1*
- *Action item 2*

## Success Metrics

| Goal | Metric | Target |
|------|--------|--------|
| *Goal 1* | *How measured* | *Target value* |

## Risk Mitigation

*Potential obstacles and responses.*

---

## Document Navigation

- Previous: [Solutions](07-solutions.md)
- Next: [Resources](09-resources.md)
```

### 09-resources.md
```markdown
# [Subtopic Title]: Resources

## Academic Research

- *Author*. "*Title*." *Journal* vol (year): pages.

## Reports and Data

- *Organization*. "*Report Title*." Year. URL.

## Books

- *Author*. *Title*. Publisher, Year.

## Organizations

| Organization | Focus | Website |
|--------------|-------|---------|
| *Org name* | *What they do* | *URL* |

## News and Journalism

- *Publication*. "*Article Title*." Date. URL.

---

## Document Navigation

- Previous: [Roadmap](08-roadmap.md)
- Next: [Actions](10-actions.md)
```

### 10-actions.md
```markdown
# [Subtopic Title]: Citizen Actions

## What You Can Do

### Individual Actions

- *Action 1*
- *Action 2*

### Community Actions

- *Action 1*
- *Action 2*

### Political Actions

- *Action 1*
- *Action 2*

## Organizations to Support

| Organization | Focus | How to Help |
|--------------|-------|-------------|
| *Org name* | *Mission* | *Ways to contribute* |

## Staying Informed

*Resources for ongoing engagement.*

---

## Document Navigation

- Previous: [Resources](09-resources.md)
- Next: [Legislation](11-legislation.md)
```

### 11-legislation.md
```markdown
# [Subtopic Title]: Legislation

## Overview

*Legislative approach for this topic.*

## Constitutional Amendments

*If needed, or state "No constitutional amendments required."*

## Federal Legislation

### [Bill Name] Act

**Purpose**: *What it accomplishes*

**Draft Text**:

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "[Name] Act".

SEC. 2. [PROVISION].
(a) IN GENERAL.—[Main requirement]
(b) DEFINITIONS.—[Key terms]
```

**Explanation**: *How it works*

**Challenges**: *Implementation barriers*

**Refinements**: *Possible improvements*

## State Model Legislation

*Adaptable state-level bills.*

## Regulatory Framework

*Administrative implementation.*

## Legal Considerations

*Constitutional issues, preemption, enforcement.*

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| *Loophole 1* | *How it could be exploited* | High/Medium/Low |

### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| *Issue 1* | *Effect* | *Why it exists* |

### Rectification Procedures

1. *Fix for loophole/shortcoming 1*
2. *Fix for loophole/shortcoming 2*

### General Implementation Concerns

*Broader issues with implementation.*

## References

*Citations to law, cases, academic sources.*

## Related Topics

- [Related Topic 1](../related-topic/11-legislation.md)

---

## Document Navigation

- Previous: [Actions](10-actions.md)
```

4. **Replace placeholders**:
   - Replace `[Subtopic Title]` with properly formatted title (e.g., "Gig Economy")
   - Update navigation links

5. **Update parent overview** if `analysis/<domain>/01-overview.md` exists:
   - Add the new subtopic to any existing subtopic list

6. **Run markdownlint** on created files to verify compliance

7. **Report results**:
   - List all created files
   - Note any issues
   - Suggest next steps (e.g., "Start by filling in 01-overview.md")
