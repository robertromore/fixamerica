# Analyze Perspectives

Generate a political perspectives analysis for a topic, evaluating how nine distinct political viewpoints assess the current state, root causes, solutions, and legislation.

## Usage

```text
/analyze-perspectives <domain>/<subtopic>
/analyze-perspectives political/campaign-finance
/analyze-perspectives political/campaign-finance --perspective Conservative
/analyze-perspectives political/electoral-reform --compromises-only
```

## Instructions

When the user runs this command with arguments `$ARGUMENTS`:

1. **Parse arguments**:
   - Extract `<domain>/<subtopic>` path
   - Check for optional flags:
     - `--perspective <name>`: Analyze only one perspective
     - `--compromises-only`: Skip individual analyses, generate only compromises
   - If no path provided, ask: "Which topic? (e.g., `political/campaign-finance`)"

2. **Verify topic exists** and read reference files:
   - `analysis/<domain>/<subtopic>/02-current-state.md` - Facts to evaluate
   - `analysis/<domain>/<subtopic>/04-root-causes.md` - Causal claims to evaluate
   - `analysis/<domain>/<subtopic>/07-solutions.md` - Solutions to score
   - `analysis/<domain>/<subtopic>/11-legislation.md` - Bills to score
   - Optionally read for context:
     - `05-stakeholders.md` - Actor mapping
     - `06-opposition.md` - Opposition arguments

3. **Extract evaluation targets** from reference files:
   - List all solutions from 07-solutions.md (look for H3 headers under "Proposed Solutions")
   - List all bills from 11-legislation.md (look for H3 headers with "Act" in name)
   - Note key claims from 02-current-state.md and 04-root-causes.md

4. **For each of the 9 perspectives**, roleplay that viewpoint to generate:

   **Perspectives to analyze:**
   - Conservative
   - Liberal
   - Progressive
   - Libertarian
   - Constitutionalist
   - Populist
   - Centrist
   - Religious Right
   - Democratic Socialist

   **For each perspective, generate:**

   a. **Faith Level Assessment (1-5)**:
      - Evaluate stated vs actual motivations
      - Check for principle consistency across contexts
      - Look for goalpost movement patterns
      - Assess zero-sum behavior tendencies
      - Provide justification for the score
      - **Include evidence citations**: Cite specific votes, platform positions, historical shifts, or documented statements supporting the assessment

   b. **Position Scores (1-10)**:
      - Current State Assessment: Do they agree with the facts presented?
      - Root Cause Agreement: Do they agree with the causal analysis?
      - Each Solution: Score 1-10 with stated position and underlying concerns
      - Each Bill: Score 1-10 with stated position and underlying concerns
      - **Include source references**: Cite party platforms, think tank positions, or official statements

   c. **Alternative Proposals**: What would this perspective prefer instead?

   d. **Coalition Potential**: Natural allies, potential bridges, unlikely partners

5. **Generate summary tables**:

   **Legislation Status Reference**: Table showing current status of each bill/amendment being evaluated (Type, Current Status, Last Action)

   **Master Comparison Table**: All perspectives, all dimensions

   **Solution Support Matrix**: Compact grid showing support levels

   **Legislation Support Matrix**: Compact grid showing support levels

   **Faith Level Distribution**: Count by level, list perspectives in each

   **Common Ground Synthesis**: Matrix showing which reforms have broad support (5+), narrow support (3-4), and structural opposition

6. **Generate compromise proposals**:

   For each viable compromise:
   - Identify which perspectives it bridges
   - Find core agreement (shared values or concerns)
   - Describe specific policy
   - Map how it addresses each perspective's concerns
   - List concessions each side makes
   - Assess viability (coalition size, good faith ratio, durability)

   **Compromise identification strategy:**
   - Look for solutions with support from 5+ perspectives
   - Find issues where left-populist and right-populist overlap
   - Identify where Centrist + any two others agree
   - Look for Libertarian + Progressive agreements (civil liberties)
   - Find Conservative + Liberal common ground

7. **Generate strategic implications**:
   - Most viable coalition
   - Key obstacles to agreement
   - How to handle bad faith actors
   - Recommended approach for reform advocates

8. **Write output file** to `analysis/<domain>/<subtopic>/12-perspectives.md`

