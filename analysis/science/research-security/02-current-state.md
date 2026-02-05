# Research Security: Current State

## Overview

As of early 2026, U.S. research security policy exists in a post-China Initiative, post-NSPM-33 implementation landscape marked by ongoing tension between security imperatives and scientific openness. Federal agencies have largely finalized their disclosure requirements, universities have built compliance infrastructure, and enforcement has shifted from criminal prosecution of researchers toward institutional accountability. However, the chilling effects of the 2018-2022 enforcement period persist, international researcher recruitment has suffered measurable declines, and the fundamental policy questions remain unresolved.

## The Threat Landscape

### Documented Foreign Research Exploitation

Foreign governments exploit U.S. research through multiple vectors:

| Vector | Description | Scale |
|--------|-------------|-------|
| Talent recruitment programs | Government-sponsored programs offering funding, lab space, and positions to overseas researchers | China alone operates 200+ such programs; Thousand Talents Plan recruited 7,000+ researchers globally |
| Undisclosed foreign affiliations | Researchers maintaining unreported positions, funding, or lab relationships abroad | NIH identified 500+ scientists with undisclosed foreign ties (2018-2022) |
| Shadow laboratories | Foreign-funded labs duplicating U.S.-funded research without disclosure | Dozens of documented cases, primarily involving Chinese institutions |
| Cyber espionage | State-sponsored hacking of research networks and data theft | FBI reports thousands of active investigations involving Chinese IP theft |
| Graduate student and postdoc exploitation | Using academic positions to access proprietary research | Difficult to quantify; most student researchers are legitimate |
| Conference and collaboration exploitation | Using legitimate scientific exchanges to acquire unpublished findings | Widespread but largely anecdotal evidence |

### Countries of Primary Concern

| Country | Primary Methods | Key Programs | Estimated Annual IP Theft |
|---------|----------------|--------------|--------------------------|
| China (PRC) | Talent programs, cyber, students, joint ventures | Thousand Talents, Changjiang Scholars, 111 Project | $200-600 billion across all sectors (FBI estimate) |
| Russia | Cyber espionage, traditional intelligence | SVR operations targeting national labs | Classified; significant in defense-adjacent research |
| Iran | Student recruitment, sanctions evasion | IRGC-linked academic programs | Moderate; focused on nuclear, defense, aerospace |
| North Korea | Cyber theft, front organizations | Lazarus Group targeting research institutions | Growing; focused on weapons and sanctions evasion |

*Note: The $200-600 billion figure encompasses all U.S. IP theft by China, not just academic research. The academic research component is a subset that is difficult to isolate.*

### Scale of the Problem

Quantifying research security threats is inherently difficult, as successful espionage is by definition covert. Available data points include:

- **NIH investigations**: Between 2018 and 2024, NIH referred approximately 220 cases to the HHS Office of Inspector General. Of scientists investigated, roughly 80% had failed to disclose foreign funding, and approximately 90% had connections to Chinese institutions. More than 100 scientists left their positions.
- **NSF referrals**: NSF's Office of Inspector General opened 150+ cases related to undisclosed foreign funding between 2019 and 2024.
- **DOE counterintelligence**: The Department of Energy manages counterintelligence programs at 17 national laboratories, with classified threat assessments indicating persistent targeting.
- **FBI assessments**: The FBI maintains approximately 2,000 active investigations related to Chinese government-directed IP theft across all sectors, with a significant subset involving university research.

### What Gets Targeted

Not all research faces equal risk. The most targeted areas include:

| Research Area | Risk Level | Why Targeted |
|---------------|-----------|--------------|
| Artificial intelligence and machine learning | Critical | Direct military and economic applications |
| Quantum computing and information science | Critical | Potential to break encryption, sensing applications |
| Semiconductors and microelectronics | Critical | Supply chain dominance, defense applications |
| Biotechnology and genomics | High | Public health, agriculture, bioweapons potential |
| Hypersonics and advanced materials | High | Military applications, missile technology |
| Autonomous systems and robotics | High | Military and industrial automation |
| Energy storage and advanced batteries | High | Economic competitiveness, military logistics |
| Space technology | Moderate-High | Dual-use satellite and launch capabilities |
| Basic biomedical research | Moderate | Long-term pharmaceutical and health applications |
| Agricultural science | Moderate | Food security, crop genetics |

