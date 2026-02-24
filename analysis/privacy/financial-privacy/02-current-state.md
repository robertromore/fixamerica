---
freshness:
  last-reviewed: 2026-02-20
  data-year: 2025
  review-cycle: 6
  sections:
    - name: "Federal Regulatory Framework"
      data-year: 2024-2025
    - name: "Fintech and Digital Payments"
      data-year: 2024-2025
    - name: "Government Financial Surveillance"
      data-year: 2024-2025
    - name: "Key Statistics"
      data-year: 2024-2025
notes:
  - Update after any CFPB rulemaking on open banking or financial data rights.
  - Monitor FinCEN beneficial ownership registry and BSA reform efforts.
  - Track IRS Form 1099-K threshold implementation for 2026 tax year.
sources:
  count: 14
  verified: 2026-02-20
  broken: 0
---

# Financial Privacy: Current State

## Federal Regulatory Framework

### Gramm-Leach-Bliley Act (GLBA)

The GLBA, enacted in 1999, is the primary federal financial privacy law. It requires financial institutions to provide privacy notices to customers and allows consumers to opt out of some information sharing with non-affiliated third parties.

**GLBA Privacy Requirements**

| Requirement | Detail | Effectiveness |
|-------------|--------|---------------|
| Privacy notices | Annual notice describing information-sharing practices | Rarely read; average consumer receives dozens per year |
| Opt-out right | Consumer can opt out of sharing with non-affiliated third parties | Fewer than 5% exercise this right (GAO, 2023) |
| Information sharing exceptions | Sharing for joint marketing, affiliates, and service providers exempt from opt-out | Exceptions swallow the rule; most sharing continues |
| Safeguards Rule | Requires information security programs | Updated in 2023 with more specific requirements |
| Preemption | Preempts some state privacy laws for financial institutions | Limits state-level innovation |

**Key Limitations**

- Opt-out model places burden on consumers, who rarely act
- Affiliate sharing exempt: large financial conglomerates share data freely among subsidiaries
- Joint marketing arrangements exempt: banks share customer data with marketing partners
- No private right of action for privacy violations
- Privacy notices are legally dense and functionally unreadable

### Fair Credit Reporting Act (FCRA)

The FCRA, enacted in 1970 and amended by the Fair and Accurate Credit Transactions Act (FACTA) in 2003, regulates consumer reporting agencies (CRAs) and the use of credit data.

**FCRA Framework**

| Provision | Requirement | Current Status |
|-----------|-------------|----------------|
| Permissible purpose | Credit reports may only be obtained for specified purposes (credit, employment, insurance, etc.) | Broadly interpreted; many entities qualify |
| Consumer access | Free annual credit report from each bureau | AnnualCreditReport.com provides access |
| Dispute rights | Consumers can dispute inaccurate information | Reinvestigation process often cursory (CFPB reports, 2023) |
| Adverse action notice | Must notify consumers when credit data causes adverse action | Compliance inconsistent |
| Accuracy requirements | CRAs and furnishers must maintain accurate information | 25-30% of reports contain errors (FTC study, 2012; conditions persist per CFPB) |
| Security freeze | Consumers can freeze credit to prevent new account openings | Free since 2018 (Economic Growth Act) |

**Key Limitations**

- Credit bureaus (Equifax, Experian, TransUnion) operate as for-profit companies with consumers as the product, not the customer
- Credit data used far beyond original lending purposes: employment screening, tenant screening, insurance pricing, utility deposits
- Dispute resolution favors furnishers over consumers
- Equifax breach (2017, 147 million records) demonstrated massive security failures; penalty was modest relative to harm

### Bank Secrecy Act / Anti-Money Laundering (BSA/AML)

The BSA, enacted in 1970 and significantly expanded by the USA PATRIOT Act (2001), creates a mass financial surveillance system.

**BSA/AML Reporting Requirements**

| Report Type | Trigger | Annual Volume | Source |
|-------------|---------|---------------|--------|
| Currency Transaction Reports (CTRs) | Cash transactions over $10,000 | 21+ million | FinCEN (2024) |
| Suspicious Activity Reports (SARs) | Suspected illegal activity | 4.6+ million | FinCEN (2024) |
| Reports of Foreign Bank and Financial Accounts (FBARs) | Foreign accounts over $10,000 | 1.5+ million | FinCEN (2024) |
| Currency and Monetary Instrument Reports (CMIRs) | Cross-border currency transport over $10,000 | 200,000+ | FinCEN (2024) |

**Effectiveness Questions**

- FinCEN processes millions of reports annually but the conviction rate for money laundering remains low relative to volume
- Estimated 1-2% of global money laundering is intercepted (UNODC, 2024)
- BSA/AML compliance costs the financial industry $46+ billion annually (LexisNexis, 2024)
- Overreporting is incentivized: institutions file "defensive SARs" to avoid penalties
- Disproportionate impact on low-income communities and immigrants who use cash and remittances

