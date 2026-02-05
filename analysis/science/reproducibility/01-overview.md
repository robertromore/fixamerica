# Reproducibility: Overview

## Executive Summary

The reproducibility crisis represents one of the most significant challenges to the integrity of modern science. Across disciplines ranging from psychology and biomedicine to economics and computer science, systematic attempts to replicate landmark findings have produced alarming failure rates. The Open Science Collaboration's 2015 effort to reproduce 100 psychology studies found that only 36% yielded statistically significant results on replication. In preclinical biomedical research, estimates suggest that 75-90% of findings cannot be reproduced. John Ioannidis's seminal 2005 paper, "Why Most Published Research Findings Are False," provided a mathematical framework demonstrating that the combination of small sample sizes, small effect sizes, researcher flexibility in analysis, and publication bias makes false findings more likely than true ones in many research contexts.

This crisis has profound consequences. Irreproducible research wastes an estimated $28 billion annually in the United States alone, delays medical treatments, undermines public trust in science, and distorts the evidence base that policymakers rely upon. The problem is not primarily one of fraud---though fraud exists---but of systemic incentives that reward novel, positive findings over rigorous, replicable work. Publish-or-perish academic culture, inadequate statistical training, selective reporting of results, and journals' preference for surprising findings all contribute to a research ecosystem that produces unreliable knowledge at scale.

Reform efforts have accelerated since the mid-2010s. Pre-registration of studies, registered reports, open data and code sharing, stricter statistical standards, and institutional changes to reward rigor over novelty are gaining traction. The Center for Open Science (COS), federal funders like NIH and NSF, and major journals have implemented policies promoting transparency and reproducibility. However, progress remains uneven, adoption is inconsistent, and fundamental incentive structures in academia have been slow to change.

## Scope

### What This Topic Covers

- **Replication crisis**: Systematic replication failures across disciplines
- **Statistical rigor**: P-hacking, HARKing, underpowered studies, and statistical reform
- **Methods transparency**: Reporting standards, open methods, and protocol sharing
- **Open science practices**: Pre-registration, registered reports, open data, open code
- **Publication bias**: File-drawer problem, preference for positive results
- **Institutional incentives**: How hiring, promotion, and funding reward novelty over rigor
- **Reproducibility initiatives**: Center for Open Science, SCORE, replication projects
- **Research integrity**: Distinguishing reproducibility problems from misconduct

### What This Topic Does Not Cover

- **Research ethics**: Covered in [Research Ethics](../research-ethics/01-overview.md)
- **Scientific integrity (fraud and misconduct)**: Covered in [Scientific Integrity](../scientific-integrity/01-overview.md)
- **Peer review reform**: Covered in [Peer Review](../peer-review/01-overview.md)
- **Research funding structures**: Covered in [Research Funding](../research-funding/01-overview.md)
- **Open science broadly**: Covered in [Open Science](../open-science/01-overview.md)

## Key Questions

### The Problem

- How widespread are replication failures across scientific disciplines?
- What proportion of published research findings are likely false or exaggerated?
- How much does irreproducible research cost the United States?
- How does the reproducibility crisis affect public trust in science?

### Root Causes

- Why do current incentive structures favor quantity and novelty over rigor?
- How do statistical practices like p-hacking and HARKing inflate false positive rates?
- What role does publication bias play in the prevalence of irreproducible findings?
- Why are sample sizes and statistical power persistently inadequate?

### Solutions

- Can pre-registration and registered reports reduce bias in the literature?
- What statistical reforms would improve the reliability of published findings?
- How should hiring, tenure, and funding criteria change to reward reproducibility?
- What role should federal funders play in mandating transparency and replication?

### Strategy

- Which reforms are gaining traction and which face resistance?
- How do we change academic culture without stifling scientific creativity?
- What can be done at the journal, institution, and funder levels?
- How do international reproducibility efforts inform U.S. policy?

## The Core Problem

### A System That Produces Unreliable Knowledge

The modern scientific enterprise is structured around incentives that systematically favor the production of novel, statistically significant findings. Researchers are rewarded---through publications, grants, jobs, and tenure---for producing exciting results. Null results, replication studies, and methodological improvements receive comparatively little professional reward. This creates predictable consequences: researchers, often unconsciously, make analytical choices that maximize the likelihood of finding significant results.

The statistical tools most commonly used in research---null hypothesis significance testing with a p < 0.05 threshold---are poorly suited to the incentive environment in which they are deployed. When combined with small sample sizes, undisclosed analytical flexibility, and selective reporting, the resulting literature contains a high proportion of false positives and exaggerated effect sizes. The published record does not represent the full body of research conducted; it represents a biased sample filtered through editorial preferences for novelty and significance.

### Scale of the Problem

| Discipline | Replication Rate | Key Study |
|-----------|-----------------|-----------|
| Psychology | 36% of 100 studies replicated | Open Science Collaboration, 2015 |
| Cancer biology | 46% of 53 studies replicated | Errington et al., 2021 |
| Economics | 61% of 18 studies replicated | Camerer et al., 2016 |
| Social sciences (Nature/Science) | 62% of 21 studies replicated | Camerer et al., 2018 |
| Preclinical pharmacology | 11-25% replication rate | Begley & Ellis, 2012; Prinz et al., 2011 |

### Cost of Irreproducibility

Freedman, Cockburn, and Simcoe (2015) estimated that approximately $28 billion per year is spent on preclinical research in the U.S. that cannot be reproduced. This figure accounts for direct research expenditures only and does not include downstream costs: failed clinical trials built on irreproducible preclinical findings, delayed treatments for patients, misallocation of research priorities, and erosion of public trust in science as an institution.

## Document Navigation

- Up: [Science](../01-overview.md)
- Next: [Current State](02-current-state.md)
