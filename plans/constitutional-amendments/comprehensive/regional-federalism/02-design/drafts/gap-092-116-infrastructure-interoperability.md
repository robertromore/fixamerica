# Gaps 92 + 116 Resolution: Article II, Section 4 Expansion

## Status: FINAL (v3)

**Resolves:** Gap 92 (Technical Standards as de facto Secession), Gap 116 (Administrative Veto via Technical Standard-Setting)

**Severity:** Medium (92), Medium (116)

**Date:** 2026-02-03

**Revision:** v3 FINAL — incorporates Round 2 fixes (1 reviewer, 5 findings)

**Target:** Article II-RF, Section 4 — new subsections (l) through (s), appended after existing (k)

**Placement Rationale:** Gap 92 originally targeted "Article IX-RF, Section 9" and Gap 116 targeted "Article II-RF, Section 4(m-o)." Article IX is the Lobbying and Anti-Corruption standalone amendment, not infrastructure. The interoperability mandate is a constraint on Regional power within the Concurrent Authority Framework — the same framework where Constitutional Labor Minimums (Gap 185) were placed at §4(h)-(k). Infrastructure interoperability follows the same structural pattern: permanent constitutional minimums that cannot be circumvented through the general variance/sunset provisions.

---

## Round 1 Convergence Analysis

### Reviewer Summary

| ID | Severity | Finding | R1 | R2 | Resolution |
|----|----------|---------|----|----|-----------|
| C1 | CRITICAL | Tiered delay thresholds — 2hr absurd for digital | LOW (sector-agnostic thresholds) | CRITICAL (F1) | **CONVERGENT** — tiered: 2hr physical, 5sec digital, real-time energy |
| C2 | CRITICAL | Deemed denial = pocket veto — flip to deemed approval | HIGH (recreates Gap 116 admin veto) | CRITICAL (F2) | **CONVERGENT** — flip to deemed approval with post-implementation ARB review |
| C3 | HIGH | Transition timing conflict (o)(4) 2yr vs (s)(3)(A) 3yr | HIGH | — | Complementary — add precedence rule for interim standards |
| C4 | HIGH | Annual change limit dangerous for cybersecurity patches | — | HIGH (F3) | Complementary — exempt security patches |
| C5 | MEDIUM | ARB pre-approval + Commerce certification = dual-veto deadlock | MEDIUM | — | Complementary — add order of operations and single decision clock |
| C6 | MEDIUM | "Financial interest" undefined at (s)(1)(E) | MEDIUM | — | Complementary — define materiality threshold |
| C7 | MEDIUM | Commerce too broad — specify NIST | — | MEDIUM (F4) | Complementary — "acting through NIST" |
| C8 | MEDIUM | Vendor lock-in via "efficiency" justification | — | MEDIUM (F5) | Complementary — add explicit vendor lock-in prohibition |
| C9 | LOW | Data sovereignty deconfliction needed | — | Q8 rec | Complementary — add deconfliction clause |

**Convergence statistics:** 2 convergent, 7 complementary, 0 contradictions

### Open Questions Resolved

| # | Question | Reviewer Consensus | v2 Resolution |
|---|----------|-------------------|---------------|
| 1 | 5% cost threshold | Retain — aligns with WTO de minimis (R1) | Retained at 5% |
| 2 | 2-hour delay threshold | Tier by infrastructure type (R1+R2 convergent) | Tiered: 2hr/5sec/real-time |
| 3 | Deemed denial vs approval | Flip to deemed approval (R1+R2 convergent) | Deemed approval with ARB review |
| 4 | Annual change limit | Exempt security patches (R2) | Exemption added |
| 5 | 5-year authority loss | Proportionate — retain (R1) | Retained |
| 6 | Art II §4 placement | Correct placement (R1+R2) | Confirmed |
| 7 | Commerce as lead agency | Specify NIST within Commerce (R2) | "Acting through NIST" |
| 8 | Art I §14 deconfliction | Add deconfliction clause (R2) | Clause added at (s)(5) |

---

## Round 2 Convergence Analysis

### Reviewer Summary

