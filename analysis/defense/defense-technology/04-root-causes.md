# Defense Technology: Root Causes

## Systemic Analysis

The U.S. military's struggle to adopt new technologies is not due to a lack of ideas or money. The DoD spends $143 billion annually on R&D -- more than most countries spend on their entire military. The problem is structural and cultural: a set of interlocking barriers that were designed for a different era and are now self-reinforcing. Each barrier makes the others harder to overcome, creating a system that resists reform even when virtually all participants acknowledge it is broken.

## Root Cause 1: The "Industrial Age" Acquisition System

The Planning, Programming, Budgeting, and Execution (PPBE) system was designed by Secretary of Defense Robert McNamara in the early 1960s to impose analytical rigor on defense spending. It was built for an era in which the government developed most technology internally, programs lasted decades, and the relevant technologies (aircraft, ships, missiles) evolved slowly.

### Hardware Bias

- The PPBE process was designed to buy aircraft carriers and tanks -- assets that take a decade to build and last for 50 years. It requires detailed requirements to be defined years before a contract is awarded, and it funds development, procurement, and sustainment through separate appropriation accounts ("colors of money").
- **Software incompatibility**: Software does not fit this model. Software is simultaneously developed, procured, and maintained; it requires continuous iteration and updates; and its requirements evolve during development. Forcing software into hardware acquisition categories creates absurdities -- a minor software update may require a new budget line item that takes two years to process through the PPBE cycle.
- **The PPBE Commission**: In 2022, Congress established the Commission on Planning, Programming, Budgeting, and Execution Reform. Its March 2024 final report found that the PPBE system is "a significant obstacle to the Department's ability to adapt" and recommended sweeping reforms including portfolio budgeting, a new software appropriation category, and delegated reprogramming authority. As of early 2026, few of these recommendations have been implemented.

### Linear "Waterfall" Development

- The traditional "waterfall" development model (define requirements, design, build, test, field) takes 7-10 years for a major system. By the time the system is fielded, the technology is often one or two generations behind the commercial state of the art.
- **Example**: The Army's Integrated Tactical Network (ITN) program took over a decade to define requirements and begin procurement. By the time the first systems were fielded, commercial 5G networks offered capabilities that surpassed the military system in bandwidth and reliability.

### "Color of Money" Restrictions

- Federal appropriations law divides defense spending into rigid categories: Research and Development (R&D), Procurement, Operations and Maintenance (O&M), and Military Personnel. Funds cannot be moved between these categories without explicit congressional authorization.
- This means that a successful software prototype developed with R&D funds cannot be "bought" with Procurement funds or "maintained" with O&M funds without separate budget actions for each -- a process that can take two fiscal years. The result is that promising technologies sit idle while the bureaucracy processes paperwork.

## Root Cause 2: The "Valley of Death"

### The Gap

There is a massive gap between winning a pilot contract or prototype demonstration (funded by R&D dollars) and securing a production contract as a Program of Record (funded by Procurement dollars). This gap -- universally known as the "Valley of Death" -- is the single most frequently cited barrier to defense innovation.

### Budget Cycle Lag

Even if a prototype is successful today, funding for production must be inserted into the President's Budget request for the fiscal year beginning 18-24 months from now, then be authorized and appropriated by Congress. The total lag from successful prototype to first production dollar can be 2-4 years.

### Startup Mortality

Small, innovative companies cannot survive this 2-4 year wait without revenue. They face a stark set of options:

- **Go bankrupt**: Many defense-focused startups run out of venture capital funding before production contracts materialize. The venture capital model expects returns within 5-7 years; the defense acquisition timeline often exceeds this.
- **Pivot to commercial markets**: Companies that can sell commercially often abandon the defense market entirely, concluding that the regulatory burden and timeline uncertainty are not worth the effort.
- **Get acquired by prime contractors**: Primes routinely acquire innovative startups, capturing their technology and talent. In some cases, the acquired technology is integrated into the prime's portfolio; in others, it is shelved to eliminate a competitive threat to legacy programs.

### Data on the Valley of Death

- GAO has found that fewer than 25% of SBIR Phase II projects transition to Phase III or a program of record.
- A 2023 RAND study estimated that more than 50% of successfully demonstrated prototypes under Other Transaction Authority (OTA) agreements fail to transition to follow-on production contracts.
- DIU's own data shows that while it can award prototype contracts in 60-90 days, the transition to production-scale contracts averages 18-36 months and often fails entirely.

