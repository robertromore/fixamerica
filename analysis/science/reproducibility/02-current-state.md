# Reproducibility: Current State

## Overview

As of 2026, the reproducibility crisis remains a central concern in science policy. Awareness has increased substantially since the early 2010s, and numerous reforms have been implemented at the journal, funder, and institutional levels. However, the fundamental incentive structures of academic science---publish-or-perish culture, reliance on citation metrics, and inadequate reward for replication---have proven resistant to change. Progress has been real but uneven, with some disciplines advancing rapidly while others lag.

## Replication Rates by Discipline

### Psychology

Psychology has been at the forefront of the reproducibility conversation since the Open Science Collaboration's landmark 2015 project, which attempted to replicate 100 studies published in three leading psychology journals. Only 36% produced statistically significant results consistent with the original, and the mean effect size of replications was roughly half that of the originals.

Subsequent large-scale efforts have reinforced these findings:

- **Many Labs 2** (2018): Tested 28 classic findings across 125 samples in 36 countries. Only 14 of 28 (50%) replicated.
- **Many Labs 5** (2020): Found that close replications of studies from the pipeline of a single journal produced mixed results, with effect sizes consistently smaller than originals.
- **Registered Replication Reports**: The Association for Psychological Science's program has produced several high-profile non-replications, including ego depletion and social priming effects.

Psychology has also led in adopting reforms: pre-registration rates have risen sharply, and several major journals now accept registered reports.

### Biomedicine

The biomedical replication crisis is arguably the most consequential, given direct implications for drug development and patient care.

- **Begley and Ellis (2012)**: Scientists at Amgen attempted to reproduce 53 landmark oncology and hematology studies. Only 6 (11%) could be confirmed.
- **Prinz, Schlange, and Asadullah (2011)**: Bayer scientists reported that only about 25% of published preclinical studies could be validated.
- **Reproducibility Project: Cancer Biology** (2021): The Center for Open Science's systematic effort found that of 53 high-profile cancer biology experiments from 23 papers, 46% of effects replicated. Many experiments could not be completed due to insufficient methodological detail in original publications.

The NIH addressed these concerns through its 2014 training modules on rigor and reproducibility, updated grant application requirements emphasizing authentication of key biological and chemical resources, and the 2023 Data Management and Sharing Policy.

### Economics

Economics has shown somewhat higher replication rates:

- **Camerer et al. (2016)**: Replicated 11 of 18 (61%) experimental economics studies from top journals.
- **Camerer et al. (2018)**: Replicated 13 of 21 (62%) social science experiments published in *Nature* and *Science*.
- **Institute for Replication**: Founded in 2022, has conducted systematic replications of influential policy-relevant economics papers, finding replication rates of roughly 60-70%.

However, observational economics research faces distinct reproducibility challenges: results are sensitive to model specification choices, sample selection, and time periods analyzed, making replication in the strict sense more difficult.

### Computer Science and Machine Learning

Reproducibility in computational fields presents unique challenges. A 2019 survey by Gundersen and Kjensmo found that only 24% of AI conference papers shared code and only 30% shared data. Key issues include:

- Dependence on specific hardware configurations (especially GPUs)
- Sensitivity to hyperparameter tuning and random seeds
- Inadequate documentation of computational environments
- Proprietary datasets and models

NeurIPS introduced a reproducibility checklist in 2019, and the ML Reproducibility Challenge has operated annually since 2018.

## Current Statistical Practices

### Prevalence of P-Hacking

P-hacking---the practice of manipulating data analysis to achieve statistical significance---remains widespread despite increased awareness. A 2019 analysis by Head et al. found evidence of p-hacking across the biomedical literature, with a suspicious clustering of p-values just below 0.05. Specific practices include:

- Collecting data until a significant result is obtained
- Selectively reporting dependent variables or conditions
- Excluding outliers post hoc to achieve significance
- Running multiple statistical tests and reporting only significant ones
- Rounding p-values down (e.g., reporting p = 0.054 as p < 0.05)

### HARKing

Hypothesizing After the Results are Known (HARKing) is the practice of presenting post hoc findings as though they were predicted a priori. Kerr (1998) documented this practice, which inflates the apparent confirmatory value of research. Surveys suggest that 40-60% of researchers have engaged in some form of HARKing, often without recognizing it as problematic.

### Underpowered Studies

Statistical power---the probability of detecting a true effect---remains persistently low in many fields. Button et al. (2013) found the median statistical power of studies in neuroscience was 21%, meaning the majority of studies were unable to reliably detect the effects they were investigating even if those effects were real. Low power increases both false negative and false positive rates (because only inflated effects reach significance in underpowered studies), contributing to the "winner's curse" in published literature.

## Institutional Landscape

### Federal Funders

**National Institutes of Health (NIH)**:

- Implemented rigor and reproducibility requirements for grant applications (2016)
- Issued the Data Management and Sharing Policy (effective January 2023), requiring data sharing plans for all NIH-funded research
- Funded the NIGMS MIDAS program for reproducible computational science
- Supported the Rigor and Transparency Index for evaluating institutional practices

**National Science Foundation (NSF)**:

