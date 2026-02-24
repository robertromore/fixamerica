# Digital Accessibility: Root Causes

## Overview

The persistence of digital inaccessibility in the United States stems from interconnected systemic failures across education, industry, regulation, and culture. Despite clear legal mandates and well-established technical standards, over 95% of websites fail basic accessibility criteria. This is not a technology problem -- the technical knowledge to build accessible digital products has existed for decades. It is a structural problem rooted in economic incentives, educational gaps, regulatory failures, and the systematic exclusion of people with disabilities from technology design processes.

## Cause Map

### Primary Causes

| Cause Category | Key Factors | Impact Level |
|---------------|-------------|--------------|
| Education failures | CS programs omit accessibility | Foundational |
| Market failures | Accessibility not valued by investors or consumers | Systemic |
| Regulatory gaps | No explicit private-sector web standards | Enabling |
| Industry culture | "Move fast and break things" ethos | Pervasive |
| Enforcement weakness | Complaint-driven, resource-limited | Perpetuating |
| Standards lag | Guidance trails technology by years | Ongoing |
| Exclusion from design | Disabled users absent from development | Structural |

## Education System Failures

### Computer Science Curriculum Gaps

Fewer than 3% of computer science programs in the United States require coursework in accessibility or inclusive design (Shinohara et al., *ACM SIGCSE*, 2018; updated survey, 2023). Developers enter the workforce without foundational knowledge of how screen readers, keyboard navigation, voice controls, and other assistive technologies interact with code. This creates a massive skills deficit at the industry's point of entry.

**Contributing factors:**

- Accreditation bodies (ABET) do not require accessibility in CS program criteria
- Accessibility is treated as a specialization rather than a core competency, similar to where security education was 20 years ago
- Faculty often lack accessibility expertise and training resources
- Textbooks and curricula focus on functionality for typical users
- Bootcamps and alternative education programs rarely cover accessibility

### Design Education Gaps

UX and design programs increasingly acknowledge accessibility but rarely integrate it throughout curricula. Most programs offer one elective course rather than embedding accessibility into every design course. The result is designers who can create visually appealing interfaces but cannot evaluate whether those interfaces are usable by people with diverse abilities.

### Continuing Education Deficits

Professional development in accessibility remains optional and unevenly available. The International Association of Accessibility Professionals (IAAP) certifies approximately 6,500 professionals in the U.S., against estimated demand exceeding 100,000 positions (IAAP, 2024; LinkedIn analysis, 2024). Most developers who learn accessibility do so through self-directed study rather than employer-provided training.

## Market Failures

### Misaligned Economic Incentives

The market systematically undervalues accessibility for several interconnected reasons:

- **Invisible user base**: People with disabilities who cannot use a website leave silently, and businesses do not track lost revenue from inaccessibility. The estimated $6.9 billion in annual e-commerce losses from inaccessibility (Click-Away Pound / AIR Foundation, 2023) is not visible to individual businesses.
- **Short-term cost focus**: Accessibility is perceived as an added cost rather than a quality attribute. Retrofitting inaccessible products is expensive; building accessibly from inception adds an estimated 1-3% to development costs (Forrester Research, 2022).
- **First-mover disadvantage**: Companies that invest in accessibility incur costs that competitors who ignore accessibility avoid, creating a race to the bottom in the absence of universal requirements.
- **Venture capital pressure**: Startup investors prioritize speed to market and user growth over accessibility. Disability is not included in standard diversity metrics that VCs track.

### Procurement Failures

Despite Section 508 requirements, federal procurement often fails to enforce accessibility in purchased technology:

- 40% of federal IT procurements did not include adequate Section 508 requirements (GAO-23-105418, 2023)
- Voluntary Product Accessibility Templates (VPATs) are self-reported by vendors and frequently inaccurate
- Procurement officers lack technical expertise to evaluate accessibility claims
- Price and feature comparisons rarely weight accessibility
- State and local government procurement is even less likely to include accessibility requirements

### Insurance and Risk Miscalculation

Businesses underestimate litigation risk because individual lawsuit damages are relatively small (typically $5,000-$25,000 in settlements). The aggregate cost of serial litigation, however, is substantial, and companies often calculate that paying individual settlements is cheaper than comprehensive remediation. This calculus perpetuates noncompliance.

## Regulatory and Enforcement Failures

### Regulatory Vacuum for Private Sector

The most significant regulatory failure is the absence of explicit federal regulations applying digital accessibility standards to private-sector websites and applications. Key gaps include:

- **No ADA Title III web regulation**: DOJ has not finalized rules specifying what digital accessibility standards private businesses must meet. The 2024 Title II rule covers state and local governments only.
- **No FCC enforcement of app accessibility**: The CVAA covers advanced communications services but does not extend to general-purpose websites and applications.
- **No FTC accessibility mandate**: The FTC's consumer protection authority has not been applied to digital inaccessibility as an unfair or deceptive practice.