## Root Cause 3: Incentive Structures

### Prime Contractor Incentives

The major defense primes (Lockheed Martin, RTX, Northrop Grumman, Boeing Defense, General Dynamics) are publicly traded companies with fiduciary obligations to maximize shareholder value. Their business model is built on long-running, cost-plus or fixed-price-incentive contracts for expensive, exquisite platforms. Disruptive technologies -- particularly cheap, attritable autonomous systems -- threaten this model in several ways:

- **Revenue displacement**: A $3 million autonomous drone wingman that replaces a $100 million manned fighter represents a 97% reduction in revenue per unit for the prime contractor.
- **Requirements capture**: Primes invest heavily in shaping DoD requirements to favor their existing capabilities. By the time a Request for Proposal (RFP) is issued, the requirements often mirror the prime's current product line so closely that no other firm can credibly compete.
- **Lobbying against disruption**: Primes spend $140+ million annually on lobbying, much of it directed at preserving funding for legacy programs that face potential displacement by new technologies. (See [Military-Industrial Complex: Current State](../military-industrial-complex/02-current-state.md).)

### Program Manager Risk Aversion

- Program managers (PMs) in the DoD acquisition workforce are evaluated primarily on whether their programs stay on schedule and on budget. They are punished for failure but rarely rewarded for bold success or for taking calculated risks on new technologies.
- The safe career move is to follow the established process and buy the known product from the established vendor. Betting on an unproven startup risks a career-ending program failure if the technology does not perform. This incentive structure systematically biases the acquisition system toward incumbents and proven (often outdated) technologies.
- **The PM rotation problem**: Military program managers typically serve 2-3 year tours. This is shorter than the development cycle of most major systems, meaning that no single PM has personal accountability for long-term program outcomes. PMs are incentivized to avoid problems during their tenure and pass risks to their successors.

## Root Cause 4: Cultural and Institutional Barriers

### Silicon Valley vs. The Pentagon

- **Culture clash**: Technology companies value speed, iteration, risk-taking, flat hierarchies, and "fail fast" experimentation. The DoD values process, hierarchy, compliance, stability, and zero-defect performance. These cultures are not merely different; they are fundamentally incompatible in many respects, and bridging them requires sustained effort from both sides.
- **Ethical concerns**: The Project Maven controversy at Google (2018) demonstrated the tension between the tech workforce and defense applications. When Google's contract to apply AI to drone imagery analysis became public, approximately 3,100 employees signed a petition demanding that Google withdraw. Google did not renew the contract and published AI ethics principles that restricted certain military applications. Similar internal resistance has occurred at Microsoft (over the IVAS augmented reality headset contract), Amazon (over Rekognition facial recognition technology), and other firms.
- **Intellectual property**: The DoD traditionally demands unlimited rights to technical data and computer software developed under contract ("data rights"). Commercial companies refuse to surrender their IP, because it is the foundation of their competitive advantage and commercial business. This conflict kills deals: a startup that gives the DoD unlimited rights to its source code cannot sell that same software commercially, destroying the dual-use business model that venture capitalists fund.

### Clearance and Compliance Barriers

- **Security clearances**: Obtaining a security clearance takes an average of 8-12 months for a Secret clearance and 12-18 months for a Top Secret/SCI clearance. The backlog has at times exceeded 600,000 pending investigations. For a startup with 20 employees, waiting a year to get clearances before they can even understand the problem they are being asked to solve is a deal-breaker.
- **Compliance costs**: Complying with defense-specific regulations (DFARS, CMMC cybersecurity certification, CUI handling requirements, ITAR) imposes overhead costs that can consume 15-30% of a small company's revenue. Large primes absorb these costs across a broad contract base; small firms cannot.
- **Facility clearance**: Companies working on classified programs must maintain a facility clearance (FCL), which requires physical security measures (SCIFs, access controls, cleared IT systems) that cost $500,000-$2 million to establish and maintain.

## Root Cause 5: Over-Classification and Data Silos

### Barriers to Entry

