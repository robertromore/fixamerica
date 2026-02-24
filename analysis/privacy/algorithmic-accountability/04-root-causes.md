# Algorithmic Accountability: Root Causes

## Overview

The lack of algorithmic accountability in the United States is not a simple regulatory oversight. It reflects deep structural forces in technology development, corporate governance, legal doctrine, and political economy. Understanding these root causes is essential for designing reforms that address the problem at its source rather than merely treating symptoms.

## Structural Root Causes

### 1. Misalignment of Commercial Incentives

The business model of algorithmic decision-making rewards speed, scale, and cost reduction -- not fairness, accuracy, or transparency.

| Incentive | Effect on Accountability |
|-----------|------------------------|
| **Cost reduction** | Algorithms deployed to replace human judgment precisely because humans are more expensive; accountability measures add cost |
| **Speed to market** | Competitive pressure favors rapid deployment over thorough testing; bias audits slow product launch |
| **Scale** | Value increases with adoption; pausing deployment for fairness testing means lost market share |
| **Optimization for metrics** | Systems optimized for narrow metrics (click-through rate, cost savings) at the expense of fairness or accuracy |
| **Network effects** | First movers in algorithmic markets build data advantages that entrench their systems regardless of quality |

Companies have little financial incentive to discover that their algorithms are biased or inaccurate. Discovery creates liability; ignorance provides plausible deniability. This structural incentive explains why most algorithmic bias is found by external researchers rather than internal teams.

### 2. Regulatory Architecture Mismatch

Existing regulatory frameworks were designed for a pre-algorithmic world and map poorly onto automated decision-making.

| Regulatory Framework | Design Assumption | Algorithmic Reality |
|---------------------|-------------------|---------------------|
| **Civil rights law** | Discriminatory intent or identifiable discriminator | Algorithms produce discriminatory outcomes without intent; no single human decision-maker |
| **Consumer protection** | Informed consumers making choices | Consumers do not know algorithms are being used or how they work |
| **Administrative law** | Government decisions made through due process | Algorithms replace deliberation with computation |
| **Tort law** | Identifiable wrongdoer causing foreseeable harm | Algorithmic harms are diffuse, emergent, and involve multiple actors |
| **Contract law** | Negotiated terms between parties | Terms of service are non-negotiable and rarely read; algorithmic decisions embedded in adhesion contracts |

The sectoral approach to US regulation (different laws for credit, health, employment, housing) creates coverage gaps. Algorithmic systems that operate across sectors or that do not fit neatly into any existing category face no regulatory requirements at all.

### 3. Information Asymmetry and Opacity

A fundamental power imbalance exists between those who build and deploy algorithmic systems and those affected by them.

| Dimension | Developer/Deployer | Affected Individual |
|-----------|-------------------|---------------------|
| **Technical knowledge** | Full understanding of system design and data inputs | No knowledge of how system works |
| **Data access** | Complete access to training data and model outputs | No access to data used in decision |
| **Legal resources** | Corporate legal teams; trade secret protections | Burden of proof on individual to demonstrate harm |
| **Detection capability** | Can identify patterns across millions of decisions | Sees only their individual outcome |
| **Remediation power** | Can modify system if motivated | No mechanism to compel changes |

This asymmetry is reinforced by trade secret law. Companies routinely claim algorithmic methods and training data as trade secrets, preventing regulators, researchers, and affected individuals from evaluating system performance. Courts have generally upheld these claims, even when algorithmic systems make consequential decisions about liberty, livelihood, and welfare.

### 4. Legal Doctrine Gaps

Several specific legal doctrines create barriers to algorithmic accountability.

**Third-Party Doctrine**: The Supreme Court's third-party doctrine (though narrowed by *Carpenter v. United States*, 2018) allows data collected by private companies to flow into algorithmic systems with fewer constitutional protections than direct government collection.

**Disparate Impact Burden of Proof**: Under current anti-discrimination law, plaintiffs must prove disparate impact statistically. Without access to algorithmic details, training data, or system outputs, this burden is functionally impossible to meet.

**Section 230 Immunity**: While primarily about content moderation, Section 230's broad immunity has been invoked to shield algorithmic recommendation systems from liability for their outputs.

**Arbitration and Class Action Waivers**: Terms of service for most platforms include mandatory arbitration and class action waivers, preventing collective challenges to algorithmic harms.

**Standing Requirements**: Courts require plaintiffs to demonstrate concrete, particularized injury. Algorithmic harms are often diffuse (everyone of a certain race scored differently) rather than individually traceable.

### 5. Political Economy of Tech Regulation

The political dynamics surrounding technology regulation create structural barriers to accountability.

