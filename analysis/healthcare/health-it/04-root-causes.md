# Health Information Technology: Root Causes

## Structural Causes

### Market Structure and Vendor Economics

**Network Effects Create Winner-Take-All Dynamics**

| Factor | Effect on Market |
|--------|------------------|
| Vendor-specific exchange networks | Data flows easily within Epic, not between vendors |
| Switching costs | $100-500M to change systems locks in customers |
| Training investments | Staff expertise tied to specific systems |
| Integration complexity | Third-party apps built for specific platforms |
| Referral patterns | Physicians refer within same EHR ecosystem |

**Implications**

- Market naturally consolidates around 2-3 dominant vendors
- New entrants cannot achieve necessary scale
- Incumbents have no incentive to enable interoperability
- Innovation must come through (or be acquired by) incumbents

### Misaligned Incentive Structure

**Provider-Payer Disconnect**

| Investment By | Benefit Accrues To |
|---------------|-------------------|
| Provider implements EHR | Payer saves on duplicate tests |
| Provider sends patient records | Receiving provider benefits |
| Provider participates in HIE | System-wide efficiency |
| Provider invests in analytics | Population health managers benefit |

**Result**: Those who pay for health IT do not capture most of the value, creating systematic underinvestment in interoperability and information sharing.

### Revenue Model Conflicts

**EHR Vendors Profit from Lock-In**

| Revenue Source | Incentive Created |
|----------------|-------------------|
| Per-user licensing | Add features to justify price |
| Interface fees | Charge for third-party connections |
| Hosting fees | Discourage alternatives |
| Consulting services | Complexity increases revenue |
| Data analytics products | Proprietary data valuable |

**Hospital Buyers Focused on Wrong Metrics**

| Purchase Focus | Missing Consideration |
|----------------|----------------------|
| Feature checklist | Actual usability |
| Certification status | Real interoperability |
| Vendor reputation | Total cost of ownership |
| IT department preferences | Clinician workflow needs |

## Economic Causes

### High Switching Costs Eliminate Competition

**Components of Switching Cost**

| Category | Typical Cost (Large System) |
|----------|---------------------------|
| New system licensing | $50-100 million |
| Implementation consulting | $100-200 million |
| Hardware/infrastructure | $20-50 million |
| Data migration | $20-50 million |
| Training | $30-50 million |
| Productivity loss | $50-100 million (during transition) |
| Interface rebuilding | $10-30 million |
| **Total** | **$280-580 million** |

**Consequence**: Once a health system selects an EHR vendor, switching is effectively impossible. Vendors can raise prices and resist changes knowing customers are trapped.

### Information Asymmetry in Purchasing

**Buyer Disadvantages**

| Asymmetry | Effect |
|-----------|--------|
| Technical complexity | Hospitals cannot evaluate EHR quality |
| Implementation variability | Success depends on vendor execution |
| Reference sites cherry-picked | Vendor controls buyer perception |
| Long sales cycle | Decisions made with incomplete information |
| Consultant conflicts | Many advisors have vendor relationships |

### Return on Investment (ROI) Challenges

**Who Benefits from Health IT Investment**

| Investment | Primary Beneficiary | Investor |
|------------|--------------------|-----------|
| Clinical documentation | Payers (claims data), Lawyers (documentation) | Providers |
| Interoperability | Receiving providers, Patients | Sending providers |
| Analytics | Payers, ACOs | Individual providers |
| Patient portals | Patients | Providers |
| Population health | Public health, ACOs | Individual providers |

The fragmented payment system ensures that those who invest in health IT rarely capture the benefits, creating systematic underinvestment.

## Regulatory Causes

### Perverse Certification Incentives

**Certification Measures Capability, Not Performance**

| Certification Requirement | What It Misses |
|--------------------------|----------------|
| API endpoint exists | Whether it works with others |
| Data can be exported | Whether format is usable |
| Decision support exists | Whether it helps clinicians |
| Security features exist | Whether they're properly configured |
| Patient access available | Whether patients can use it |

**Consequences**

- Vendors optimize for certification tests, not real use
- Certified products may fail in practice
- Certification creates compliance theater
- Real interoperability not tested

### Enforcement Failures

**Information Blocking Prohibition**

