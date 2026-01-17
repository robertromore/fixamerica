---
allowed-tools: Read, Glob, Grep, Edit, WebSearch
---

# Freshness Check

Check if analysis topic content is up-to-date and properly sourced. Works recursively on all topics and subtopics in the `analysis/` folder. Uses YAML frontmatter to enable quick scanning without parsing entire documents.

## Usage

```
/freshness-check <path>              # Quick check (e.g., "political", "political/electoral-reform")
/freshness-check <path> --deep       # Full content scan of all files
/freshness-check <path> --update     # Add/update frontmatter to files that need it
/freshness-check --all               # Check all topics recursively
/freshness-check --stale             # Show only stale topics
/freshness-check --missing           # Show files that need frontmatter but don't have it
```

Example: `/freshness-check political/electoral-reform`

## Frontmatter Schema

Files with time-sensitive content should have this frontmatter:

```yaml
---
freshness:
  last-reviewed: 2025-01-12
  data-year: 2024
  review-cycle: 12
  sections:
    - name: "Trust and Approval"
      data-year: 2025
    - name: "Electoral Competition"
      data-year: 2024
notes:
  - Flag future immigration orders for legal analysis updates.
  - Revisit when Supreme Court issues new ruling on X.
sources:
  count: 12
  verified: 2025-01-12
  broken: 0
---
```

See `docs/templates/frontmatter-schema.md` for full documentation.

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

### 1. Parse Arguments

- If `--all`: scan entire `analysis/` directory recursively
- If `--stale`: filter to show only stale topics
- If `--missing`: filter to show only files without frontmatter
- If `--deep`: run full content scan
- If `--update`: add/update frontmatter after scanning
- Otherwise: scan the specified path under `analysis/`

### 2. Path Resolution

1. If path is a domain (e.g., "political"), check `analysis/political/` and all subtopics
2. If path is a subtopic (e.g., "political/electoral-reform"), check that folder only
3. Recursively find all `.md` files in the target path
4. Skip non-analysis files (like README.md if any exist)

### 3. Quick Mode (default)

For each `.md` file found:

1. Read first 50 lines looking for YAML frontmatter (`---` delimiters)
2. If frontmatter exists with `freshness:` block:
    - Check if `last-reviewed` is older than `review-cycle` months (default: 12)
    - Check if `data-year` is more than 1 year behind current year
    - Check per-section freshness if `sections:` array exists
    - Determine status: Fresh (< 6 months), Aging (6-12 months), Stale (> 12 months)
3. If `notes:` array exists:
    - Collect all notes for display in report
    - These are future reminders (e.g., "Flag when X happens", "Revisit when Y")
4. If no frontmatter: Flag as "needs metadata"
5. Aggregate results by topic/subtopic

### 4. Deep Mode (--deep)

For each `.md` file:

1. Parse entire file for date indicators:
    - Date anchors: `(as of YYYY)`, `(YYYY)`, `YYYY data`, `FY YYYY`
    - Section headers with dates: `### Statistics (as of 2024)`
    - Source citations with years
    - URLs with dates embedded
2. Extract oldest and newest data years per section
3. Count total sources (URLs, citation patterns)
4. Check if Sources section exists and is populated
5. Compare findings against frontmatter (if present)
6. Flag discrepancies between frontmatter claims and actual content

### 5. Update Mode (--update)

1. Run deep scan on each file
2. For files without frontmatter:
    - Generate frontmatter block based on scan results
    - Set `last-reviewed` to today
    - Set `data-year` to newest year found
    - Populate `sections` array with detected sections and their years
    - Count sources
3. For files with existing frontmatter:
    - Update `last-reviewed` to today
    - Update `data-year` if scan found newer data
    - Sync `sections` array with actual content
    - Update source count
4. Prompt: "Update N files with freshness metadata? (y/n)"
5. If confirmed, write frontmatter to each file

### 6. Generate Report

#### For Single Topic

