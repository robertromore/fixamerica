# Gap 214 Briefing: The Swarm Loophole (Army of None)

## Step 2 — External Review Briefing

**Gap**: 214 (The Swarm Loophole / Army of None)
**File**: 19-emerging-technology.md, line 1573
**Severity**: Critical
**Status**: Requires Development
**Overlap**: ~20-25% (LOW — genuinely needs new text)

---

## 1. Summary

A Region could acquire military-equivalent force capability while technically complying with State Defense Force personnel caps by purchasing autonomous armed drones, robotic systems, and AI-enabled targeting platforms classified as "equipment" rather than "personnel." With 5,000 human operators and 100,000 autonomous drones, a Region achieves combat capability equivalent to 500,000 soldiers. The proposal prohibits autonomous lethal systems for Regional/State governments, requires human-in-the-loop control for armed systems, creates equivalent force calculations, and closes the private intermediary path.

**Architectural Challenge**: The existing personnel cap framework (Art XI §13) counts "all full-time, part-time, and volunteer members" — but only *people*. Autonomous systems are not "members." The prohibition on "combat aircraft or armed drones" (§13(b)(3)) applies only to State Defense Forces, not Regional Guard forces or law enforcement. The PMC prohibition (Art XI-RF §4) addresses private *human* military contractors but not autonomous *systems* owned directly by government or through shell entities. The Digital Force Equivalence (Art XI §11) establishes the precedent that non-kinetic capabilities count as "force" but applies only to federal cyber operations, not Regional autonomous weapons.

---

## 2. Existing Provisions (What Already Exists)

| Provision | Location | Relevance |
|-----------|----------|-----------|
| SDF armed drone prohibition | Art XI §13(b)(3) | "Combat aircraft or armed drones" prohibited for State Defense Forces — but applies only to SDFs, not Regional Guard or law enforcement |
| SDF personnel cap | Art XI §13(a) | 0.5% of population or 10,000 — "personnel includes all full-time, part-time, and volunteer members" — does not count autonomous systems |
| SDF prohibited capabilities | Art XI §13(b)(1)-(5) | Heavy weapons, armored vehicles, armed drones, offensive cyber, CBRN — SDF-specific; no equivalent for Regional Guard |
| SDF automatic reclassification | Art XI §13(d) | SDF exceeding caps or possessing prohibited capabilities reclassified as National Guard — no equivalent trigger for autonomous weapons |
| Monopoly on Force | Art XI-RF §4(a) | Lethal force as inherently governmental function — addresses *who* can use force (humans, not PMCs), not *what* systems can be deployed |
| PMC prohibition | Art XI-RF §4(b)-(f) | Prohibits private military contractors — addresses human actors; does not cover autonomous systems owned by government |
| Regional PMC prohibition | Art XI-RF §4(f) | Regions may not "hire private military or armed security contractors" or "authorize private entities to exercise law enforcement powers" — human-centric |
| Digital Force Equivalence | Art XI §11 | Cyber-kinetic operations = domestic deployment of force; requires Two-Key — precedent for force equivalence, but for cyber, not autonomous weapons |
| Armed drones as hostilities | Art XI §2(h)(3) | "Use of armed drones" constitutes hostilities for war powers — relevant for federal use abroad, not Regional/State domestic acquisition |
| ETRB | Art II §9 | Classifies emerging technologies into federal/Regional/State domains — potential classification body but no weapons-specific mandate |
| Two-Key authorization | Art XI §3 | Domestic deployment requires dual Presidential + Governor authorization — applies to deployment decisions, not acquisition |
| Regional Guard establishment | Art XI-RF §1 | Creates Regional Guard framework — no force composition restrictions |
| Regional Guard federalization | Art XI-RF §2 | Emergency federalization procedures — could federalize Regional Guard but doesn't prevent autonomous weapons acquisition |
| Counter-deployment authority | Art XI §15(e) | Proportional force response to unauthorized deployment — reactive, not preventive |
| Duty to refuse unlawful orders | Art XI §5 | Military personnel must refuse unconstitutional orders — autonomous systems cannot refuse |

