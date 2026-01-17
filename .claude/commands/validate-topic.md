# Validate Topic

Run comprehensive validation on an analysis topic for formatting, structure, and content quality.

## Usage

```
/validate-topic <domain>/<subtopic>
```

Example: `/validate-topic justice/policing`

Or validate all topics: `/validate-topic --all`

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse arguments**:
   - If specific topic provided, validate that topic
   - If `--all` flag, validate entire `analysis/` directory
   - If no arguments, ask: "Which topic to validate? (or use `--all`)"

2. **Run markdownlint** on all topic files:

   ```bash
   npx markdownlint-cli analysis/<domain>/<subtopic>/*.md
   ```

   Check against project `.markdownlint.json` configuration:
   - ATX-style headers (`#` not underlines)
   - Dash-style lists (`-` not `*` or `+`)
   - 4-space indentation for nested lists
   - Fenced code blocks with backticks
   - Asterisk emphasis (`*italic*`, `**bold**`)

3. **Check file naming conventions**:
   - Files must be numbered 01-11
   - Names must match standard: `01-overview.md`, `02-current-state.md`, etc.
   - No extra files without clear purpose

4. **Check frontmatter on time-sensitive files**:

   Files that should have freshness frontmatter:
   - `01-overview.md` - If contains key statistics
   - `02-current-state.md` - Always (most time-sensitive)
   - `08-roadmap.md` - If contains political landscape, timelines
   - `11-legislation.md` - If contains bill status, pending legislation

   For each applicable file, check for YAML frontmatter with:
   - `freshness.last-reviewed` - Date of last review
   - `freshness.data-year` - Year of most recent data
   - `sources.count` - Number of citations

   Flag as WARNING if frontmatter is missing on these files.
   Suggest: "Run `/freshness-check [path] --update` to add frontmatter"

5. **Validate document structure** for each file:

   **All files must have**:
   - Single H1 title at top
   - Document Navigation section at bottom
   - Proper header hierarchy (no skipping levels)

   **Specific file requirements**:

   | File | Required Sections |
   |------|-------------------|
   | 01-overview.md | Overview, Scope, Key Facts, Why This Matters |
   | 02-current-state.md | Present Conditions, Key Data |
   | 03-history.md | Historical Development |
   | 04-root-causes.md | Systemic Analysis |
   | 05-stakeholders.md | Who Is Affected, Who Has Power |
   | 06-opposition.md | Who Opposes Reform, Opposition Arguments |
   | 07-solutions.md | Reform Framework, Proposed Solutions |
   | 08-roadmap.md | Strategic Approach, Phases |
   | 09-resources.md | At least 2 resource categories |
   | 10-actions.md | Individual Actions, Political Actions |
   | 11-legislation.md | See detailed check below |
   | 12-perspectives.md | Perspective Definitions, Scoring Framework, 9 perspective sections, Summary Tables, Compromise Proposals |

6. **Detailed 11-legislation.md validation**:

   **Required sections** (ERROR if missing):
   - [ ] Overview
   - [ ] Constitutional Amendments OR explicit "not needed" statement
   - [ ] Federal Legislation with draft text
   - [ ] State Model Legislation
   - [ ] Regulatory Framework
   - [ ] Legal Considerations
   - [ ] Loopholes, Shortcomings, and Rectification
   - [ ] References
   - [ ] Related Topics
   - [ ] Document Navigation

   **Loopholes section must contain** (ERROR if missing):
   - [ ] Potential Loopholes table with columns: Loophole, Description, Severity
   - [ ] Shortcomings table with columns: Issue, Impact, Root Cause
   - [ ] Rectification Procedures (numbered list)

   **Draft legislation must follow format**:
   - SEC. numbering for federal bills
   - SECTION numbering for state bills
   - Proper subsection lettering (a), (b), (c)

7. **Detailed 12-perspectives.md validation** (if file exists):

   **Required sections** (ERROR if missing and file is not placeholder):
   - [ ] Perspective Definitions table
   - [ ] Scoring Framework (Position Scores and Faith Levels)
   - [ ] All 9 perspective sections:
     - [ ] Conservative Perspective
     - [ ] Liberal Perspective
     - [ ] Progressive Perspective
     - [ ] Libertarian Perspective
     - [ ] Constitutionalist Perspective
     - [ ] Populist Perspective
     - [ ] Centrist Perspective
     - [ ] Religious Right Perspective
     - [ ] Democratic Socialist Perspective
   - [ ] Summary Tables section with:
     - [ ] Master Comparison table
     - [ ] Solution Support Matrix
     - [ ] Faith Level Distribution
   - [ ] Compromise Proposals section (at least 1 proposal)
   - [ ] Strategic Implications
   - [ ] Document Navigation

   **Each perspective section must contain**:
   - [ ] Faith Level Assessment with score and justification
   - [ ] Position Scores table (Current State, Root Causes)
   - [ ] Solution Evaluations table
   - [ ] Legislation Evaluations table (if 11-legislation.md has bills)
   - [ ] Alternative Proposals
   - [ ] Coalition Potential

   **Placeholder detection**: If file contains "This file is a placeholder" or only has Overview and Status sections, treat as incomplete (WARNING, not ERROR)