### Right to Financial Privacy Act (RFPA)

The RFPA, enacted in 1978 in response to *United States v. Miller* (1976), provides limited protections against government access to financial records.

**RFPA Protections**

| Protection | Detail | Limitation |
|------------|--------|------------|
| Notice requirement | Government must notify customer of records request | Numerous exceptions, including national security |
| Subpoena, summons, or warrant | Government must use legal process | Administrative subpoenas have low threshold |
| Delay of disclosure | Customer can challenge in court | Short timeline for challenges |
| Covered institutions | Banks, savings institutions, credit card issuers, credit unions | Does not cover fintech apps, payment processors, or data brokers |

**Key Limitations**

- Does not cover financial technology companies, payment apps, or cryptocurrency exchanges
- National security exception effectively eliminates protections for intelligence investigations
- Government purchases of commercial financial data bypass RFPA entirely
- Does not apply to state and local government

---

## Fintech and Digital Payments

### The Fintech Privacy Gap

Financial technology companies occupy an ambiguous regulatory space for privacy purposes:

| Entity Type | Examples | GLBA Coverage | RFPA Coverage | FCRA Coverage |
|-------------|----------|---------------|---------------|---------------|
| Traditional banks | Chase, Bank of America, Wells Fargo | Yes | Yes | Indirect (as furnishers) |
| Credit unions | Navy Federal, BECU | Yes | Yes | Indirect |
| Neobanks | Chime, Varo, SoFi | Varies (depends on charter/partner bank) | Varies | Indirect |
| Payment apps | Venmo, Cash App, Zelle, PayPal | Partial (as money transmitters) | Generally no | Generally no |
| Buy-now-pay-later | Affirm, Klarna, Afterpay | Partial | No | Some reporting |
| Cryptocurrency exchanges | Coinbase, Kraken, Gemini | BSA applies; GLBA varies | Generally no | No |
| Personal finance apps | Mint, Plaid, Rocket Money | Generally no (data aggregators) | No | No |
| Robo-advisors | Wealthfront, Betterment | Yes (as investment advisers) | Varies | No |

**Data Collection by Fintech**

Fintech apps collect data that traditional banks also hold but with fewer regulatory constraints:

- Full transaction histories (what you buy, where, when, from whom)
- Income and employment data
- Account balances and financial health indicators
- Social connections (Venmo's public-by-default transaction feed)
- Location data from mobile devices
- Device and behavioral data for fraud prevention (and marketing)

### Open Banking and Consumer Financial Data

**CFPB Section 1033 Rulemaking**

The CFPB's rulemaking under Section 1033 of the Dodd-Frank Act aims to establish consumer rights to access and share their financial data with authorized third parties.

| Aspect | Status (2025) |
|--------|---------------|
| Proposed rule | Issued October 2023 |
| Final rule | Issued October 2024 |
| Compliance timeline | Phased: largest institutions first (2026); smallest last (2030) |
| Key provisions | Consumer right to access; authorized third-party access via API; data security requirements; limitations on secondary use |
| Privacy implications | Empowers consumers but creates new data exposure channels |
| Industry response | Banks cautious; fintech supportive; data aggregators mixed |

**Privacy Concerns with Open Banking**

- Third-party access to full financial transaction histories
- Secondary use of financial data beyond consumer's intended purpose
- Liability unclear when data is misused by authorized third parties
- Consent revocation and data deletion practices vary
- Screen scraping (credential sharing) creates security risks even as API-based access improves

### Cryptocurrency and Financial Privacy

| Issue | Current State |
|-------|---------------|
| Exchange KYC/AML | Major exchanges (Coinbase, Kraken) comply with BSA; collect extensive identity data |
| IRS reporting | Cryptocurrency broker reporting requirements (Infrastructure Investment and Jobs Act, 2021); effective for transactions beginning 2025 |
| Blockchain surveillance | Companies (Chainalysis, Elliptic) track blockchain transactions for law enforcement; FinCEN contracts |
| Privacy coins | Monero, Zcash offer enhanced privacy; some exchanges delisting due to regulatory pressure |
| Self-custody | Non-custodial wallets not directly subject to KYC but face increasing regulatory scrutiny |
| CBDC | Federal Reserve exploring digital dollar; significant privacy concerns about government transaction visibility |

---

## Government Financial Surveillance

### FinCEN and Financial Intelligence

FinCEN operates the largest financial intelligence database in the United States:

**FinCEN Database Scale**

| Metric | Value | Source |
|--------|-------|--------|
| Total BSA filings in database | 400+ million records | FinCEN (2024) |
| Agencies with access | 500+ federal, state, and local agencies | FinCEN (2024) |
| Database queries per year | Millions | FinCEN (2024) |
| Employees | Approximately 300 | Treasury budget documents |

**FinCEN Leaks (2020)**: The International Consortium of Investigative Journalists published leaked SARs showing that major banks filed reports about suspicious transactions totaling $2+ trillion while continuing to process them, raising questions about the effectiveness of the entire BSA/AML framework.

### IRS Information Reporting

The IRS receives extensive financial information through mandatory reporting:

| Form | Trigger | Volume (annually) |
|------|---------|-------------------|
| 1099-INT | Interest income over $10 | Hundreds of millions |
| 1099-DIV | Dividend income | Hundreds of millions |
| 1099-K | Third-party payment network transactions (threshold: $600 per 2021 law; enforcement delayed) | Growing significantly |
| 1099-B | Broker transactions | Hundreds of millions |
| FBAR | Foreign accounts over $10,000 | 1.5+ million |
| Form 8938 | Foreign financial assets (FATCA) | Hundreds of thousands |

**1099-K Controversy**: The American Rescue Plan Act (2021) lowered the Form 1099-K reporting threshold from $20,000/200 transactions to $600. Implementation has been repeatedly delayed (IRS Notice 2023-74; IRS IR-2024-299), with the $600 threshold expected to take effect for tax year 2026. Critics argue it subjects millions of casual sellers and gig workers to invasive reporting.

### Government Purchase of Financial Data

Government agencies increasingly purchase commercial financial data, bypassing traditional legal process:

| Agency | Practice | Source |
|--------|----------|--------|
| IRS | Purchased location data from data brokers to identify tax evaders | Sen. Wyden investigation (2021) |
| ICE/CBP | Purchased financial transaction data for immigration enforcement | Georgetown Law Center on Privacy and Technology (2022) |
| DEA | Purchased bulk financial transaction data | Wall Street Journal investigation (2023) |
| State/local | Purchased credit header data and financial profiles for investigations | ACLU reports (2023) |

---

## Financial Data Brokers

### Industry Structure

Financial data brokers operate at the intersection of credit reporting, marketing data, and investigative services:

| Broker Type | Examples | Data Sources | Customers |
|-------------|----------|-------------|-----------|
| Credit bureaus (also brokers) | Equifax, Experian, TransUnion | Creditors, public records, data furnishers | Lenders, insurers, employers, landlords |
| Financial marketing data | Acxiom, Oracle Data Cloud, Epsilon | Transaction data, public records, surveys | Marketers, financial services companies |
| Investigative/risk | LexisNexis Risk Solutions, Thomson Reuters CLEAR | Court records, financial filings, property records | Law enforcement, insurance, legal |
| Alternative credit data | SageStream, PRBC | Utility payments, rent, telecom | Lenders seeking alternative credit assessment |

### Use of Financial Data Beyond Lending

Financial data is increasingly used for purposes far removed from the original credit context:

| Use | Description | Privacy Concern |
|-----|-------------|-----------------|
| Employment screening | Credit checks for job applicants | Financial difficulties correlate with poverty, not character; disproportionate impact on minorities |
| Tenant screening | Credit and eviction records for rental applicants | Errors in reports can prevent housing access |
| Insurance pricing | Credit-based insurance scores | Penalizes financial misfortune; racial disparities |
| Utility deposits | Credit scores determine deposit requirements | Regressive impact on low-income consumers |
| Marketing targeting | Financial behavior predicts purchasing | Manipulative and discriminatory targeting possible |
| Government investigations | Financial profiles for law enforcement | Warrantless surveillance through data purchases |

---

## State Law Developments

| State | Key Financial Privacy Provision | Year |
|-------|--------------------------------|------|
| California | CCPA/CPRA covers financial information not already subject to GLBA | 2018/2020 |
| Vermont | Data broker registration includes financial data brokers | 2018 |
| New York | SHIELD Act requires data security for financial information | 2019 |
| Illinois | Employee Credit Privacy Act restricts employer credit checks | 2011 |
| Nevada | Financial data included in state privacy law | 2023 |
| Colorado | Credit-based insurance scoring restrictions | 2024 |

**GLBA preemption issue**: The GLBA's preemption provision limits state authority over financial institutions, creating tension with state privacy laws. The CFPB and state AGs have debated the scope of this preemption.

---

## Summary

Financial privacy in the United States is governed by an outdated patchwork of laws designed for traditional banking that have not kept pace with digital payments, fintech, open banking, or data brokerage. The opt-out model of GLBA is functionally ineffective. The BSA/AML system generates mass surveillance of financial transactions with questionable effectiveness. The third-party doctrine eliminates Fourth Amendment protection for bank records. Credit bureaus hold enormous power over Americans' lives with limited accountability. Government agencies purchase commercial financial data to avoid legal process requirements. Reform requires updating every major piece of the financial privacy framework while addressing new challenges from fintech, cryptocurrency, and open banking.

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
- Up: [Overview](01-overview.md)