## Policy Framework

### NSPM-33 Implementation

National Security Presidential Memorandum 33, issued January 14, 2021, directed federal agencies to:

- Standardize disclosure requirements for federally funded researchers
- Establish clear definitions of "research security" and "foreign talent recruitment programs"
- Develop consequences for disclosure violations
- Create interagency coordination mechanisms
- Protect research environments from inappropriate politicization

OSTP published implementation guidance in January 2022 and updated guidance in February 2023. Key provisions include:

| Requirement | Status (as of 2026) |
|-------------|---------------------|
| Standardized disclosure forms | Implemented across major agencies; variations remain |
| Digital persistent identifiers (e.g., ORCID) | Required by NSF, NIH; adoption uneven elsewhere |
| Research security training | Mandatory at most funded institutions |
| Malign foreign talent recruitment program definitions | Finalized; covers programs requiring IP transfer, secrecy, or conflicting obligations |
| Consequences for violations | Range from funding suspension to debarment; criminal referral for fraud |
| International research security information sharing | Agreements with Five Eyes and allied nations in progress |

### Agency-Specific Policies

| Agency | Key Policies | Enforcement Approach |
|--------|-------------|---------------------|
| NIH | NOT-OD-19-114 (foreign component disclosure), updated COI policies | Administrative (funding suspension, debarment); referrals to OIG |
| NSF | Expanded disclosure on biographical sketch and current/pending support | Administrative; OIG investigations |
| DOE | DOE Order 142.6 (insider threat), Foreign Government Talent Recruitment Programs prohibition | Security clearance revocation, funding termination |
| DOD | CMMC requirements, Fundamental Research clause in contracts | Contract-based enforcement, security clearance review |
| IARPA | Enhanced security screening for performers | Program-specific security requirements |
| DARPA | Controlled unclassified information (CUI) requirements | Contract-based, often classified adjunication |

### Export Controls and Fundamental Research

The fundamental research exclusion, established by NSDD-189 (1985) and reaffirmed periodically since, holds that basic research results should be unrestricted absent classification. This principle remains formally in effect but faces pressure:

- **Emerging technology controls**: The CHIPS and Science Act (2022) and subsequent Commerce Department rulings have expanded export controls on semiconductors, AI, and quantum computing, creating tension with fundamental research norms
- **Deemed export rules**: Technology transfers to foreign nationals within the U.S. require licenses if the technology is controlled; universities have sought and received broad exclusions for fundamental research, but the boundaries are contested
- **CUI expansion**: The Controlled Unclassified Information framework continues to expand, potentially covering more research that was previously open
- **Academic Technology Clearinghouse**: Proposed mechanisms for pre-publication review of sensitive research remain controversial

## The China Initiative and Its Aftermath

### Origins and Execution (2018-2022)

Attorney General Jeff Sessions launched the China Initiative in November 2018 with stated goals of identifying and prosecuting trade secret theft, economic espionage, and violations related to the Foreign Agents Registration Act. The initiative expanded to include cases of grant fraud and false statements by researchers who failed to disclose Chinese affiliations.

### Case Outcomes

| Category | Number | Notable Cases |
|----------|--------|---------------|
| Successful espionage/trade secret prosecutions | ~10-15 | Hao Zhang (Avago/Skyworks secrets), Hongjin Tan (petroleum trade secrets) |
| Grant fraud convictions or guilty pleas | ~10-15 | Song Guo Zheng (falsifying NIH disclosures), Feng Tao (wire fraud) |
| Acquittals or dismissed cases | ~10-15 | Hu Anming (acquitted on all charges), Gang Chen (charges dropped), Xiaoxing Xi (charges dropped) |
| Cases pending or under appeal (as of 2022 termination) | Several | Various stages of litigation |

### High-Profile Failures

Several cases became emblematic of overreach:

- **Xiaoxing Xi** (Temple University, 2015): Accused of sharing schematics for a pocket heater with China; charges dropped when the government's own expert acknowledged the device in question was not the one described in the indictment
- **Gang Chen** (MIT, 2021): Arrested for failing to disclose Chinese affiliations on DOE forms; charges dropped in January 2022 after it emerged the forms did not require the disclosures prosecutors alleged were omitted
- **Hu Anming** (University of Tennessee, 2020): Acquitted on all counts of wire fraud and false statements; jury found the government failed to prove he intentionally concealed NASA funding ties to a Chinese university

### Termination and Transition

Assistant Attorney General Matthew Olsen announced the China Initiative's end on February 23, 2022, replacing it with a "Strategy for Countering Nation-State Threats" that:

- Broadened focus beyond China to all nation-state threats
- Shifted emphasis from individual researcher prosecution to institutional accountability
- Required additional DOJ review of cases involving academic researchers
- Maintained enforcement against genuine espionage and trade secret theft

## Chilling Effects

### Measurable Impacts

| Indicator | Finding | Source |
|-----------|---------|--------|
| Chinese student enrollment decline | 8% decline in Chinese graduate applications to U.S. STEM programs (2019-2023) | Council of Graduate Schools |
| Researcher departures | 1,400+ Chinese-origin scientists left U.S. academia for positions in China (2021-2023) | multiple academic studies |
| Collaboration reduction | 20-25% decline in U.S.-China co-authored publications (2020-2024) | bibliometric analyses |
| Self-censorship | 42% of Asian American scientists report avoiding collaborations due to security concerns | survey by Committee of 100 |
| Recruitment difficulties | 78% of university administrators report increased difficulty recruiting international researchers | AAU survey |
| Administrative burden | Average 15-20 additional hours per PI per year on disclosure compliance | institutional estimates |

### Qualitative Effects

- **Fear and anxiety**: Asian and Asian American researchers report heightened fear of investigation, particularly those with any connection to Chinese institutions
- **Over-compliance**: Institutions imposing restrictions beyond what federal policy requires, creating patchwork burdens
- **Collaboration avoidance**: Researchers declining legitimate international partnerships to avoid scrutiny
- **Talent diversion**: Top international students choosing Canada, UK, Australia, and EU over the U.S.
- **Self-selection**: Chinese-origin researchers declining U.S. job offers or leaving academia entirely
- **Community fracture**: Erosion of trust between researchers of different national backgrounds within U.S. institutions

## Institutional Responses

### University Actions

Major research universities have responded with:

- **Dedicated research security offices**: Most AAU institutions now have research security officers or offices
- **Compliance training**: Mandatory training programs for principal investigators on disclosure requirements
- **Pre-submission review**: Review of grant applications for potential undisclosed foreign ties
- **Travel vetting**: Pre-travel review for faculty visiting countries of concern
- **Legal support**: Expanded legal counsel availability for faculty facing investigations
- **Anti-discrimination measures**: Statements and programs addressing anti-Asian bias linked to security enforcement

### Federal Coordination

- **National Science and Technology Council (NSTC)**: Research security subcommittee coordinates policy across agencies
- **Research Security Programs Office**: Established within OSTP to coordinate NSPM-33 implementation
- **JASON Advisory Group**: Provides classified and unclassified analysis of research security threats
- **National Academies**: Multiple studies on balancing security and openness (2019, 2022, 2024)

## Current Gaps and Challenges

| Gap | Description | Consequence |
|-----|-------------|-------------|
| Inconsistent standards | Agencies differ in disclosure requirements and definitions | Researcher confusion, uneven compliance |
| Insufficient due process | Grant-related investigations often lack formal adjudication procedures | Researchers denied fair hearing before career consequences |
| Racial profiling residue | Enforcement patterns still correlate with ethnicity more than behavior | Ongoing discrimination, talent loss |
| Classification creep | Expanding CUI and emerging technology controls blur fundamental research boundaries | Uncertainty about what research can be published openly |
| Compliance burden asymmetry | Individual PIs bear disproportionate compliance costs | Research time diverted to paperwork |
| Allied-nation coordination gaps | Limited information sharing with partner nations on threats | Duplicative investigations, missed threats |
| Small institution capacity | Smaller universities lack resources for robust compliance programs | Uneven protection across research enterprise |
| Whistleblower protection gaps | Researchers who report concerns face retaliation risks | Under-reporting of genuine security issues |

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Science](../01-overview.md)