8. **Check citation format** per `docs/citation-guide.md`:

   **Valid formats**:
   - U.S. Code: `52 U.S.C. § 10301`
   - Court cases: `*Case Name*, [volume] U.S. [page] ([year])`
   - Academic: `Author. "Title." *Journal* vol (year): pages.`
   - URLs: Must be complete with protocol

   **Flag**:
   - Uncited claims (statements of fact without sources)
   - Broken or malformed citations
   - Missing publication years

9. **Check cross-references**:

- Verify all internal links point to existing files
- Check relative path format (`../topic/file.md`)
- Flag orphan references (links to non-existent files)

1. **Content quality checks** (WARNINGS, not errors):
    - Files under 200 words (likely incomplete)
    - Files with only template text
    - Tables with empty cells
    - TODO or placeholder markers
    - Missing alt text for any images

2. **Generate validation report**:

```markdown
## Validation Report: [domain]/[subtopic]

### Summary

| Category | Errors | Warnings |
|----------|--------|----------|
| Markdown formatting | 2 | 5 |
| File structure | 0 | 1 |
| Frontmatter | 0 | 3 |
| Legislation format | 3 | 2 |
| Citations | 1 | 8 |
| Cross-references | 0 | 3 |
| Content quality | 0 | 4 |
| **Total** | **6** | **26** |

### Errors (Must Fix)

#### Markdown Formatting

1. **03-history.md:45** - MD001: Header levels should increment by one
2. **07-solutions.md:112** - MD004: Inconsistent list style (expected dash)

#### Legislation Format

1. **11-legislation.md** - Missing "Loopholes, Shortcomings, and Rectification" section
2. **11-legislation.md:89** - Federal bill missing SEC. 1 SHORT TITLE
3. **11-legislation.md** - Missing Potential Loopholes table

#### Citations

1. **04-root-causes.md:67** - Malformed citation: missing year

### Warnings (Should Fix)

#### Frontmatter

1. **02-current-state.md** - Missing freshness frontmatter (run `/freshness-check --update`)
2. **08-roadmap.md** - Missing freshness frontmatter
3. **11-legislation.md** - Missing freshness frontmatter

#### Content Quality

1. **02-current-state.md** - Only 156 words (likely incomplete)
2. **08-roadmap.md:34** - Contains "TODO" marker
3. **05-stakeholders.md** - Table has 3 empty cells
4. **09-resources.md** - Only 1 resource category (recommend 2+)

#### Cross-References

1. **07-solutions.md:89** - Link to `../lobbying/07-solutions.md` - file does not exist
2. **11-legislation.md** - Related Topics section has only 1 entry
3. **06-opposition.md** - No cross-references (consider adding)

#### Citations Needed

1. **02-current-state.md:23** - "Studies show..." (needs citation)
2. **04-root-causes.md:45** - Statistical claim without source
...

### File-by-File Status

| File | Errors | Warnings | Status |
|------|--------|----------|--------|
| 01-overview.md | 0 | 1 | ⚠ |
| 02-current-state.md | 0 | 3 | ⚠ |
| 03-history.md | 1 | 2 | ✗ |
| 11-legislation.md | 3 | 2 | ✗ |
...

### Recommended Actions

1. **Critical**: Add loopholes analysis to 11-legislation.md
2. **High**: Fix header hierarchy in 03-history.md
3. **Medium**: Add citations to statistical claims
4. **Low**: Expand 02-current-state.md content
```

1. **For `--all` validation**, produce summary:

```markdown
## Project-Wide Validation Summary

### Topics with Errors

| Topic | Errors | Top Issue |
|-------|--------|-----------|
| justice/policing | 5 | Missing loopholes analysis |
| economic/taxation | 3 | Malformed citations |

### Topics Passing Validation

- political/electoral-reform ✓
- political/campaign-finance ✓
- healthcare/costs ✓

### Most Common Issues

| Issue | Occurrences | Severity |
|-------|-------------|----------|
| Missing loopholes analysis | 12 | Error |
| Missing frontmatter | 89 | Warning |
| Incomplete content (<200 words) | 23 | Warning |
| Uncited claims | 45 | Warning |

### Project Health Score: 72/100

- Structure: 95%
- Formatting: 88%
- Legislation compliance: 65%
- Citation coverage: 62%
```

1. **Offer fixes**:

- "Auto-fix markdown formatting issues?"
- "Generate missing loopholes sections?"
- "Run `/add-legislation` for topics missing legislation files?"
- "Run `/freshness-check --update` to add frontmatter?"
- "Run `/analyze-perspectives` to generate perspectives analysis?"
