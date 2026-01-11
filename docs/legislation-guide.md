# Legislation File Guide

This guide establishes standards for the `11-legislation.md` files that accompany each topic in the FixAmerica project. These files contain concrete legislative proposals with draft legal text.

## Purpose

The legislation file bridges the gap between policy ideas (in `07-solutions.md`) and practical implementation. It provides:

- Actual draft legislative language
- Constitutional amendment text where needed
- Explanations of why specific language was chosen
- Potential legal challenges and how to address them
- Model legislation that advocates can adapt

## File Structure

### Required Sections

```markdown

# [Topic]: Legislation and Legal Framework

## Overview

Brief introduction to the legislative approach for this topic.

## Constitutional Amendments

(If applicable - many topics won't need this)

### [Amendment Name]

**Purpose**: Why this amendment is necessary
**Draft Text**: The actual amendment language
**Explanation**: Section-by-section breakdown
**Potential Challenges**: Legal/political obstacles
**Refinements**: How to address challenges

## Federal Legislation

### [Bill Name]

**Purpose**: What problem this solves
**Draft Text**: Key statutory language
**Explanation**: Why written this way
**Potential Challenges**: Constitutional, practical, political
**Refinements**: Alternative approaches

## State Model Legislation

### [Model Act Name]

**Purpose**: State-level implementation
**Draft Text**: Model statutory language
**Explanation**: Design choices
**Adaptations**: How states might customize

## Regulatory Framework

### [Agency/Regulation]

**Authority**: Existing statutory basis
**Draft Regulation**: Regulatory text
**Explanation**: Implementation details

## Legal Considerations

### Constitutional Issues
### Preemption Questions
### Enforcement Mechanisms
### Sunset and Review Provisions

## Loopholes, Shortcomings, and Rectification

### [Legislation Name]

#### Potential Loopholes

(Table identifying exploitable gaps in the legislation)

#### Shortcomings

(Table identifying inherent limitations and their root causes)

#### Rectification Procedures

(Numbered list of specific fixes for identified issues)

### General Implementation Concerns

(Cross-cutting issues affecting multiple provisions)

## References

## Related Topics

## Document Navigation

```text

## Writing Legal Text

### Principles

| Principle | Application |
|-----------|-------------|
| Clarity | Avoid ambiguity; define terms |
| Specificity | Concrete requirements, not vague goals |
| Enforceability | Clear who enforces, how, penalties |
| Durability | Anticipate future challenges |
| Flexibility | Allow regulatory adaptation |

### Constitutional Amendment Format

Follow the style of existing amendments:

```markdown
**Section 1.** [Substantive right or prohibition]

**Section 2.** [Scope or definitions if needed]

**Section 3.** Congress shall have the power to enforce this article
by appropriate legislation.

**Section 4.** This article shall take effect [timing provision].

```text

### Statutory Format

Use standard legislative structure:

```markdown
**SEC. 101. SHORT TITLE.**

This Act may be cited as the "[Name] Act of [Year]".

**SEC. 102. FINDINGS.**

Congress finds the following:
(1) [Finding]
(2) [Finding]

**SEC. 103. DEFINITIONS.**

In this Act:
(1) TERM.—The term "[term]" means [definition].

**SEC. 104. [SUBSTANTIVE PROVISION].**

(a) IN GENERAL.—[Main requirement]
(b) EXCEPTIONS.—[Any exceptions]
(c) ENFORCEMENT.—[How enforced]

```text

## Explanation Sections

For each piece of draft text, explain:

1. **Why this language**: The policy goal and how the text achieves it
2. **Alternatives considered**: Other approaches and why not chosen
3. **Precedents**: Similar language in existing law
4. **Key terms**: Why specific words were chosen

Example:

```markdown
**Explanation**:

The phrase "knowing or reckless disregard" establishes a mens rea
requirement that:

- Avoids strict liability (which courts might strike down)
- Covers both intentional bad actors and willfully ignorant ones
- Mirrors language upheld in [Case Name]

We chose "shall" rather than "may" to create a mandatory duty,
not discretionary authority. This ensures consistent enforcement
regardless of administration priorities.

```text

## Addressing Challenges

### Legal Challenges

| Challenge Type | How to Address |
|----------------|----------------|
| First Amendment | Narrow tailoring, content-neutral alternatives |
| Commerce Clause | Document interstate effects |
| Federalism | Spending power, conditional funding |
| Due Process | Clear standards, appeals processes |
| Equal Protection | Rational basis or narrow tailoring |

### Political Challenges

| Challenge Type | How to Address |
|----------------|----------------|
| Partisan opposition | Bipartisan framing, cross-cutting coalitions |
| Industry opposition | Transition periods, grandfather clauses |
| Implementation concerns | Phased rollout, pilot programs |
| Cost concerns | Funding mechanisms, cost-benefit analysis |

## Refinement Section

Each proposal should include a "Refinements" section addressing:

