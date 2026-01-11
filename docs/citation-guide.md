# Citation Guide

This guide establishes the citation standards for the FixAmerica project to ensure all factual claims are properly sourced and verifiable.

## What Needs Citations

### Always Cite

| Type | Example |
|------|---------|
| Statistics | "72% of Americans support..." |
| Named theories/laws | "Duverger's Law states..." |
| Historical facts with dates | "The Voting Rights Act of 1965..." |
| Quotes | "As Madison wrote..." |
| Study findings | "Research shows that..." |
| Named person's observations | "Maurice Duverger observed..." |
| Specific dollar amounts | "$4 billion in lobbying..." |
| Court decisions | "In Citizens United v. FEC..." |

### May Not Need Citations

| Type | Example |
|------|---------|
| Common knowledge | "The US has two major parties" |
| Definitions | "A primary election is..." |
| Logical deductions | "This creates an incentive to..." |
| General descriptions | "Congress has two chambers" |

## Citation Format

We use **footnotes** for citations. This keeps the main text readable while providing full source information.

### Basic Format

```markdown
The text makes a claim that needs a source.[^1]

[^1]: Author Last, First. "Title." *Publication*, Date. <URL>

```text

**Note**: URLs in footnotes must be wrapped in angle brackets `<URL>` to pass markdown linting.

### Examples by Source Type

**Academic Paper**

```markdown
Plurality voting systems tend toward two-party dominance.[^1]

[^1]: Duverger, Maurice. *Political Parties: Their Organization and Activity in the Modern State*. Wiley, 1954.

```text

**News Article**

```markdown
Local newspapers have declined by 70% since 2005.[^1]

[^1]: Sullivan, Margaret. "The Local News Crisis Is Destroying What aEli Democracy Needs Most." *Washington Post*, June 28, 2022. <https://www.washingtonpost.com/...>

```text

**Government/Organization Report**

```markdown
Campaign spending exceeded $14 billion in 2020.[^1]

[^1]: OpenSecrets. "Cost of Election." 2021. <https://www.opensecrets.org/elections-overview/cost-of-election>

```text

**Court Decision**

```markdown
The Supreme Court ruled that corporate spending on elections is protected speech.[^1]

[^1]: *Citizens United v. Federal Election Commission*, 558 U.S. 310 (2010).

```text

**Research Study**

```markdown
False information spreads six times faster than accurate information.[^1]

[^1]: Vosoughi, Soroush, Deb Roy, and Sinan Aral. "The Spread of True and False News Online." *Science* 359, no. 6380 (2018): 1146-1151. <https://doi.org/10.1126/science.aap9559>

```text

**Website/Organization**

```markdown
FairVote advocates for ranked-choice voting.[^1]

[^1]: FairVote. "Ranked Choice Voting." <https://www.fairvote.org/rcv>

```text

## Footnote Placement

### In Document

Place all footnote definitions at the **end of the document**, before the "Related Topics" and "Document Navigation" sections:

```markdown

## Main Content

Some claim that needs citation.[^1]

Another claim.[^2]

## References

[^1]: First source...
[^2]: Second source...

## Related Topics

- [Link](path)

## Document Navigation

- Previous: [Doc](path)
- Next: [Doc](path)

```text

### Numbering

- Use sequential numbers starting at 1
- Each document has its own numbering (resets per file)
- If a source is used multiple times, use the same footnote number

## Inline Links (Supplementary)

For key people, organizations, or concepts, you may also add inline links:

```markdown
[Maurice Duverger](https://en.wikipedia.org/wiki/Maurice_Duverger) observed that plurality voting systems tend toward two-party dominance.[^1]

[^1]: Duverger, Maurice. *Political Parties*. Wiley, 1954.

```text

## Finding Sources

### Recommended Source Types

| Priority | Source Type |
|----------|-------------|
| 1 | Peer-reviewed academic papers |
| 2 | Government reports and data |
| 3 | Established think tank reports |
| 4 | Major news organizations |
| 5 | Official organization websites |

### Source Databases

- **Academic**: Google Scholar, JSTOR, SSRN
- **Government**: Congress.gov, census.gov, data.gov
- **Legal**: Oyez.org, SCOTUSblog, CourtListener
- **Elections**: OpenSecrets, FEC.gov, Ballotpedia
- **News**: Major outlets (NYT, WaPo, WSJ, AP, Reuters)
- **Think Tanks**: Brookings, Pew, Brennan Center, Cato

## Quality Standards

### Good Citations

- Link directly to primary source when possible
- Include URLs for online sources
- Use archived links (web.archive.org) for potentially unstable URLs
- Prefer recent sources for statistics (within 5 years)

### Avoid

- Wikipedia as a primary source (use it to find primary sources)
- Partisan blogs without primary source verification
- Sources behind hard paywalls without alternatives
- Broken or dead links

## Running the Citation Checker

Use the citation checker script to find claims that may need sources:

```bash
./scripts/find-uncited-claims.sh [directory]

```text

This will identify:

- Statistics without citations
- Named people/theories without sources
- Studies referenced without citations
- Claims using words like "research shows" without sources
