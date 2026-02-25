---
freshness:
  last-reviewed: 2026-02-05
  data-year: 2025
  review-cycle: 12
  sections:
    - name: "Space Force Structure and Budget"
      data-year: 2025
    - name: "Adversary ASAT Capabilities"
      data-year: 2025
    - name: "Space Debris Environment"
      data-year: 2025
notes:
  - Monitor FY2026 Space Force budget request for proliferated LEO funding.
  - Track UN COPUOS debris mitigation guidelines update.
  - Update after any new ASAT tests or space security incidents.
sources:
  count: 14
  verified: 2026-02-05
  broken: 0
---

# Space Defense: Current State

## U.S. Space Force Structure and Organization

### U.S. Space Force (USSF)

- **Mission**: To organize, train, and equip space forces in order to protect U.S. and allied interests in space and to provide space capabilities to the joint force.
- **Structure**: The Space Force is the sixth branch of the U.S. Armed Forces, organized under the Department of the Air Force. Its members are known as "Guardians."
- **Personnel**: Approximately 16,000 active-duty Guardians, making it the smallest U.S. military branch. The force also draws on approximately 9,000 civilian employees and relies on contractor support for many technical functions. By comparison, the Air Force has approximately 325,000 active-duty members.
- **Budget**: The FY2025 budget request for the Space Force was approximately $29.4 billion, reflecting the growing priority placed on space capabilities. This represents a significant increase from $15.4 billion in FY2021 -- a near-doubling in four years that reflects both new program starts and the transfer of existing programs from other services.
- **Chief of Space Operations**: General B. Chance Saltzman serves as the chief military officer of the Space Force and is a member of the Joint Chiefs of Staff.
- **Field Commands**:
    - **Space Operations Command (SpOC)**: Headquartered at Peterson Space Force Base, Colorado. Conducts space operations, including satellite operations, missile warning, space domain awareness, electromagnetic warfare, and orbital warfare. SpOC is the largest field command and the primary operational arm of the Space Force.
    - **Space Systems Command (SSC)**: Headquartered at Los Angeles Air Force Base, California. Responsible for developing, acquiring, and sustaining space systems. Manages launch operations, satellite procurement, ground systems, and the Space Development Agency (which was absorbed into SSC in 2023). SSC manages the National Security Space Launch (NSSL) program.
    - **Space Training and Readiness Command (STARCOM)**: Headquartered at Peterson Space Force Base. Responsible for training Guardians, developing space doctrine, and operating the National Space Test and Training Complex for space wargaming and exercises.

### U.S. Space Command (USSPACECOM)

- **Mission**: A unified combatant command responsible for conducting operations in, from, and to the space domain. While the Space Force organizes and equips forces, Space Command employs them in operations.
- **Relationship to Space Force**: Analogous to the relationship between the U.S. Army (organizes and trains) and U.S. Central Command (conducts operations). Space Command draws forces from all services but primarily from the Space Force.
- **Commander**: A four-star general officer. The command is headquartered at Peterson Space Force Base, Colorado (after a prolonged basing dispute that initially selected Huntsville, Alabama before reverting to Colorado Springs in 2023).
- **Combined Space Operations Center (CSpOC)**: Located at Vandenberg Space Force Base, California. The primary operational hub for space domain awareness, satellite operations, and space battle management. The CSpOC integrates data from the Space Surveillance Network, allied sensors, and commercial providers to maintain the authoritative catalog of objects in orbit.
- **Key Subordinate Organizations**: The Combined Force Space Component Command (CFSCC) provides space effects to combatant commanders worldwide. The Joint Task Force-Space Defense (JTF-SD) is responsible for protecting and defending U.S. and allied space capabilities against hostile action.

### Space Development Agency (SDA)

The SDA, established in 2019 and now integrated into Space Systems Command, represents a deliberate effort to disrupt the traditional defense space acquisition model. Its primary mission is the Proliferated Warfighter Space Architecture (PWSA).

