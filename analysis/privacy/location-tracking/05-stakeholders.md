# Location Tracking: Stakeholders

## Who Benefits from the Status Quo

### Location Data Brokers

**Who They Are**

- Companies that aggregate and sell location data derived from mobile apps, carriers, and connected devices
- Notable players: SafeGraph, Placer.ai, Babel Street (formerly Venntel), X-Mode Social/Outlogic, Gravy Analytics, Near Intelligence, Foursquare
- Specialty firms selling foot traffic analytics, movement pattern data, and device-level location histories

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| Multi-billion dollar revenue | Selling aggregated location data to advertisers, retailers, real estate firms, hedge funds, and government agencies |
| Government contracts | Direct sales of location data to ICE, CBP, IRS, FBI, DHS, Secret Service, and DIA |
| Low acquisition costs | Purchasing location data cheaply from app SDKs and advertising exchanges, reselling at significant markup |
| Regulatory arbitrage | Operating outside any location-specific federal regulatory framework |
| "Anonymization" defense | Claiming data is de-identified to avoid consent requirements, despite scientific evidence of re-identification |

**Level of Opposition to Reform**: **Very High**

- Location data brokerage is a core business model; regulation requiring consent would dramatically reduce data supply
- Government contracts provide stable, high-margin revenue; warrant requirements would eliminate this market
- Transparency requirements would expose practices to public scrutiny and litigation

### Advertising Technology Industry

**Who They Are**

- Demand-side platforms, supply-side platforms, and ad exchanges that process real-time bidding (RTB) data
- Location-based advertising networks
- Key players: Google (DV360), Meta, The Trade Desk, Xandr (Microsoft), and thousands of smaller ad-tech firms
- Industry associations: Interactive Advertising Bureau (IAB), Network Advertising Initiative (NAI)

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| Premium pricing for location-targeted ads | Location-targeted ads earn 2-3x the CPM of non-targeted ads |
| $32+ billion annual market | US location-targeted advertising market (eMarketer, 2024) |
| Real-time bidding data access | Every ad auction broadcasts precise device location to hundreds of companies |
| Behavioral profiling | Location history enriches user profiles for more valuable targeting |

**Level of Opposition to Reform**: **High**

- Location data is a foundational input to the digital advertising economy
- Consent requirements for location sharing would reduce available data and ad revenue
- Industry-wide infrastructure (RTB) inherently leaks location data at massive scale

### Mobile App Developers

**Who They Are**

- Developers of apps that collect location data through device permissions
- Includes navigation, weather, fitness, social media, news, gaming, and utility apps
- Companies embedding third-party SDKs that harvest location data in exchange for analytics tools or revenue

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| SDK revenue | Location data brokers pay app developers to embed SDKs that collect location data |
| Free analytics tools | SDK providers offer free analytics in exchange for access to user location data |
| Location-based features | Location data enables mapping, weather, and proximity features that drive user engagement |
| Advertising revenue | In-app advertising with location targeting generates higher revenue per impression |

**Level of Opposition to Reform**: **Moderate to High**

- Many "free" app business models depend on location data monetization
- Strict consent requirements would reduce the volume of location data available for sale or analytics
- Small developers would face compliance costs

### Wireless Carriers

**Who They Are**

- Major carriers: AT&T, Verizon, T-Mobile
- Regional carriers and MVNOs
- Trade association: CTIA (Cellular Telecommunications Industry Association)

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| Data monetization | Sale of cell-site location information (CSLI) and aggregated location analytics |
| Advertising partnerships | Location data enhances carrier advertising offerings |
| Government cooperation | Compliance with law enforcement requests maintains regulatory relationships |
| E911 infrastructure | Location capabilities serve as justification for continuous location tracking infrastructure |

**Level of Opposition to Reform**: **Moderate**

- Carriers face some regulation under ECPA but oppose expansion
- CTIA actively lobbies against stricter location privacy requirements
- Carriers benefit from legal ambiguity around CSLI retention and sharing

