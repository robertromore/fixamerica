# Monitoring: Overview

## Purpose

While the `analysis/` directory examines systemic problems, root causes, and proposed solutions, the `monitoring/` directory tracks **ongoing events and developments** that indicate democratic health or deterioration. This is the project's early warning system and accountability record.

Monitoring serves several functions:

1. **Documentation**: Creating a factual record of events relevant to democratic governance
2. **Pattern Recognition**: Identifying trends that may not be visible in individual incidents
3. **Accountability**: Tracking whether political figures and institutions act consistently with democratic norms
4. **Early Warning**: Flagging developments that match historical patterns of democratic backsliding

## How Monitoring Differs from Analysis

| Aspect | Analysis | Monitoring |
|--------|----------|------------|
| Time focus | Historical and structural | Current and ongoing |
| Content | Problems, causes, solutions | Events, indicators, scores |
| Update frequency | Periodic | Continuous as events occur |
| Format | Narrative essays | Structured data and incident logs |
| Goal | Understanding | Tracking and alerting |

## Core Principles

### Objectivity and Evidence

All monitored events must be:

- **Verifiable**: Based on public statements, actions, court filings, official documents, or credible reporting
- **Sourced**: Every entry must cite primary sources where possible
- **Factual**: Describe what happened, not interpretations or predictions
- **Contextual**: Include relevant context without editorializing

### Consistent Methodology

Each monitoring area defines:

- **Indicator categories**: What types of events are tracked
- **Scoring criteria**: How severity or significance is assessed
- **Update procedures**: When and how the record is updated
- **Review processes**: How entries are verified and corrected

### Non-Partisan Application

Monitoring criteria apply equally regardless of party affiliation. The same standards used to evaluate one political figure must apply to all others. Methodology should be defined before application to avoid motivated reasoning.

## Directory Structure

```
monitoring/
├── 00-overview.md              # This file
├── democratic-health/          # Broad indicators of democratic functioning
│   ├── 00-overview.md
│   ├── institutional-trust/    # Public confidence in institutions
│   ├── electoral-integrity/    # Election administration quality
│   ├── press-freedom/          # Media independence indicators
│   └── civic-participation/    # Engagement and participation metrics
├── threat-tracking/            # Specific threats to democracy
│   ├── 00-overview.md
│   ├── authoritarian-indicators/   # Actions matching authoritarian patterns
│   ├── democratic-backsliding/     # Systemic backsliding indicators + DBS
│   ├── corruption-indicators/      # Ethics violations and self-dealing
│   ├── institutional-decay/        # Erosion of norms and guardrails
│   └── rights-violations/          # Civil liberties and rights concerns
└── figures/                    # Individual actor profiles
    └── 00-overview.md
```

## Relationship to Analysis

Monitoring areas should link to relevant analysis topics:

| Monitoring Area | Related Analysis |
|-----------------|------------------|
| Democratic health | [Political Reform](../analysis/political/01-overview.md) |
| Authoritarian indicators | [Executive Reform](../analysis/political/executive-reform/01-overview.md) |
| Corruption | [Ethics and Accountability](../analysis/political/ethics-accountability/01-overview.md) |
| Institutional decay | [Government Transparency](../analysis/political/government-transparency/01-overview.md) |
| Rights violations | [Justice](../analysis/justice/01-overview.md), [Voting Rights](../analysis/political/voting-rights/01-overview.md) |

## Getting Started

Each monitoring subdirectory should contain:

1. **00-overview.md**: Purpose, scope, and methodology for that area
2. **Indicator definitions**: What events qualify for tracking
3. **Scoring rubrics**: How to assess severity or significance
4. **Event logs**: Chronological record of tracked events
5. **Summaries**: Periodic assessments of patterns and trends

## Subdirectories

- [Democratic Health](democratic-health/00-overview.md): Positive indicators of democratic functioning
- [Threat Tracking](threat-tracking/00-overview.md): Threats and warning signs
- [Democratic Backsliding](threat-tracking/democratic-backsliding/00-overview.md): Systemic backsliding indicators and DBS runs
- [Figures](figures/00-overview.md): Individual actor profiles and tracking