| ID | Severity | Finding | Resolution |
|----|----------|---------|-----------|
| D1 | HIGH | (r)(6) 120-day clock has no default outcome or tie-breaker if ARB/NIST miss clock or disagree | Add deemed approval default + split tie-breaker (ARB on barrier questions, NIST on technical feasibility) |
| D2 | MEDIUM | (q)(3) deemed certification lacks interim controls — bad standard locks in before ARB review | Add provisional status for deemed certifications + interim injunction authority |
| D3 | MEDIUM | (s)(5)(C) joint dispute resolution has no timeline or default | Add 90-day decision clock + privacy-preserving interim mode pending judicial review |
| D4 | LOW | (n)(3)(C) "no measurable additional latency" for energy is zero-tolerance — false positives | Delegate numeric threshold to NIST with interim floor |
| D5 | LOW | (s)(1)(F) open-standards mandate lacks safety exception for proprietary-only specs | Add narrow NIST-certified safety exception with open-standard development mandate |

**Convergence statistics (cumulative):** 0 contradictions across 15 total findings (R1: 10, R2: 5)

---

## 1. Problem Summary

These two gaps address the same fundamental vulnerability through complementary mechanisms:

| Gap | Threat | Vector | Existing Coverage |
|-----|--------|--------|-------------------|
| 92 | Engineering secession | Proprietary technical standards creating physical incompatibility | Art I §6 guarantees transit rights but does not require technical interoperability |
| 116 | Administrative fragmentation | Uncoordinated standard-setting fragmenting the National Common Market | Art II §4 establishes concurrent framework but does not address infrastructure standards specifically |

Both exploit the "Floors Not Ceilings" principle: a Region that adopts "superior" technical standards for its power grid, rail signaling, or digital credentials can create hard borders through engineering rather than law, achieving functional secession while remaining technically compliant with the Non-Blockade rule.

### Gaming Vectors (from Gap 92)

1. **Proprietary Power Grid:** Unique voltage/frequency/connector standards isolate energy trade
2. **Incompatible Rail Gauge:** Different track gauge requires transloading at borders
3. **Digital Credential Island:** Unique digital identity standard blocks non-resident access
4. **Standards Arms Race:** Annual proprietary updates prevent neighboring Regions from maintaining compatibility

---

## 2. Consolidation Analysis

Gap 116 is explicitly documented as supplementing Gap 92. Overlapping elements:

| Element | Gap 92 | Gap 116 | Consolidated |
|---------|--------|---------|-------------|
| Federal standard-setting | §9(e): "minimum interoperability standards" | §4(m): "minimum technical standards" | Single federal authority with domain-specific mandate |
| Regional innovation | §9(g): "exceeding federal floors" | §4(n): "exceed federal standards" | Unified backward-compatibility requirement |
| Pre-implementation review | §9(h): Commerce Dept certification | §4(o): Commerce Dept certification | Single certification process |
| Interoperability mandate | §9(a): constitutional prohibition | Not in Gap 116 | Gap 92 provides the structural mandate |
| Critical infrastructure definition | §9(b): five-category definition | Not in Gap 116 | Gap 92 provides scope |
| Material barrier standard | §9(c): objective test with thresholds | Not in Gap 116 | Gap 92 provides measurement |
| ARB enforcement | §9(i-k): complaint, remediation, federal implementation | Not in Gap 116 | Gap 92 provides enforcement |
| Anti-circumvention | §9(l-n): rapid change prohibition, innovation protection | Not in Gap 116 | Gap 92 provides anti-gaming |

**Design Decision:** Merge into a single provision retaining Gap 92's full structure with Gap 116's backward-compatibility requirement and domain-specific federal authority integrated throughout.

---

## 3. Proposed Constitutional Text

The following subsections are appended to Article II, Section 4 after existing subsection (k):

#### Critical Infrastructure Interoperability

*Resolves Gap 92 — "Technical Standards" as de facto Secession, and Gap 116 — "Administrative Veto" via Technical Standard-Setting. Establishes a permanent infrastructure interoperability mandate within the Concurrent Authority Framework, preventing Regions from achieving functional secession through engineering incompatibility while preserving Regional authority to innovate above federal floors.*

(l) **Infrastructure Interoperability Mandate.** No Region may adopt, implement, or maintain technical, engineering, or operational standards for Critical Infrastructure that create a material barrier to:

(1) the transit of energy across Regional boundaries, including generation, transmission, and distribution interconnection;

(2) the movement of goods via rail, road, waterway, or pipeline, including signaling, gauge, and safety system compatibility;

(3) the portability of digital credentials, professional licenses, and identity verification systems across Regional boundaries;

(4) the interconnection of telecommunications, data, and emergency communications networks.