**Key Conclusion**: The constitution has robust personnel caps and capability prohibitions for State Defense Forces (Art XI §13) but **zero equivalent restrictions on Regional Guard forces** (Art XI-RF §§1-3). The SDF armed drone prohibition (§13(b)(3)) does not apply to Regional Guard. The PMC prohibition (Art XI-RF §4) addresses private human contractors but not autonomous systems owned by government. The Digital Force Equivalence (§11) establishes that non-kinetic capabilities count as "force" — this precedent supports extending the equivalence concept to autonomous weapons, but no provision currently does so. Most critically, **no provision counts autonomous systems toward any personnel or force cap**.

---

## 3. Architectural Context

### Article XI-RF Section Map (10-armed-forces.md)

| Section | Content | Status |
|---------|---------|--------|
| §1 | Establishment of Regional Guard Forces | Existing |
| §2 | Federalization of Regional Guard | Existing (subsections a-q) |
| §3 | Integration with State National Guard | Existing (subsections a-h) |
| §4 | Monopoly on Force / PMC Prohibition | Existing (subsections a-h) |
| **§5** | **Next available** | **Primary candidate for Gap 214** |

### Article XI Section Map (military-civilian-control.md — single-topic)

| Section | Content | Gap 214 Relevance |
|---------|---------|-------------------|
| §1 | Civilian Supremacy | Not directly relevant |
| §2 | Congressional War Powers | §2(h)(3) — armed drones as hostilities |
| §3 | Two-Key Authorization | Domestic deployment framework |
| §4 | Prohibited Uses of Armed Forces | Crowd control, political purposes |
| §5 | Duty to Refuse Unlawful Orders | Human-specific; autonomous systems cannot refuse |
| §6 | National Guard and State Defense Forces | Guard structure |
| §7 | Transparency and Accountability | Reporting requirements |
| §8 | Military Justice and Service Member Rights | Not relevant |
| §9 | Counter-Key Authority | Governor refusal mechanism |
| §10 | Judicial Key Override | Judicial intervention |
| §11 | Digital Force Equivalence | **Key precedent** — cyber = force |
| §12 | Infrastructure Independence Guarantees | Not directly relevant |
| §13 | State Defense Force Limitations | **Key provision** — personnel caps, drone prohibition, but SDF-only |
| §14 | Congressional Key Override | Override mechanisms |
| §15 | Officer Corps Independence | Loyalty oath prohibition |
| **§16** | **Next available** | **Alternative placement for Gap 214** |

---

## 4. Design Questions

Reviewers should address:

**D1: Placement.** The proposal targets "Article XI, Section 8" but §8 is occupied (Military Justice). Options:

- (a) Art XI-RF §5 (next available in Regional Guard file) — autonomous weapons as Regional force constraint alongside §§1-4
- (b) Art XI §16 (next available in single-topic amendment) — autonomous weapons as broader military control alongside §§13 (SDF limits), §11 (digital force equivalence)
- (c) Hybrid: primary provision in Art XI-RF §5 (Regional constraint), cross-reference amendments to Art XI §13 (extend SDF prohibitions to include autonomous systems in force count)
- (d) Art XI §13 expansion — add autonomous weapons subsections to existing SDF Limitations section
- (e) Art XI §11 expansion — extend Digital Force Equivalence to cover autonomous weapons

**D2: Scope — Regional Guard vs. all sub-federal.** The proposal prohibits autonomous lethal systems for "Regional, State, or Local governments." Issues:

