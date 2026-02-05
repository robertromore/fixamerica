# Reproducibility: Root Causes

## Overview

The reproducibility crisis is not primarily the result of fraud, incompetence, or any single methodological error. It is the predictable outcome of a system in which institutional incentives, statistical practices, publication norms, and training deficiencies interact to produce unreliable research at scale. Understanding these root causes is essential for designing effective interventions.

## Systemic Cause Map

```text
Publish-or-Perish Culture
    |
    v
Pressure to Produce Novel, Significant Findings
    |
    +---> P-hacking / Analytical Flexibility
    |         |
    |         v
    |     Inflated False Positive Rates
    |
    +---> HARKing / Post Hoc Storytelling
    |         |
    |         v
    |     Confirmatory Appearance of Exploratory Work
    |
    +---> Small Sample Sizes (Cost/Time Pressure)
    |         |
    |         v
    |     Low Statistical Power ---> Winner's Curse
    |
    +---> Selective Reporting of Outcomes
              |
              v
          Publication Bias (Positive Results Published)
              |
              v
          Distorted Literature ---> Failed Replications
```

## Root Cause 1: Perverse Incentive Structures

### The Publish-or-Perish Ecosystem

Academic careers are built on publications. Hiring committees, tenure review boards, and grant panels evaluate researchers primarily on their publication records---the number of papers, the prestige of journals, and the citation counts of their work. This system creates relentless pressure to produce publishable results, which in practice means novel, statistically significant findings.

**How this drives irreproducibility:**

- Researchers are incentivized to find significant results, creating conscious and unconscious bias in data analysis
- Null results and replication studies are professionally unrewarding, so researchers avoid them
- Speed is rewarded over meticulousness; getting to publication first matters more than getting it right
- Quantity of publications is easier to measure than quality, so quantity dominates evaluation

### The Journal Impact Factor

The Journal Impact Factor (JIF), originally designed as a tool for librarians to evaluate journal subscriptions, has become the dominant metric for evaluating individual researchers' work. High-impact-factor journals favor novel, surprising findings, which creates a selection pressure for exactly the kind of results most likely to be false positives (low prior probability, dramatic claims).

**Consequences:**

- Researchers target high-impact journals, which favor surprising results
- Surprising results are, by definition, less likely to be true a priori
- Results that are selected for being surprising will regress toward the mean on replication
- The JIF rewards journals for publishing attention-grabbing findings, not reliable ones

### Funding Pressures

Grant success rates at NIH have declined from approximately 30% in the 1990s to under 20% in recent years. Competition for funding creates pressure to:

- Produce preliminary data that appears promising (even if based on underpowered pilot studies)
- Propose novel hypotheses rather than systematic replications
- Maximize the number of publications from each grant to support future applications
- Avoid reporting null results that might make future funding applications less competitive

## Root Cause 2: Statistical and Methodological Problems

### The P-Value Framework

The dominant statistical framework in science---null hypothesis significance testing (NHST) with a p < 0.05 threshold---is poorly suited to the research environment in which it is applied. Key problems:

- **Arbitrary threshold**: The p < 0.05 threshold has no deep scientific justification. Fisher proposed it as a rough guide, not a decision rule. It corresponds to a 1-in-20 false positive rate under ideal conditions, but actual false positive rates are far higher due to multiple testing, analytical flexibility, and publication bias
- **Misinterpretation**: Researchers and readers routinely misinterpret p-values. A p-value does not indicate the probability that the null hypothesis is true, the probability that the result is a false positive, or the probability that the result will replicate. Yet it is commonly treated as all three
- **Dichotomous thinking**: The significant/non-significant distinction encourages binary thinking about evidence, obscuring the actual strength of evidence and creating a cliff effect at p = 0.05
- **Ignores base rates**: NHST does not incorporate prior probability. A p < 0.05 result testing an implausible hypothesis is far more likely to be a false positive than the same result testing a plausible one, but the framework treats them identically

### P-Hacking and Researcher Degrees of Freedom

Simmons, Nelson, and Simonsohn (2011) demonstrated that ordinary, accepted research practices give researchers enormous flexibility in how they analyze data. These "researcher degrees of freedom" include:

| Practice | Description | Effect on False Positive Rate |
|----------|-------------|-------------------------------|
| Optional stopping | Analyzing data as it comes in and stopping when p < 0.05 | Can double or triple false positive rate |
| Flexible exclusion criteria | Deciding which data points to exclude after seeing results | Can inflate false positive rate to 50%+ |
| Multiple dependent variables | Measuring many outcomes but reporting only significant ones | Each additional DV adds false positive opportunity |
| Flexible covariates | Including or excluding control variables based on results | Can produce significance from null effects |
| Subgroup analysis | Testing for effects in subgroups only when full sample is null | Multiplies false positive opportunities |
| Analytical flexibility | Choosing between multiple valid analytical approaches post hoc | Each choice is a new test |

Simmons et al. showed that combining just a few of these practices could inflate false positive rates from the nominal 5% to over 60%.

### HARKing

Hypothesizing After the Results are Known is particularly insidious because it converts exploratory findings (which require higher evidentiary standards due to multiple testing) into apparently confirmatory ones (which appear to meet the standard p < 0.05 threshold). HARKing is:

- Often unconscious: researchers genuinely believe they predicted findings that emerged from exploration
- Difficult to detect: without pre-registered hypotheses, reviewers cannot distinguish prediction from postdiction
- Encouraged by the narrative structure of scientific papers, which present research as a linear process of hypothesis, test, and confirmation

### Inadequate Statistical Power

Low statistical power is one of the most pervasive and damaging methodological problems in science. Its effects are counterintuitive and poorly understood:

- **Missed true effects**: Underpowered studies frequently fail to detect real effects (high false negative rate)
- **Inflated effect sizes**: When underpowered studies do find significant results, those results necessarily have inflated effect sizes (the "winner's curse"), because only exaggerated effects could reach significance with so few observations
- **Higher false positive rate**: Counterintuitively, the positive predictive value (proportion of significant results that are true positives) is lower when power is low, because the ratio of false positives to true positives increases
- **Unreliable literature**: A literature populated by underpowered studies is a literature populated by a mix of false positives and true positives with inflated effect sizes---neither of which will replicate cleanly

## Root Cause 3: Publication Bias

### The File Drawer Problem

Journals overwhelmingly publish studies with statistically significant results. Non-significant results---the "file drawer"---are less likely to be submitted by authors, less likely to be accepted by editors, and less likely to be cited if published. This creates a systematic distortion of the literature:

- The published record does not represent the full body of evidence on any question
- Effect sizes in the published literature are systematically inflated because only large (often exaggerated) effects reach significance and publication
- Meta-analyses based on published studies overestimate effects because they cannot account for unpublished null results
- Researchers rationally anticipate publication bias and adjust their behavior accordingly (targeting analyses that yield significant results)

### Evidence of Publication Bias

- Fanelli (2010) found that the proportion of published papers reporting positive results has increased over time, from about 70% in 1990 to over 85% by 2007, a trend inconsistent with increasing knowledge but consistent with increasing selection pressure
- In clinical trials, studies with positive results are published at approximately twice the rate of negative studies (Dickersin, 2005)
- Registered clinical trials with positive results are published an average of 2 years faster than those with negative results

### Journal Selection Criteria

High-profile journals explicitly or implicitly favor:

- **Novelty**: New findings over confirmations of existing ones
- **Significance**: Statistically significant results over null findings
- **Large effect sizes**: Dramatic claims over modest ones
- **Broad interest**: General-audience appeal over specialist rigor
- **Clean narratives**: Tidy stories over messy, complex, or ambiguous results

These criteria systematically select for the kinds of findings most likely to be false or exaggerated.

## Root Cause 4: Training and Education Deficits

### Statistical Training

Most scientists receive inadequate statistical training. Graduate programs in psychology, biology, and other fields typically require one or two statistics courses, which focus on procedural application of tests (when to use a t-test vs. an ANOVA) rather than on conceptual understanding of evidence, uncertainty, and inference. Specific deficits include:

- Misunderstanding of p-values and confidence intervals
- Unfamiliarity with statistical power and sample size planning
- Lack of training in Bayesian methods or alternative frameworks
- No exposure to the problems of multiple testing, researcher degrees of freedom, or selective reporting
- Limited training in data management, version control, and computational reproducibility

### Methods Reporting

Researchers are not trained to write methods sections with sufficient detail for replication. A study of the Reproducibility Project: Cancer Biology found that many of the original papers lacked critical methodological details---specific reagent concentrations, equipment settings, environmental conditions---that were necessary for replication. Researchers do not deliberately omit these details; they are simply not trained to identify what information replicators would need.

### Research Design

Many researchers receive limited formal training in research design, particularly regarding:

- The importance of pre-specifying hypotheses and analysis plans
- The distinction between exploratory and confirmatory research
- The consequences of multiple testing and analytical flexibility
- Appropriate sample size determination
- The role of randomization, blinding, and controls

## Root Cause 5: Cultural and Social Factors

### Groupthink and Paradigm Protection

Scientific communities develop shared assumptions and theoretical commitments that can resist disconfirmation. When a finding is consistent with prevailing theory, it is accepted with less scrutiny. When a replication failure challenges a well-established finding, the failure may be attributed to methodological differences rather than to the original finding being wrong.

### Status and Authority

Findings from high-status researchers at prestigious institutions, published in high-impact journals, receive more deference and less critical scrutiny. Replication failures of such work face higher bars for acceptance, and junior researchers may be reluctant to challenge established figures.

### Competition and Secrecy

The competitive nature of academic science discourages data and method sharing. Researchers fear being scooped, losing competitive advantage, or having errors exposed. This secrecy makes independent verification difficult and allows errors to persist undetected.

### Complexity of Modern Research

As research becomes more complex---involving larger datasets, more sophisticated analyses, longer causal chains, and more specialized techniques---the potential for errors increases and the ability of others to evaluate and reproduce the work decreases.

## Interaction Effects

These root causes do not operate independently. They form a reinforcing system:

1. **Incentives drive behavior**: Publish-or-perish pressure leads researchers to use flexible methods and report selectively
2. **Methods enable bias**: Statistical tools like NHST, combined with analytical flexibility, provide the technical means to achieve the significant results that incentives demand
3. **Publication bias filters the literature**: Only significant results survive the publication filter, creating a biased evidence base
4. **Training perpetuates the cycle**: Researchers are trained in the same flawed methods by advisors who succeeded under the same incentive structure
5. **Culture reinforces norms**: The competitive, prestige-oriented culture of science makes reform personally costly for individuals

This systemic character explains why awareness alone has been insufficient to solve the problem. Individual researchers who adopt better practices face professional costs in a system that rewards the old way of doing science.

## References

- Simmons, Joseph P., Leif D. Nelson, and Uri Simonsohn. "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant." *Psychological Science* 22, no. 11 (2011): 1359-1366.
- Ioannidis, John P. A. "Why Most Published Research Findings Are False." *PLOS Medicine* 2, no. 8 (2005): e124.
- Button, Katherine S., et al. "Power Failure: Why Small Sample Size Undermines the Reliability of Neuroscience." *Nature Reviews Neuroscience* 14 (2013): 365-376.
- Fanelli, Daniele. "'Positive' Results Increase Down the Hierarchy of the Sciences." *PLOS ONE* 5, no. 4 (2010): e10068.
- Nosek, Brian A., Jeffrey R. Spies, and Matt Motyl. "Scientific Utopia: II. Restructuring Incentives and Practices to Promote Truth Over Publishability." *Perspectives on Psychological Science* 7, no. 6 (2012): 615-631.
- Smaldino, Paul E., and Richard McElreath. "The Natural Selection of Bad Science." *Royal Society Open Science* 3, no. 9 (2016): 160384.
- Kerr, Norbert L. "HARKing: Hypothesizing After the Results are Known." *Personality and Social Psychology Review* 2, no. 3 (1998): 196-217.

## Document Navigation

- Previous: [History](03-history.md)
- Up: [Science](../01-overview.md)
- Next: [Stakeholders](05-stakeholders.md)