(m) **Critical Infrastructure Definition.** For purposes of this section, "Critical Infrastructure" means:

(1) electric power generation, transmission, and distribution systems, including interconnection hardware and load-balancing protocols;

(2) rail networks, signaling systems, and rolling stock compatibility standards;

(3) major highways, bridges, tunnels, and their tolling, signaling, and safety systems;

(4) digital identity, payment, credentialing, and verification systems used by governmental entities or required for access to public services;

(5) telecommunications, internet, and emergency communications networks;

(6) pipeline systems for energy, water, or other bulk commodity transport.

The Department of Commerce, acting through the National Institute of Standards and Technology (NIST), in consultation with the ARB, may add categories to this definition by regulation when new infrastructure types with cross-Regional interconnection significance emerge. No category may be removed except by constitutional amendment.

(n) **Material Barrier Standard.** A "material barrier" exists when any of the following conditions is met:

(1) technical incompatibility requires conversion equipment, transloading, or reformatting processes at or near Regional boundaries that would not be required for the same transit within the Region;

(2) the cost of conversion, adaptation, or compliance with Regional standards exceeds five percent (5%) of the value of the goods, services, or energy in transit;

(3) technical differences impose delay exceeding the following thresholds, measured against equivalent transit within the Region:

- (A) two (2) hours for physical freight, vehicle, or rolling stock transit;
- (B) five (5) seconds for digital credential verification, authentication, or identity system transactions;
- (C) for energy transmission and grid interconnection, latency thresholds established by NIST, calibrated to ensure that cross-Regional energy flows are not materially disadvantaged relative to intra-Regional flows. Until NIST publishes specific thresholds, additional latency attributable to cross-Regional standards incompatibility shall not exceed one hundred (100) milliseconds for grid synchronization and frequency regulation signals, or five (5) seconds for bulk power scheduling and dispatch;
- (D) thirty (30) minutes for telecommunications and data network interconnection handoffs;

(4) credentials, licenses, or digital identity instruments valid in one Region are not recognized or are not technically operable in another Region due to standards incompatibility;

(5) a pattern of incremental standard changes, none individually meeting thresholds (1) through (4), cumulatively creates equivalent barrier effects over any thirty-six (36) month period.

The ARB shall develop and publish methodologies for measuring material barriers, including domain-specific threshold calibration, updated no less than every five (5) years. Disputed barrier measurements shall be resolved by the ARB within ninety (90) days of petition.

(o) **Federal Interoperability Floors.** The Federal Department of Commerce, acting through the National Institute of Standards and Technology (NIST), shall establish and maintain minimum interoperability standards ("Interoperability Floors") for each category of Critical Infrastructure defined in subsection (m):

(1) Interoperability Floors shall specify the technical requirements for cross-Regional compatibility, including but not limited to: voltage and frequency standards for electric power; track gauge, signaling protocols, and freight car specifications for rail; digital credential formats, authentication protocols, and data exchange standards for identity systems; and interconnection protocols for communications networks;

(2) Interoperability Floors shall be developed in consultation with Regional governments, industry experts, relevant federal agencies, and international standards organizations, and shall be based on best available technology, existing international standards (including ISO, IEEE, and ITU standards), and the objective of maintaining the National Common Market as a single integrated economic space;

(3) Interoperability Floors shall balance interoperability with legitimate technological advancement. NIST shall not mandate specific technologies when multiple technologies can achieve equivalent interoperability;

(4) Interoperability Floors shall be reviewed and, if necessary, updated every five (5) years. Between reviews, NIST may issue interim standards in response to emergent technologies, provided that interim standards include a minimum two (2) year transition period. Interim standards follow their own two-year transition timeline and are not subject to the major/minor classification under subsection (s)(3)(A).

(p) **Regional Innovation Within Floors.** Regions may adopt infrastructure standards exceeding Interoperability Floors established under subsection (o), provided that:

(1) the Regional standard maintains full backward compatibility with the applicable Interoperability Floor. "Full backward compatibility" means that equipment, systems, credentials, and vehicles conforming to the Interoperability Floor can operate within the Region without modification, conversion, or additional cost to the operator;

(2) interstate users — including persons, goods, vehicles, and energy in transit — experience no additional burden, delay, cost, or technical requirement beyond what would be experienced under the Interoperability Floor;

(3) the variation serves a genuine technical, safety, or efficiency purpose. The burden of demonstrating genuine purpose rests on the Region;