```markdown
## Freshness Report: [domain]/[subtopic]

### Summary

| Metric | Value | Status |
|--------|-------|--------|
| Files scanned | 11 | |
| With frontmatter | 4 | |
| Fresh (< 6 months) | 3 | ✓ |
| Aging (6-12 months) | 1 | ⚠ |
| Stale (> 12 months) | 0 | |
| Missing metadata | 7 | ✗ |

### File Details

| File | Last Reviewed | Data Year | Status |
|------|---------------|-----------|--------|
| 01-overview.md | 2025-01-12 | 2024 | ✓ Fresh |
| 02-current-state.md | 2025-01-12 | 2025 | ✓ Fresh |
| 08-roadmap.md | Never | Unknown | ✗ Missing |
| 11-legislation.md | 2024-06-15 | 2024 | ⚠ Aging |

### Section Freshness (--deep mode only)

| File | Section | Data Year | Status |
|------|---------|-----------|--------|
| 02-current-state.md | Trust and Approval | 2025 | ✓ Current |
| 02-current-state.md | Electoral Competition | 2024 | ⚠ Aging |
| 08-roadmap.md | Virginia Campaign | 2023 | ✗ Stale |

### Notes/Reminders

| File | Note |
|------|------|
| 02-current-state.md | Flag future immigration orders for legal analysis updates. |
| 02-current-state.md | Revisit when Supreme Court issues new ruling on X. |

### Recommendations

1. Run `/freshness-check [path] --update` to add frontmatter to 7 files
2. Refresh "Electoral Competition" section with 2025 data
3. Update Virginia Campaign in 08-roadmap.md
4. Review 2 notes/reminders for potential action
```

#### For --all or Domain-Level

```markdown
## Freshness Report: analysis/

### Summary

| Metric | Count |
|--------|-------|
| Topics scanned | 23 |
| Subtopics scanned | 48 |
| Files scanned | 450 |
| With frontmatter | 45 |
| Fresh | 30 |
| Stale | 15 |
| Missing metadata | 405 |

### By Topic

| Topic | Files | Fresh | Aging | Stale | Missing |
|-------|-------|-------|-------|-------|---------|
| political/ | 11 | 5 | 1 | 0 | 5 |
| political/electoral-reform/ | 11 | 3 | 2 | 0 | 6 |
| political/campaign-finance/ | 11 | 2 | 0 | 1 | 8 |
| economic/ | 11 | 2 | 0 | 0 | 9 |
| healthcare/ | 11 | 0 | 0 | 0 | 11 |
...

### Priority Actions

1. **Critical**: 15 files have stale data (> 12 months old)
2. **High**: 405 files missing freshness metadata
3. **Medium**: 20 files aging (6-12 months)

### Offer

"Search for updated statistics for stale sections? (y/n)"
```

### 7. Auto-Refresh Offer

When stale data is identified:

1. List the specific stale sections with their current data years
2. Ask: "Search for updated statistics for these sections? (y/n)"
3. If yes, for each stale section:
    - Run web search for current data
    - Present findings
    - Offer to update content
    - If updated, refresh frontmatter

### 8. Which Files Need Frontmatter

Files that typically need freshness tracking:

- `01-overview.md` - Key statistics section
- `02-current-state.md` - Most time-sensitive; current data and trends
- `08-roadmap.md` - Political landscape, state status, timelines
- `11-legislation.md` - Bill status, pending legislation

Files that usually don't need freshness tracking:

- `03-history.md` - Historical facts rarely change
- `04-root-causes.md` - Systemic analysis, not time-sensitive
- `05-stakeholders.md` - Generally stable
- `06-opposition.md` - Generally stable
- `07-solutions.md` - Proposed reforms, not data-driven
- `09-resources.md` - Links may need checking, but content stable
- `10-actions.md` - Action items, not data-driven

### 9. Integration Notes

- **validate-topic**: Can check for frontmatter presence, defer details to freshness-check
- **topic-status**: Can show freshness summary alongside completion status
- **llm-review**: Can include freshness check as part of review cycle