- **PWSA Design**: A mesh network of hundreds of small satellites in low Earth orbit organized into functional "layers":
    - **Tracking Layer**: Satellites with wide-field-of-view infrared sensors to detect and track ballistic and hypersonic missiles from launch through intercept.
    - **Transport Layer**: Satellites providing low-latency, jam-resistant optical inter-satellite data links to move targeting data from sensors to shooters.
    - **Custody Layer**: Satellites providing persistent tracking of targets for engagement by missile defense interceptors.
    - **Battle Management Layer**: Software-defined satellites that integrate sensor data and coordinate engagements.
- **Acquisition Approach**: The SDA uses two-year development cycles ("tranches") rather than the decade-long timelines typical of traditional space programs. It leverages commercial satellite bus designs and commercial-grade components to reduce costs.
- **Status**: Tranche 0 (demonstration) and Tranche 1 satellites have been launched, with approximately 30 satellites on orbit as of early 2025. Tranche 2 and 3 contracts have been awarded to companies including L3Harris, Northrop Grumman, York Space Systems, and Lockheed Martin.

## Critical Satellite Constellations

The U.S. military and civilian economy depend on several key satellite constellations. The loss or degradation of any of these would have immediate and severe consequences.

### Navigation: GPS

| Parameter | Value |
|---|---|
| Constellation Size | 31 operational satellites |
| Orbit | Medium Earth Orbit (MEO), ~20,200 km altitude |
| Modernization | GPS III and IIIF (improved accuracy, anti-jamming M-code for military, new civil signals) |
| Prime Contractor | Lockheed Martin (GPS III/IIIF satellites) |
| Dependence | Precision-guided munitions, logistics, civilian aviation, financial transactions, emergency services, electrical grid timing |
| Economic Dependence | A 2019 RTI International study estimated that GPS generates $1.4 trillion in annual economic benefits to the U.S. economy |

- **Vulnerability**: GPS signals are extremely weak by the time they reach Earth's surface (approximately -130 dBm -- weaker than the thermal noise floor), making them susceptible to jamming and spoofing. Russia and China have both demonstrated GPS jamming capabilities in operational theaters. Russia routinely jams GPS signals in the Baltic region, in Ukraine, and near its military bases in Syria. Chinese military exercises near Taiwan have included GPS disruption.
- **M-Code**: The military's encrypted, anti-jam signal (M-code) is being fielded on GPS III satellites and through the Military GPS User Equipment (MGUE) program, but fielding the receivers across the force has been slow. Full M-code capability is not expected until the late 2020s.
- **Alternative PNT**: The DoD is investing in alternative positioning, navigation, and timing (PNT) technologies to reduce GPS dependence, including inertial navigation, celestial navigation, and signals of opportunity.

### Missile Warning: SBIRS and Next-Gen OPIR

| Parameter | Value |
|---|---|
| Current System | Space Based Infrared System (SBIRS) -- 6 satellites in GEO and HEO |
| Replacement | Next-Generation Overhead Persistent Infrared (Next-Gen OPIR) |
| Next-Gen OPIR Prime | Lockheed Martin (GEO); Northrop Grumman (polar/HEO) |
| Orbit | Geosynchronous Earth Orbit (GEO), ~35,786 km altitude; Highly Elliptical Orbit (HEO) for polar coverage |
| Mission | Detect ballistic missile launches within seconds using infrared sensors |
| Dependence | Nuclear deterrence, theater missile defense, battlespace awareness |

- **Vulnerability**: As high-value, low-density assets in predictable GEO orbits, these satellites are prime targets for ASAT weapons and directed-energy attacks. Their loss would blind the U.S. to ballistic missile launches, with catastrophic implications for nuclear deterrence and missile defense. The shift to Next-Gen OPIR aims to improve survivability with more advanced sensors and redundancy, but the constellation will remain small and vulnerable compared to proliferated alternatives.
- **PWSA Complement**: The SDA's Tracking Layer is designed to supplement (not replace) SBIRS/Next-Gen OPIR with a proliferated constellation of infrared sensors in LEO, providing additional coverage against advanced threats like hypersonic glide vehicles that are harder to track from GEO.

