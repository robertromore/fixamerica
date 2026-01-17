---
allowed-tools: Read, Glob, Grep, Edit, WebSearch
---

# Citation Check

Audit and normalize date references and source citations in analysis files. Ensures every data point notes its snapshot date and cites a specific source.

## Usage

```
/citation-check <path>                # Audit a topic (e.g., "political/electoral-college")
/citation-check <path> --fix          # Fix issues interactively
/citation-check <path> --update       # Search for newer sources and update
/citation-check --all                 # Audit all topics
```

Example: `/citation-check political/electoral-college --fix`

## Purpose

This skill complements `/freshness-check`:

| Skill | Purpose |
|-------|---------|
| `/freshness-check` | Detect stale content, track review status via frontmatter |
| `/citation-check` | Normalize date formats, add missing citations, update stale sources |

Typical workflow:
1. `/freshness-check` to find stale sections
2. `/citation-check --fix` to normalize and update
3. `/freshness-check --update` to refresh frontmatter

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

### 1. Parse Arguments

- If `--all`: scan entire `analysis/` directory recursively
- If `--fix`: interactively fix issues found
- If `--update`: search for newer sources and offer to update content
- Otherwise: audit the specified path under `analysis/`

### 2. Scan for Issues

For each `.md` file, check for these issue types:

#### A. Undated Headings with Time-Sensitive Content

**Flag** section headers that contain statistics or current data but lack date context:

```markdown
# BAD - no date context
### Key Statistics
### Current Position

# GOOD - date context present
### Key Statistics (2024 snapshot)
### Current Position (latest public update: Dec. 2024)
```

**Detection patterns:**
- Headers containing: "Statistics", "Current", "Status", "Position", "Recent"
- Headers followed by tables with numbers
- Headers in files: `01-overview.md`, `02-current-state.md`, `08-roadmap.md`

#### B. Undated Data Points

**Flag** specific numbers/claims without year context:

```markdown
# BAD - no year
| Trust in government | 17% |
- 209 electoral votes secured

# GOOD - year context
| Trust in government | 17% (2025) |
- 209 electoral votes secured (Dec. 2024)
```

**Detection patterns:**
- Percentages without years: `\d+%` not followed by `(20\d\d)`
- Electoral/vote counts without dates
- "X states have..." without year
- Dollar amounts without cycle/year

#### C. Missing Source Citations

**Flag** tables or statistics without inline or nearby source citations:

```markdown
# BAD - no source
| Metric | Value |
| Trust | 17% |

# GOOD - source present
| Metric | Value |
| Trust | 17% |

*Source: Pew Research Center, Dec. 2025.*
```

**Detection patterns:**
- Tables not followed by `*Source:` or `*Sources:` within 3 lines
- Statistical claims not followed by citation
- Look for orphan data (numbers without attribution)

#### D. Vague Source References

**Flag** sources that lack specific dates or retrieval info:

```markdown
# BAD - vague
*Source: Pew Research Center*
*Source: National Popular Vote Inc.*

# GOOD - specific
*Source: Pew Research Center, Dec. 2025.*
*Source: National Popular Vote Inc., status update dated Dec. 2024.*
```

#### E. Inconsistent Date Formats

**Flag** mixed date formats and normalize to standard:

```markdown
# Inconsistent
(as of 2024)
(2024 data)
(current as of December 2024)

# Standard formats
(2024 snapshot)           # For data from a specific year
(Dec. 2024)               # For specific month
(latest update: Dec. 2024) # For status/position data
```

### 3. Generate Audit Report

```markdown
## Citation Audit: [path]

### Summary

| Issue Type | Count | Severity |
|------------|-------|----------|
| Undated headings | 5 | High |
| Undated data points | 12 | High |
| Missing sources | 8 | High |
| Vague sources | 4 | Medium |
| Inconsistent date formats | 6 | Low |
| **Total** | **35** | |

### Issues by File

#### 02-current-state.md

| Line | Issue | Current | Suggested |
|------|-------|---------|-----------|
| 45 | Undated heading | `### Key Statistics` | `### Key Statistics (2024 snapshot)` |
| 52 | Undated data | `17%` | `17% (2025)` |
| 60 | Missing source | Table without citation | Add `*Source: ...*` |

#### 08-roadmap.md

| Line | Issue | Current | Suggested |
|------|-------|---------|-----------|
| 34 | Vague source | `National Popular Vote Inc.` | `National Popular Vote Inc., Dec. 2024` |
| 46 | Undated heading | `### Current Position` | `### Current Position (Dec. 2024)` |

### Recommended Actions

1. Add date context to 5 section headings
2. Add year markers to 12 data points
3. Add source citations after 8 tables
4. Specify dates for 4 vague sources
5. Normalize 6 date formats to standard
```

### 4. Fix Mode (--fix)

For each issue found, prompt:

```
Issue: Undated heading at line 45
Current:  ### Key Statistics
Suggested: ### Key Statistics (2024 snapshot)

[A]ccept / [E]dit / [S]kip / [Q]uit?
```

- **Accept**: Apply the suggested fix
- **Edit**: Let user modify the suggestion
- **Skip**: Move to next issue
- **Quit**: Stop fixing, show summary of changes made

After all fixes:
1. Show summary of changes
2. Offer to update frontmatter via `/freshness-check --update`

### 5. Update Mode (--update)

For data points identified as potentially stale:

1. Show the current value and its source date
2. Offer to search for updated data:
   ```
   Found: "209 electoral votes" (Dec. 2024)
   Search for updated NPV status? [Y/n]
   ```
3. If yes, run web search for current data
4. Present findings and offer to update:
   ```
   Current NPV status (Jan. 2025):
   - Still 209 EVs (17 states + DC)
   - No new states since Maine (2024)

   Update content? [Y/n]
   ```
5. If updated, also update the source citation with new date

### 6. Standard Date Formats

Use these formats consistently:

| Context | Format | Example |
|---------|--------|---------|
| Annual data | `(YYYY snapshot)` | `(2024 snapshot)` |
| Specific month | `(Mon. YYYY)` | `(Dec. 2024)` |
| Status/position | `(latest update: Mon. YYYY)` | `(latest update: Dec. 2024)` |
| Fiscal year | `(FY YYYY)` | `(FY 2024)` |
| Range | `(YYYY-YYYY)` | `(2020-2024)` |

### 7. Source Citation Formats

Standard inline source format:

```markdown
*Source: [Organization], [Date/Report].*
*Sources: [Org1], [Date]; [Org2], [Date].*
```

Examples:
```markdown
*Source: Pew Research Center, Dec. 2025.*
*Source: National Popular Vote Inc., status update dated Dec. 2024.*
*Sources: OpenSecrets, 2024 cycle data; FEC reports.*
*Source: U.S. Census Bureau, 2024 Presidential Election Tables (released Jan. 2025).*
```

### 8. Integration with Other Skills

- **After `/citation-check --fix`**: Suggest running `/freshness-check --update` to sync frontmatter
- **Before `/freshness-check --deep`**: `/citation-check` can pre-normalize dates for better detection
- **With `/validate-topic`**: Citation issues can be included in validation warnings

### 9. Priority Order for Fixes

1. **High priority**: Missing sources (credibility issue)
2. **High priority**: Undated headings (reader confusion)
3. **Medium priority**: Undated data points (verification difficulty)
4. **Medium priority**: Vague sources (hard to verify)
5. **Low priority**: Inconsistent formats (style issue)
