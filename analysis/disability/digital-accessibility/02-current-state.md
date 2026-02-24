---
topic: Digital Accessibility
domain: Disability
last-reviewed: 2026-02-20
data-sources:
  - name: WebAIM Million
    url: https://webaim.org/projects/million/
    data-year: 2024
  - name: UsableNet ADA Digital Accessibility Report
    url: https://usablenet.com
    data-year: 2024
  - name: GAO Section 508 Audit
    url: https://www.gao.gov
    data-year: 2023
  - name: CDC Disability and Health Data System
    url: https://www.cdc.gov/dhds/
    data-year: 2023
  - name: W3C Web Accessibility Initiative
    url: https://www.w3.org/WAI/
    data-year: 2024
key-metrics:
  websites-with-wcag-failures: 0.959
  avg-errors-per-homepage: 56.8
  federal-508-full-compliance: 0.30
  federal-web-lawsuits-2023: 4605
  americans-with-disabilities: 61000000
---

# Digital Accessibility: Current State

## Present Conditions

The digital landscape in the United States remains overwhelmingly inaccessible to people with disabilities despite more than three decades of legal mandates and two decades of internationally recognized technical standards. The gap between legal obligation and actual compliance is stark: while the ADA prohibits discrimination in places of public accommodation and Section 508 requires federal technology to be accessible, the vast majority of websites, applications, and digital services fail to meet basic accessibility criteria.

## Web Accessibility Landscape

### Overall Compliance

| Metric | Value | Source |
|--------|-------|--------|
| Top 1 million homepages with WCAG failures | 95.9% | WebAIM Million (2024) |
| Average detectable errors per homepage | 56.8 | WebAIM Million (2024) |
| Pages with low contrast text | 81.0% | WebAIM Million (2024) |
| Pages with missing alt text | 54.5% | WebAIM Million (2024) |
| Pages with empty links | 45.1% | WebAIM Million (2024) |
| Pages with missing form labels | 43.4% | WebAIM Million (2024) |
| Pages with missing document language | 17.1% | WebAIM Million (2024) |

### Most Common Failures

| WCAG Failure | Prevalence | Impact |
|--------------|-----------|--------|
| Low contrast text | 81.0% of homepages | Affects users with low vision, color blindness |
| Missing alt text for images | 54.5% of homepages | Renders images invisible to screen reader users |
| Empty links | 45.1% of homepages | Creates navigational dead ends for keyboard users |
| Missing form input labels | 43.4% of homepages | Makes forms unusable for screen reader users |
| Empty buttons | 27.2% of homepages | Prevents interaction with controls |
| Missing document language | 17.1% of homepages | Disrupts screen reader pronunciation |

### Trends Over Time

| Year | Homepages with Errors | Avg Errors per Page | Change |
|------|----------------------|---------------------|--------|
| 2019 | 98.1% | 59.6 | Baseline |
| 2020 | 98.1% | 60.9 | +2.2% errors |
| 2021 | 97.4% | 51.4 | -15.6% errors |
| 2022 | 96.8% | 50.8 | -1.2% errors |
| 2023 | 96.3% | 49.9 | -1.8% errors |
| 2024 | 95.9% | 56.8 | +13.8% errors |

*Note: The 2024 increase in average errors per page despite slight improvement in failure rate reflects growing website complexity.* Source: WebAIM Million Reports (2019-2024).

## Federal Government Compliance

### Section 508 Status

| Agency Category | Full Compliance | Partial Compliance | Noncompliant |
|----------------|----------------|-------------------|-------------|
| Cabinet departments (15) | 4 (27%) | 8 (53%) | 3 (20%) |
| Independent agencies (25 audited) | 8 (32%) | 12 (48%) | 5 (20%) |
| Overall federal average | 30% | 50% | 20% |

Source: GAO-23-105418, "Information Technology: Agencies Need to Fully Implement Key Practices for Section 508 Compliance" (2023).

### Government Website Issues