### Communications: SATCOM

| System | Orbit | Purpose | Prime Contractor |
|---|---|---|---|
| Advanced Extremely High Frequency (AEHF) | GEO | Nuclear command and control, strategic communications | Lockheed Martin |
| Wideband Global SATCOM (WGS) | GEO | High-bandwidth tactical communications | Boeing |
| Protected Tactical SATCOM (PTS) | Various | Anti-jam, secure tactical communications | In development |
| Evolved Strategic SATCOM (ESS) | GEO | Next-gen nuclear C2 replacement for AEHF | Northrop Grumman |
| Commercial SATCOM | Various | Supplemental bandwidth (up to 80% of DoD SATCOM bandwidth is commercial) | Multiple providers |

- **Vulnerability**: Heavy reliance on commercial SATCOM creates supply chain and targeting risks. The 2022 Russian cyberattack on Viasat's KA-SAT network at the start of the Ukraine invasion demonstrated the vulnerability of commercial SATCOM to state-level attack. The attack disabled tens of thousands of satellite modems across Europe within hours, disrupting Ukrainian military communications and also affecting civilian infrastructure including German wind turbines. This event was a watershed moment in demonstrating that commercial space assets are legitimate targets in modern conflict.
- **Starlink as SATCOM**: SpaceX's Starlink constellation (~6,000+ satellites) provided critical communications to Ukrainian forces after the Viasat attack, demonstrating the resilience of proliferated LEO constellations to cyberattack and electronic warfare. However, Starlink terminals also experienced Russian electronic warfare interference, and Musk's decisions about enabling coverage over contested areas raised questions about dependence on a single commercial provider's political decisions.

### Intelligence, Surveillance, and Reconnaissance (ISR)

- **National Reconnaissance Office (NRO)**: Operates classified electro-optical, synthetic aperture radar, and signals intelligence satellites. The NRO's budget is classified within the National Intelligence Program (estimated at approximately $20 billion annually across all intelligence agencies' space programs).
- **Modernization**: The NRO announced in 2023 a major expansion of its constellation, contracting with commercial providers (including SpaceX for launch) and purchasing commercial imagery and signals collection as supplements to national systems.
- **Commercial ISR Providers**: Companies including Maxar Technologies (WorldView satellites, 30 cm resolution), Planet Labs (200+ Dove satellites providing daily global coverage), BlackSky (real-time satellite imagery), and Capella Space (synthetic aperture radar) provide imagery that supplements NRO capabilities at lower classification levels, enabling broader sharing with allies and partners.
- **Vulnerability**: ISR satellites in LEO must pass predictably over targets and are trackable, making them vulnerable to both kinetic and non-kinetic ASAT threats. The shift toward larger commercial constellations provides some resilience through numbers, but also increases the number of potential targets and complicates adversary targeting decisions.

## Adversary ASAT Capabilities

### China (People's Republic of China)

China is the most capable and active peer competitor in space. The PLA Strategic Support Force (PLASSF) integrates space, cyber, and electronic warfare capabilities into a single organization, reflecting China's doctrine of treating space and information as unified domains.