9. **Report results**:
   - Summary of faith level distribution
   - Highest-support solutions
   - Most viable compromise proposals
   - Note any perspectives with very low faith scores

## Scoring Rubrics

### Position Scores (1-10)

| Score | Meaning | Typical Indicators |
|-------|---------|-------------------|
| 10 | Full agreement | "This analysis is correct" |
| 8-9 | Strong agreement | "Mostly right with minor quibbles" |
| 6-7 | Substantial agreement | "Agree on fundamentals, differ on emphasis" |
| 5 | Mixed | "Some valid points, some disagreements" |
| 3-4 | Substantial disagreement | "Fundamentally misguided approach" |
| 1-2 | Strong opposition | "Completely wrong, would make things worse" |

### Faith Levels (1-5)

| Level | Label | Indicators |
|-------|-------|------------|
| 5 | Full Good Faith | Consistent principles; stated = actual; willing to compromise; acknowledges valid opposing points |
| 4 | Mostly Good Faith | Generally consistent; minor strategic exceptions; engaged in good faith |
| 3 | Mixed Faith | Some genuine + some strategic; selective engagement; sometimes moves goalposts |
| 2 | Mostly Bad Faith | Pretextual objections; goalposts move regularly; selective principles; stated ≠ actual |
| 1 | Full Bad Faith | Pure obstruction; zero-sum warfare; oppose because opponents support; no consistent principles |

### Bad Faith Indicators to Look For

- **Hidden interests**: Donor protection, incumbent protection, partisan advantage disguised as principle
- **Zero-sum mindset**: "If they support it, we oppose it" regardless of policy merits
- **Movable goalposts**: Objections change when concerns are addressed
- **Selective principles**: "States' rights" only when convenient; "free speech" only for allies
- **Pretextual arguments**: Stated concerns not the real reasons for opposition

## Perspective Roleplay Guidelines

When roleplaying each perspective, embody their:

**Conservative**: Skepticism of government solutions, preference for tradition and incremental change, concern about unintended consequences, fiscal restraint, individual responsibility, federalism

**Liberal**: Belief in government as problem-solver, emphasis on equality and fairness, support for regulation and safety nets, progressive on social issues, pragmatic reform

**Progressive**: Focus on systemic/structural change, emphasis on economic justice and worker power, skepticism of corporate influence, support for transformative rather than incremental reform

**Libertarian**: Maximum individual liberty, minimal state intervention, free market solutions, skepticism of both parties' authoritarianism, civil liberties focus

**Constitutionalist**: Original intent interpretation, strict enumerated powers, federalism, skepticism of federal overreach, procedural legitimacy concerns

**Populist**: Anti-elite sentiment, pro-worker economic policy, skepticism of both Wall Street and Washington, economic nationalism, immigration skepticism

**Centrist**: Pragmatism over ideology, preference for bipartisan solutions, incremental progress, evidence-based policy, coalition-building

**Religious Right**: Faith-based values, traditional morality, religious liberty concerns, social conservatism, family values

**Democratic Socialist**: Worker ownership and control, universal public programs, skepticism of capitalism, emphasis on labor rights and public goods

## Example Output Excerpt

```markdown
### Conservative Perspective

#### Faith Level Assessment

**Score: 4/5 - Mostly Good Faith**

| Indicator | Assessment |
|-----------|------------|
| Stated vs actual motivations | Generally consistent; some donor-protection mixed in |
| Principle consistency | Federalism arguments applied consistently |
| Goalpost stability | Stable; same objections over time |
| Zero-sum behavior | Low; willing to engage on specifics |

**Justification:** Most conservative objections reflect genuine philosophical concerns about federal power and market intervention, though some opposition to disclosure requirements appears motivated by donor protection.

#### Position Scores

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Current State Assessment | 6/10 | Agrees money has too much influence but disputes framing of corporate role |
| Root Cause Agreement | 4/10 | Disagrees that money is primary cause; sees regulation as problem |
```

## Handling Edge Cases

- **Topics with no legislation**: Skip legislation evaluation, note in output
- **Topics with many solutions**: Group similar solutions, provide range scores
- **High controversy topics**: Be especially careful about faith assessments; cite specific evidence
- **Perspectives not relevant**: Some perspectives may have no strong position; note as "No strong position (N/A)"
