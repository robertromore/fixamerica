---
freshness:
  last-reviewed: 2025-01-12
  data-year: 2024
  review-cycle: 6
  sections:
    - name: "The Problem Today"
      data-year: 2024
    - name: "Current Threat Landscape"
      data-year: 2024
    - name: "Current Defenses"
      data-year: 2024
    - name: "Impact Analysis"
      data-year: 2024
notes:
  - Watch post-2024 election audits/grant updates for the next round of security stats.
  - Monitor CISA/FEC data and any new federal funding announcements planned for FY26.
sources:
  count: 7
  verified: 2025-01-12
  broken: 0
---

# Election Security: Current State

## The Problem Today (2024 snapshot)

### A Vulnerable Infrastructure

American elections are administered by approximately 10,000 jurisdictions across 50 states, each with different equipment, procedures, and resources. This decentralization provides some resilience against centralized attacks but creates vast inconsistency in security posture.

**The Attack Surface**

```text

┌─────────────────────────────────────────────────────────────┐
│              ELECTION INFRASTRUCTURE ATTACK SURFACE          │
└─────────────────────────────────────────────────────────────┘
                              │
    ┌─────────────────────────┼─────────────────────────────┐
    ▼                         ▼                             ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────────┐
│ VOTING        │    │ VOTER         │    │ INFORMATION       │
│ SYSTEMS       │    │ REGISTRATION  │    │ ECOSYSTEM         │
│               │    │               │    │                   │
│ Voting machines│   │ Databases     │    │ Social media      │
│ Tabulators    │    │ E-pollbooks   │    │ News outlets      │
│ Ballot marking│    │ Online portals│    │ Official websites │
│ Results       │    │ DMV links     │    │ Candidate info    │
│ reporting     │    │               │    │                   │
└───────────────┘    └───────────────┘    └───────────────────┘

```text

### Voting Machine Landscape

**Current Equipment by Type**

| Equipment Type | Jurisdictions Using | Security Level | Auditability |
|----------------|---------------------|----------------|--------------|
| Hand-marked paper ballots | ~75% | Highest | Full |
| Ballot marking devices (BMD) | ~60% | Medium | Depends on design |
| DRE with VVPAT | ~10% | Medium | Limited |
| Paperless DRE | ~5% | Lowest | None |

*Note: Percentages reflect share of jurisdictions offering each equipment type; many jurisdictions use multiple types (e.g., hand-marked ballots as default with BMDs for accessibility). Source: Verified Voting, 2024.*

**Progress Since 2016**

| Metric | 2016 | 2024 | Change |
|--------|------|------|--------|
| States with paper ballot mandate | 32 | 47 | +15 |
| Jurisdictions using paperless DRE | ~20% | ~5% | -15% |
| States requiring post-election audits | 33 | 45 | +12 |
| States using risk-limiting audits | 2 | 12 | +10 |

*Source: Verified Voting, NCSL, 2024.*

### Key Statistics (2024 snapshot)

**Voting System Security**

| Issue | Status |
|-------|--------|
| Average voting machine age | 10+ years |
| Machines running obsolete software | ~40% |
| Jurisdictions with inadequate cybersecurity | ~60% |
| Cost to replace aging equipment nationwide | $1+ billion |

*Source: Brennan Center for Justice, 2024.*

**Federal Investment (FY 2018-2024)**

| Funding Source | Amount | Adequacy |
|----------------|--------|----------|
| HAVA funds (2018-2024) | $1.2 billion | Insufficient |
| Annual election security grants | $400-450 million | Below need |
| CISA election security budget | ~$200 million | Growing |

*Source: EAC, CISA, 2024.*

**Known Vulnerabilities**

| Vulnerability | Status | Risk |
|---------------|--------|------|
| Voting machines with known exploits | Many identified | High |
| Internet connectivity in some systems | Present | Critical |
| Supply chain risks | Unaddressed | High |
| Insider threat protections | Inconsistent | Medium |
| Results transmission security | Varies | High |

*Source: CISA, Brennan Center, 2024.*

## Current Threat Landscape