| Capability | Description | Status |
|---|---|---|
| **Direct-Ascent ASAT** | Ground-launched kinetic kill vehicle that physically destroys a satellite. China tested this capability in 2007, destroying the FY-1C weather satellite at ~865 km altitude, generating over 3,500 trackable debris fragments. Additional tests were conducted in 2013 (DN-2, reaching near-GEO altitudes) and 2014 (DN-3). | Operational |
| **Co-Orbital ASAT** | Satellites capable of maneuvering close to a target satellite and destroying or disabling it. The SJ-17 and SJ-21 spacecraft have demonstrated advanced proximity operations and satellite grappling. In January 2022, SJ-21 was observed grappling a defunct BeiDou satellite and moving it to a graveyard orbit -- a capability with obvious weapons implications. | Tested and developing |
| **Ground-Based Laser** | Directed-energy weapons capable of dazzling or blinding satellite optical sensors from the ground. China has reportedly built multiple ASAT laser facilities, including one identified at Xinjiang. | Developing/Early operational |
| **Electronic Warfare** | GPS jamming and satellite communications jamming capabilities demonstrated in exercises and near Taiwan. China has also demonstrated uplink jamming against satellite communications. | Operational |
| **Cyber ASAT** | Capability to hack satellite ground stations and command-and-control links. Chinese cyber intrusions into satellite operator networks have been documented by U.S. intelligence agencies. | Assessed operational |
| **Space Surveillance** | Extensive ground-based and space-based surveillance network to track U.S. satellites and support targeting for ASAT operations. | Operational |

**Chinese Space Program Scale**: China conducted more orbital launches than any other nation in 2023 (67 launches vs. 116 for U.S. commercial/government combined). It operates the BeiDou navigation system (global constellation of 35+ satellites), the Tiangong space station, and is planning crewed lunar missions for 2030. China's civil-military fusion doctrine means that all Chinese space capabilities have potential military applications.

### Russia

Russia maintains a diverse and mature ASAT portfolio inherited from and expanded beyond Soviet-era programs.

| Capability | Description | Status |
|---|---|---|
| **Direct-Ascent ASAT (Nudol/PL-19)** | Ground-launched kinetic kill vehicle. Russia tested the system in November 2021, destroying the defunct Cosmos 1408 satellite, generating over 1,500 trackable debris fragments and forcing ISS astronauts to shelter. Russia conducted approximately 10 Nudol flight tests between 2014 and 2021. | Operational |
| **Co-Orbital ASAT (Cosmos 2542/2543)** | Russia has launched satellites that maneuver close to U.S. national security satellites, conducting surveillance and demonstrating the ability to threaten them. In 2020, Cosmos 2543 released a sub-satellite that maneuvered near a U.S. government satellite, prompting the U.S. Space Command to issue a public statement calling the behavior "unusual and disturbing." | Operational |
| **Electronic Warfare** | Extensive GPS jamming capability; demonstrated in Ukraine, Syria, and the Baltic region. Russia deploys the Tirada-2 satellite communications jamming system and the Krasukha-4 electronic warfare system. The Peresvet mobile laser system is deployed to dazzle satellite optical sensors and protect mobile ICBM launchers from satellite surveillance. | Operational |
| **Nuclear Space Weapon (Reported)** | In 2024, reports emerged that Russia was developing a space-based nuclear weapon or nuclear-powered electronic warfare device intended to disable satellite constellations through electromagnetic pulse (EMP). If deployed, such a weapon would violate the Outer Space Treaty's prohibition on nuclear weapons in orbit. | Under development |
| **Burevestnik/Other Novel Systems** | Russia has pursued several exotic space and near-space weapons concepts, though many have experienced development difficulties. | Various stages |

### Other Actors

- **India**: Conducted a kinetic ASAT test in March 2019 (Mission Shakti), destroying a satellite at ~300 km altitude. The low altitude meant most debris re-entered the atmosphere within months, but the test demonstrated India's capability. India subsequently endorsed the U.S.-led ASAT testing moratorium.
- **Iran and North Korea**: Both possess ballistic missile technology that could theoretically be adapted for ASAT purposes, but neither has demonstrated a dedicated ASAT capability. Iran has launched satellites, demonstrating some space technology competence. North Korea's ballistic missile tests serve a dual-use function.
- **France**: Has publicly announced development of "active defense" capabilities for its military satellites, including the ability to maneuver away from threats and potentially deploy defensive systems. France's Commandement de l'espace represents Europe's most assertive space defense posture.

