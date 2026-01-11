# Add Legislation File

Generate a properly structured 11-legislation.md file for an analysis topic.

## Usage

```
/add-legislation <domain>/<subtopic>
```

Example: `/add-legislation housing/zoning`

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse arguments** to extract `<domain>` and `<subtopic>`
   - If no arguments, ask: "Which topic needs a legislation file? (e.g., `housing/zoning`)"
   - Verify the topic directory exists

2. **Check if 11-legislation.md already exists**
   - If yes, ask: "Legislation file exists. Overwrite, merge, or cancel?"
   - If merge, read existing content to preserve

3. **Read existing topic files** to understand context:
   - `01-overview.md` - scope and key issues
   - `07-solutions.md` - proposed reforms (basis for legislation)
   - `04-root-causes.md` - problems to address
   - `06-opposition.md` - challenges to anticipate

4. **Determine if constitutional amendments are needed**:
   - Check if solutions require constitutional change
   - Look for references to constitutional barriers
   - Ask user if unclear: "Does this topic require constitutional amendments?"

5. **Generate the legislation file** following this structure:

```markdown
# [Subtopic Title]: Legislation

## Overview

[Based on 01-overview.md and 07-solutions.md, describe the legislative approach]

The legislative strategy for [topic] involves:

- [Key legislative goal 1]
- [Key legislative goal 2]
- [Key legislative goal 3]

## Constitutional Amendments

[If needed:]

### Amendment [Number]: [Title]

**Section 1.** [Substantive provision]

**Section 2.** Congress shall have the power to enforce this article by appropriate legislation.

**Section 3.** This article shall take effect [timing].

**Purpose**: [Why this amendment is necessary]

**Analysis**: [Constitutional implications]

[If not needed:]

No constitutional amendments are required for these reforms. The proposed legislation operates within existing constitutional authority under [relevant clause/power].

## Federal Legislation

### [Primary Bill Name] Act

**Purpose**: [What the bill accomplishes]

**Draft Text**:

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "[Name] Act".

SEC. 2. FINDINGS.
Congress finds that—
(1) [Finding 1];
(2) [Finding 2];
(3) [Finding 3].

SEC. 3. DEFINITIONS.
In this Act:
(1) [TERM].—The term "[term]" means [definition].

SEC. 4. [MAIN PROVISION].
(a) IN GENERAL.—[Primary requirement]
(b) REQUIREMENTS.—[Specific requirements]
(c) EXCEPTIONS.—[Any exceptions]
(d) ENFORCEMENT.—[Enforcement mechanism]

SEC. 5. REGULATIONS.
Not later than [timeframe] after the date of enactment of this Act, the [Agency] shall promulgate regulations to carry out this Act.

SEC. 6. AUTHORIZATION OF APPROPRIATIONS.
There are authorized to be appropriated such sums as may be necessary to carry out this Act.

SEC. 7. EFFECTIVE DATE.
This Act shall take effect [timing].
```

**Explanation**: [How the bill works, section by section]

**Challenges**: [Implementation barriers, political obstacles]

**Refinements**: [Possible improvements or alternatives]

---

[Repeat for additional bills as needed]

## State Model Legislation

### [State Model Bill Name] Act

**Purpose**: [What states can accomplish]

**Draft Text**:

```text
SECTION 1. SHORT TITLE.
This Act may be cited as the "[State] [Name] Act".

SECTION 2. DEFINITIONS.
As used in this Act:
(a) "[Term]" means [definition].

SECTION 3. [MAIN PROVISION].
[Substantive requirements]

SECTION 4. ENFORCEMENT.
[State enforcement mechanism]

SECTION 5. EFFECTIVE DATE.
This Act takes effect [timing].
```

**Explanation**: [How states can adapt this]

**Variation notes**: [How different states might modify]

## Regulatory Framework

### [Agency] Regulations

**Authority**: [Statutory basis]

**Key regulatory requirements**:

1. **[Regulation area 1]**
   - [Requirement]
   - [Standard]

2. **[Regulation area 2]**
   - [Requirement]
   - [Standard]

**Implementation timeline**: [Phases]

**Enforcement mechanisms**: [How compliance is ensured]

## Legal Considerations

### Constitutional Issues

- **[Issue 1]**: [Analysis of constitutional question]
- **[Issue 2]**: [Analysis]

### Preemption

[Federal-state preemption analysis]

### Enforcement

[Enforcement mechanisms and standing issues]

### Judicial Review

[Likely legal challenges and responses]

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity | Exploitation Risk |
|----------|-------------|----------|-------------------|
| [Loophole 1] | [How it could be exploited] | High/Medium/Low | [Who might exploit] |
| [Loophole 2] | [How it could be exploited] | High/Medium/Low | [Who might exploit] |
| [Loophole 3] | [How it could be exploited] | High/Medium/Low | [Who might exploit] |

### Shortcomings

| Issue | Impact | Root Cause | Difficulty to Fix |
|-------|--------|------------|-------------------|
| [Issue 1] | [Effect on goals] | [Why it exists] | High/Medium/Low |
| [Issue 2] | [Effect on goals] | [Why it exists] | High/Medium/Low |

### Rectification Procedures

1. **[Loophole/Issue 1]**: [Specific fix - amendment language or regulatory change]
2. **[Loophole/Issue 2]**: [Specific fix]
3. **[Loophole/Issue 3]**: [Specific fix]

### General Implementation Concerns

- **Capacity**: [Agency capacity issues]
- **Funding**: [Resource requirements]
- **Timeline**: [Realistic implementation concerns]
- **Political durability**: [Risk of repeal or undermining]

## References

### Statutes

- [Relevant U.S. Code citation]

### Case Law

- *[Case name]*, [citation] ([year]) - [relevance]

### Academic Sources

- [Author]. "[Title]." *[Journal]* [vol] ([year]): [pages].

### Reports

- [Organization]. "[Title]." [Year]. [URL]

## Related Topics

- [Related Topic 1: Legislation](../related-topic/11-legislation.md) - [How related]
- [Related Topic 2: Legislation](../other-topic/11-legislation.md) - [How related]

---

## Document Navigation

- Previous: [Actions](10-actions.md)
```

6. **Write the file** to `analysis/<domain>/<subtopic>/11-legislation.md`

7. **Run markdownlint** to verify formatting

8. **Report results**:
   - Confirm file created
   - List sections included
   - Note any placeholders that need filling
   - Suggest: "Review loopholes analysis carefully - this section is critical"

9. **Offer follow-up**:
   - "Run `/validate-topic` to check formatting"
   - "Run `/cross-reference` to add links to related legislation"