1. **Fallback positions**: Narrower versions if full proposal fails
2. **Strengthening options**: More aggressive versions if political will exists
3. **Technical corrections**: Known issues to fix in future amendments
4. **Sunset provisions**: Built-in review and renewal requirements

## Loopholes, Shortcomings, and Rectification Section

Each legislation file should include a comprehensive analysis of potential weaknesses. This section appears after Legal Considerations and before References.

### Structure

For each major piece of legislation in the file:

#### Potential Loopholes

Create a table with three columns:

| Loophole | Description | Severity |
|----------|-------------|----------|
| Name | How bad actors might exploit this gap | Critical/High/Medium/Low |

**Severity Ratings**:

- **Critical**: Could completely undermine the legislation's purpose
- **High**: Significant exploitation potential affecting many cases
- **Medium**: Exploitable in some circumstances or by sophisticated actors
- **Low**: Minor gap with limited practical impact

**Common Loophole Types**:

- Threshold gaming (structuring to stay below limits)
- Definition ambiguity (interpreting terms narrowly)
- Jurisdictional escape (moving activity to non-covered areas)
- Procedural manipulation (using process to defeat substance)
- Shell games (using intermediaries to obscure activity)

#### Shortcomings

Create a table identifying inherent limitations:

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Limitation name | How this affects the legislation's goals | Why this exists |

**Common Root Causes**:

- Constitutional limitations (First Amendment, federalism, etc.)
- Political compromise (necessary to pass legislation)
- Scope limitations (intentional narrowing)
- Resource constraints (enforcement capacity)
- Implementation challenges (practical difficulties)

#### Rectification Procedures

Provide a numbered list of specific fixes:

1. **Short-term administrative**: Changes that can be made through regulation
2. **Legislative amendments**: Statutory changes to close loopholes
3. **Enforcement guidance**: DOJ/agency interpretation to strengthen application
4. **Future legislation**: Follow-on bills to address shortcomings
5. **Constitutional amendments**: For issues requiring constitutional change

### General Implementation Concerns

At the end of the loopholes section, include:

- **Systemic Issues**: Cross-cutting problems affecting multiple provisions
- **Sunset and Review Provisions**: Required review mechanisms and automatic adjustments

### Example Loophole Analysis

```markdown
### Campaign Disclosure Act

#### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Threshold structuring | Donors may make multiple contributions just below the $1,000 disclosure threshold | High |
| Timing manipulation | Large donations made immediately after reporting deadlines delay public disclosure | Medium |
| Shell organization | Donors may create multiple LLCs to contribute separately | High |

#### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| No real-time disclosure | Public learns of donations weeks after they're made | Technical implementation limits |
| Foreign verification | Difficult to verify domestic vs. foreign funding sources | Enforcement resource limits |

#### Rectification Procedures

1. **Aggregate threshold**: Apply disclosure threshold to cumulative donations from same source
2. **48-hour expedited reporting**: Require faster disclosure for donations over $5,000
3. **Beneficial ownership**: Require disclosure of individuals behind LLC contributions
4. **Technology investment**: Fund real-time disclosure database infrastructure

```text

## Examples

### Good: Specific and Enforceable

```markdown
**SEC. 201. DISCLOSURE REQUIREMENTS.**

(a) IN GENERAL.—Not later than 24 hours after making an independent
expenditure in excess of $10,000 with respect to a covered election,
a covered organization shall file a disclosure report with the
Commission containing—
  (1) the name and address of the covered organization;
  (2) the amount of the expenditure; and
  (3) the name of each person who contributed more than $1,000
      to such organization during the 12-month period preceding
      the expenditure.

```text

### Bad: Vague and Unenforceable

```markdown
Organizations making significant political expenditures should
disclose their donors in a timely manner.

```text

## Quality Checklist

Before finalizing a legislation file, verify:

- [ ] All terms are defined
- [ ] Enforcement mechanism is clear
- [ ] Penalties/consequences specified
- [ ] Timeline/deadlines included
- [ ] Regulatory authority designated
- [ ] Funding source identified (if needed)
- [ ] Constitutional basis articulated
- [ ] Potential challenges addressed
- [ ] Explanation sections complete
- [ ] Refinements/alternatives provided
- [ ] Loopholes identified with severity ratings
- [ ] Shortcomings documented with root causes
- [ ] Rectification procedures specified for each issue
- [ ] General implementation concerns addressed
- [ ] Sunset and review provisions included

## Relationship to Other Files

| File | Relationship |
|------|--------------|
| 07-solutions.md | Policy ideas that legislation implements |
| 08-roadmap.md | Timeline for passing legislation |
| 06-opposition.md | Who will oppose and why |
| 10-actions.md | How citizens can advocate for legislation |

## Citation Requirements

Legislative proposals should cite:

- Existing laws being amended (with U.S. Code citations)
- Court cases establishing constitutional parameters
- Model legislation from other jurisdictions
- Academic analysis of similar proposals

See [Citation Guide](citation-guide.md) for format.