- Requires data management plans for all proposals
- Supports the Center for Open Science and other reproducibility infrastructure
- Funds the Directorate for Technology, Innovation and Partnerships with open science mandates
- Supports training grants emphasizing rigor and reproducibility

**OSTP**:

- The 2022 Nelson Memo directed federal agencies to ensure that publications and data from federally funded research are freely available to the public by 2025
- The 2025 OSTP Year of Open Science initiatives promoted reproducibility practices across agencies

### Major Journals

| Journal/Publisher | Reproducibility Policies |
|-------------------|-------------------------|
| *Nature* portfolio | Reporting checklists, data availability statements, code availability requirements |
| *Science* | Data and code sharing requirements, enhanced methods reporting |
| PLOS | Open data mandate, pre-registration badges |
| Elsevier | Registered Reports offered at select journals, data sharing encouraged |
| APA journals | Pre-registration encouraged, open science badges |
| *eLife* | Publish-then-review model (2022), emphasis on rigor over novelty |

### Center for Open Science (COS)

The COS, founded by Brian Nosek in 2013, remains the leading organization promoting reproducibility reforms. Key initiatives:

- **Open Science Framework (OSF)**: Free platform for pre-registration, data sharing, and project management; over 800,000 users as of 2025
- **Registered Reports**: COS has promoted adoption at over 350 journals
- **TOP Guidelines**: Transparency and Openness Promotion guidelines adopted by over 5,000 journals
- **SCORE Project**: Systematic assessment of the credibility of research claims
- **Badges**: Open Data, Open Materials, and Pre-registration badges for published articles

## Key Metrics

| Indicator | Current Value | Trend |
|-----------|--------------|-------|
| Studies pre-registered on OSF | 130,000+ (cumulative through 2025) | Increasing |
| Journals accepting Registered Reports | 350+ | Increasing |
| Journals adopting TOP Guidelines (any level) | 5,000+ | Increasing |
| NIH-funded studies with data sharing plans | Required for all (since Jan 2023) | Stable (mandated) |
| Estimated annual cost of irreproducible preclinical research | $28 billion | Uncertain |
| Proportion of researchers who have pre-registered a study | ~25-30% (varies by field) | Increasing |
| Replication studies as % of published literature | ~1-3% | Slowly increasing |

## Current Debates

### Statistical Reform

The most contentious current debate concerns the appropriate threshold for statistical significance. Benjamin et al. (2018) proposed redefining statistical significance from p < 0.05 to p < 0.005, arguing this would reduce false positive rates by approximately 60%. Critics, including Lakens et al. (2018), argued this would increase false negative rates, disadvantage small labs, and fail to address the underlying problem of dichotomous thinking about evidence.

An alternative movement advocates abandoning the significance threshold entirely in favor of reporting effect sizes, confidence intervals, and Bayesian analyses. The American Statistical Association's 2019 editorial, "Moving to a World Beyond 'p < 0.05,'" endorsed this direction but stopped short of mandating specific alternatives.

### Incentive Alignment

Despite widespread recognition that academic incentives drive the reproducibility crisis, progress in restructuring those incentives has been slow. Most hiring and tenure committees still prioritize publication counts, journal impact factors, and grant totals. The Declaration on Research Assessment (DORA), which calls for abandoning journal-based metrics in hiring, has been signed by over 3,000 institutions but implementation varies widely.

### Replication as a Research Activity

Replication studies remain difficult to fund, publish, and receive professional credit for. While some journals now welcome replications, researchers who dedicate significant effort to replication work risk career disadvantage compared to peers producing novel findings. The Institute for Replication and other organizations have attempted to create professional pathways for replication work, but these remain marginal.

## References

- Open Science Collaboration. "Estimating the Reproducibility of Psychological Science." *Science* 349, no. 6251 (2015): aac4716.
- Begley, C. Glenn, and Lee M. Ellis. "Raise Standards for Preclinical Cancer Research." *Nature* 483, no. 7391 (2012): 531-533.
- Ioannidis, John P. A. "Why Most Published Research Findings Are False." *PLOS Medicine* 2, no. 8 (2005): e124.
- Freedman, Leonard P., Iain M. Cockburn, and Timothy S. Simcoe. "The Economics of Reproducibility in Preclinical Research." *PLOS Biology* 13, no. 6 (2015): e1002165.
- Benjamin, Daniel J., et al. "Redefine Statistical Significance." *Nature Human Behaviour* 2 (2018): 6-10.
- Wasserstein, Ronald L., Allen L. Schirm, and Nicole A. Lazar. "Moving to a World Beyond 'p < 0.05.'" *The American Statistician* 73, sup1 (2019): 1-19.
- Camerer, Colin F., et al. "Evaluating the Replicability of Social Science Experiments in Nature and Science between 2010 and 2015." *Nature Human Behaviour* 2 (2018): 637-644.
- National Institutes of Health. "Final NIH Policy for Data Management and Sharing." *Federal Register* (2020).

## Document Navigation

- Previous: [Overview](01-overview.md)
- Up: [Science](../01-overview.md)
- Next: [History](03-history.md)