| Designed To | Actual Result |
|-------------|---------------|
| Prevent vendors from blocking data | Limited enforcement actions |
| Enable third-party apps | Vendors charge high fees |
| Facilitate exchange | Technical barriers remain |
| Protect patient access | Process barriers persist |

**Why Enforcement Is Weak**

| Factor | Effect |
|--------|--------|
| Complex definitions | Hard to prove information blocking |
| Multiple exceptions | Vendors claim exemptions |
| ONC understaffed | Limited investigation capacity |
| Political pressure | Vendor lobbying |
| Burden of proof | Difficult to establish intent |

### Regulatory Fragmentation

**Multiple Agencies with Overlapping Authority**

| Agency | Health IT Role | Coordination Issues |
|--------|----------------|---------------------|
| ONC | Standards, certification | Limited enforcement power |
| CMS | Payment incentives, conditions | Focused on payment, not IT |
| FDA | Software as medical device | Scope limitations |
| FTC | Antitrust, competition | Health IT not priority |
| OCR | HIPAA enforcement | Privacy focus only |
| State regulators | Varies by state | 50+ different approaches |

## Institutional Causes

### Hospital IT Departments as Gatekeepers

**IT vs. Clinical Priorities**

| IT Priority | Clinical Need |
|-------------|---------------|
| System stability | Workflow flexibility |
| Vendor support | Third-party innovation |
| Standardization | Specialty customization |
| Security (restrictive) | Data access |
| Budget predictability | Feature investment |

**Consequences**

- IT departments block innovations that complicate their operations
- Vendor relationships become entrenched
- Clinical workflow needs subordinated to IT preferences
- Security used as excuse to prevent interoperability

### Physician Leadership Gaps

**Why Physician Informaticists Are Marginalized**

| Factor | Effect |
|--------|--------|
| Career path unclear | Few physicians pursue informatics |
| Compensation lower | Clinical medicine pays more |
| Decision authority limited | IT/finance make key decisions |
| Clinical demands | Informatics is "extra" work |
| Training gaps | Few CMIOs have deep technical expertise |

### Fragmented Healthcare Delivery

**Thousands of Independent Entities**

| Entity Type | Approximate Count |
|-------------|------------------|
| Hospitals | 6,000+ |
| Physician practices | 250,000+ |
| Clinics | 10,000+ |
| Long-term care facilities | 15,000+ |
| Home health agencies | 11,000+ |
| Labs | 10,000+ |
| Pharmacies | 60,000+ |

Each entity makes independent technology decisions, creating a patchwork of incompatible systems.

## Technical Causes

### Legacy Architecture

**Historical Technical Decisions Still Constraining**

| Legacy Element | Current Problem |
|----------------|-----------------|
| HL7 v2 messaging | Inconsistent implementations |
| Proprietary databases | Data locked in silos |
| On-premise hosting | Limited cloud capabilities |
| Document-based exchange | Not computable data |
| Custom interfaces | Point-to-point complexity |

### Standards Implementation Variability

**FHIR Adoption Challenges**

| Standard | Implementation Reality |
|----------|----------------------|
| FHIR R4 | Inconsistent extension use |
| USCDI | Optional elements often missing |
| C-CDA | Wide interpretation variation |
| Terminology (SNOMED, LOINC) | Mapping inconsistencies |

**"Same Standard, Different Implementations"**

Even when systems use the same standard, data exchange fails because:

- Optional elements implemented differently
- Extensions create incompatibilities
- Terminology mapping varies
- Validation rules differ
- Interpretation of requirements varies

### Security vs. Usability Tradeoffs

**Security Theater**

| Security Measure | Usability Impact | Actual Security Benefit |
|------------------|------------------|------------------------|
| Frequent password changes | User frustration, workarounds | Minimal (often counterproductive) |
| Session timeouts | Workflow interruption | Modest |
| Authentication complexity | Delayed access | Moderate |
| Device restrictions | Limited mobility | Variable |
| Network segmentation | Exchange barriers | High |

## Political Causes

### Vendor Political Influence

**Lobbying and Political Contributions**

| Activity | Effect |
|----------|--------|
| Industry association lobbying | Shapes regulation |
| Individual vendor lobbying | Weakens requirements |
| Revolving door | Regulators become consultants |
| Campaign contributions | Congressional oversight limited |
| Trade press influence | Favorable coverage |

**Epic's Political Strategy**