- (a) Art XI §13 only restricts SDFs. The Regional Guard (Art XI-RF §§1-3) has no equivalent capability restrictions. Should the prohibition apply equally to both?
- (b) Law enforcement agencies are not covered by §13 at all. Should police departments be included?
- (c) Should the prohibition be absolute (no autonomous lethal systems at any sub-federal level) or graduated (stricter for military, lighter for law enforcement)?
- (d) Does a blanket sub-federal prohibition implicitly allow federal autonomous lethal systems? Should the provision address federal use as well?

**D3: Definition of "Autonomous Lethal System."** The proposal defines four categories (§(a)(i)-(iv)). Issues:

- (a) "Without direct human command for each engagement" — does this capture semi-autonomous systems where a human approves a target list but the system executes autonomously?
- (b) "Swarm of unmanned systems capable of coordinated lethal action" — at what number does a "group" become a "swarm"? Two drones coordinating? Twenty?
- (c) "Any system using artificial intelligence to make targeting or engagement decisions" — does this capture existing fire-control systems (auto-turrets, missile guidance) that use AI for targeting?
- (d) "Can operate without continuous human control" — does this capture systems that can operate autonomously but are typically human-controlled? A rifle that *can* be fired remotely is technically capable of operating without continuous control.
- (e) Should the definition focus on capability (what the system *can* do) or deployment configuration (how it *is* operated)?
- (f) Should the ETRB classify which systems fall under the definition, or should the constitution define it?

**D4: Human-in-the-loop standard.** The proposal requires "affirmative human decision for each engagement" and a 1:5 operator ratio. Issues:

- (a) "Affirmative human decision for each engagement" — is this workable at speed? Modern combat operates at machine speed; requiring human approval for each engagement may be tactically impossible.
- (b) 1:5 operator ratio — is this the right number? Too strict (hampers legitimate law enforcement drone use)? Too loose (rubber-stamp oversight)?
- (c) "Real-time human control, not merely human supervision" — how is this distinguished? What constitutes "real-time control" vs. "supervision"?
- (d) Should the HITL standard differ for lethal vs. non-lethal systems?
- (e) Should the HITL standard differ for Regional Guard (military) vs. law enforcement use?
- (f) How does this interact with ETRB technology classification (Art II §9)? Should ETRB certify HITL compliance?

**D5: Equivalent force calculation.** The proposal assigns fixed ratios: armed unmanned = 10 personnel, surveillance drone = 5, AI targeting = 100. Issues:

- (a) Fixed constitutional ratios will become obsolete as technology changes. A 2025 drone is very different from a 2075 drone.
- (b) Should ratios be set by statute or ETRB determination rather than constitutional text?
- (c) The "Federal Military Affairs Commission" referenced in §(e)(iv) does not exist in the constitution. Should this be the ETRB (Art II §9) or the IFC or another existing body?
- (d) Should equivalence be capability-based (destructive power relative to a soldier) or count-based (one drone = X personnel)?
- (e) How does this interact with Art XI §13(a) personnel cap? Does it apply only to SDF or also to Regional Guard?
- (f) Should the calculation apply to federal forces as well? If a Region can only have 10,000 personnel-equivalents, can the federal government deploy unlimited autonomous systems domestically?

**D6: Law enforcement vs. military classification.** Gaming vector G1 ("law enforcement equipment" label). Issues:

- (a) The proposal applies to Regional/State/Local governments broadly, but existing military restrictions (§13) apply only to SDFs. A Region could reclassify its drone force as "police."
- (b) Legitimate police drone use exists (search and rescue, accident documentation, suspect tracking). Where is the line between legitimate law enforcement and de facto military capability?
- (c) Should the provision define a capability threshold below which drones are "law enforcement equipment" and above which they are "military equivalent"?
- (d) Art XI-RF §4(a)(6) reserves "security operations requiring authority to use lethal force" as inherently governmental. Should armed law enforcement drones be treated as inherently governmental too?
- (e) Should lethal capability be the line? All drones with lethal capability = military; non-lethal drones = law enforcement?

