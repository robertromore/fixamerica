# Infrastructure Coordination

**Parent Document:** [00-introduction.md](../00-introduction.md)

**Phase:** All Phases

**Status:** Draft

---

## Purpose

Infrastructure Coordination defines MCF's approach to **shared and cross-boundary infrastructure**—telecommunications, transportation networks, utilities, and ports/airports—that require coordination for economic activity regardless of political boundaries.

Infrastructure determines what economic activity is possible. Without reliable telecommunications, CMS benefits cannot be delivered. Without accessible transportation, employment mobility is theoretical. MCF establishes minimum infrastructure coordination to enable economic integration without determining infrastructure ownership.

---

## Design Principles

### 1. Access Over Ownership

MCF ensures infrastructure access for economic activity without determining who owns or controls infrastructure.

**What This Means:**

- Focus on functional access
- Multiple providers acceptable
- Ownership disputes not resolved
- Access arrangements operational

### 2. Reliability Standards

Economic integration requires predictable infrastructure. MCF establishes reliability expectations without taking operational control.

**What This Means:**

- Minimum reliability thresholds
- Accountability for disruptions
- Redundancy where possible
- Emergency provisions

### 3. Non-Weaponization

Infrastructure cannot be weaponized against civilian economic activity within MCF.

**What This Means:**

- Infrastructure shutoffs as economic coercion prohibited
- Civilian infrastructure protected
- Maintenance access guaranteed
- Emergency restoration priority

### 4. Technical Interoperability

Different systems must work together. MCF establishes technical standards for interoperability.

**What This Means:**

- Standard interfaces
- Data format alignment
- Technical cooperation
- No forced system integration

### 5. Operational Autarky

MCF critical systems -- finance, connectivity, utilities -- must be capable of sustaining essential functions without the active cooperation of any single party's national infrastructure.

**What This Means:**

- Connection to national systems is preferred for efficiency
- Independence is required for resilience
- Each critical system must have an operational mode that does not depend on Host State infrastructure cooperation
- Autarky provisions are not assertions of sovereignty; they are engineering requirements for survivability

**Instantiations:**

| Domain | Normal Mode | Autarky Mode |
|--------|-------------|--------------|
| **Finance** | ILS/USD clearing through national banking | MVTP closed-loop ledger (see [Economic Integration Section 4.4](01-economic-integration.md)) |
| **Connectivity** | Commercial telecom + ISP | LEO satellite backbone + private local networks (see Telecommunications Section 5 below) |
| **Electricity** | National grid connection (IEC) | Solar micro-grid + battery storage (see Utilities Section 1a below) |
| **Water** | National supply (Mekorot) | On-site treatment + atmospheric generation (see [Water Resources](../06-sensitive-issues/01-water-resources.md)) |
| **Materials** | Israeli port customs | Jordan Corridor (see Port Access Section 1a below) |

---

## Telecommunications

### 1. Current Landscape

**Israeli Telecommunications:**

- Advanced infrastructure
- Multiple providers
- Full international connectivity
- Comprehensive mobile coverage

**Palestinian Telecommunications:**

- Limited spectrum access
- Infrastructure constraints
- Dependency on Israeli connections
- Gaza connectivity challenges

**Cross-Border Issues:**

- Spectrum allocation disputes
- International gateway access
- Roaming arrangements
- Equipment import restrictions

### 2. MCF Telecommunications Principles

**Access Guarantees:**

| Element | Standard |
|---------|----------|
| **CMS connectivity** | CMS holders must have reliable connectivity for benefit access |
| **Business connectivity** | Cross-community business requires reliable communication |
| **Emergency communication** | Emergency services must function across boundaries |
| **MCF operations** | MCF institutions require secure communications |

**Non-Interference:**

- No jamming or interference with civilian communications
- No bulk surveillance through MCF (parties retain own authorities)
- No communication shutoffs as coercion
- Emergency exceptions narrowly defined

### 3. Spectrum Coordination

**Challenge:**

Spectrum is finite; allocations affect coverage on both sides.

**MCF Role:**

| Function | Scope |
|----------|-------|
| **Coordination** | Facilitate technical spectrum discussions |
| **Interference resolution** | Technical dispute resolution |
| **Information** | Share coverage and interference data |
| **No allocation** | MCF does not allocate spectrum |