(4) the Region has obtained pre-implementation certification under subsection (q).

(q) **Pre-Implementation Certification.** Before adopting, implementing, or materially modifying infrastructure standards for any category of Critical Infrastructure:

(1) the Region shall submit the proposed standards, together with a Technical Impact Assessment, to NIST no less than one hundred twenty (120) days before the proposed effective date;

(2) the Technical Impact Assessment shall include: (A) a detailed description of the proposed standard; (B) identification of all Interoperability Floor requirements applicable to the infrastructure category; (C) analysis of backward compatibility under subsection (p)(1); (D) analysis of interstate user impact under subsection (p)(2); (E) documentation of the genuine technical, safety, or efficiency purpose under subsection (p)(3); (F) estimated conversion costs for affected interstate users, if any;

(3) NIST shall issue an Interoperability Certification or a Certification Denial within ninety (90) days. If NIST fails to act within ninety (90) days, the standard is deemed certified and the Region may proceed with implementation under provisional status. Provisional status means: (A) NIST shall publish the deemed certification in the National Infrastructure Transparency System with a prominent "DEEMED — NOT REVIEWED" designation; (B) the standard remains subject to post-implementation review for one hundred eighty (180) days after implementation, during which any Region, the federal government, or any person or entity demonstrating economic interest may petition the ARB for review; (C) during the provisional period, any affected Region may seek an interim injunction from the ARB upon a showing of probable material barrier, without filing a full petition; (D) upon petition or injunction request, the ARB shall review the standard under the material barrier criteria of subsection (n) and may order modification, suspension, or withdrawal; (E) if the one hundred eighty (180) day provisional period expires without petition or injunction, the deemed certification becomes final;

(4) standards for which Certification has been expressly denied may not be implemented. A Region may resubmit modified standards with a new Technical Impact Assessment;

(5) NIST shall publish all submissions, Technical Impact Assessments, Certifications, Denials, and deemed certifications in the National Infrastructure Transparency System established under Article I, Section 6(q);

(6) Certification decisions, including deemed certifications and provisional-period ARB orders, are subject to de novo judicial review. Any Region, the federal government, or any person or entity demonstrating economic interest may challenge a Certification or Denial.

(r) **Enforcement and Remediation.** Upon finding that a Region has adopted, implemented, or maintained infrastructure standards creating a material barrier in violation of subsection (l):

(1) the ARB may receive complaints from any Region, the federal government, or any person or entity experiencing a material barrier, and shall investigate potential violations;

(2) upon finding a violation, the ARB shall order the Region to modify its standards to achieve compliance within one hundred eighty (180) days. The ARB order shall specify the particular standards creating the barrier and the minimum modifications necessary for compliance;

(3) the Region shall bear all costs of modification, including transition costs for users who adopted the non-compliant Regional standard in reliance on the Region's Certification (if any was issued);

(4) the Region shall compensate affected parties for documented economic losses caused by the material barrier during the period of non-compliance. Compensation shall include direct losses, consequential damages, and litigation costs. No sovereign immunity defense is available against claims under this subsection;

(5) if the Region fails to achieve compliance within the one hundred eighty (180) day remediation period, the federal government may implement compatible standards directly within the Region. Implementation costs shall be recovered from the Region's equalization transfers or other federal payments. The Region shall lose independent standard-setting authority in the affected infrastructure category for five (5) years;

(6) a Region found to have violated subsection (l) three (3) or more times within ten (10) years, whether in the same or different infrastructure categories, shall be designated a Repeat Interoperability Offender. A designated Region shall obtain ARB pre-approval before proposing any infrastructure standard change; upon ARB pre-approval, the Region shall then obtain NIST certification under subsection (q) before implementation. The ARB and NIST shall coordinate to provide a single consolidated decision within one hundred twenty (120) days. If the ARB and NIST fail to issue a consolidated decision within one hundred twenty (120) days, the proposed standard is deemed approved subject to ARB-imposed interim monitoring conditions, including reversibility requirements and quarterly compliance reporting. If the ARB and NIST disagree, the ARB determination shall prevail on questions of material barrier existence under subsection (n), and NIST shall prevail on questions of technical feasibility and standards compliance; disputes over characterization shall be resolved by the ARB with NIST's dissent published in NITS. Designation continues for ten (10) years or until the Region demonstrates sustained compliance;

