# Authoritarian Indicators: Overview

## Purpose

This monitoring area tracks actions and statements by political figures that match patterns historically associated with democratic backsliding and authoritarian governance. The methodology draws on comparative politics research documenting how democracies erode.

## Theoretical Foundation

### How Democracies Die

Research by scholars including Steven Levitsky, Daniel Ziblatt, Juan Linz, and the V-Dem Institute has identified common patterns in democratic backsliding:

1. **Gradual erosion**: Modern autocrats rarely seize power through coups; they win elections and then incrementally undermine constraints
2. **Institutional capture**: Key institutions (courts, election administration, law enforcement) are politicized and turned against opponents
3. **Norm violation**: Written rules matter less than unwritten norms; breaking norms without legal consequence enables further violations
4. **Legitimacy attacks**: Opponents are delegitimized as enemies, criminals, or traitors rather than political competitors
5. **Information control**: Independent media is attacked, discredited, or captured

### Warning Signs

Levitsky and Ziblatt identify four key warning signs of authoritarian behavior:

1. **Rejection of democratic rules of the game**
2. **Denial of legitimacy of political opponents**
3. **Toleration or encouragement of violence**
4. **Readiness to curtail civil liberties**

This monitoring framework operationalizes these warning signs into trackable indicators.

## Indicator Categories

### Category A: Electoral Legitimacy

Actions undermining confidence in elections without evidence:

| ID | Indicator | Description |
|----|-----------|-------------|
| A1 | Fraud allegations | Claiming election fraud without credible evidence |
| A2 | Result rejection | Refusing to accept certified election results |
| A3 | Process obstruction | Attempting to prevent vote counting or certification |
| A4 | Elector manipulation | Pressuring officials to alter results |
| A5 | Voter suppression | Actions designed to prevent eligible citizens from voting |

### Category B: Rule of Law

Actions undermining legal constraints and equal justice:

| ID | Indicator | Description |
|----|-----------|-------------|
| B1 | Prosecution threats | Threatening to prosecute political opponents |
| B2 | Investigation interference | Obstructing lawful investigations |
| B3 | Judicial pressure | Attacking judges or attempting to influence cases |
| B4 | Pardon abuse | Using pardon power to shield allies or obstruct justice |
| B5 | Legal immunity claims | Asserting immunity from legal accountability |

### Category C: Institutional Independence

Actions politicizing traditionally non-partisan institutions:

| ID | Indicator | Description |
|----|-----------|-------------|
| C1 | DOJ politicization | Using Justice Department against political opponents |
| C2 | Intelligence politicization | Weaponizing intelligence agencies |
| C3 | Military politicization | Involving military in domestic politics |
| C4 | Civil service purge | Removing officials for political loyalty tests |
| C5 | Inspector general removal | Eliminating oversight officials |

### Category D: Opposition Delegitimization

Rhetoric or actions treating opponents as illegitimate:

| ID | Indicator | Description |
|----|-----------|-------------|
| D1 | Enemy language | Describing opponents as enemies, traitors, or vermin |
| D2 | Dehumanization | Using dehumanizing language about groups |
| D3 | Criminalization rhetoric | Describing lawful opposition as criminal |
| D4 | Loyalty demands | Requiring personal loyalty over institutional duty |
| D5 | Media attacks | Labeling critical press as enemies or fake |

### Category E: Violence and Intimidation

Toleration or encouragement of political violence:

| ID | Indicator | Description |
|----|-----------|-------------|
| E1 | Violence endorsement | Praising or encouraging political violence |
| E2 | Mob incitement | Inciting crowds toward violent action |
| E3 | Intimidation tolerance | Failing to condemn supporter intimidation |
| E4 | Militia association | Associating with paramilitary or militia groups |
| E5 | Official intimidation | Threatening officials who don't comply |

### Category F: Power Concentration

Actions concentrating power in the executive:

| ID | Indicator | Description |
|----|-----------|-------------|
| F1 | Emergency abuse | Misusing emergency powers for routine governance |
| F2 | Congressional bypass | Acting unilaterally where legislation required |
| F3 | Oversight refusal | Refusing to cooperate with congressional oversight |
| F4 | Term limit challenges | Suggesting extension of term limits |
| F5 | Succession interference | Actions to influence or prevent succession |

## Severity Scoring

Each tracked event receives a severity score:

| Score | Level | Criteria | Examples |
|-------|-------|----------|----------|
| 1 | Minor | Rhetoric without action; isolated statement | Single tweet; off-hand comment |
| 2 | Moderate | Repeated rhetoric; formal statement | Campaign speech pattern; official announcement |
| 3 | Serious | Concrete action taken; policy implemented | Executive order; firing official; legal filing |
| 4 | Severe | Significant institutional harm; lasting damage | Mass firings; obstruction of proceeding |
| 5 | Critical | Fundamental threat to democratic function | Violence; refusing transfer of power |

## Event Documentation Format

Each tracked event follows this structure:

```markdown
### [Date]: [Brief Title]

**Category**: [Indicator ID and name]
**Severity**: [1-5]
**Actor(s)**: [Who was involved]

**Description**:
[Factual description of what occurred]

**Sources**:
- [Primary source 1]
- [Primary source 2]

**Context**:
[Relevant background if needed]
```

## Aggregation and Scoring

### Individual Scores

For each tracked figure:

- **Category scores**: Sum of severity scores within each category
- **Total score**: Sum across all categories
- **Trend**: Direction of scores over time (increasing/stable/decreasing)

### Comparative Context

Scores should be interpreted in context:

- Historical comparison to same figure over time
- Comparison to baseline norms in American politics
- Comparison to patterns seen in backsliding democracies internationally

## Tracked Figures

Individual figure tracking is maintained in subdirectories or linked from [Figures](../../figures/00-overview.md):

- Each figure has their own event log
- Events are cross-referenced to this methodology
- Summary scores are periodically updated

## Quality Standards

### Inclusion Criteria

Events are included when they:

- Are publicly documented with credible sources
- Clearly match one or more indicator definitions
- Rise above routine political activity
- Can be described factually without interpretation

### Exclusion Criteria

Events are NOT included when they:

- Are based on anonymous sources alone
- Represent normal political disagreement
- Require significant interpretation to fit indicators
- Cannot be verified through public record

### Corrections

If an entry is found to be inaccurate:

1. The entry is marked with a correction notice
2. The corrected information is added
3. Severity scores are adjusted if warranted
4. A log of corrections is maintained

## Limitations

This methodology has inherent limitations:

- **Selection bias**: Which events get media coverage affects what's tracked
- **Interpretation**: Some events require judgment about indicator fit
- **Severity subjectivity**: Scoring involves some subjective assessment
- **Incomplete record**: Not all relevant events may be publicly known