- Excessive classification requirements prevent uncleared commercial companies from understanding military problems or bidding on contracts. A startup cannot develop an AI solution for a military problem if it cannot access the data that defines the problem.
- A 2020 study by the Public Interest Declassification Board estimated that 50-90% of classified information could be safely declassified without harming national security. The culture of over-classification serves institutional interests (restricting competition, avoiding embarrassment, maintaining bureaucratic power) more than it serves security.

### Siloed Data

- Data necessary to train AI models is often trapped in classified silos, proprietary formats, or legacy systems that lack modern APIs. The DoD operates hundreds of data centers with inconsistent standards, making it extremely difficult to aggregate the training datasets that machine learning requires.
- **CDAO's challenge**: The Chief Digital and AI Office was created in part to break down data silos, but it faces resistance from services and agencies that view their data as institutional assets and resist sharing.
- **Classified-unclassified divide**: Much of the most valuable defense data (signals intelligence, imagery, operational reports) exists at the classified level, but the best AI development tools and talent operate in unclassified commercial environments. Bridging this gap -- training models on classified data while developing algorithms in unclassified environments -- is technically challenging and bureaucratically fraught.

## Root Cause 6: The Talent Crisis

### Compensation Gap

Government civilian and military personnel in technical roles earn significantly less than their private-sector counterparts:

| Role | Government Salary (typical) | Private Sector Salary (typical) | Gap |
|---|---|---|---|
| Software engineer (mid-level) | $100,000-$130,000 | $180,000-$350,000+ | 40-170% |
| AI/ML researcher | $120,000-$150,000 | $250,000-$600,000+ | 100-300% |
| Cybersecurity specialist | $90,000-$130,000 | $150,000-$300,000 | 60-130% |
| Systems engineer | $110,000-$140,000 | $160,000-$250,000 | 15-80% |

*Sources: OPM General Schedule pay tables; Levels.fyi; Glassdoor; CRS reports.*

### Structural Barriers to Talent

- **Rigid hiring**: The federal hiring process (USAJobs) takes an average of 98 days from posting to offer, compared to 2-4 weeks at major tech companies. By the time a government offer arrives, the candidate has already accepted a private sector position.
- **No lateral entry**: The military does not allow experienced civilians to enter at mid-career ranks commensurate with their expertise. A 35-year-old AI researcher with a PhD and 10 years of industry experience would have to enter the military as a junior officer (O-1 or O-2), which is unacceptable to most qualified candidates.
- **Career rigidity**: Both military and civilian career tracks are linear and seniority-based, with limited ability to reward exceptional technical performance or to move laterally between technical and managerial roles.

## Causal Chain of Innovation Stagnation

```text
Cold War success creates rigid, hardware-centric bureaucracy (PPBE, 1960s)
    |
Commercial tech sector outpaces government R&D (1990s-2000s)
    |
DoD attempts to access commercial tech but applies industrial-age rules
    |
Startups face "Valley of Death": 2-4 year gap between prototype and production
    |
IP conflicts, clearance barriers, and compliance costs deter commercial firms
    |
Primes dominate market, incentivized to protect legacy platforms over disruptive innovation
    |
Best technical talent flows to private sector (2-3x compensation gap)
    |
Over-classification and data silos prevent AI development on defense-relevant data
    |
Result: U.S. military fields technology that is years behind the commercial state of the art
    while China integrates commercial and military innovation through state direction
```

## Interaction Effects

These root causes do not operate in isolation. They interact in ways that make the system highly resistant to reform:

- The **PPBE budget cycle** creates the **Valley of Death**, which kills startups, which reduces competition, which strengthens **prime contractor dominance**, which funds lobbying to preserve the PPBE system.
- **Over-classification** prevents commercial firms from understanding defense problems, which reinforces the **culture clash** between Silicon Valley and the Pentagon, which deters the **talent** needed to reform the system from within.
- **Risk-averse program managers** default to incumbent contractors, which reduces the market for new entrants, which makes venture capitalists less willing to fund defense startups, which widens the **Valley of Death**.
- The **compensation gap** means the government cannot hire the technical experts needed to evaluate new technologies, which increases **information asymmetry** between the government and contractors, which enables primes to shape requirements in their favor.

The result is a self-reinforcing system in which each barrier supports and enables the others, creating a network of obstacles that is far more durable than any individual reform effort.

---

## Document Navigation

- Up: [Defense Technology](../01-overview.md)
- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