(7) cross-references to existing enforcement: treble damages under Article I, Section 6(n) apply to violations found to be in bad faith; repeat offender provisions under Article I, Section 6(p) apply independently and concurrently with this subsection.

(s) **Anti-Circumvention and Innovation Protection.**

(1) **Prohibited Circumvention Strategies.** Regions may not:

(A) invoke "innovation," "efficiency," "modernization," "security," or "environmental" justifications for standards whose primary effect is creating barriers to inter-Regional infrastructure connectivity;

(B) change infrastructure standards more frequently than once per calendar year for any single infrastructure category, unless the change is (i) required by a federal Interoperability Floor update, (ii) addresses a documented safety emergency, or (iii) constitutes a cybersecurity vulnerability patch or security update that does not alter the interoperability characteristics of the standard. A Region that changes standards more frequently without meeting exceptions (i) through (iii) creates a rebuttable presumption of a standards arms race intended to prevent neighboring Regions from maintaining compatibility;

(C) condition access to Regional infrastructure, services, or markets on adoption of proprietary Regional standards that exceed Interoperability Floors, except where the Region has obtained Certification under subsection (q) and the condition serves a genuine safety purpose;

(D) use procurement specifications, licensing requirements, or regulatory mandates to effectively require non-interoperable standards for infrastructure serving interstate functions;

(E) adopt standards developed by or exclusively licensed to entities in which the Region, its officials, or their immediate family members hold a material financial interest. A "material financial interest" means direct ownership exceeding one percent (1%) of the entity, a controlling interest regardless of percentage, or an active management or board role. Diversified holdings through mutual funds, pension funds, or index funds do not constitute a material financial interest. Standards adopted in violation of this clause create an irrebuttable presumption of barrier intent;

(F) mandate the use of proprietary hardware, software, or protocols for Critical Infrastructure when equivalent open standards — meaning publicly available, royalty-free specifications maintained by recognized standards organizations — exist and can achieve the same functional requirements. Where no equivalent open standard exists and NIST certifies that a proprietary specification is necessary to meet documented safety or operational requirements that cannot be achieved through available open standards, the Region may adopt the proprietary specification subject to Certification under subsection (q) and a requirement that the Region fund or participate in the development of an equivalent open standard, with progress reported to NIST annually. This prohibition extends to procurement specifications, certification requirements, and interoperability conditions that effectively mandate proprietary solutions.

(2) **Legitimate Innovation Protection.** This section does not prohibit:

(A) genuine technological innovation that advances national capability, provided backward compatibility is maintained under subsection (p)(1);

(B) pilot programs for new technologies approved by NIST, limited to three (3) years and geographically bounded within the Region, provided interstate transit corridors are exempted from the pilot;

(C) Regional standards that exceed Interoperability Floors while maintaining full compatibility, certified under subsection (q);

(D) emergency temporary modifications to infrastructure standards in response to natural disaster, cyberattack, or physical infrastructure failure, provided the modifications are reported to NIST within forty-eight (48) hours, limited to the duration of the emergency, and designed to restore interoperable operation as rapidly as practicable.

(3) **Technology Transition Support.** When Interoperability Floors are updated under subsection (o)(4):

(A) Regions shall have a minimum transition period of three (3) years for major standard changes and one (1) year for minor standard changes. NIST shall classify each update as major or minor at the time of publication;

(B) the Capacity Development Program under Article XXI, Section 7(f), where still operational, and otherwise federal grants appropriated for this purpose, shall support transition costs for Regions with demonstrated fiscal need as certified by the IFC;

(C) legacy equipment and systems conforming to the prior Interoperability Floor shall remain operable during the transition period. No Region or federal agency may require immediate retirement of conforming legacy systems.

(4) **Permanence.** The Interoperability Mandate of subsection (l) is a permanent provision of this Constitution. It is not subject to the sunset provisions of subsection (d), the variance provisions of subsection (e), or any other mechanism that would permit its suspension. Interoperability Floors established under subsection (o) may evolve with technology, but the constitutional requirement that no Region may create material barriers through technical standards is inviolable.

(5) **Data Sovereignty Deconfliction.** Where infrastructure interoperability under this section requires the exchange, verification, or processing of data subject to the data sovereignty provisions of Article I, Section 14:

(A) interoperability mechanisms shall be designed to achieve verification without requiring the transfer of underlying personal data across Regional boundaries, using privacy-preserving protocols such as zero-knowledge proofs, federated queries, or tokenized verification;