## Space Debris Environment

The orbital debris environment is a growing threat to all space operations.

### Current Status

| Metric | Value | Source |
|---|---|---|
| Tracked Objects (10 cm+) | ~36,000 | U.S. Space Surveillance Network, 2024 |
| Estimated Objects (1-10 cm) | ~1,000,000 | ESA Space Debris Office |
| Estimated Objects (1 mm - 1 cm) | ~130,000,000 | ESA Space Debris Office |
| Average Collision Speed (LEO) | ~10 km/s (22,000 mph) | NASA Orbital Debris Program |
| ISS Debris Avoidance Maneuvers (annual avg) | ~3-5 per year | NASA |
| Active Satellites in Orbit | ~10,000+ | UCS Satellite Database, 2024 |
| Total Objects in Orbit (including inactive) | ~13,000+ cataloged payloads | ESA, 2024 |

- **Kessler Syndrome Risk**: At current debris growth rates, certain orbital altitudes -- particularly around 800-1,000 km -- may approach a tipping point where cascading collisions generate debris faster than natural orbital decay removes it, potentially rendering those orbits unusable. NASA models suggest that even without any future launches or explosions, the debris population in this band will continue to grow through collisions alone.
- **Major Debris-Generating Events**:
    - 2007 Chinese ASAT test: ~3,500+ tracked fragments at ~865 km (long-lived debris, will persist for decades)
    - 2009 Iridium 33/Cosmos 2251 collision: ~2,300+ tracked fragments (the first accidental hypervelocity collision between two intact satellites)
    - 2021 Russian ASAT test: ~1,500+ tracked fragments at ~480 km (lower altitude means faster decay, but still hazardous for years)
- **Conjunction Warnings**: The 18th Space Defense Squadron issues approximately 50,000 conjunction data messages per day to satellite operators worldwide, warning of potential close approaches. The vast majority are false alarms, but operators must evaluate each one, consuming significant operational resources.
- **Mega-Constellation Impact**: SpaceX's Starlink (6,000+ satellites, planning up to 42,000), Amazon's Kuiper (planned 3,236 satellites), and OneWeb (600+ satellites) are dramatically increasing the number of objects in congested LEO altitudes. While these operators implement debris mitigation measures (including controlled deorbiting at end of life), the sheer volume raises baseline collision probability and strains tracking capacity.

## Space Situational Awareness (SSA)

### U.S. Space Surveillance Network

- **18th Space Defense Squadron**: Operates the Space Surveillance Network, a global network of ground-based radars and optical telescopes that tracks objects in orbit. The network includes approximately 30 sensors at locations worldwide.
- **Space Fence**: An advanced S-band ground-based radar on Kwajalein Atoll in the Marshall Islands, built by Lockheed Martin at a cost of approximately $1.5 billion. Became operational in 2020. The Space Fence can detect objects as small as 10 cm in LEO and has significantly increased the number of tracked objects in the catalog. A second Space Fence site in Australia has been proposed but not funded.
- **Combined Space Operations Center (CSpOC)**: Located at Vandenberg Space Force Base, California. The primary hub for space situational awareness and space battle management.
- **Geosynchronous Space Situational Awareness Program (GSSAP)**: A constellation of satellites in near-GEO orbit that can maneuver to inspect and characterize objects in geosynchronous orbit. GSSAP satellites provide close-range observations of foreign satellites in GEO that ground-based sensors cannot match.
- **Commercial SSA**: Companies like LeoLabs (operates a global network of phased-array radars for LEO tracking), ExoAnalytic Solutions (operates a network of optical telescopes for GEO tracking), and Numerica Corporation provide commercial space tracking services that supplement government capabilities.

### Limitations