### Automakers and Connected Vehicle Companies

**Who They Are**

- Major automakers: GM, Ford, Toyota, Tesla, BMW, Mercedes-Benz, Honda, and others
- Connected vehicle platforms: OnStar (GM), FordPass, Tesla's data systems
- Vehicle data aggregators: Otonomo, Wejo
- Insurance telematics partners: LexisNexis Risk Solutions, Verisk

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| Revenue from data sharing | Selling driving and location data to insurers, advertisers, and analytics firms |
| Insurance partnerships | GM/LexisNexis model: vehicle data shared with insurers for premium adjustment |
| Product development | Location and driving data used to improve autonomous driving and connected features |
| Subscription revenue | Connected services generate ongoing subscription fees that depend on data collection |

**Level of Opposition to Reform**: **Moderate to High**

- 25 of 25 major automakers studied share or sell vehicle data (Mozilla Foundation, 2023)
- Connected vehicle business models increasingly depend on data monetization
- GM/LexisNexis scandal (2024) revealed extent of data sharing without clear consent

### Government Agencies

**Who They Are**

- Federal law enforcement and intelligence: ICE, CBP, FBI, DEA, IRS, Secret Service, DIA, DHS
- State and local law enforcement
- National security agencies

**What They Gain**

| Benefit | Mechanism |
|---------|-----------|
| Warrantless surveillance capability | Purchasing commercial location data avoids Fourth Amendment warrant requirements |
| Immigration enforcement | ICE/CBP track undocumented immigrants using commercial location data |
| Criminal investigations | Location data used for suspect tracking, alibis, and pattern analysis |
| Geofence capabilities | Reverse location searches identify all devices present at a location during a specific time |
| National security intelligence | DIA and other agencies use commercial location data for foreign intelligence |

**Level of Opposition to Reform**: **High**

- Government agencies have built operational capabilities around commercial location data purchases
- Warrant requirements would slow investigations and reduce access
- Agencies argue national security and public safety exceptions justify current practices

---

## Who Is Harmed by the Status Quo

### General Public

**Scale:** 270+ million smartphone users in the United States

**Harms:**

| Harm | Description |
|------|-------------|
| Loss of locational privacy | Movements tracked continuously; 200-600+ location data points generated per phone per day |
| No meaningful consent | 56% of Americans do not know apps share location with third parties; less than 9% read location privacy policies |
| Inability to opt out | Disabling location degrades phone functionality; carrier CSLI collection is unavoidable |
| Data breach exposure | Centralized location databases create catastrophic breach risks (Gravy Analytics breach, January 2025) |
| De-anonymization vulnerability | 95% of individuals identifiable from 4 data points; "anonymized" location data is not anonymous |

### Immigrants and Undocumented Individuals

**Scale:** Approximately 11 million undocumented immigrants in the United States

**Specific harms:**

- ICE and CBP purchase commercial location data from Venntel/Babel Street to track and arrest undocumented immigrants (Georgetown Law, "American Dragnet," 2022)
- Location data near border areas, immigration courts, and community organizations reveals immigration status
- Chilling effect deters immigrants from accessing health care, schools, and social services
- No warrant requirement for government purchase of commercial location data

### Reproductive Healthcare Seekers

**Scale:** 72+ million women of reproductive age; additional individuals seeking reproductive care

**Specific harms:**

- Location data near abortion clinics available for purchase by data brokers (FTC v. Kochava, 2022; SafeGraph investigation, 2022)
- Post-*Dobbs*, location data creates legal risk in states with abortion restrictions
- Data broker advertisements explicitly offered data on clinic visitors
- Geofence warrants around clinics could identify patients

### Protesters and Political Activists

**Scale:** Millions of Americans who attend protests, rallies, political meetings, and religious gatherings

**Specific harms:**