(B) Interoperability Floors established under subsection (o) for digital credential and identity systems (subsection (m)(4)) shall be developed in coordination with the data governance framework of Article I, Section 14, and shall not require Regions to compromise data sovereignty protections in order to achieve credential portability;

(C) disputes over the intersection of interoperability requirements and data sovereignty protections shall be resolved jointly by the ARB and the relevant data governance authority within ninety (90) days of petition. If the ARB and data governance authority fail to reach a joint resolution within ninety (90) days, the infrastructure shall operate in a temporary privacy-preserving mode — maintaining interoperability through privacy-preserving protocols under clause (A) without requiring full data exchange — pending judicial review. Either body may refer the dispute to the Constitutional Court, which shall resolve it within one hundred twenty (120) days. Neither the interoperability mandate nor data sovereignty protections shall have automatic precedence; the court shall balance both constitutional interests on the facts of the specific dispute.

---

## 4. Design Rationale

| Mechanism | Problem Addressed | Axiom Connection |
|-----------|-------------------|------------------|
| Interoperability Mandate (l) | Technical barriers = functional secession | Axiom 4 (Floors Not Ceilings) |
| Critical Infrastructure Definition (m) | Scope gaming (what counts as "infrastructure"?) | Axiom 5 (Remove Ambiguity) |
| Material Barrier Standard (n) | Subjective vs. objective barrier determination | Axiom 5 (Remove Ambiguity) |
| Tiered delay thresholds (n)(3) | Sector-agnostic thresholds create false positives/negatives | Axiom 5 (Remove Ambiguity) |
| NIST-calibrated energy threshold (n)(3)(C) | Zero-tolerance latency creates false positives | Axiom 5 (Remove Ambiguity) |
| Federal Interoperability Floors (o) | No baseline compatibility requirement exists | Axiom 4 (Floors Not Ceilings) |
| NIST specification (o) | Commerce too broad — need domain expertise | Axiom 5 (Remove Ambiguity) |
| Interim standard precedence (o)(4) | Timing conflict with transition periods | Axiom 5 (Remove Ambiguity) |
| Backward Compatibility (p) | "Innovation" as pretext for incompatibility | Axiom 1 (Assume Bad Faith) |
| Deemed Approval (q)(3) | Administrative veto by inaction = Gap 116 vulnerability | Axiom 1 (Assume Bad Faith) |
| Provisional status + interim injunction (q)(3) | Deemed approval without controls locks in bad standards | Axiom 3 (Authority to Scale) |
| Enforcement and Remediation (r) | Non-compliance without consequences | Axiom 3 (Authority to Scale) |
| Repeat Offender — default + tie-breaker (r)(6) | Clock miss or disagreement recreates delay veto | Axiom 5 (Remove Ambiguity) |
| Cybersecurity patch exemption (s)(1)(B) | Annual limit chills security updates | Axiom 4 (Floors Not Ceilings) |
| Financial interest materiality (s)(1)(E) | Overbroad definition sweeps in diversified holdings | Axiom 5 (Remove Ambiguity) |
| Vendor lock-in prohibition + safety exception (s)(1)(F) | Proprietary mandates create lock-in; safety-only specs need escape valve | Axiom 1 + Axiom 4 |
| Anti-Circumvention (s)(1) | Gaming via justification labels | Axiom 1 (Assume Bad Faith) |
| Legitimate Innovation (s)(2) | Chilling genuine advancement | Axiom 4 (Floors Not Ceilings) |
| Transition Support (s)(3) | Unfunded mandate for standard changes | Axiom 3 (Authority to Scale) |
| Permanence (s)(4) | Sunset/variance gaming | Axiom 1 (Assume Bad Faith) |
| Data Sovereignty Deconfliction + decision clock (s)(5) | Interoperability vs. privacy deadlock | Axiom 5 (Remove Ambiguity) |

---

## 5. Cross-References