**Technical Arrangements:**

- Interference mitigation
- Border area coordination
- Emergency frequency reservation
- Technical working group

### 4. Connectivity Requirements

**For CMS Benefits:**

- Internet access sufficient for service delivery
- Mobile coverage for communication
- Data services for economic activity
- Voice services for emergencies

**For Business:**

- Reliable bandwidth
- Reasonable latency
- International connectivity
- Payment system connectivity

### 5. MCF Independent Connectivity (Satellite-First Architecture)

MCF operational systems depend on telecommunications for core functions: MVTP settlement, CMS registry access, JSVC incident reporting, PCC monitoring, and Digital Phase -1 engagement. Per the Operational Autarky Principle (Design Principle 5), MCF connectivity must not depend on any single party's commercial telecom infrastructure.

**Architecture:**

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Primary backbone** | Low Earth Orbit (LEO) satellite constellation (guarantor-contracted) | MCF institutional connectivity independent of terrestrial telecom |
| **Local distribution** | Private 5G / Wi-Fi 6 networks on unlicensed or internationally protected spectrum bands (ISM bands) | Last-mile connectivity within SAZ/PCC areas |
| **Terrestrial supplement** | Commercial Israeli/Palestinian telecom | Additional capacity when available; not required for critical operations |

**LEO Satellite Backbone:**

- Guarantor states contract LEO satellite capacity (e.g., Starlink, OneWeb, or EU-provided constellation) for MCF institutional uplink
- VSAT terminals deployed at all MCF institutional sites, SAZ administrative centers, and PCC checkpoints
- Satellite uplink provides connectivity independent of Israeli fiber optic backbone and frequency allocations
- Jamming a LEO constellation constitutes a hostile act against the satellite operator's flag state, raising the cost of interference beyond bilateral Israeli-Palestinian dynamics

**Private Local Networks:**

- SAZ and PCC areas deploy private 5G/Wi-Fi 6 networks for local distribution
- ISM bands (2.4 GHz, 5 GHz, 6 GHz) are internationally protected and cannot be selectively denied without disrupting the host country's own civilian economy
- MCF-managed local networks serve CMS holder access to digital services, MVTP transactions, and institutional communications
- Equipment imported through the Jordan Corridor (see Port Access Section 1a) to bypass telecom equipment import restrictions

**Degradation-as-Interference:**

Systematic bandwidth throttling and frequency denial are explicitly classified as interference under MCF non-interference rules (Section 2 above). Measurable thresholds:

| Metric | Interference Threshold | Documentation |
|--------|----------------------|---------------|
| **Bandwidth** | <50% of baseline capacity sustained >48 hours | Infrastructure Coordination Unit certifies |
| **Latency** | >500ms average sustained >24 hours | Automated monitoring |
| **Service availability** | <90% uptime over any 7-day period | Automated monitoring |
| **Frequency denial** | MCF spectrum request unanswered >60 days | Infrastructure Coordination Unit documents |

Threshold breaches trigger documentation and escalation per spoiler response protocols as a category of infrastructure interference.

**Offline-Capable Systems:**

Critical MCF systems must operate in degraded-connectivity mode:

- CMS verification: Local caching with periodic synchronization
- MVTP transactions: Store-and-forward with settlement on reconnection
- JSVC incident reporting: Local recording with batch upload
- PCC monitoring: Autonomous operation with periodic data sync

### 6. Gaza Telecommunications

**Specific Challenges:**

- Limited infrastructure
- Power dependency
- Import restrictions on equipment
- International connectivity constraints

**MCF Approach:**

| Element | Action |
|---------|--------|
| **Infrastructure protection** | Telecom infrastructure protected |
| **Power coordination** | Power access for telecom facilities |
| **Maintenance** | Equipment import for repair/maintenance |
| **Connectivity** | International connectivity support |
| **Satellite access** | LEO satellite terminals for MCF operations (per Section 5) |

---

## Transportation Networks

### 1. Road Transportation

**Current Landscape:**

- Checkpoints and barriers
- Separated road networks in places
- Permit requirements
- Travel time unpredictability

**MCF Transportation Principles:**