- Geofence warrants used to identify protest attendees (Kenosha BLM protest, 2021)
- Location data reveals attendance at political rallies, exposing political affiliation
- Chilling effect on First Amendment assembly and speech
- Law enforcement use of location data for protest surveillance without individualized suspicion

### Domestic Violence Survivors

**Scale:** 10+ million adults experience domestic violence annually (CDC)

**Specific harms:**

- AirTags, Tile trackers, and phone-based stalking used by abusers to locate victims (National Network to End Domestic Violence, 2023)
- People-search sites expose shelter locations through aggregated location data
- Shared device plans allow abusers to monitor victims' movements
- Tracker detection tools are imperfect and unavailable to many victims

### LGBTQ+ Individuals

**Scale:** Estimated 20+ million LGBTQ+ adults in the United States

**Specific harms:**

- Location data at LGBTQ+ venues available for purchase from data brokers
- In hostile jurisdictions, location-based identification creates safety risks
- Gender-affirming care facility visits trackable through location data
- Duke University study (2023) confirmed sensitive location data available for purchase

### Military and Intelligence Personnel

**Scale:** 1.3+ million active duty service members plus intelligence community personnel

**Specific harms:**

- Commercial location data used to track movements at NSA, CIA, Pentagon, and classified facilities (*New York Times*, 2024)
- Foreign adversaries can purchase same commercial location data available domestically
- Service members' home locations, routines, and family connections exposed
- National security implications of commercially available tracking of defense personnel

### Communities of Color

**Scale:** Disproportionate impact on Black, Latino, and other minority communities

**Specific harms:**

- Predictive policing algorithms incorporate location data, reinforcing over-policing of minority neighborhoods
- Location-based insurance pricing (connected vehicles) can function as proxy for racial discrimination
- Foot traffic analytics used in real estate can reinforce redlining patterns (Brookings, 2023)
- Geofence warrants disproportionately deployed in communities of color

---

## Institutional Stakeholders

### Technology Platform Companies

**Position:** Mixed

- Apple has implemented App Tracking Transparency (ATT), significantly reducing iOS location tracking; positions as privacy leader
- Google eliminated Sensorvault for geofence warrants (December 2023) but remains largest collector of location data through Android and Maps
- Meta collects location data through Instagram, Facebook, and WhatsApp; opposes strict location regulation
- Microsoft relatively less exposed on consumer location but operates advertising platform

### Retail and Real Estate Industries

**Position:** Generally oppose stronger regulation

- Use foot traffic analytics from location data brokers for site selection, competitive intelligence, and customer behavior analysis
- Location data powers retail analytics platforms (Placer.ai, SafeGraph)
- Real estate developers use foot traffic data for property valuation and investment decisions
- Oppose consent requirements that would reduce available foot traffic data

### Insurance Industry

**Position:** Oppose restrictions on location data use

- Auto insurers use driving data from connected vehicles for premium adjustment
- Life and health insurers explore location-derived health inferences
- GM/LexisNexis scandal (2024) revealed widespread data sharing between automakers and insurers
- Oppose transparency and consent requirements for location-based underwriting

### Academic Researchers

**Position:** Support privacy with research exceptions

- Use aggregated location data for epidemiology, urban planning, transportation, and social science research
- SafeGraph provided location data to researchers during COVID-19 for public health analysis
- Support de-identification standards but oppose blanket restrictions on research use
- Advocate for research exceptions in any location privacy legislation

---

## Government Stakeholders

### Federal Trade Commission

**Role:** Primary federal enforcement on commercial location data practices

**Position:**

- Aggressively pursuing enforcement against location data brokers (FTC v. Kochava, 2022; FTC v. X-Mode/Outlogic, 2022; FTC v. InMobi, 2016)
- Advocates for comprehensive federal privacy legislation with location data provisions
- Limited by need to prove unfairness or deception; lacks prescriptive location privacy authority
- Supports private right of action and increased enforcement resources