### Foreign Adversaries

**Nation-State Capabilities**

| Actor | Documented Activity | Capability Level |
|-------|---------------------|------------------|
| Russia | 2016 DNC hack, state targeting, disinformation | Sophisticated |
| China | Voter data interest, influence operations | Sophisticated |
| Iran | Voter intimidation emails (2020), influence ops | Moderate |
| North Korea | Financial crimes, potential disruption | Moderate |

**Types of Foreign Operations**

| Operation Type | Example | Impact |
|----------------|---------|--------|
| System probing | All 50 states scanned (2016) | Intelligence gathering |
| Database targeting | Illinois, Arizona breaches (2016) | Data theft potential |
| Information operations | Social media manipulation | Opinion manipulation |
| Hack and leak | DNC, Podesta emails | Campaign disruption |

*Source: Senate Intelligence Committee Reports, 2019-2020; CISA.*

### Domestic Threats

**Internal Actors**

| Threat | Examples | Mitigation |
|--------|----------|------------|
| Corrupt election officials | Tina Peters (CO), 2020 access breaches | Background checks, oversight |
| Poll workers | Equipment tampering potential | Training, supervision |
| Vendors | Insider access to systems | Contract requirements, audits |
| Contractors | Election night system access | Access controls |

**Election Denial Movement**

| Activity | Impact |
|----------|--------|
| Harassment of election officials | Mass resignations, experience loss |
| Equipment access attempts | Security breaches (e.g., Coffee County, GA) |
| False fraud claims | Public confidence erosion |
| Obstructing certification | Delayed results, legal chaos |

### Technological Threats

**Emerging Risks**

| Technology | Threat | Current Defense |
|------------|--------|-----------------|
| AI-generated content | Deepfakes, synthetic media | Limited detection |
| AI-powered disinformation | Scale, personalization | Inadequate |
| Quantum computing (future) | Encryption breaking | Not yet prepared |
| Supply chain attacks | Compromised components | Insufficient verification |

## Current Defenses

### Federal Infrastructure

**CISA Election Security Services**

| Service | Description | Uptake (2024) |
|---------|-------------|--------|
| Vulnerability scanning | Free system assessment | ~95% of states |
| Physical security reviews | Site assessments | ~80% of states |
| Incident response | 24/7 support | Available to all |
| Tabletop exercises | Scenario training | Growing participation |
| Information sharing | Threat intelligence | All states connected |

*Source: CISA, 2024.*

**Election Assistance Commission (EAC)**

| Function | Status |
|----------|--------|
| Voting system certification | Active but slow |
| Best practices guidance | Published |
| Grant administration | Ongoing |
| Clearinghouse function | Operational |

### State and Local Measures

**Common Security Practices (2024 snapshot)**

| Practice | Adoption Rate |
|----------|---------------|
| Multi-factor authentication | ~70% of states |
| Intrusion detection systems | ~60% of election offices |
| Security awareness training | ~50% of election workers |
| Incident response plans | ~45% of jurisdictions |
| Regular security assessments | ~40% of jurisdictions |

*Source: CISA, EAC, 2024.*

**Audit Implementation (2024 snapshot)**

| Audit Type | States Requiring |
|------------|------------------|
| Any post-election audit | 45 |
| Risk-limiting audit | 12 |
| Hand count audit | 28 |
| Automatic recount threshold | 43 |

*Source: NCSL, Verified Voting, 2024.*

## Impact Analysis

### On Election Administration

**Resource Strain**

| Challenge | Impact |
|-----------|--------|
| Funding shortfalls | Deferred upgrades, aging equipment |
| Staffing losses | 30%+ turnover since 2020 |
| Threat complexity | Overwhelming for small jurisdictions |
| Compliance burden | Time diverted from core functions |

**Official Burnout**

| Issue | Statistics |
|-------|------------|
| Threats received | 1 in 3 officials report threats |
| Resignations since 2020 | Record levels nationwide |
| Experience loss | Decades of expertise departing |
| Recruitment difficulty | Struggle to fill positions |

### On Voter Confidence

