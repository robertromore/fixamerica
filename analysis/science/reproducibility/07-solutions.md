# Reproducibility: Solutions

## Overview

Addressing the reproducibility crisis requires interventions at multiple levels: changing how individual researchers conduct and report studies, how journals select and publish findings, how funders allocate resources and set requirements, and how institutions evaluate and reward scientists. The most promising reforms align individual incentives with system-level goals, making it professionally advantageous to do rigorous, transparent, reproducible work.

## Solution Category 1: Pre-Registration and Registered Reports

### Pre-Registration of Studies

**What it is**: Before collecting data, researchers publicly register their hypotheses, methods, and analysis plan on a platform like the Open Science Framework (OSF), AsPredicted, or ClinicalTrials.gov. The time-stamped registration creates a verifiable record of what was planned before results were known.

**How it helps**:

- Eliminates HARKing by creating a clear record of a priori predictions
- Reduces p-hacking by constraining analytical flexibility to pre-specified analyses
- Distinguishes confirmatory from exploratory analyses, allowing both but requiring transparency about which is which
- Creates accountability without eliminating flexibility (exploratory analyses can still be reported, labeled as such)

**Evidence of effectiveness**:

- Kaplan and Irvin (2015) found that clinical trials registered before data collection were far less likely to report significant results than unregistered trials (8% vs. 57%), suggesting that pre-registration dramatically reduces the inflation of positive findings
- Pre-registered studies in psychology show smaller average effect sizes than non-pre-registered studies, consistent with reduced bias
- Over 130,000 studies have been pre-registered on OSF as of 2025

**Limitations**:

- Pre-registration is most appropriate for confirmatory research; purely exploratory work does not lend itself to pre-specification
- Vague or overly broad pre-registrations can preserve analytical flexibility, defeating the purpose
- Compliance monitoring is limited; it is unclear how often pre-registered plans are followed

**Implementation status**: Widely adopted in psychology, growing in biomedicine and economics. Required by some journals and recommended by major funders.

### Registered Reports

**What it is**: A publication format in which Stage 1 peer review evaluates the research question, hypotheses, and methodology *before* data collection. If the study design is accepted, the journal commits to publishing the final paper regardless of whether results are statistically significant. Stage 2 peer review evaluates only whether the study was conducted as planned and the conclusions are supported.

**How it helps**:

- Eliminates publication bias entirely for registered reports, because publication is guaranteed regardless of results
- Removes the incentive to p-hack, HARk, or selectively report, because the outcome does not affect publication
- Improves study design by incorporating peer review input before data collection, when design changes are still possible
- Provides professional reward (a guaranteed publication) for rigorous work, regardless of results

**Evidence of effectiveness**:

- Scheel et al. (2021) found that only 4% of registered reports reported null results compared to 96% of standard reports in the same journals, a dramatic shift consistent with the elimination of publication bias
- Registered reports have higher statistical power than comparable standard reports
- Over 350 journals now offer the registered reports format

**Limitations**:

- Not appropriate for all research types (purely exploratory work, secondary data analysis, some observational studies)
- Slower publication timeline due to two rounds of peer review
- Limited adoption in some fields (e.g., bench sciences where experiments are rapid and iterative)
- Requires editorial infrastructure and reviewer commitment

**Implementation status**: Rapidly growing. Championed by COS, adopted by journals across disciplines including *Nature Human Behaviour*, *Cortex*, *BMC Biology*, and *Royal Society Open Science*.

## Solution Category 2: Statistical Reform

### Redefining or Abandoning Significance Thresholds

**Options**:

- **Lower the threshold**: Benjamin et al. (2018) proposed p < 0.005 as the threshold for "significant" findings, with p < 0.05 redefined as "suggestive." This would reduce false positive rates by approximately 60%
- **Abandon thresholds entirely**: The American Statistical Association (2019) recommended moving away from dichotomous significance testing toward continuous measures of evidence
- **Report effect sizes and confidence intervals**: Emphasize the magnitude and uncertainty of effects rather than their statistical significance
- **Adopt Bayesian methods**: Use Bayes factors or posterior probabilities, which directly address the probability that a hypothesis is true given the data

**How these help**:

- Reduce the rate of false positives in the published literature
- Encourage researchers to focus on the strength and precision of evidence rather than on crossing a threshold
- Make it harder to achieve "significance" through analytical manipulation
- Provide more informative summaries of research findings

**Evidence of effectiveness**:

- Fields that have adopted stricter thresholds (particle physics uses 5-sigma, equivalent to p < 0.0000003) have far lower false positive rates
- Studies using Bayesian methods tend to produce more conservative, replicable conclusions
- Reporting effect sizes and confidence intervals provides more decision-relevant information than p-values alone

**Implementation status**: Highly debated. No consensus has emerged on a single replacement for the current system, which has slowed adoption. Many journals now require reporting of effect sizes and confidence intervals alongside p-values.

### Mandatory Power Analysis

**What it is**: Require researchers to conduct and report a priori power analyses demonstrating that their study has adequate statistical power (typically 80% or higher) to detect effects of the expected size.

**How it helps**:

- Ensures that studies are large enough to detect the effects they are investigating
- Reduces the "winner's curse" (inflated effect sizes in underpowered studies that reach significance)
- Makes the expected effect size explicit, forcing researchers to justify their expectations
- Discourages underpowered studies that waste resources

**Implementation status**: Required by some funders (e.g., NIH for clinical trials) and journals, but compliance is inconsistent and many power analyses use unrealistically large expected effect sizes.

## Solution Category 3: Transparency and Open Science

### Open Data

**What it is**: Researchers share the data underlying their published findings in publicly accessible repositories, allowing others to verify analyses, conduct alternative analyses, and reuse data for new research.

**How it helps**:

- Enables computational reproducibility: independent researchers can verify that reported analyses produce reported results
- Detects errors, including both honest mistakes and data fabrication
- Increases the value of publicly funded research by allowing data reuse
- Creates accountability for analytical choices

**Challenges**:

- Privacy concerns for human subjects data require careful de-identification or restricted-access arrangements
- Large datasets may require specialized infrastructure for storage and access
- Data without adequate documentation (metadata, codebooks) is difficult to reuse
- Concerns about free-riding on others' data collection efforts

**Implementation status**: Mandated by NIH (since January 2023), required by PLOS and many other journals, enabled by repositories such as Dryad, Figshare, Zenodo, and the Harvard Dataverse.

### Open Code and Methods

**What it is**: Researchers share the analysis code, scripts, and computational environment used to produce their results, along with sufficiently detailed methods descriptions.

**How it helps**:

- Enables exact computational reproduction of results
- Reveals analytical choices that are not described in methods sections
- Allows detection of coding errors, which are common in complex analyses
- Facilitates method reuse and adaptation

**Implementation status**: Growing. GitHub and GitLab are widely used for code sharing. Platforms like Code Ocean and Binder enable executable environments. However, code sharing remains far less common than data sharing, and shared code is often poorly documented.

### Reporting Guidelines and Checklists

**What it is**: Standardized checklists specifying the minimum information that must be reported in a published study. Examples include CONSORT (randomized trials), STROBE (observational studies), PRISMA (systematic reviews), and the Nature reporting checklists.

**How it helps**:

- Ensures that methods sections contain sufficient detail for evaluation and replication
- Standardizes reporting across studies, facilitating meta-analysis
- Makes omissions and deviations from protocol visible

**Implementation status**: Over 400 reporting guidelines are listed on the EQUATOR Network. Compliance is variable; many journals require checklists but do not enforce them rigorously.

## Solution Category 4: Institutional and Incentive Reform

### Reforming Hiring, Tenure, and Promotion

**What it is**: Changing the criteria by which researchers are evaluated to reward rigor, transparency, and reproducibility rather than publication count, journal prestige, and citation metrics.

**Specific proposals**:

- Evaluate candidates on the rigor and transparency of their work, not the volume
- Credit pre-registration, data sharing, code sharing, and replication studies in hiring and tenure decisions
- Adopt DORA principles: evaluate individual articles on their own merit, not on the basis of journal impact factor
- Include reproducibility and open science practices in annual reviews and promotion criteria

**How it helps**: Directly addresses the root cause of the crisis by aligning individual career incentives with system-level goals.

**Implementation status**: DORA has been signed by over 3,000 institutions, but actual changes in hiring and tenure criteria have been slow. Some departments (e.g., psychology departments at the Universities of Munich, Bristol, and others) have explicitly included open science criteria in hiring. The Netherlands has pioneered the Recognition and Rewards initiative, which de-emphasizes metrics in favor of broader evaluation of research quality, societal impact, and team science.

### Funding for Replication

**What it is**: Dedicated funding streams for replication studies, either through new programs or through requirements that a proportion of grant funding be allocated to replication.

**Specific proposals**:

- Create dedicated replication funding programs at NIH and NSF
- Require that a percentage (e.g., 5-10%) of research budgets in each program be allocated to replication of key findings
- Fund replication centers or consortia that systematically replicate influential findings in specific fields
- Count successful replications and well-conducted failed replications as positive outcomes in grant reporting

