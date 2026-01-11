# Cross-Reference Topics

Find and add cross-references between related analysis topics.

## Usage

```
/cross-reference <domain>/<subtopic>
```

Example: `/cross-reference political/campaign-finance`

Or scan all topics: `/cross-reference --all`

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse arguments**:
   - If specific topic provided, focus on that topic
   - If `--all` flag, scan entire `analysis/` directory
   - If no arguments, ask: "Which topic to cross-reference? (or use `--all`)"

2. **Build topic index** by scanning `analysis/` directory:
   - List all topics and subtopics
   - Extract key terms from each `01-overview.md`
   - Note existing cross-references in each topic

3. **For the target topic, identify related topics** by:

   **Keyword matching**:
   - Extract key terms from target topic's files
   - Find topics that mention these terms
   - Weight by frequency and section (title matches > body matches)

   **Domain relationships**:
   - Same domain = likely related
   - Known domain connections (e.g., political ↔ economic, healthcare ↔ social)

   **Explicit references**:
   - Find topics that already reference the target
   - Find topics the target already references

   **Thematic clusters**:
   ```
   Electoral cluster: electoral-reform, redistricting, voting-rights, campaign-finance
   Economic justice cluster: inequality, taxation, wages, labor
   Criminal justice cluster: policing, courts, sentencing, prisons, reentry
   Healthcare cluster: healthcare, mental-health, drugs, aging
   ```

4. **Generate cross-reference report**:

```markdown
## Cross-Reference Analysis: [domain]/[subtopic]

### Existing References

| File | References To | Referenced By |
|------|---------------|---------------|
| 01-overview.md | campaign-finance, lobbying | electoral-reform |
| 07-solutions.md | redistricting | - |
| 11-legislation.md | - | voting-rights |

### Suggested New References

#### High Relevance

| Topic | Relevance | Suggested Location | Reason |
|-------|-----------|-------------------|--------|
| political/lobbying | 95% | 04-root-causes.md | Both address money in politics |
| political/ethics-accountability | 88% | 06-opposition.md | Shared stakeholders |

#### Medium Relevance

| Topic | Relevance | Suggested Location | Reason |
|-------|-----------|-------------------|--------|
| economic/inequality | 72% | 05-stakeholders.md | Economic impacts |
| media/local-journalism | 65% | 07-solutions.md | Transparency solutions |

### Recommended Additions

1. **In 04-root-causes.md**, add:
   ```markdown
   See also [Lobbying: Root Causes](../lobbying/04-root-causes.md) for related analysis of money in politics.
   ```

2. **In 07-solutions.md**, add:
   ```markdown
   Related reforms in [Ethics and Accountability](../ethics-accountability/07-solutions.md) complement these proposals.
   ```

3. **In 11-legislation.md Related Topics section**, add:
   ```markdown
   - [Lobbying: Legislation](../lobbying/11-legislation.md) - Complementary reforms
   - [Ethics and Accountability: Legislation](../ethics-accountability/11-legislation.md) - Enforcement synergies
   ```
```

5. **Ask user to confirm** which references to add:
   - "Add all suggested references?"
   - "Select specific references to add?"
   - "Review and edit suggestions first?"

6. **Apply approved cross-references**:
   - Add inline references at suggested locations
   - Update "Related Topics" sections in legislation files
   - Ensure bidirectional linking where appropriate

7. **For `--all` scan, produce summary**:

```markdown
## Cross-Reference Summary

### Topics with Few Cross-References (< 3)

| Topic | Current | Suggested |
|-------|---------|-----------|
| tribal/sovereignty | 1 | 5 |
| agriculture/food-systems | 2 | 4 |

### Isolated Topics (No References)

- science/research-funding
- disability/accessibility

### Most Connected Topics

| Topic | Outbound | Inbound | Total |
|-------|----------|---------|-------|
| political/electoral-reform | 12 | 18 | 30 |
| economic/inequality | 8 | 15 | 23 |

### Recommended Priority Actions

1. Add references to isolated topics
2. Create bidirectional links for one-way references
3. Connect thematic clusters more tightly
```

8. **Validation**:
   - Verify all referenced files exist
   - Check for broken links
   - Ensure relative paths are correct

9. **Report results**:
   - Number of references added
   - Files modified
   - Any broken links found
   - Suggest running `/validate-topic` to confirm