- The current network struggles to track objects smaller than 10 cm, which can still be lethal to spacecraft. A 1 cm fragment in LEO carries the kinetic energy equivalent of a hand grenade.
- The rapidly growing number of objects (driven by mega-constellations like Starlink) is straining tracking capacity. The catalog is growing at approximately 20-30% per year.
- Data sharing with allies and commercial operators is improving but remains hampered by classification concerns. The Department of Commerce's Office of Space Commerce is developing an Open Architecture Data Repository to serve as a civilian hub for space traffic coordination data, but the transition from DoD to Commerce has been slow.
- Cislunar space (between GEO and the Moon) represents a growing awareness gap. As activities extend toward the Moon (Artemis program, commercial lunar missions, Chinese lunar plans), the absence of persistent cislunar surveillance creates a potential blind spot for threats approaching from beyond GEO.

## Commercial Space Integration

The commercial space sector has fundamentally transformed the national security space landscape.

### Key Developments

- **SpaceX Dominance**: SpaceX provides the majority of U.S. national security launch services and operates the Starlink constellation (~6,000+ satellites), which has demonstrated military utility in the Ukraine conflict. SpaceX's Falcon 9 conducted over 90 launches in 2023, making it the world's most frequently launched rocket. Falcon Heavy provides heavy-lift capability for national security payloads. The Starship super-heavy launch vehicle, still in development, promises to revolutionize payload delivery with its ability to lift over 100 metric tons to orbit.
- **Proliferated LEO Architecture**: The Space Development Agency (SDA) is building the Proliferated Warfighter Space Architecture (PWSA), a mesh network of hundreds of small satellites in LEO for missile tracking and data transport. This represents a shift from small numbers of large, expensive satellites to large numbers of smaller, cheaper ones. The SDA contracts with both traditional defense primes and commercial satellite manufacturers like York Space Systems.
- **Commercial ISR**: Companies like Maxar, Planet, and BlackSky provide commercial satellite imagery that supplements NRO capabilities. The NRO's Commercial Systems Program Office manages the acquisition of commercial imagery. The Ukraine conflict demonstrated the value of commercial satellite imagery for battlespace awareness and public accountability.
- **United Launch Alliance (ULA)**: The Boeing/Lockheed Martin joint venture provides the Vulcan Centaur launch vehicle for national security missions under the NSSL Phase 2 contract. The NSSL program maintains at least two launch providers to ensure assured access to space.
- **Blue Origin**: Jeff Bezos's space company is developing the New Glenn orbital launch vehicle and is a potential future NSSL provider, which would add a third competitor to SpaceX and ULA.
- **Rocket Lab**: The New Zealand/U.S. company provides small-satellite launch services and has won contracts for responsive launch and satellite manufacturing for the Space Force.

### Challenges

- **Protecting Commercial Assets**: If commercial satellites used by the military are targeted during conflict, does the government have obligations to defend or replace them? What are the escalation implications of attacking a commercial constellation? The legal status of dual-use commercial satellites under the law of armed conflict is ambiguous and has not been tested.
- **Supply Chain Security**: Dependence on a small number of commercial providers creates single points of failure. SpaceX's dominance in launch raises concentration risk concerns -- Elon Musk's personal control over the world's most critical launch provider creates geopolitical and governance risks that have no precedent. The 2024 controversy over Starlink coverage decisions in Ukraine underscored this vulnerability.
- **Dual-Use Ambiguity**: Commercial satellites that serve both military and civilian purposes complicate targeting decisions for adversaries and legal determinations about legitimate military targets. An adversary attacking a Starlink satellite used by Ukraine's military would also be disrupting internet service for civilians worldwide.
- **Contract Structures**: Traditional government satellite procurement involves cost-plus contracts with extensive government oversight. Commercial space services are typically purchased as services on fixed-price contracts. The tension between these models -- government desire for control versus commercial desire for flexibility -- remains unresolved.

---

## Document Navigation

- Up: [Defense](../01-overview.md)
- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