**Public Perception (2024 Polling)**

| Metric | Finding |
|--------|---------|
| Trust elections "very secure" | ~30% |
| Believe fraud is major problem | ~35% |
| Confidence in local elections | Higher than national |
| Partisan gap in confidence | 40+ points |

*Source: Pew Research Center, Gallup, 2024.*

**Consequences of Low Confidence**

| Outcome | Effect |
|---------|--------|
| Lower turnout | Cynicism reduces participation |
| Contested results | Litigation, certification delays |
| Civil unrest | January 6 as extreme example |
| International perception | Weakened democratic standing |

### On National Security

**Strategic Implications**

| Area | Impact |
|------|--------|
| Foreign influence | Adversaries exploit divisions |
| Alliance credibility | Partners question U.S. stability |
| Domestic extremism | Election denial fuels violence |
| Policy continuity | Transition uncertainty |

## Recent Developments

### 2020 Election Security

**What Worked**

| Success | Description |
|---------|-------------|
| Paper ballot expansion | Record paper trail coverage |
| CISA coordination | Effective threat sharing |
| Successful defense | No evidence of vote manipulation |
| Audit verification | Results confirmed where audited |

**What Didn't Work**

| Failure | Description |
|---------|-------------|
| Misinformation tsunami | False claims spread faster than facts |
| Official harassment | Unprecedented threats and pressure |
| Equipment breaches | Multiple unauthorized access incidents |
| Certification challenges | Attempts to overturn legitimate results |

### 2022 and 2024 Trends

**Positive Developments**

| Development | Significance |
|-------------|--------------|
| More states adopt RLAs | Stronger audit framework |
| CISA capacity growth | More support available |
| Election official training | Improved preparedness |
| Bipartisan security bills | Some Congressional progress |

**Concerning Trends**

| Trend | Concern |
|-------|---------|
| AI-generated content | New disinformation vector |
| Continued official departures | Experience drain |
| Politicization of security | Reform blocked by partisanship |
| Underfunding | Needs exceed resources |

## Key Takeaways

1. **Progress has been made**: Paper ballot coverage and audit capabilities have expanded significantly since 2016

2. **Threats are evolving**: Adversaries and domestic actors continue to develop new attack vectors

3. **Funding is inadequate**: Federal investment falls far short of actual security needs

4. **Officials are under siege**: Threats and harassment are driving experienced workers away

5. **Public confidence is fragile**: Misinformation has damaged trust regardless of actual security

6. **Decentralization is double-edged**: Provides resilience but creates inconsistency

7. **Bipartisanship is essential**: Security should not be partisan, but has become so

8. **Audits are critical**: Paper ballots plus risk-limiting audits provide strong verification

## Sources

### Voting Equipment and Security

- Verified Voting. "The Verifier: Voting Equipment in the United States," 2024. <https://verifiedvoting.org/verifier/>
- Brennan Center for Justice. "Voting Machines at Risk," 2024. <https://www.brennancenter.org/>
- NCSL. "Post-Election Audits," 2024. <https://www.ncsl.org/elections-and-campaigns/post-election-audits>

### Federal Programs

- CISA. "Election Infrastructure Security," 2024. <https://www.cisa.gov/topics/election-security>
- Election Assistance Commission (EAC). "Election Security Grants," 2024. <https://www.eac.gov/>

### Threat Intelligence

- U.S. Senate Select Committee on Intelligence. "Russian Active Measures Campaigns and Interference in the 2016 U.S. Election," Volumes I-V, 2019-2020.
- CISA. "Foreign Threats to the 2024 U.S. Elections," 2024.

### Public Opinion

- Pew Research Center. "Election Security and Public Confidence," 2024.
- Gallup. "Confidence in Election Integrity," 2024.

## Related Topics

- [History](03-history.md) - How election security evolved
- [Root Causes](04-root-causes.md) - Why vulnerabilities persist
- [Voting Rights: Current State](../voting-rights/02-current-state.md) - Access considerations
- [Media and Information: Current State](../media-and-information/02-current-state.md) - Misinformation landscape

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
