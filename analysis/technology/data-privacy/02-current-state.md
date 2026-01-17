# Data Privacy: Current State

## Overview

Americans live in an environment of pervasive data collection with minimal legal protection. Every digital interaction generates data that is collected, analyzed, shared, and sold, often without meaningful consent or awareness. The current legal framework—a patchwork of sector-specific federal laws and varying state laws—leaves most data practices unregulated.

## Data Collection Landscape

### Who Collects Data

| Category | Examples | Data Types |
|----------|----------|------------|
| **Platforms** | Google, Meta, Amazon, Apple | Everything |
| **Apps** | Social, gaming, utility apps | Behavior, location, contacts |
| **Websites** | Most commercial sites | Browsing, purchases |
| **Data brokers** | Acxiom, LexisNexis, Oracle | Aggregated profiles |
| **Retailers** | In-store and online | Purchases, loyalty data |
| **Financial** | Banks, credit cards | Transactions, credit |
| **Telecoms** | Carriers, ISPs | Location, browsing |
| **Employers** | Workplace monitoring | Productivity, communications |
| **Government** | Various agencies | Administrative, surveillance |

### Types of Data Collected

| Category | Specific Data |
|----------|---------------|
| **Identity** | Name, SSN, DOB, address, phone |
| **Behavioral** | Browsing, purchases, app usage |
| **Location** | GPS, cell tower, WiFi, Bluetooth |
| **Communications** | Email, messages, calls |
| **Biometric** | Face, fingerprint, voice |
| **Health** | Conditions, medications, fitness |
| **Financial** | Income, spending, credit |
| **Social** | Connections, interests, affiliations |
| **Inferred** | Predictions about you |

### Collection Scale

| Metric | Estimate |
|--------|----------|
| Data points per person (data brokers) | 1,500+ |
| Location pings per day (smartphone) | 5,000+ |
| Third-party trackers per website (average) | 10+ |
| Companies with data on average person | 4,000+ |
| Data broker records | 3+ billion profiles |

## Data Broker Industry

### Market Overview

| Metric | Value |
|--------|-------|
| Industry revenue | $250+ billion |
| Number of brokers | 4,000+ |
| Top players | Acxiom, Experian, Oracle, LexisNexis |
| Records per major broker | Billions |

### Data Broker Types

| Type | Function | Examples |
|------|----------|----------|
| **Marketing data** | Consumer targeting | Acxiom, Oracle |
| **People search** | Individual lookup | Spokeo, BeenVerified |
| **Risk assessment** | Fraud, credit | LexisNexis, Experian |
| **Location data** | Movement tracking | Venntel, Babel Street |
| **Social data** | Social media aggregation | Various |

### How Data Flows

```
Original Collection (apps, websites, purchases)
         ↓
Aggregation (data brokers combine sources)
         ↓
Enrichment (add inferred data)
         ↓
Segmentation (categorize people)
         ↓
Sale/Licensing (to buyers)
         ↓
Use (advertising, decisions, surveillance)
```

## Current Legal Framework

### Federal Laws

| Law | Year | Coverage | Limitations |
|-----|------|----------|-------------|
| **HIPAA** | 1996 | Health providers | Narrow scope; excludes apps |
| **FCRA** | 1970 | Credit reporting | Limited to credit |
| **COPPA** | 1998 | Children under 13 | Age 13+unprotected |
| **GLBA** | 1999 | Financial institutions | Limited opt-out only |
| **FERPA** | 1974 | Educational records | Excludes ed tech |
| **VPPA** | 1988 | Video rental | Extremely narrow |
| **ECPA** | 1986 | Electronic communications | Outdated, weak |
| **CCPA/CPRA** | 2018/2020 | California residents | State only |

### Gaps in Federal Law

| Gap | Consequence |
|-----|-------------|
| No general privacy law | Most data unprotected |
| No data minimization | Collect everything |
| No purpose limitation | Use for any purpose |
| No sale restrictions | Sell freely |
| Weak enforcement | Limited penalties |
| No private right of action | Can't sue in most cases |

### State Laws

| State | Law | Effective | Key Features |
|-------|-----|-----------|--------------|
| California | CPRA | 2023 | Comprehensive; agency created |
| Virginia | CDPA | 2023 | Business-friendly |
| Colorado | CPA | 2023 | Consumer rights |
| Connecticut | CTDPA | 2023 | Strong provisions |
| Utah | UCPA | 2023 | Business-friendly |
| 10+ more | Various | 2024-2025 | Varying strength |