| Issue | Finding | Source |
|-------|---------|--------|
| Agency Section 508 programs | Only 11 of 24 CFO Act agencies had mature 508 programs | OMB Section 508 Annual Assessment (FY 2023) |
| ICT testing coverage | Fewer than 50% of federal ICT products undergo accessibility testing | GSA Government-wide IT Accessibility Program (2024) |
| Procurement accessibility | 40% of federal IT procurements did not include adequate 508 requirements | GAO-23-105418 (2023) |
| Complaint resolution | Average federal 508 complaint takes 180+ days to resolve | DHS Office of Accessible Systems and Technology (2023) |

## Litigation Landscape

### Federal ADA Digital Accessibility Lawsuits

| Year | Total Filed | Title III (Public Accommodation) | Title II (Government) |
|------|------------|--------------------------------|----------------------|
| 2018 | 2,285 | 2,258 | 27 |
| 2019 | 2,256 | 2,214 | 42 |
| 2020 | 3,550 | 3,503 | 47 |
| 2021 | 4,055 | 3,996 | 59 |
| 2022 | 3,255 | 3,186 | 69 |
| 2023 | 4,605 | 4,528 | 77 |

Source: UsableNet Year-End ADA Digital Accessibility Reports (2018-2024).

### Industries Most Targeted

| Industry | Share of 2023 Lawsuits | Common Issues |
|----------|----------------------|---------------|
| E-commerce/retail | 38% | Inaccessible product pages, checkout barriers |
| Food service | 14% | Online ordering, menu accessibility |
| Entertainment/leisure | 12% | Ticket purchase, event information |
| Banking/financial | 9% | Account management, forms, transactions |
| Healthcare | 7% | Patient portals, appointment scheduling |
| Education | 6% | LMS platforms, course materials |
| Travel/hospitality | 5% | Booking systems, itinerary management |
| Other | 9% | Various |

Source: UsableNet Year-End ADA Report (2024).

### Key Legal Precedents

| Case | Year | Holding |
|------|------|---------|
| *National Federation of the Blind v. Target Corp.* | 2006 | Websites connected to physical stores are covered by ADA Title III |
| *Gil v. Winn-Dixie Stores* | 2021 (11th Cir.) | Narrowly held that website must have nexus to physical location; created circuit split |
| *Robles v. Domino's Pizza* | 2019 (9th Cir.) | ADA applies to websites and apps of public accommodations; DOJ regulations not prerequisite |
| *Langer v. Kohl's Department Stores* | 2022 | Mootness doctrine allows companies to fix and dismiss; weakens enforcement |
| *DOJ v. Rite Aid* | 2024 | DOJ settlement established WCAG 2.1 AA as compliance standard |

## Standards and Guidelines

### Current Standards

| Standard | Version | Scope | Status |
|----------|---------|-------|--------|
| WCAG 2.0 | 2008 | Web content | ISO standard; Section 508 baseline |
| WCAG 2.1 | 2018 | Web content + mobile | W3C Recommendation; DOJ reference |
| WCAG 2.2 | 2023 | Enhanced cognitive, mobile | W3C Recommendation |
| WCAG 3.0 | Draft | Next generation, broader scope | W3C Working Draft |
| Section 508 Standards | 2017 refresh | Federal ICT | 47 C.F.R. Part 1194 |
| EN 301 549 | v3.2.1 (2021) | European ICT standard | EU Directive requirement |
| PDF/UA (ISO 14289) | 2012, rev. 2024 | Accessible PDFs | ISO standard |

### Testing Tools and Limitations

| Approach | Coverage | Limitations |
|----------|----------|-------------|
| Automated testing (axe, WAVE, Lighthouse) | 30-40% of WCAG criteria | Cannot assess meaning, context, usability |
| Manual expert testing | 80-90% of WCAG criteria | Expensive, time-intensive, requires expertise |
| Assistive technology testing | Real-world usability | Varies by AT, requires skilled testers |
| User testing with disabled participants | Functional outcomes | Small samples, not scalable |