| Principle | Application |
|-----------|-------------|
| **Predictability** | Travel times reasonably predictable |
| **Access** | CMS holders have defined access routes |
| **Dignity** | Travel conditions respect human dignity |
| **Economic** | Commercial transport functional |

**Road PCCs:**

| Type | Purpose |
|------|---------|
| **Commuter corridors** | Regular employment travel |
| **Commercial corridors** | Goods transport |
| **General mobility** | CMS holder movement |
| **Emergency** | Medical and emergency access |

**Checkpoint Coordination:**

- CMS-holder lanes where feasible
- Processing time standards
- Complaint mechanisms
- No arbitrary delays

### 2. Public Transportation

**Cross-Community Transit:**

| Element | Approach |
|---------|----------|
| **Bus services** | Cross-boundary routes for employment |
| **Rail** | Connection where infrastructure exists |
| **Shared services** | Operated by private or public entities |
| **Standards** | Safety and accessibility standards |

**MCF Role:**

- Facilitate service authorization
- Set minimum standards
- Coordinate schedules
- Not operate services directly

### 3. Commercial Transport

**Goods Movement:**

| Type | Arrangements |
|------|--------------|
| **Raw materials** | Defined crossings; inspection protocols |
| **Finished goods** | Commercial corridors; customs coordination |
| **Agricultural** | Perishable goods priority |
| **Industrial** | Regular commercial access |

**Logistics Coordination:**

- Crossing schedules
- Inspection protocols
- Documentation standards
- Dispute resolution for delays

### 4. Gaza Transportation

**Specific Challenges:**

- Closure restrictions
- Limited exit points
- Goods import constraints
- Person movement restrictions

**MCF Approach:**

| Element | Action |
|---------|--------|
| **Crossing coordination** | Predictable crossing operations |
| **Commercial access** | Defined commercial transport |
| **Person movement** | CMS holder exit coordination |
| **Emergency** | Medical and humanitarian access |

**Note:** MCF cannot override Israeli or Egyptian border controls but can facilitate coordination and predictability.

---

## Ports and Airports

### 1. Port Access

**Current Situation:**

- No Palestinian deep-water port
- Gaza port non-operational
- Goods through Israeli ports
- Dependency and delays

**MCF Approach:**

| Element | Action |
|---------|--------|
| **Existing ports** | Palestinian goods access to Israeli ports |
| **Customs coordination** | Facilitated clearance |
| **Future ports** | No prejudice to future development |
| **Inspection** | Security with efficiency |

### 1a. Jordan Corridor: Primary Material Entry Point

**Rationale:** MCF cannot override Israeli or Egyptian border controls (see Gaza Transportation note). Goods transiting Israeli ports are subject to Israeli customs classification, which historically classifies construction materials (cement, steel rebar, aggregates) as dual-use or restricted. This creates a pre-corridor supply chain vulnerability that MCF's internal customs protocols cannot remedy.

To mitigate this dependency, MCF designates the **King Hussein Bridge (Allenby Bridge) crossing from Jordan** as the Primary Material Entry Point for West Bank SAZ construction and infrastructure projects.

**Jordan Corridor Design:**