### State Attorneys General

**Role:** State-level enforcement and policy leadership

**Position:**

- Several states (California, Illinois, New York, Washington) actively enforce location privacy
- Support state authority and oppose federal preemption of stronger state protections
- Coalition actions against location data brokers gaining momentum
- Resource constraints limit enforcement capacity

### Congressional Champions

**Key actors:**

| Lawmaker | Position | Key Actions |
|----------|----------|-------------|
| Sen. Ron Wyden (D-OR) | Leading privacy advocate | Investigations of government data purchases; Fourth Amendment Is Not For Sale Act |
| Sen. Rand Paul (R-KY) | Privacy hawk on government access | Supports warrant requirements for location data |
| Sen. Ed Markey (D-MA) | Consumer privacy advocate | Privacy legislation and location data broker regulation |
| Rep. Anna Eshoo (D-CA) | Tech accountability | Location privacy provisions in comprehensive privacy bills |

---

## Advocacy Organizations

### Privacy and Civil Liberties

| Organization | Focus | Position |
|-------------|-------|----------|
| Electronic Frontier Foundation (EFF) | Digital rights | Strong advocacy for location privacy; opposes geofence warrants and government purchases |
| ACLU | Civil liberties broadly | Focuses on Fourth Amendment, geofence warrants, and immigration-related location surveillance |
| Electronic Privacy Information Center (EPIC) | Privacy policy | Advocates for comprehensive location privacy legislation |
| Center for Democracy and Technology (CDT) | Technology policy | Supports data minimization and consent for location data |
| Georgetown Center on Privacy and Technology | Privacy research | "American Dragnet" report documenting government location data purchases |
| Surveillance Technology Oversight Project (STOP) | Surveillance technology | Opposes geofence warrants and location-based policing tools |

### Industry Associations

| Organization | Position on Location Privacy Reform |
|-------------|--------------------------------------|
| Interactive Advertising Bureau (IAB) | Opposes strict consent requirements; supports self-regulation |
| CTIA (Wireless Industry) | Opposes expansion of location privacy regulation |
| US Chamber of Commerce | Opposes comprehensive privacy legislation |
| Network Advertising Initiative (NAI) | Self-regulatory framework; opposes prescriptive rules |
| Alliance for Automotive Innovation | Opposes restrictions on connected vehicle data |

---

## Stakeholder Power Map

| Stakeholder | Power Level | Alignment with Reform | Key Leverage |
|-------------|-------------|----------------------|--------------|
| Location data brokers | High | Strongly against | Lobbying, government contracts, industry associations |
| Advertising technology industry | Very high | Against | Lobbying, market dominance, campaign contributions |
| Wireless carriers | High | Against | Lobbying through CTIA, regulatory relationships |
| Automakers | High | Against | Lobbying, consumer relationships, Alliance for Automotive Innovation |
| Government agencies (law enforcement) | High | Against (on purchase restrictions) | National security arguments, political influence |
| Technology platforms (Google, Apple, Meta) | Very high | Mixed | Lobbying, market power; Apple partially aligned with reform |
| FTC | Moderate | Supportive | Enforcement authority, public visibility |
| State AGs | Moderate | Mostly supportive | Enforcement, multistate coalitions |
| Privacy advocates | Moderate | Strongly supportive | Public opinion, litigation, media, research |
| General public | Low individually, high collectively | Strongly supportive (72% concerned about location tracking) | Votes, public opinion, consumer behavior |
| Immigrants/vulnerable populations | Very low | Strongly supportive | Moral authority, coalition partners |
| Academic researchers | Low-moderate | Mixed | Expert credibility, institutional support |
| Congressional privacy champions | Moderate | Supportive | Legislative authority, investigation power |

## Document Navigation

- Previous: [Root Causes](04-root-causes.md)
- Next: [Opposition](06-opposition.md)
- Up: [Overview](01-overview.md)