Source: Deque Systems / W3C WAI evaluation methodology documentation (2024).

## Sector-Specific Conditions

### Education

| Metric | Value | Source |
|--------|-------|--------|
| Higher ed websites meeting WCAG 2.1 AA | Fewer than 20% | EDUCAUSE Review (2023) |
| LMS platforms with known barriers | All major platforms have documented issues | NCDAE evaluations (2024) |
| DOE OCR digital accessibility complaints | 280+ filed (FY 2023) | Department of Education OCR (2024) |
| Accessible e-textbooks | Approximately 40% of new titles | Association of American Publishers (2023) |

### Healthcare

| Metric | Value | Source |
|--------|-------|--------|
| Hospital websites meeting WCAG 2.0 AA | 29% | Lazar et al., *JAMIA* (2023) |
| Telehealth platforms with accessibility features | 35% had adequate features | National Council on Disability (2024) |
| Patient portal screen reader compatibility | 41% partially compatible | Pew / NCD joint study (2023) |

### E-Commerce

| Metric | Value | Source |
|--------|-------|--------|
| Top 100 retailers meeting WCAG 2.1 AA | 12% | Nucleus Research (2024) |
| Revenue lost to inaccessibility | $6.9 billion annually | Click-Away Pound / AIR Foundation (2023) |
| Accessible checkout processes | 23% of top retailers | Baymard Institute (2024) |

## International Comparison

| Country/Region | Key Regulation | Scope | Enforcement |
|---------------|---------------|-------|-------------|
| European Union | European Accessibility Act (2019/882) | Private sector products and services | Mandatory compliance by June 2025 |
| United Kingdom | Equality Act 2010 + PSBAR 2018 | Public and private sector | Monitoring body with enforcement powers |
| Canada | Accessible Canada Act (2019) | Federally regulated entities | Accessibility Commissioner |
| Australia | Disability Discrimination Act 1992 | Public and private sector | Australian Human Rights Commission |
| United States | ADA + Section 508 | Public accommodations + federal ICT | Litigation-driven; no explicit web regulation |

## Workforce and Industry

### Accessibility Professionals

| Metric | Value | Source |
|--------|-------|--------|
| IAAP-certified professionals in U.S. | Approximately 6,500 | IAAP membership data (2024) |
| Estimated demand for accessibility roles | 100,000+ positions | LinkedIn / Indeed job postings analysis (2024) |
| CS programs requiring accessibility coursework | Fewer than 3% | Shinohara et al., *ACM SIGCSE* (2018); updated survey (2023) |
| Companies with dedicated accessibility teams | 28% of Fortune 500 | Business Disability Forum survey (2024) |

### Industry Commitments

| Initiative | Participants | Status |
|-----------|-------------|--------|
| Accessibility.com Partner Program | 500+ companies | Voluntary |
| IAAP organizational membership | 200+ organizations | Voluntary |
| Microsoft Accessibility Conformance Reports | Public reporting | Industry practice |
| Apple Accessibility features | Built-in platform features | Ongoing development |
| Google Accessibility initiatives | Products and developer tools | Ongoing development |

## Emerging Challenges

### Artificial Intelligence

- AI-generated content frequently lacks accessible structure (alt text, headings, semantic markup)
- Machine learning interfaces (chatbots, voice assistants) may not work with screen readers
- Automated captioning accuracy: 80-90% for clear speech, below 60% for accented or disordered speech (Stanford HAI, 2024)
- AI-powered hiring tools may discriminate against disabled applicants through inaccessible interfaces or biased algorithms

### Extended Reality (XR)

- Virtual reality environments are largely inaccessible to users with vision, hearing, or motor disabilities
- Augmented reality applications typically lack accessible interaction alternatives
- No established accessibility standards exist for XR environments (W3C XR Accessibility draft, 2024)

### Internet of Things (IoT)

- Smart home devices often lack accessible setup and management interfaces
- Healthcare IoT devices may have inaccessible displays or controls
- No comprehensive IoT accessibility standards exist in U.S. regulation

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