**How it helps**: Creates a professional pathway for replication work, ensures that influential findings are verified, and generates a more accurate understanding of effect sizes.

**Implementation status**: Limited. Some small-scale replication funding exists (e.g., the Institute for Replication, DARPA SCORE), but no major funder has created a large-scale replication program.

### Badges and Recognition Systems

**What it is**: Visual badges attached to published articles indicating compliance with open science practices---open data, open materials, pre-registration.

**How it helps**:

- Provides visible recognition for good practices
- Creates social pressure for adoption
- Allows readers to quickly assess the transparency of a study

**Evidence of effectiveness**: Kidwell et al. (2016) found that the journal *Psychological Science* saw a dramatic increase in data sharing (from less than 3% to over 39% of articles) after introducing open science badges.

**Implementation status**: Widely adopted by psychology journals, growing in other fields.

## Solution Category 5: Technology and Infrastructure

### Open Science Framework (OSF)

**What it is**: A free, open-source platform developed by COS that provides pre-registration, data sharing, code sharing, project management, and collaboration tools for researchers.

**How it helps**: Reduces the practical barriers to adopting open science practices by providing a single, free, user-friendly platform.

**Implementation status**: Over 800,000 users, widely adopted across disciplines.

### Automated Reproducibility Checking

**What it is**: Software tools that automatically check whether reported analyses can be reproduced from shared data and code, flag statistical errors in manuscripts (e.g., statcheck), or assess the quality of reporting.

**Examples**:

- **statcheck**: Automatically detects inconsistencies in reported statistical results in psychology papers
- **Code Ocean**: Provides executable computational environments for verifying results
- **ReproZip**: Packages computational environments for sharing and reproduction

**Implementation status**: Growing but not yet standard. statcheck has screened tens of thousands of published papers and found error rates of 10-50% depending on the journal.

## Solution Comparison Matrix

| Solution | Effectiveness | Feasibility | Cost | Adoption Level |
|----------|--------------|-------------|------|---------------|
| Pre-registration | High (reduces HARKing, p-hacking) | High (free platforms exist) | Low | Moderate and growing |
| Registered reports | Very high (eliminates publication bias) | Moderate (requires journal adoption) | Low | Moderate and growing |
| Lower significance threshold | Moderate (reduces false positives) | Moderate (controversial) | Low | Low (debated) |
| Open data | High (enables verification) | Moderate (privacy, infrastructure) | Moderate | Growing (mandated by NIH) |
| Open code | High (enables reproduction) | High (platforms exist) | Low | Low-moderate |
| Reporting guidelines | Moderate (improves methods descriptions) | High (widely available) | Low | Moderate (variable enforcement) |
| Tenure/hiring reform | Very high (addresses root cause) | Low (institutional resistance) | Low | Very low |
| Replication funding | High (creates verification infrastructure) | Moderate (requires political will) | Moderate | Very low |
| Badges | Moderate (social incentive) | High (easy to implement) | Very low | Moderate |

## References

- Nosek, Brian A., Charles R. Ebersole, Alexander C. DeHaven, and David T. Mellor. "The Preregistration Revolution." *Proceedings of the National Academy of Sciences* 115, no. 11 (2018): 2600-2606.
- Scheel, Anne M., et al. "An Excess of Positive Results: Comparing the Standard Psychology Literature with Registered Reports." *Advances in Methods and Practices in Psychological Science* 4, no. 2 (2021): 1-12.
- Benjamin, Daniel J., et al. "Redefine Statistical Significance." *Nature Human Behaviour* 2 (2018): 6-10.
- Kidwell, Mallory C., et al. "Badges to Acknowledge Open Practices: A Simple, Low-Cost, Effective Method for Increasing Transparency." *PLOS Biology* 14, no. 5 (2016): e1002456.
- Kaplan, Robert M., and Veronica L. Irvin. "Likelihood of Null Effects of Large NHLBI Clinical Trials Has Increased over Time." *PLOS ONE* 10, no. 8 (2015): e0132382.
- Wasserstein, Ronald L., Allen L. Schirm, and Nicole A. Lazar. "Moving to a World Beyond 'p < 0.05.'" *The American Statistician* 73, sup1 (2019): 1-19.
- Nosek, Brian A., et al. "Promoting an Open Research Culture." *Science* 348, no. 6242 (2015): 1422-1425.

## Document Navigation

- Previous: [Opposition](06-opposition.md)
- Up: [Science](../01-overview.md)
- Next: [Roadmap](08-roadmap.md)
