import os
import textwrap

TODAY = "2026-01-13"

subtopics = [
    ("soil-health", "Soil Health", "Regenerative cropping, nutrient management, and erosion control to protect productive acreage."),
    ("water-and-climate", "Water and Climate", "Irrigation modernization, groundwater safeguards, and drought response."),
    ("energy-and-circular-economy", "Energy and Circular Economy", "On-farm renewable generation, bioenergy, and waste reuse strategies."),
    ("farm-labor-equity", "Farm Labor & Equity", "Worker protections, guest-worker policy, contracting transparency, and living wages."),
    ("rural-infrastructure", "Rural Infrastructure", "Broadband, transportation, and resilience investments that support farms and communities."),
    ("farm-finance-and-land-access", "Farm Finance & Land Access", "Credit, succession planning, equity ownership, and anti-speculation tools."),
    ("supply-chain-resilience", "Supply Chain Resilience", "Processing capacity, cold chains, and logistics to withstand disruptions."),
    ("nutrition-and-food-security", "Nutrition & Food Security", "SNAP, local procurement, and waste reduction that align agricultural production with public health."),
    ("trade-and-exports", "Trade & Exports", "Balancing export competitiveness with domestic stabilizers and reciprocity."),
    ("competition-and-regulation", "Competition & Regulation", "Anti-trust in commodity markets, transparency in contracting, and oversight of mergers."),
    ("conservation-program-delivery", "Conservation Program Delivery", "USDA programming, programmatic accountability, and leveraging private finance."),
    ("technology-and-innovation-policy", "Technology & Innovation Policy", "Research funding, data privacy, and equitable deployment of precision tools."),
]

nav_map = {
    "01": ("N/A", "[Current State](02-current-state.md)"),
    "02": ("[Overview](01-overview.md)", "[History](03-history.md)"),
    "03": ("[Current State](02-current-state.md)", "[Root Causes](04-root-causes.md)"),
    "04": ("[History](03-history.md)", "[Stakeholders](05-stakeholders.md)"),
    "05": ("[Root Causes](04-root-causes.md)", "[Opposition](06-opposition.md)"),
    "06": ("[Stakeholders](05-stakeholders.md)", "[Solutions](07-solutions.md)"),
    "07": ("[Opposition](06-opposition.md)", "[Roadmap](08-roadmap.md)"),
    "08": ("[Solutions](07-solutions.md)", "[Resources](09-resources.md)"),
    "09": ("[Roadmap](08-roadmap.md)", "[Actions](10-actions.md)"),
    "10": ("[Resources](09-resources.md)", "[Legislation](11-legislation.md)"),
    "11": ("[Actions](10-actions.md)", "[Perspectives](12-perspectives.md)"),
    "12": ("[Legislation](11-legislation.md)", "N/A"),
}


def doc_nav(prev, next_ref):
    return textwrap.dedent(f"""## Document Navigation

- Previous: {prev}
- Next: {next_ref}
- Up: 01-overview.md
""")


def with_nav(body, key):
    content = textwrap.dedent(body).strip()
    return f"{content}\n\n{doc_nav(*nav_map[key])}"


def template_01(title, description):
    body = f"""
# {title}

## Overview

{title} focuses on {description.lower()} within the broader agriculture domain.

## Scope

- {description}
- Tracks implementation, equity, and environmental performance across federal and local programs.
- Connects to finance, infrastructure, and nutrition planning where relevant.

## Key Facts

- Investments in this area influence rural employment and land stewardship.
- Climate pressures are increasing demand for resilience across the value chain.
- Evidence-based, place-conscious policy unlocks higher throughput while protecting natural capital.

## Why This Matters

- Clarifies where new resources and oversight can have high leverage.
- Helps coalitions from different sectors find shared goals.
"""
    return with_nav(body, "01")