| Factor | Effect |
|--------|--------|
| **Industry lobbying** | Technology industry spent $70+ billion on lobbying 2019-2024 (OpenSecrets); algorithmic accountability bills consistently weakened or blocked |
| **Revolving door** | Regulators move to industry; industry executives move to regulatory positions; shared assumptions and relationships |
| **Campaign contributions** | Tech industry major donor to both parties; creates reluctance to regulate |
| **Knowledge asymmetry** | Legislators lack technical expertise to evaluate algorithmic systems; reliance on industry for information |
| **Innovation narrative** | Industry frames all regulation as anti-innovation; policymakers fear being seen as hostile to technology |
| **Fragmented advocacy** | Civil rights, consumer, labor, and privacy groups pursue separate agendas rather than unified algorithmic accountability |
| **Bipartisan dysfunction** | Left and right oppose algorithms for different reasons (discrimination vs. censorship) and struggle to find common ground |

### 6. Data Infrastructure Lock-In

The data infrastructure underlying algorithmic systems creates path dependencies that resist reform.

- **Historical data encodes historical discrimination**: Algorithms trained on historical data inevitably learn patterns of racial, gender, and economic discrimination. Correcting this requires either not using historical data (reducing accuracy) or actively adjusting for bias (which companies resist as "reverse discrimination")
- **Data collection is structurally biased**: Marginalized communities are simultaneously over-surveilled (more police data, more child welfare data) and under-represented (less healthcare data, less financial data), producing algorithms that over-police and under-serve
- **Feedback loops compound bias**: Algorithmic outputs become future inputs. Predictive policing sends more police to minority neighborhoods, which generates more arrest data, which the algorithm interprets as higher crime, which sends more police
- **Infrastructure costs create switching barriers**: Organizations that have invested millions in algorithmic systems resist reforms that would require fundamental redesign

### 7. Abdication of Government Responsibility

Government agencies have been among the most aggressive adopters of algorithmic systems while being among the least accountable.

| Government Failure | Examples |
|-------------------|----------|
| **Adopting commercial systems without validation** | States purchasing criminal risk tools without independent testing; agencies adopting hiring algorithms from vendors without bias audits |
| **Outsourcing accountability** | Contracting algorithmic decisions to private vendors, then claiming vendor systems are proprietary and beyond public scrutiny |
| **Insufficient procurement standards** | No federal procurement requirements for algorithmic fairness, accuracy, or transparency prior to OMB M-24-10 (2024) |
| **Defunding oversight** | Regulatory agencies chronically underfunded relative to the industries they oversee; FTC has ~1,100 employees for entire US economy |
| **Executive order fragility** | AI governance policies established by executive order (EO 14110) can be rescinded by next administration |

### 8. Cultural and Ideological Factors

Broader cultural assumptions about technology contribute to the accountability gap.

- **Techno-solutionism**: Widespread belief that algorithms are objective, neutral, and superior to human judgment, despite extensive evidence of bias
- **Efficiency as paramount value**: Cultural emphasis on efficiency and cost reduction provides ideological cover for replacing accountable human judgment with unaccountable algorithmic systems
- **Individualism**: American emphasis on individual responsibility obscures systemic algorithmic harms; if an algorithm denied your loan, the cultural response is "improve your credit" rather than "fix the algorithm"
- **Free market ideology**: Belief that market forces will discipline bad algorithms; in practice, affected individuals lack information to make market-based choices

## Interaction of Root Causes

These root causes reinforce each other in a self-perpetuating cycle:

1. Commercial incentives drive rapid deployment without accountability
2. Regulatory gaps provide no legal requirement for accountability
3. Information asymmetry prevents affected individuals from detecting problems
4. Political economy blocks legislative reform
5. Cultural assumptions provide ideological justification for the status quo
6. Government adoption normalizes unaccountable algorithmic systems
7. Data infrastructure lock-in makes reform increasingly costly over time

Breaking this cycle requires interventions at multiple points simultaneously -- mandatory transparency, updated legal frameworks, empowered enforcement agencies, and cultural shifts in how society views algorithmic power.

## Sources

- Barocas, Solon, and Andrew Selbst. "Big Data's Disparate Impact." *California Law Review* 104 (2016): 671-732
- Benjamin, Ruha. *Race After Technology* (2019)
- Eubanks, Virginia. *Automating Inequality* (2018)
- Noble, Safiya. *Algorithms of Oppression* (2018)
- O'Neil, Cathy. *Weapons of Math Destruction* (2016)
- OpenSecrets, Technology Sector Lobbying Data (2019-2024)
- Pasquale, Frank. *The Black Box Society* (2015)
- Selbst, Andrew, et al. "Fairness and Abstraction in Sociotechnical Systems." *Conference on Fairness, Accountability, and Transparency* (2019)

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