**D7: Mass surveillance drone prohibition.** Proposed §(c) prohibits persistent surveillance, facial recognition on drones, cross-jurisdictional tracking, and weaponizable surveillance. Issues:

- (a) Does this duplicate existing privacy protections (Art IV §7 Acquisition Shield, Art IV §10 Digital Papers)?
- (b) "Persistent surveillance of public spaces" — does this prohibit traffic cameras, red-light cameras, and other fixed surveillance?
- (c) "Facial recognition systems on autonomous aerial platforms" — does "autonomous aerial" exclude manually piloted police helicopters with cameras?
- (d) "Systems that could be weaponized through software update" — this is extremely broad. Any drone with a payload capability could theoretically be weaponized through modification. Does this prohibit all drones with payload capacity?
- (e) Should the surveillance prohibition be separated from the military prohibition? They address different constitutional concerns (Fourth Amendment vs. force balance).

**D8: Federal authorization requirement.** Proposed §(d) requires congressional authorization for deployments exceeding 100 armed systems. Issues:

- (a) Congressional authorization for equipment purchases is unusual. Congress authorizes military operations, not procurement. Should this be a reporting requirement instead?
- (b) Does "100 armed unmanned systems" apply per deployment or total inventory? A Region with 99 armed drones in storage needs no authorization?
- (c) Should the threshold be capability-based (equivalent force) rather than count-based?
- (d) "Specific Federal authorization from Congress" — does this mean an Act of Congress, or could it be delegated to an agency?
- (e) Should the ETRB or another body serve as the authorization gateway rather than Congress?

**D9: Private intermediary prohibition.** Proposed §(f) extends prohibitions to entities controlled by or contracting with Regional government. Issues:

- (a) "Entities controlled by or contracting with Regional government" — what constitutes "control"? Minority ownership? Board appointments? Regulatory authority?
- (b) "Public-private partnerships deploying autonomous systems" — does this prohibit PPPs for legitimate infrastructure monitoring (pipeline inspection drones, power line drones)?
- (c) "Systems purchased with Regional funds regardless of nominal ownership" — does this capture federally-funded systems that Regions administer?
- (d) How does this interact with Art XI-RF §4(f) (Regional PMC prohibition)? Is it duplicative or complementary?
- (e) Should there be an explicit look-through principle: any autonomous system that could be commandeered by Regional authority on demand is covered, regardless of ownership structure?

**D10: Enforcement mechanisms.** Proposed §(g) authorizes federal seizure, Guard federalization, prosecution, and personal liability. Issues:

- (a) "Federal seizure of prohibited autonomous systems" — does this require a warrant? Or is it administrative seizure?
- (b) "Immediate federalization of Regional National Guard" — does this follow Art XI-RF §2 procedures or bypass them?
- (c) "Prosecution for illegal weapons possession" — by analogy to what existing crime? Is this a new federal offense?
- (d) Should enforcement be graduated (notice → compliance period → seizure) or immediate?
- (e) Should there be a whistleblower mechanism for personnel who report prohibited autonomous weapons programs?
- (f) Who monitors compliance? DOD? ETRB? A new body?

**D11: Interaction with Art XI §13 (SDF Limitations).** The existing SDF framework provides a pattern. Issues:

- (a) Should Art XI §13(b) be amended to explicitly include "autonomous lethal systems" in the prohibited capabilities list (currently: heavy weapons, armored vehicles, armed drones, offensive cyber, CBRN)?
- (b) Should Art XI §13(a) be amended to count autonomous systems toward the personnel cap using the equivalence formula?
- (c) Should Art XI §13(d) (automatic reclassification) be extended to trigger when a Region acquires prohibited autonomous capabilities?
- (d) Should the Gap 214 provision apply to SDFs as well, or rely on existing §13 prohibitions for SDFs and add new provisions only for Regional Guard?

**D12: Federal autonomous weapons — symmetry question.** The proposal restricts only sub-federal governments. Issues:

- (a) If Regions cannot have autonomous weapons, should the federal government's domestic use also be restricted? An unconstrained federal autonomous force is equally threatening to constitutional balance.
- (b) Should the Two-Key framework (Art XI §3) apply to federal domestic deployment of autonomous systems?
- (c) Should there be a constitutional limit on autonomous-to-human force ratio for federal military?
- (d) Should Art XI §5 (Duty to Refuse) address the fact that autonomous systems *cannot* refuse unlawful orders?

**D13: Constitutional vs. statutory scope.** The proposal has 7 subsections. Which belong in the constitution vs. implementing legislation?

- Constitutional-level candidates:
    - (i) Prohibition on autonomous lethal systems for sub-federal governments
    - (ii) Human-in-the-loop requirement (principle)
    - (iii) Equivalent force calculation mandate
    - (iv) Private intermediary prohibition (principle)
- Statutory-level candidates:
    - (v) Specific operator ratios (1:5)
    - (vi) Specific force equivalence numbers (10, 5, 100)
    - (vii) Specific deployment thresholds (100 systems)
    - (viii) Surveillance drone technical specifications
    - (ix) Federal authorization procedures

**D14: ETRB role in weapons classification.** Art II §9 establishes the ETRB for technology domain assignment. Issues:

- (a) Should the ETRB classify which systems constitute "autonomous lethal systems" under the definition?
- (b) Should the ETRB set the operator ratios and equivalence factors (replacing fixed constitutional numbers)?
- (c) Should the ETRB certify HITL compliance for Regional/State armed systems?
- (d) Can the ETRB waive or create exceptions? (Compare Art III §8(i)(3) — ETRB "may not waive, reduce, or create exceptions" to cognitive liberty rights.)

---

## 5. Gaming Vectors

From the proposal:

| # | Vector | Description |
|---|--------|-------------|
| G1 | Law Enforcement Label | Armed drones classified as "police equipment"; operated by police department, not military; federal military restrictions don't apply |
| G2 | Private Security Intermediary | Drones owned by "private security contractor" controlled by Regional sovereign wealth fund; technical separation provides legal cover |
| G3 | Remote Control Fiction | Region claims drones are "human-controlled" with one operator "supervising" 10,000 drones; nominal HITL compliance |
| G4 | Defensive Only Pretext | Drones positioned at borders for "critical infrastructure protection"; defensive capability identical to offensive |

Additional gaming vectors identified:

| # | Vector | Description |
|---|--------|-------------|
| G5 | Software Update Weaponization | Region purchases non-lethal surveillance drones, then adds lethal capability via software/hardware update after acquisition; "converted" systems bypass initial restrictions |
| G6 | Dual-Use Technology | Commercial agricultural drones, delivery drones, or inspection drones stockpiled in quantity; individually non-threatening but collectively deployable as swarm; each unit below any definitional threshold |
| G7 | Foreign Purchase/Import | Region contracts with foreign manufacturer (China, Turkey) for autonomous systems; import occurs before federal authorization can intervene; possession precedes detection |
| G8 | Research Exemption | Region establishes "autonomous systems research facility" at state university; systems developed for "research" are tested, refined, and warehouse-ready; "research" exemption shields acquisition |
| G9 | Incremental Acquisition | Region acquires systems one at a time below any deployment threshold; no single purchase triggers authorization; aggregate capability builds over years |
| G10 | Multi-Region Pooling | Three Regions each acquire 30 armed systems (below 100-system threshold); mutual defense compact commits all 90 systems to joint deployment under unified command |
| G11 | Contractor-Operated Systems | Region hires private contractor to *operate* autonomous systems (not just own them); Region claims it doesn't "possess" the systems; contractor-operated drone fleet is nominally independent |
| G12 | Non-Lethal Redesignation | Autonomous systems equipped with "non-lethal" payloads (tear gas, rubber bullets, sonic weapons) that are lethal in practice when deployed at scale; "non-lethal" classification avoids prohibition |
| G13 | Critical Infrastructure Protection | Autonomous systems deployed to protect nuclear plants, dams, power grid under federal critical infrastructure mandate; "federally authorized" protection becomes standing autonomous force |
| G14 | Militia Classification | Region classifies autonomous systems as "well-regulated militia" equipment under Second Amendment; claims constitutional right to autonomous weapons for collective defense |