| Element | Specification |
|---------|---------------|
| **Entry point** | King Hussein Bridge / Allenby Bridge crossing |
| **Inspection authority** | UVB inspection at crossing (leveraging UVB's mandate for unilateral verification) |
| **Material scope** | Construction materials (cement, steel, rebar, aggregates, glass, lumber), infrastructure equipment, heavy machinery |
| **Customs transition** | Goods clear Jordanian export customs, transit the crossing under UVB inspection, and enter MCF customs jurisdiction directly (Tier 1 classification per [Economic Integration Section 2.2](01-economic-integration.md)) |
| **Security verification** | UVB confirms goods match manifest; random sampling per MCF protocols; no dual-use reclassification |

**Jordan Corridor Advantages:**

- Bypasses Israeli port customs for construction materials
- Leverages Jordan's role as a regional guarantor with direct border access
- Utilizes existing crossing infrastructure (King Hussein Bridge is operational)
- UVB inspection provides security verification independent of Israeli or Palestinian customs authority

**Jordan Corridor Limitations:**

- Crossing capacity constrains throughput (infrastructure upgrades may be needed)
- Jordan must consent to corridor designation (leverages Jordanian guarantor role per [Guarantor Selection](../04-guarantor-architecture/01-guarantor-selection.md))
- Israeli security presence at the crossing creates residual dependency (requires guarantor-negotiated transit protocols)
- Southern West Bank / Gaza requires alternative routing (Egyptian crossings, maritime options)

**Alternative Supply Routes:**

| Route | Applicable Territory | Constraints |
|-------|---------------------|-------------|
| **King Hussein Bridge (primary)** | West Bank (north and central) | Jordan consent; crossing capacity |
| **Egyptian crossings (Rafah, Kerem Abu Salem)** | Gaza, southern territory | Egyptian consent; Gaza security conditions |
| **Guarantor direct procurement** | All MCF territory | Guarantor states procure and ship via their own logistics; highest cost but bypasses all national customs |
| **Maritime (future)** | Gaza, coastal territory | Requires port development or floating terminal; long-term option |

**Pre-Positioned Material Reserves:**

MCF maintains strategic reserves of key construction materials within MCF domains:

- Minimum 90-day supply of cement, steel, and aggregates for active SAZ construction projects
- Reserve locations within SAZ territory or PCC-accessible warehousing
- Replenishment through Jordan Corridor as primary channel
- Reserve adequacy reviewed quarterly by Infrastructure Coordination Unit

### 2. Airport Access

**Current Situation:**

- No operational Palestinian airport
- Dependency on Ben Gurion (limited) and Jordanian airports
- Gaza airport destroyed
- Travel constraints

**MCF Approach:**

| Element | Action |
|---------|--------|
| **Existing airports** | CMS holder access facilitation |
| **Future airports** | No prejudice to future development |
| **Travel coordination** | VIP/CMS facilitation lanes where possible |
| **Documentation** | MCF credential recognition for travel |

### 3. Cross-Border Infrastructure

**Coordination Areas:**

| Area | Coordination |
|------|--------------|
| **Crossing points** | Operating hours; processing standards |
| **Inspection facilities** | Shared inspection where agreed |
| **Documentation** | Standard formats; electronic processing |
| **Dispute resolution** | Delay and denial resolution |

---

## Utilities Infrastructure

### 1. Electricity

**Coordination Areas:**

| Area | MCF Role |
|------|----------|
| **Supply reliability** | Minimum reliability standards |
| **Emergency power** | Critical facility backup |
| **Grid connection** | Technical interconnection standards |
| **Payment** | Payment mechanism coordination |

**Protection:**

- Power infrastructure protected
- Shutoffs as coercion prohibited
- Maintenance access guaranteed
- Emergency restoration priority

### 1a. Off-Grid Primary Design (SAZ Power Independence)

Per the Operational Autarky Principle (Design Principle 5), SAZ and PCC infrastructure must be designed as **islandable micro-grids** capable of sustaining critical operations without national grid connection.

**Default SAZ Power Design:**

| Component | Specification |
|-----------|---------------|
| **Primary source** | Solar photovoltaic + battery storage, sized for critical operations (hospitals, water pumps, administration, telecom) |
| **Secondary source** | Wind generation and/or waste-to-energy where site conditions permit |
| **Grid connection** | Treated as supplementary bulk power source, not a survival dependency |
| **Backup** | Diesel/natural gas generators for extended low-solar periods |

**Design Standard:**

- All SAZ site plans must include independent power generation sufficient for critical operations (medical, water, communications, administration) without grid connection
- Grid connection is pursued for efficiency and cost reduction but is not required for SAZ operational viability
- Guarantor states provide renewable energy technology (solar panels, battery systems, inverters) as part of SAZ construction support obligations

**Connection Refusal as Interference:**

If the national grid provider (IEC or equivalent) does not provide a connection plan within 90 days of a formal MCF connection request for an established SAZ:

1. Infrastructure Coordination Unit documents the refusal
2. Refusal classified as infrastructure obstruction subject to guarantor escalation
3. MCF proceeds with independent power generation (already in place as default design)
4. Pattern of connection refusals documented as systematic interference per spoiler response protocols

**Rationale:** This inverts the monopoly vulnerability. The SAZ is self-sufficient by default. Grid connection is a convenience that reduces operating costs, not a chokepoint that determines viability. If IEC connects, all affected parties benefit from efficiency. If IEC refuses, the SAZ operates independently and the refusal is documented as obstruction.

### 2. Natural Gas

**Coordination Areas:**

| Area | MCF Role |
|------|----------|
| **Supply access** | Access to available supplies |
| **Infrastructure** | Pipeline protection |
| **Future development** | No prejudice to offshore resources |

**Note:** Gaza offshore gas is politically sensitive; MCF does not adjudicate but protects any operational infrastructure.

### 3. Water Infrastructure

**Covered In:** [Water Resources](../06-sensitive-issues/01-water-resources.md)

**Key Points:**

- Infrastructure protection
- Emergency access
- No allocation determination
- Operational coordination

---

## Technical Standards

### 1. Interoperability Standards

**Purpose:**

Enable systems to work together without forcing integration.

**Areas:**

| Domain | Standards |
|--------|-----------|
| **Telecommunications** | Technical interface standards |
| **Transportation** | Documentation; vehicle standards |
| **Utilities** | Technical interconnection standards |
| **Payments** | Transaction format standards |

### 2. Safety Standards

**Areas:**

| Domain | Standards |
|--------|-----------|
| **Transportation** | Vehicle safety; road standards |
| **Telecommunications** | Equipment safety |
| **Utilities** | Electrical safety; pressure standards |
| **Construction** | Building codes (reference) |

### 3. Data Standards

**For Infrastructure:**

- Operational data formats
- Real-time sharing protocols
- Emergency notification standards
- Performance reporting formats

---

## Infrastructure Protection

### 1. Protected Infrastructure

**Categories:**

| Type | Protection Level |
|------|------------------|
| **Life-critical** | Highest (medical, water, emergency) |
| **Economic-critical** | High (ports, major routes, telecom hubs) |
| **Operational** | Standard (general infrastructure) |

**Protection Means:**

- Physical protection where feasible
- Targeting prohibition
- Maintenance access guarantee
- Rapid repair priority

### 2. Disruption Response

**Response Protocol:**

| Disruption Type | Response |
|-----------------|----------|
| **Intentional attack** | Documentation; security response; repair |
| **Collateral damage** | Assessment; repair priority |
| **Operational failure** | Coordination for repair |
| **Natural event** | Emergency response; repair |

### 3. Accountability

**For Infrastructure Harm:**

- Documentation and attribution
- Repair responsibility determination
- Compensation claims (to dispute resolution)
- Pattern identification

---

## Phased Approach

### Phase 0: Emergency Coordination

**Priority:**

- Emergency infrastructure access
- Critical repair coordination
- Basic telecommunications for MCF
- Humanitarian transport

### Phase 1: Operational Coordination

**Expansion:**

- Regular PCC transportation
- CMS telecommunications access
- Utility reliability standards
- Commercial transport coordination

### Phase 2+: Enhanced Cooperation

**If Conditions Allow:**

- Comprehensive transport networks
- Advanced telecommunications coordination
- Infrastructure investment facilitation
- Deep technical cooperation

---

## Institutional Arrangements

### 1. Infrastructure Coordination Unit

**Functions:**

- Technical coordination facilitation
- Dispute resolution (operational)
- Standards development support
- Performance monitoring

**Composition:**

- Technical experts
- Party representatives
- MCF Secretariat support
- International technical support

### 2. Sector Working Groups

**Possible Groups:**

| Sector | Focus |
|--------|-------|
| **Telecommunications** | Spectrum; connectivity; standards |
| **Transportation** | Roads; crossings; commercial |
| **Utilities** | Power; water; gas |
| **Ports/Airports** | Access; procedures |

### 3. Dispute Resolution

**Infrastructure Disputes:**

- Technical disputes: Expert resolution
- Operational disputes: Coordination unit
- Significant disputes: MCF institutional process
- Ownership disputes: Excluded (political)

---

## References

- [Economic Architecture Overview](00-overview.md)
- [Labor Mobility](02-labor-mobility.md)
- [Water Resources](../06-sensitive-issues/01-water-resources.md)
- [PCC Protocols](../01-phase-0-institutions/03-pcc-protocols.md)
