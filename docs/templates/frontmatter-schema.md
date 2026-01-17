# Frontmatter Schema for Analysis Files

This document defines the YAML frontmatter schema used to track content freshness and source metadata in analysis files.

## Purpose

Frontmatter enables:

- Quick freshness checks without parsing entire documents
- Per-section tracking of data currency
- Source counting and verification status
- Automated staleness detection

## Schema

```yaml
---
freshness:
  last-reviewed: YYYY-MM-DD    # Date file was last reviewed for accuracy
  data-year: YYYY              # Year of most recent data cited in file
  review-cycle: 12             # Months until next review needed (default: 12)
  sections:                    # Optional: per-section freshness tracking
    - name: "Section Name"     # Must match H2 or H3 header exactly
      data-year: YYYY          # Year of data in that section
notes:                         # Optional: future reminders for reviewers
  - "Flag when X happens"      # e.g., pending court case, expected legislation
  - "Revisit after Y"          # e.g., election results, agency rulemaking
sources:
  count: N                     # Total number of source citations
  verified: YYYY-MM-DD         # Date sources were last checked for broken links
  broken: N                    # Number of known broken links (0 = all good)
---
```

## Field Definitions

### freshness.last-reviewed

**Type:** Date (YYYY-MM-DD)
**Required:** Yes

The date when someone last reviewed this file for accuracy. Updated by `/freshness-check --update` or manually after reviewing content.

### freshness.data-year

**Type:** Year (YYYY)
**Required:** Yes

The year of the most recent time-sensitive data cited anywhere in the file. For example, if a file cites "2024 statistics" and "2023 reports," this should be `2024`.

### freshness.review-cycle

**Type:** Integer (months)
**Required:** No (default: 12)

How many months before this file should be reviewed again. Use shorter cycles for rapidly changing topics:

- `6` - Fast-moving topics (elections, legislation status)
- `12` - Standard policy topics (default)
- `24` - Stable topics (historical analysis)

### freshness.sections

**Type:** Array of objects
**Required:** No

Per-section freshness tracking for files with mixed-age data. Each section object has:

- `name`: String matching the section header exactly
- `data-year`: Year of data in that section

Example:

```yaml
sections:
  - name: "Trust and Approval"
    data-year: 2025
  - name: "Electoral Competition"
    data-year: 2024
  - name: "Money in Politics"
    data-year: 2024
```

### notes

**Type:** Array of strings
**Required:** No

Future reminders for reviewers about when to update content. Use for:

- Pending events: "Flag after 2026 midterm results"
- Court cases: "Revisit when Supreme Court rules on X v. Y"
- Legislation: "Update when bill HR 1234 moves"
- Policy changes: "Flag future immigration executive orders for legal analysis"

Notes are displayed in `/freshness-check` reports to prompt reviewers to check if conditions have been met.

Example:

```yaml
notes:
  - Flag future immigration, climate, or student-debt unilateral moves for legal analysis updates.
  - Revisit presidential immunity jurisprudence when new Supreme Court opinions emerge.
```

### sources.count

**Type:** Integer
**Required:** No (default: 0)

Total number of source citations in the file. Includes:

- URLs
- Academic citations
- Legal citations (case law, statutes)
- Inline source references

### sources.verified

**Type:** Date (YYYY-MM-DD)
**Required:** No

Date when source links were last checked for accessibility. Use `/freshness-check --verify-links` to check and update.

### sources.broken

**Type:** Integer
**Required:** No (default: 0)

Number of known broken links. Zero indicates all links were working as of `sources.verified` date.

## Freshness Status

The `/freshness-check` skill determines status based on `last-reviewed`:

| Status | Criteria | Meaning |
|--------|----------|---------|
| ✓ Fresh | < 6 months old | Recently reviewed, likely current |
| ⚠ Aging | 6-12 months old | Should review soon |
| ✗ Stale | > 12 months old | Needs immediate review |

For `data-year`:

| Status | Criteria | Meaning |
|--------|----------|---------|
| ✓ Current | Same as current year | Data is current |
| ⚠ Aging | 1 year behind | Consider updating |
| ✗ Stale | 2+ years behind | Data likely outdated |

## Which Files Need Frontmatter

**Typically needs frontmatter:**

- `01-overview.md` - Contains key statistics
- `02-current-state.md` - Most time-sensitive; current data and trends
- `08-roadmap.md` - Political landscape, state status, timelines
- `11-legislation.md` - Bill status, pending legislation

**Usually doesn't need frontmatter:**

- `03-history.md` - Historical facts rarely change
- `04-root-causes.md` - Systemic analysis, not time-sensitive
- `05-stakeholders.md` - Generally stable
- `06-opposition.md` - Generally stable
- `07-solutions.md` - Proposed reforms, not data-driven
- `09-resources.md` - Links may need checking, but content stable
- `10-actions.md` - Action items, not data-driven

## Example

Full frontmatter for a current-state file:

```yaml
---
freshness:
  last-reviewed: 2025-01-12
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "Trust and Approval"
      data-year: 2025
    - name: "Electoral Competition"
      data-year: 2025
    - name: "Money in Politics"
      data-year: 2024
    - name: "Voter Participation"
      data-year: 2024
    - name: "Partisan Polarization"
      data-year: 2025
notes:
  - Update after 2026 midterm results are certified.
  - Flag any major Supreme Court election law decisions.
sources:
  count: 15
  verified: 2025-01-12
  broken: 0
---
# Political Reform: Current State

...content...
```

## Updating Frontmatter

**Automatic:** Run `/freshness-check <path> --update` to scan content and generate/update frontmatter.

**Manual:** After reviewing content, update:

1. `last-reviewed` to today's date
2. `data-year` if you added newer data
3. Section years if specific sections were updated
4. `sources.count` if sources changed
5. `notes` - add reminders for future events; remove notes when conditions are met

## Related

- `/freshness-check` - Skill that reads and updates frontmatter
- `/validate-topic` - Checks for frontmatter presence
- `docs/citation-guide.md` - How to format source citations
