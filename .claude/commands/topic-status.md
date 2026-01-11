# Topic Status

Check completeness and quality of an analysis topic.

## Usage

```
/topic-status <domain>/<subtopic>
```

Example: `/topic-status political/electoral-reform`

Or run without arguments to check all topics: `/topic-status`

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse arguments**:
   - If specific path provided, check that topic only
   - If no arguments, scan all topics in `analysis/` directory

2. **For each topic, check file existence**:

   Expected files:
   - `01-overview.md`
   - `02-current-state.md`
   - `03-history.md`
   - `04-root-causes.md`
   - `05-stakeholders.md`
   - `06-opposition.md`
   - `07-solutions.md`
   - `08-roadmap.md`
   - `09-resources.md`
   - `10-actions.md`
   - `11-legislation.md`

3. **For each existing file, gather metrics**:
   - Word count
   - Whether it contains only template/placeholder text
   - Number of citations (look for patterns like `*Author*, Year` or URLs)
   - Number of cross-references to other topics

4. **For 11-legislation.md specifically, check required sections**:
   - [ ] Overview
   - [ ] Constitutional Amendments (or explicit "not needed")
   - [ ] Federal Legislation
   - [ ] State Model Legislation
   - [ ] Regulatory Framework
   - [ ] Legal Considerations
   - [ ] Loopholes, Shortcomings, and Rectification
     - [ ] Potential Loopholes table
     - [ ] Shortcomings table
     - [ ] Rectification Procedures
   - [ ] References
   - [ ] Related Topics
   - [ ] Document Navigation

5. **Generate status report**:

```markdown
## Topic Status: [domain]/[subtopic]

### File Completeness

| File | Status | Words | Citations | Notes |
|------|--------|-------|-----------|-------|
| 01-overview.md | ✓ Complete | 450 | 3 | |
| 02-current-state.md | ⚠ Template | 120 | 0 | Needs content |
| 03-history.md | ✗ Missing | - | - | |
...

### Legislation File Analysis

| Section | Status |
|---------|--------|
| Overview | ✓ |
| Loopholes Analysis | ✗ Missing |
...

### Summary

- **Completion**: 7/11 files (64%)
- **Content depth**: 3/7 files have substantial content
- **Citations needed**: 4 files have zero citations
- **Legislation gaps**: Missing loopholes analysis

### Recommendations

1. Create missing file: 03-history.md
2. Add content to template files: 02-current-state.md
3. Add loopholes analysis to 11-legislation.md
4. Add citations to: 04-root-causes.md, 05-stakeholders.md
```

6. **For all-topics scan**, produce summary table:

```markdown
## All Topics Status

| Domain | Subtopic | Files | Complete | Legislation |
|--------|----------|-------|----------|-------------|
| political | electoral-reform | 11/11 | 9/11 | ✓ Full |
| political | campaign-finance | 8/11 | 6/11 | ⚠ No loopholes |
| economic | taxation | 5/11 | 3/11 | ✗ Missing |
...

### Priority Actions

1. **Critical**: 3 topics missing legislation files
2. **High**: 7 topics missing loopholes analysis
3. **Medium**: 12 topics need more citations
```

7. **Offer follow-up actions**:
   - "Run `/scaffold-topic` to create missing files"
   - "Run `/add-legislation` to create legislation file"
   - "Run `/validate-topic` for detailed formatting check"