- Cultivates image as employee-owned "good actor"
- Significant Wisconsin political presence
- CEO Judy Faulkner personally influential
- Avoids public company scrutiny
- Presents interoperability as achieved

### Partisan Non-Issue

**Health IT Has Bipartisan Dysfunction**

| Party | Position |
|-------|----------|
| Republicans | Generally pro-industry, deregulation |
| Democrats | Supported HITECH, limited follow-through |
| Both | Accept vendor campaign contributions |
| Both | Limited constituent pressure |

### Congressional Expertise Gaps

**Why Congress Doesn't Act**

| Factor | Effect |
|--------|--------|
| Technical complexity | Members don't understand issues |
| No crisis narrative | Problems diffuse, not dramatic |
| Industry employment | Jobs in districts |
| Lobbying resources | Industry outspends advocates |
| Competing priorities | Healthcare cost dominates |

## Cultural Causes

### Medicine's Paper-Era Mental Models

**Persistent Paradigms**

| Paper-Era Model | Digital Implication |
|-----------------|---------------------|
| "My patient" | Data sharing as loss of control |
| Paper chart as artifact | Record as legal document |
| Dictation workflow | EHR typing as burden |
| Memory and judgment | Decision support as threat |
| Autonomy | Standardization as constraint |

### Risk Aversion in Healthcare

**Conservative Adoption Culture**

| Factor | Effect |
|--------|--------|
| Patient safety emphasis | Change seen as risk |
| Regulatory burden | New technology requires compliance |
| Liability concerns | Familiar systems are "known" risk |
| Institutional inertia | "We've always done it this way" |
| Implementation trauma | Bad experiences with technology |

### Digital Divide in Medicine

**Generational and Training Gaps**

| Cohort | Typical Attitude |
|--------|------------------|
| Digital natives (residents) | Expect modern interfaces |
| Mid-career physicians | Adapted but frustrated |
| Late-career physicians | Often resistant |
| Nurses | Varies widely |
| Administrative staff | Often undertrained |

## Interconnected Causes

### The Self-Reinforcing System

```text
Vendor Lock-In
      ↓
Limited Competition
      ↓
No Pressure for Interoperability
      ↓
Proprietary Data Formats
      ↓
Switching Costs Increase
      ↓
Vendor Lock-In (cycle)
```

### Feedback Loops

**Documentation Burden Loop**

| Phase | Dynamic |
|-------|---------|
| Compliance requirements | More documentation needed |
| EHR enables documentation | Templates proliferate |
| Copy-paste available | Notes bloat |
| More data in record | Harder to find relevant info |
| More click burden | Clinician frustration |
| Demand for improvement | Vendors add features |
| More complexity | More documentation burden |

**Market Concentration Loop**

| Phase | Dynamic |
|-------|---------|
| Large vendor gains share | Network effects strengthen |
| More data in network | Value of joining increases |
| Referral preferences | Physicians refer within network |
| Training investments | Staff skilled in dominant system |
| New entrant barriers | Hard to compete |
| Acquisitions | Large vendor acquires innovators |
| More concentration | Cycle continues |

## Why Reform Is Difficult

### Beneficiaries of Status Quo

| Beneficiary | Stake |
|-------------|-------|
| Dominant vendors | Billions in revenue |
| Implementation consultants | Large vendor expertise |
| Hospital IT departments | Current relationships |
| Health system executives | Risk of change |
| Billing/coding industry | Complexity creates jobs |

### Diffuse Harm

| Harmed Party | Challenge |
|--------------|-----------|
| Patients | Don't know what's possible |
| Clinicians | Burned out but not organized |
| Taxpayers | Invisible cost |
| New entrants | No market access, no voice |
| Public health | Underfunded, understaffed |

### Complexity Barrier to Action

| Factor | Effect |
|--------|--------|
| Technical complexity | Hard to explain to policymakers |
| Diffuse accountability | No single villain |
| Gradual harm | No acute crisis |
| Success metrics unclear | Hard to measure improvement |
| Incumbent expertise | Industry defines "solutions" |

## Related Topics

- [Stakeholders](05-stakeholders.md) - Who benefits and loses
- [Opposition](06-opposition.md) - Why reform is blocked
- [Healthcare: Root Causes](../04-root-causes.md) - Broader healthcare dynamics

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