### Enforcement Resource Constraints

| Agency | Role | Limitation |
|--------|------|-----------|
| DOJ Civil Rights Division | ADA enforcement | Investigates fewer than 5% of complaints; digital cases are a small subset |
| Access Board | Section 508 standards | Advisory role only; cannot bring enforcement actions |
| GSA | Section 508 compliance support | Guidance and tools but no enforcement authority |
| EEOC | Employment technology | Focuses on hiring discrimination, not broad digital access |
| DOE OCR | Educational technology | Complaint-driven; investigates individual institutions |

Source: GAO reports (2023); agency budget documents (FY 2024).

### Standards Development Lag

Accessibility standards consistently trail technology development:

- WCAG 2.0 (2008) did not address mobile accessibility, which was already mainstream
- WCAG 2.1 (2018) added mobile criteria 11 years after the iPhone launched
- WCAG 2.2 (2023) remains insufficient for AI-powered interfaces, XR, and IoT
- WCAG 3.0 has been in development since 2017 with no expected completion date before 2026
- Section 508 standards (refreshed 2017) reference WCAG 2.0, not 2.1 or 2.2

This lag means that even organizations attempting good-faith compliance lack clear guidance for emerging technologies.

## Industry and Cultural Factors

### Development Culture

The technology industry's dominant culture prioritizes speed, visual appeal, and engagement metrics over accessibility:

- **"Ship fast" mentality**: Agile development practices and rapid deployment cycles deprioritize accessibility testing, which is often deferred to future sprints or never completed
- **Visual design dominance**: Design culture rewards visual innovation, while accessible design is perceived as constraining or boring
- **Metrics blindness**: Key performance indicators (conversion rates, engagement, retention) do not track disabled user experience, making inaccessibility invisible to product teams
- **Testing gaps**: QA processes test for functionality and performance but rarely include accessibility. Only 28% of Fortune 500 companies have dedicated accessibility teams (Business Disability Forum, 2024).

### Ableism in Technology

Systemic ableism in the technology industry manifests in:

- **Design assumptions**: Products are designed for a "typical" user who can see, hear, use a mouse, and process complex visual information
- **Disability erasure**: User personas rarely include disabled users; user research seldom recruits disabled participants
- **Workforce exclusion**: People with disabilities are underrepresented in technology roles (approximately 5% of tech workforce versus 26% of general population), reducing the likelihood that accessibility issues are identified during development (Bureau of Labor Statistics, 2023)
- **"Edge case" framing**: Accessibility needs are classified as edge cases rather than mainstream requirements, deprioritizing them in resource allocation

### Platform and Framework Defaults

Technology platforms and development frameworks often ship with inaccessible defaults:

- Popular UI component libraries (some React, Vue, Angular components) produce inaccessible HTML
- Content management systems generate pages with accessibility errors by default
- WYSIWYG editors produce content without proper semantic structure
- AI code generation tools frequently produce inaccessible code
- Template marketplaces sell inaccessible themes and templates

## Feedback Loop Analysis

### The Inaccessibility Cycle

1. CS programs do not teach accessibility
2. Developers enter the workforce without accessibility skills
3. Products are built without accessibility consideration
4. People with disabilities cannot use digital products
5. Disabled users are invisible in usage data and user research
6. Business case for accessibility is not demonstrated
7. Companies do not invest in accessibility training or hiring
8. Demand for accessibility education remains low
9. CS programs continue to omit accessibility (return to step 1)

### The Enforcement Cycle

1. Congress does not mandate specific digital accessibility standards for private sector
2. DOJ does not issue regulations
3. Businesses lack clear compliance targets
4. Lawsuits increase due to inaccessibility
5. Industry lobbies for litigation restrictions (e.g., ADA Education and Reform Act)
6. Political pressure delays or weakens regulatory action
7. Regulatory vacuum persists (return to step 1)

## Contributing Factors Summary

| Factor | Mechanism | Severity |
|--------|-----------|----------|
| No private-sector web regulation | Businesses lack enforceable compliance targets | Critical |
| CS education omits accessibility | Developers lack foundational skills | Critical |
| Market ignores disabled users | No economic incentive for compliance | High |
| Enforcement resource scarcity | Violations go undetected and unpunished | High |
| Standards lag technology | Good-faith compliance is unclear for new technologies | High |
| Ableism in tech culture | Disability needs excluded from design process | High |
| Procurement enforcement gaps | Federal buying power not leveraged | Medium |
| Platform/framework defaults | Inaccessible code produced by default | Medium |
| Automated testing limitations | Organizations think they are compliant when they are not | Medium |

---

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