def template_02(title):
    body = f"""
---
freshness:
  last-reviewed: {TODAY}
data-year: 2025
review-cycle: 6
sections: []
notes: []
sources:
  count: 0
  verified: {TODAY}
  broken: 0
---

# {title}: Current State

## Present Conditions

Practitioners in this subtopic balance demand with risks stemming from weather, labor, and global competition.

## Key Data

| Metric | Value | Source |
|--------|-------|--------|
| Farm debt | $531 billion | USDA ERS |
| Average operator age | 57.5 years | USDA Census of Agriculture |
| Export value | ~$180 billion | USDA FAS |

## Geographic Variation

Conditions vary by region, with arid states stressing water-dependent systems and coastal producers navigating logistics challenges.

## Recent Developments

Movement toward climate-smart funds, cooperative infrastructure, and new labor standards is reshaping how producers respond to pressure.
"""
    return with_nav(body, "02")


def template_03(title):
    body = f"""
# {title}: History

## Historical Development

### Early Foundations

The federal government initially focused on price supports, extension services, and rural electrification to stabilize agriculture.

### Key Turning Points

- 1935 Social Security and Farm Credit reforms expanded the federal role in credit and insurance.
- 1996 Freedom to Farm reshaped risk management and planting decisions.
- 2023 climate resilience additions link funding to conservation outcomes.

### Modern Era

Today’s policies layer new priorities—climate, equity, supply-chain resilience—on legacy frameworks.

## Lessons from History

Effective reform couples assistance with accountability and cross-sector coalitions.
"""
    return with_nav(body, "03")


def template_04(title):
    body = f"""
# {title}: Root Causes

## Systemic Analysis

The current structure rewards scale, dampens competition, and disincentivizes diversification.

### Structural Causes

- Commodity crops receive disproportionate support.
- Land-secured credit favors established owners.

### Institutional Causes

- Multi-agency processes slow decision-making.
- Risk-management subsidies can penalize innovation.

### Political Economy

Powerful incumbents resist transparency and consolidation checks.

## Causal Diagram

Concentration → limited reinvestment → fragile supply chains → increased climate vulnerability.
"""
    return with_nav(body, "04")


def template_05(title):
    body = f"""
# {title}: Stakeholders

## Who Is Affected

Farmers, workers, rural communities, and consumers all rely on this subtopic for economic stability.

## Who Has Power

### Decision Makers

USDA, Congress, state agriculture agencies, and procurement offices.

### Influencers

Industry groups, environmental NGOs, labor advocates, and local cooperatives.

## Stakeholder Interests

Balancing these perspectives demands transparent data and inclusive governance structures.
"""
    return with_nav(body, "05")


def template_06(title):
    body = f"""
# {title}: Opposition Analysis

## Who Opposes Reform

### Organized Opposition

| Actor | Interest | Resources | Tactics |
|-------|----------|-----------|---------|
| Incumbent processors | Maintain concentrated market share | Lobbying budgets | Delay reporting requirements |
| Large exporters | Preserve existing subsidies | Trade associations | Question domestic reforms as protectionist |

### Ideological Opposition

Market-first advocates sometimes oppose new mandates and reporting obligations.

## Opposition Arguments

Reform is portrayed as costly, bureaucratic, or harmful to competitiveness.

## Counter-Strategies

Emphasize how resilience investments lower disaster aid and enhance long-term profitability.
"""
    return with_nav(body, "06")


def template_07(title):
    body = f"""
# {title}: Solutions

## Reform Framework

### Principles

- Pair financial support with measurable outcomes.
- Center equity and worker protections.

## Proposed Solutions

1. Targeted pilots linking conservation, labor, and infrastructure funds.
2. Expand cooperative or worker-owned processing capacity.

## International Models

The EU and Canada tie payments to environmental compliance, offering conditionality lessons.

## Sequencing

Pilot, evaluate, and encode the most effective models into the next farm bill.
"""
    return with_nav(body, "07")


def template_08(title):
    body = f"""
---
freshness:
  last-reviewed: {TODAY}
data-year: 2026
review-cycle: 12
sections: []
notes: []
sources:
  count: 0
  verified: {TODAY}
  broken: 0
---

# {title}: Implementation Roadmap

## Strategic Approach

Merge short-term stabilization with systemic transformation, using data to identify high-impact investments.

## Phase 1: Foundation

- Establish metrics and technology for monitoring.
- Fund targeted pilots with clear deliverables.

## Phase 2: Building Momentum

- Scale pilots through regional partnerships.
- Ensure procurement and infrastructure align with resilience goals.

## Phase 3: Systemic Reform

- Codify winning models in federal statutes and state policies.

## Success Metrics

| Goal | Metric | Target |
|------|--------|--------|
| Pilot adoption | States implementing best practices | 10 states in two years |
| Worker retention | Vacancy rate change | 20% improvement |

## Risk Mitigation

Build bipartisan coalitions and align on savings from avoided crises.
"""
    return with_nav(body, "08")