| Provision | Cross-Reference | Relationship |
|-----------|----------------|-------------|
| §4(l) Interoperability Mandate | Art I §6 (Right of Transit) | §6 guarantees transit rights; §4(l) prevents technical circumvention of transit rights |
| §4(m) Critical Infrastructure | Art I §6(q) NITS | NITS provides transparency for infrastructure status; §4(m) defines infrastructure scope for interoperability |
| §4(n) Material Barrier | Art I §6(c) Material Barrier (if exists) | Align barrier definitions across provisions |
| §4(o) Federal Floors | Art II §4(a)-(f) Concurrent Framework | Interoperability Floors follow the same floor/ceiling pattern but with permanence |
| §4(q)(3) Provisional Status | Art I §6(q) NITS | Deemed certifications published with "DEEMED — NOT REVIEWED" designation |
| §4(q)(5) Publication | Art I §6(q) NITS | All submissions and certifications published in NITS |
| §4(r)(4) Damages | Art I §6(m)-(n) Damages/Treble | Cross-reference for bad-faith treble damages |
| §4(r)(5) Federal Implementation | Art I §6(o) Federal Operational Assumption | Same federal implementation authority pattern |
| §4(r)(6) Repeat Offender | Art I §6(p) Repeat Offender | Concurrent designation mechanism |
| §4(s)(3)(B) Transition Support | Art XXI §7(f) Capacity Development | Fiscal support for lower-capacity Regions |
| §4(s)(4) Permanence | Art II §4(k)(1) Permanence | Same permanence pattern as Labor Minimums |
| §4(s)(5) Data Sovereignty | Art I §14 Data Sovereignty | Deconfliction — interoperability without compromising data governance |
| §4(s)(5)(C) Court Referral | Constitutional Court | Dispute resolution for interoperability vs. data sovereignty conflicts |

---

## 6. Change Logs

### v2 Changes (Round 1)

| # | Change | Source | Subsection |
|---|--------|--------|-----------|
| 1 | Tiered delay thresholds: 2hr physical, 5sec digital, real-time energy, 30min telecom | R1+R2 convergent (C1) | (n)(3)(A-D) |
| 2 | "Acting through NIST" added to Commerce delegation | R2-F4 (C7) | (m) final para, (o) intro |
| 3 | Interim standard precedence rule — own 2yr timeline, not subject to major/minor | R1-HIGH (C3) | (o)(4) final sentence |
| 4 | Deemed denial flipped to deemed approval with post-implementation ARB review | R1+R2 convergent (C2) | (q)(3) |
| 5 | Repeat offender dual-veto resolved — ARB first, then NIST, 120-day consolidated clock | R1-MEDIUM (C5) | (r)(6) |
| 6 | Cybersecurity patch exemption from annual change limit | R2-F3 (C4) | (s)(1)(B)(iii) |
| 7 | "Financial interest" defined — >1% or controlling interest; diversified holdings excluded | R1-MEDIUM (C6) | (s)(1)(E) |
| 8 | Vendor lock-in prohibition — proprietary mandates banned where open standards exist | R2-F5 (C8) | (s)(1)(F) NEW |
| 9 | Data sovereignty deconfliction clause — privacy-preserving interoperability | R2-Q8 (C9) | (s)(5) NEW |
| 10 | All 8 open questions resolved per reviewer consensus | R1+R2 | See open questions table |

### v3 Changes (Round 2)

| # | Change | Source | Subsection |
|---|--------|--------|-----------|
| 11 | Repeat offender 120-day clock: deemed approval default with ARB interim monitoring conditions; split tie-breaker (ARB on barrier, NIST on feasibility) | R2-D1 HIGH | (r)(6) |
| 12 | Deemed certification provisional status: "DEEMED — NOT REVIEWED" NITS designation, 180-day provisional period, interim injunction authority on probable barrier showing | R2-D2 MEDIUM | (q)(3)(A-E) |
| 13 | Data sovereignty joint resolution: 90-day decision clock, privacy-preserving interim mode, Constitutional Court referral within 120 days | R2-D3 MEDIUM | (s)(5)(C) |
| 14 | Energy latency: NIST-calibrated threshold replacing zero-tolerance; interim floor of 100ms grid sync / 5sec bulk dispatch | R2-D4 LOW | (n)(3)(C) |
| 15 | Open-standards safety exception: NIST-certified proprietary adoption when no open equivalent exists, with mandatory open-standard development obligation | R2-D5 LOW | (s)(1)(F) |

---

## 7. Subsection Renumbering Note

Article II, Section 4 currently contains subsections (a) through (k). The new subsections begin at (l) and continue through (s). No renumbering of existing subsections is required.

The section group header "#### Critical Infrastructure Interoperability" is added before subsection (l), following the pattern of "#### Constitutional Labor and Safety Minimums" before subsection (h).