---

## 6. Verification Questions

**V1**: Does Art XI-RF (10-armed-forces.md) have any capability restrictions on Regional Guard forces comparable to Art XI §13's SDF restrictions?
**Answer**: NO — Art XI-RF §§1-3 establish, federalize, and integrate Regional Guard forces. §4 prohibits PMCs. No section restricts Regional Guard capability, personnel ratios, or weapons systems. The SDF restrictions in Art XI §13 are SDF-specific.

**V2**: Does Art XI §13(b)(3) ("combat aircraft or armed drones") cover autonomous ground systems, autonomous naval systems, or autonomous weapons that are not drones?
**Answer**: NO — §13(b)(3) says "combat aircraft or armed drones." Ground-based autonomous weapons, autonomous naval vessels, robotic sentries, and non-aerial autonomous systems are not covered.

**V3**: Does Art XI §11 (Digital Force Equivalence) create precedent for counting autonomous weapons as "force"?
**Answer**: YES — §11(a) defines "domestic deployment of force" to include cyber-kinetic operations, infrastructure interdiction, and financial manipulation — all non-physical forms of force. The functional test in §11(c) says determination "shall be based on its practical effect... not on the mechanism employed or the label assigned." This directly supports extending force equivalence to autonomous weapons.

**V4**: Does the ETRB (Art II §9) have explicit authority over military technology classification?
**Answer**: PARTIAL — §9 gives ETRB authority over "emerging technologies" generally, with criteria including "systemic risks" and "catastrophic or irreversible harm." No explicit military carve-out, but no explicit inclusion either. The ETRB classifies technologies into federal/Regional/State domains — it does not prohibit technologies.

**V5**: Does Art XI-RF §4 (Monopoly on Force / PMC Prohibition) cover autonomous systems owned and operated directly by Regional government?
**Answer**: NO — §4 addresses private military contractors, private entities, and private militia organizations. Autonomous systems owned and operated directly by Regional government are not "private" and therefore fall outside §4's scope. The section assumes force is exercised by *humans* (sworn officers vs. private contractors).

---

## 7. Reviewer Instructions

Please provide:

1. **Findings** (numbered, with severity: HIGH/MEDIUM/LOW)
2. **Recommendations for each design question** (D1-D14)
3. **Additional design questions** not covered above
4. **Additional gaming vectors** not covered above
5. **Verification answers** (V1-V5) if you can determine them
6. **Draft text** improvements or concerns with the proposed language
7. **Design decisions summary** table

Focus especially on:

- The placement question: Art XI-RF §5 (Regional Guard file) vs. Art XI §16 (single-topic) vs. hybrid with §13 cross-references
- Whether the prohibition should be absolute (no autonomous lethal systems for sub-federal) or regulated (with HITL and force equivalence)
- The definition of "autonomous lethal system" — too broad (captures legitimate systems) or too narrow (easily gamed through relabeling)
- The operator ratio and force equivalence numbers — should these be constitutional or statutory/ETRB-determined?
- The law enforcement exception problem (G1, G12) — where is the line between police drone and military drone?
- The federal symmetry question (D12) — should federal domestic autonomous weapons also be restricted?
- Whether the mass surveillance drone prohibition (§(c)) should be separated from the military prohibition
- The software update weaponization vector (G5) — how to address systems that are non-lethal at acquisition but lethal after modification
- Whether Art XI §13 needs cross-reference amendments to extend SDF restrictions to autonomous systems
- The ETRB role: classifier, certifier, ratio-setter, or all three?