### State Law Coverage

| Element | Strong States | Weak States |
|---------|---------------|-------------|
| Consumer rights | CA, CO, CT | UT, IA |
| Private enforcement | CA (limited) | Most states |
| Opt-out of sale | All | All |
| Sensitive data | Most | Most |
| Data minimization | Some | Few |

## FTC Enforcement

### Current Authority

| Tool | Scope | Limitation |
|------|-------|------------|
| Section 5 (unfair/deceptive) | Broad but case-by-case | No rulemaking until recently |
| COPPA enforcement | Children under 13 | Narrow |
| FCRA enforcement | Credit | Limited scope |
| Gramm-Leach-Bliley | Financial | Limited scope |

### Recent Enforcement

| Case | Year | Issue | Outcome |
|------|------|-------|---------|
| Meta (Cambridge Analytica) | 2019 | Consent violations | $5B fine |
| Zoom | 2020 | Security claims | Settlement |
| X-Mode (Outlogic) | 2024 | Location data sale | $1.75M fine |
| Various | Ongoing | Dark patterns, data | Multiple cases |

### Enforcement Limitations

| Limitation | Effect |
|------------|--------|
| Resource constraints | Few cases possible |
| Case-by-case | No general rules |
| Fines insufficient | Cost of doing business |
| No private enforcement | Individuals can't sue |
| Political interference | Commissioners divided |

## Industry Practices

### Consent Mechanisms

| Practice | Reality |
|----------|---------|
| Privacy policies | Unread (97%+), unreadable (college reading level) |
| Cookie banners | Dark patterns push acceptance |
| "I agree" buttons | Bundled, take-it-or-leave-it |
| Opt-out | Buried, difficult, incomplete |
| Privacy settings | Complex, defaults favor collection |

### Dark Patterns

| Pattern | Description |
|---------|-------------|
| **Confirm-shaming** | Guilting opt-out choices |
| **Forced disclosure** | Require data for access |
| **Privacy zuckering** | Confusing settings |
| **Trick questions** | Misleading options |
| **Hidden information** | Burying privacy terms |
| **Obstruction** | Making opt-out difficult |

### Tracking Technologies

| Technology | Purpose |
|------------|---------|
| **Cookies** | Browser tracking |
| **Device fingerprinting** | Cross-browser tracking |
| **Mobile advertising IDs** | App tracking |
| **Location services** | Physical tracking |
| **Pixels/beacons** | Email, web tracking |
| **SDKs** | In-app data collection |

## Consumer Awareness and Attitudes

### Awareness Levels

| Topic | Awareness |
|-------|-----------|
| That data is collected | 95%+ |
| Extent of collection | Low |
| Who has their data | Very low |
| How data is used | Low |
| Rights available | Very low |
| How to exercise rights | Very low |

### Attitudes

| Attitude | Percentage |
|----------|------------|
| Concerned about privacy | 79% |
| Feel lack of control | 81% |
| Distrust data handling | 72% |
| Want more regulation | 70%+ |
| Read privacy policies | 3-9% |
| Actually understand them | <1% |

## Security and Breaches

### Breach Statistics

| Metric | 2023 Value |
|--------|------------|
| Reported breaches | 3,200+ |
| Records exposed | 400+ million |
| Average cost per breach | $4.5 million |
| Average time to identify | 200+ days |

### Major Recent Breaches

| Organization | Year | Records |
|--------------|------|---------|
| T-Mobile | 2023 | 37 million |
| MOVEit | 2023 | 60+ million |
| Various healthcare | 2023 | Millions |
| Government contractors | Ongoing | Varies |

## International Comparison

| Jurisdiction | Framework | Key Difference |
|--------------|-----------|----------------|
| **EU (GDPR)** | Comprehensive | Stronger rights, enforcement |
| **UK** | GDPR-derived | Similar to EU |
| **Canada** | PIPEDA | Moderate protection |
| **Brazil** | LGPD | GDPR-like |
| **US** | Patchwork | Weakest among peers |

### GDPR Advantages Over US

| Element | GDPR | US |
|---------|------|-----|
| Consent standard | Affirmative | Often implied |
| Purpose limitation | Required | Rarely |
| Data minimization | Required | Rarely |
| Right to erasure | Guaranteed | Limited |
| Private enforcement | Available | Mostly unavailable |
| Fines | Up to 4% revenue | Much lower |
| DPA resources | Substantial | Limited |

---

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Overview](01-overview.md)