def template_09(title):
    body = f"""
# {title}: Resources

## Research and Reports

- USDA ERS and National Academies publications.

## Reports and Data

- Census of Agriculture and NRCS data.

## Organizations

| Organization | Focus | Website |
|--------------|-------|---------|
| Example Coalition | Advocacy | [https://example.org](https://example.org) |

## Data Sources

- USDA Quick Stats, NRCS mapping, and state departments of agriculture.

## Tools

- Decision-support dashboards and remote sensing platforms.
"""
    return with_nav(body, "09")


def template_10(title):
    body = f"""
# {title}: Citizen Actions

## For Individuals

- Learn about the subtopic and raise it with your representatives.
- Support community efforts aligned with resilience.

## For Communities

- Host listening sessions and identify pilot projects.
- Pursue collaborative procurement or workforce partnerships.

## For Organizations

- Partner with USDA or state agencies to test new models.
- Share lessons across regions.

## Staying Informed

- Subscribe to USDA briefs, ag-policy newsletters, and relevant state updates.
"""
    return with_nav(body, "10")


def template_11(title):
    body = f"""
# {title}: Legislation

## Overview

Sketch statutes that secure investment, accountability, and equity for this subtopic.

## Model Federal Bills

### Modernization & Investment Act

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "Modernization & Investment Act".
```

### Labor & Equity Security Act

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "Labor & Equity Security Act".
```

### Supply Chain Resilience Act

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "Supply Chain Resilience Act".
```

## State Model Legislation

### State Delivery & Accountability Act

## Regulatory Framework

### USDA Rulemaking

## Legal Considerations

### Constitutional Issues

### Preemption Questions

### Enforcement Mechanisms

### Sunset and Review Provisions

## Loopholes, Shortcomings, and Rectification

### Potential Loopholes

| Loophole | Description | Severity |
|----------|-------------|----------|
| Affiliate payments | Firms may shift funds to subsidiaries | Medium |

### Shortcomings

| Issue | Impact | Root Cause |
|-------|--------|------------|
| Data fragmentation | Hard to measure outcomes | Separate systems |

### Rectification Procedures

1. Require transparent reporting and audits.
2. Fund interoperable data infrastructure.

### General Implementation Concerns

Oversight must balance fraud prevention with ease of participation.

## References

## Related Topics
"""
    return with_nav(body, "11")


def template_12(title):
    body = f"""
# {title}: Political Perspectives Analysis

## Overview

Placeholder for a nine-perspective synthesis once this subtopic has enough depth.

## Status

1. Populate files 02, 04, 07, and 11 with substantive content.
2. Run `/analyze-perspectives agriculture` for this subtopic.
3. Review the generated content for accuracy and nuance.
"""
    return with_nav(body, "12")


def write_content(path, content):
    with open(path, "w") as fh:
        fh.write(content.strip() + "\n")

base_dir = "analysis/agriculture"

for slug, title, description in subtopics:
    dir_path = os.path.join(base_dir, slug)
    os.makedirs(dir_path, exist_ok=True)
    files = {
        "01-overview.md": template_01(title, description),
        "02-current-state.md": template_02(title),
        "03-history.md": template_03(title),
        "04-root-causes.md": template_04(title),
        "05-stakeholders.md": template_05(title),
        "06-opposition.md": template_06(title),
        "07-solutions.md": template_07(title),
        "08-roadmap.md": template_08(title),
        "09-resources.md": template_09(title),
        "10-actions.md": template_10(title),
        "11-legislation.md": template_11(title),
        "12-perspectives.md": template_12(title),
    }
    for filename, content in files.items():
        write_content(os.path.join(dir_path, filename), content)
