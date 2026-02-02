# Gap 213 — Neural Warrant (Cognitive Liberty)

## External Review Briefing

**Date**: 2026-02-01
**Gap**: 213 — Neural Warrant (Cognitive Liberty)
**Severity**: Critical
**Category**: Emerging Technology
**Overlap with existing provisions**: ~10-15% (VERY LOW)
**Recommendation**: New constitutional text required

---

## 1. Gap Summary

The Fourth Amendment protects "persons, houses, papers, and effects" from unreasonable searches. It does not explicitly protect neural data — the electrical patterns of thought itself. Brain-computer interfaces (BCIs) are emerging commercially (Neuralink, etc.), and without constitutional protection, governments could mandate neural monitoring under safety pretexts, effectively criminalizing thought.

**The core failure**: A Region mandates "attention monitoring headsets" for commercial drivers. The safety justification provides legal cover. Mission creep expands monitoring to ideological screening. No Fourth Amendment protection because BCIs are "voluntarily" worn as a condition of employment.

### Proposed resolution

The gap analysis proposes Article III-RF §12 (Cognitive Liberty Shield). The placement needs correction — Art III currently has §§1-7, and Art III-RF §12 doesn't align with the RF architecture. Proposed correction: **Art III §8** (next available in Rights Floors), bumping DLRS from proposed §8 to proposed §9.

Six subsections:

- **(a)** Neural privacy as fundamental right (brain patterns, BCI data, inferences)
- **(b)** Prohibition on compelled neural access
- **(c)** Warrant requirement for neural data
- **(d)** Absolute mental privacy (thoughts can't be criminalized)
- **(e)** Private sector limitations
- **(f)** Enforcement (exclusionary rule, statutory damages, personal liability)

---

## 2. Overlap Analysis

| Proposal Element | Existing Provision | Coverage | Notes |
|---|---|---|---|
| Neural privacy as right (a) | Art III §7 — biometric records as property | ~10% | General biometric protection; neural not mentioned |
| Compelled access prohibition (b) | None | 0% | No comparable provision anywhere in the constitution |
| Warrant requirement (c) | Art IV §7 (Acquisition Shield) + §10 (Digital Papers) | ~25% | Cover warrants for biometric/digital data; strong scaffolding but neural not specified |
| Absolute mental privacy (d) | None | 0% | Entirely new constitutional principle |
| Private sector limitations (e) | Art IV §10(f) — third-party data obligations | ~15% | Third-party duties exist; no neural-specific employer restrictions |
| Enforcement (f) | Art III §§6-7 enforcement clauses | ~20% | Similar patterns (voidability, personal liability); no neural-specific remedies |

**Strong existing scaffolding:**

- **Art IV §7 (Acquisition Shield)** — Already covers biometric data purchase, abrogates third-party doctrine, equivalence principle (can't buy what you'd need a warrant to search)
- **Art IV §10 (Digital Papers)** — Extends Fourth Amendment to data in third-party custody, covers health data, aggregation principle
- **Art III §7 (Digital Habeas Corpus)** — Biometric records as individual property, analog redundancy, data portability

These provisions protect data *about* a person. None protects *thoughts themselves*. The conceptual gap is that existing provisions address the *container* (data) but not the *content* (cognition).

---

## 3. Cross-Gap Interactions

| Related Gap | Status | Connection |
|---|---|---|
| Gap 69 (Data Privacy) | Partially Mitigated | Neural data as most sensitive personal data |
| Gap 208 (Black Box / Algorithmic Tyranny) | ✅ Resolved (Art II §7-A + Art III §6) | AI analysis of neural patterns requires human review under §6 |
| Gap 209 (Digital Death / Identity Revocation) | ✅ Resolved (Art III §7) | Neural identity as component of digital identity |
| Gap 218 (Commercial Data Purchase) | ✅ Resolved (Art IV §7) | Acquisition Shield covers biometric purchases but not neural mandates |
| Gap 245 (Digital Papers) | ✅ Resolved (Art IV §10) | Third-party data protection extends to neural data held by BCI companies |
| Gap 19 (Neurotechnology) | Partially Mitigated | General neurotechnology regulation |

---

## 4. Design Questions

Reviewers should address:

**D1: Placement.** The proposal says Art III-RF §12, but the RF architecture places technology-era rights in the core Art III in 02-powers-and-rights.md (§§6-7 are already there). Options:

- (a) Art III §8 in 02-powers-and-rights.md — continues the pattern of §6 (human review), §7 (digital habeas corpus), §8 (cognitive liberty). Bumps DLRS from proposed §8 to §9.
- (b) Extend Art IV §7 (Acquisition Shield) or §10 (Digital Papers) with neural-specific subsections — keeps search/seizure provisions together but mixes substantive right with procedural protection
- (c) Art III §7 expansion — add neural data as a subcategory of biometric/identity data within digital habeas corpus
- Which placement best distinguishes the *substantive right* (thoughts are private) from the *procedural right* (data requires a warrant)?

**D2: Relationship to existing search-and-seizure provisions.** The warrant requirement in §(c) substantially parallels Art IV §7 (Acquisition Shield) and §10 (Digital Papers). Issues:

- (a) Should §(c) cross-reference Art IV §§7/10 rather than creating a parallel warrant requirement?
- (b) The Acquisition Shield already abrogates the third-party doctrine for biometrics — does Gap 213 need to re-abrograte it for neural data?
- (c) Could the Acquisition Shield's "information covered" list (§7(b)) simply be extended to include neural data, making a separate warrant section unnecessary?
- (d) If §(c) is kept, how does it interact with Art IV §10's exclusionary rule, notice requirements, and minimization standards?

**D3: "Absolute mental privacy" — scope and consequences.** Subsection (d) states "neural patterns may not be used as evidence of intent for any crime." Issues:

- (a) This prohibits using brain scans to prove mens rea even when the defendant consents — is this the intent?
- (b) If a defendant voluntarily submits their own neural data as exculpatory evidence, can the prosecution rebut it with neural evidence?
- (c) "Pre-crime prediction is prohibited" — does this extend to risk assessment tools used in bail/sentencing that incorporate behavioral (not neural) data?
- (d) "Thoughts, beliefs, and intentions may not be criminalized" — this is already the law (thoughts aren't crimes). What does constitutionalizing it add beyond declaratory effect?
- (e) Should there be a distinction between *reading* thoughts (searching the mind) and *using* voluntarily disclosed thoughts (evidence rules)?

**D4: Medical and therapeutic exception.** BCIs are used therapeutically for Parkinson's, epilepsy, paralysis, and depression. Issues:

- (a) Medical providers treating patients with therapeutic BCIs necessarily collect neural data — are they subject to the private sector restrictions in §(e)?
- (b) Should there be an explicit therapeutic/research exception?
- (c) If a patient with a therapeutic BCI commits a crime, can the BCI data be subpoenaed? The warrant requirement in §(c) would apply, but should therapeutic BCIs have heightened protection?
- (d) Neural data collected during emergency medical treatment (unconscious patient) — covered by medical privacy or by this provision?

**D5: Private sector scope.** Subsection (e) restricts private employers and insurers. Issues:

- (a) The Constitution typically restricts *government*, not private actors. Private restrictions usually come from statute (Civil Rights Act, ADA, etc.). Is a constitutional private-sector restriction appropriate here?
- (b) If the justification is that private neural monitoring inevitably flows to government, the Acquisition Shield (Art IV §7) already blocks government purchase of such data. Is §(e) redundant?
- (c) Should §(e) be narrowed to prohibit private actors from *sharing* neural data with government (which the Acquisition Shield handles) rather than prohibiting private collection entirely?
- (d) Alternative: constitutionalize only the government prohibition; leave private sector regulation to statute

**D6: Statutory damages in constitutional text.** Subsection (f)(ii) sets "$100,000 per violation." Issues:

- (a) Hard dollar amounts in constitutional text become obsolete through inflation
- (b) Art III §7 uses "treble damages" (ratio-based, inflation-proof). Art IV §7(f)(iv) uses "1,000 FPU per incident" (indexed unit)
- (c) Should this use FPU (Federal Payment Unit) or a ratio-based approach consistent with existing provisions?
- (d) What is the right magnitude? Neural violations are arguably more severe than data violations

**D7: Emergency and national security exceptions.** The proposal provides no exceptions. Issues:

- (a) Is absolute mental privacy truly absolute? What about a nuclear terrorism suspect who knows the location of a device?
- (b) The existing constitution provides emergency exceptions for some rights (emergency powers can suspend certain processes). Should cognitive liberty be in the "eternity clause" category (never suspendable)?
- (c) If there is an exception, what standard applies? Super-warrant? FISA-like court? Multi-key authorization?
- (d) The ticking-bomb scenario is often cited but extremely rare — does constitutionalizing an exception for it create an exploitable loophole?

**D8: Cognitive manipulation.** The proposal addresses *reading* thoughts but not *writing* to the brain. Issues:

- (a) Should there be a prohibition on government use of technology to *influence* brain activity (transcranial stimulation, neural modulation)?
- (b) Should "cognitive liberty" include freedom from unwanted neural influence, not just freedom from surveillance?
- (c) If a government correctional program uses neural modulation for "rehabilitation," is this covered?
- (d) How does this interact with existing Eighth Amendment protections?

**D9: Children and incapacitated persons.** Issues:

- (a) Can parents consent to neural monitoring of their children (e.g., educational attention monitoring)?
- (b) Can guardians consent to neural monitoring of incapacitated persons?
- (c) Should there be age-based restrictions on BCI use regardless of consent?
- (d) The "compelled access" prohibition in §(b) would prevent schools from mandating attention-monitoring BCIs — is this the intent?

**D10: Evidentiary asymmetry.** If neural data can never be used as evidence of intent:

- (a) A defendant could have neural data proving innocence but refuse to disclose it
- (b) A defendant could voluntarily submit favorable neural data while the prosecution cannot challenge with neural counter-evidence
- (c) This creates an asymmetric evidence regime where neural data is admissible only for defendants
- (d) Should the rule be: neural data admissible only with the *subject's* consent, regardless of which party offers it?

**D11: Interaction with ETRB.** The ETRB (Art II §9) assigns provisional jurisdiction for emerging technologies. Neurotechnology is emerging.

- (a) Should the ETRB have authority to classify specific neurotechnologies as "neural data collection devices" subject to this section?
- (b) Should the ETRB be able to temporarily authorize neural monitoring for safety purposes (e.g., pilot fatigue detection) pending congressional action?
- (c) If the ETRB assigns neurotechnology to Regional jurisdiction, does this section's federal floor override?
- (d) The ETRB framework is designed for regulatory uncertainty; cognitive liberty should not be uncertain. Should neurotechnology be carved out of ETRB jurisdiction?

**D12: International and military context.** Issues:

- (a) Military use of BCIs (enhanced targeting, communication) — does this section apply to military personnel?
- (b) Intelligence agencies using neural interrogation techniques on foreign nationals — covered?
- (c) Foreign BCIs used by US persons — does this section apply extraterritorially?
- (d) Should there be a military/intelligence carve-out, or does absolute mental privacy apply to all government actors?

---

## 5. Gaming Vectors

Reviewers should evaluate whether the proposed text closes these attack paths:

**G1: The "safety first" pretext.** Region mandates "fatigue detection" headsets for commercial drivers, pilots, first responders. Stated purpose is safety. Actual capability includes ideological monitoring. The proposal prohibits compelled BCI use, but what about genuine safety monitoring that collects neural data as a byproduct? Can a Region argue that fatigue monitoring is "not neural data" because it only measures "attention levels"?

**G2: The "voluntary" coercion.** No law mandates BCIs. But every employer requires them. Insurance gives discounts for BCI wearers. Schools monitor student attention. The proposal's §(b)(iv) prohibits "incentive structures that effectively coerce neural monitoring" — but where is the line between a genuine benefit and coercive incentive? Is a 50% insurance discount coercive?

**G3: The "metadata, not thoughts" defense.** Region claims it collects only "attention metrics" (awake/drowsy), not actual thoughts. But attention patterns over time reveal ideology, interests, and beliefs. The proposal covers "inferences about thoughts, emotions, intentions, or beliefs derived from neural data" in §(a)(iii) — but is "attention level" an inference about thoughts?

**G4: The corporate pipeline.** Private company mandates BCI for employment. Company analyzes neural data. Government doesn't directly access neural data — it accesses *employment records* that note "employee showed concerning neural patterns." The information laundering circumvents the warrant requirement. The Acquisition Shield (Art IV §7) may address this, but should this section explicitly close the employment-records back door?

**G5: The therapeutic Trojan horse.** Government subsidizes therapeutic BCIs for veterans (PTSD treatment). BCIs collect neural data as part of treatment. Government uses "treatment compliance monitoring" to access neural data. The medical exception (if any) becomes an access pathway.

**G6: The consent manufacture.** Region creates a "Neural Freedom Card" — citizens who voluntarily submit to periodic neural scans receive tax benefits, expedited government services, and priority housing. No one is *compelled*, but non-participants face significant disadvantages. At what point does voluntary consent become manufactured consent?

**G7: The educational monitoring expansion.** Schools deploy "attention monitoring" BCIs to "improve learning outcomes." Parents consent because it's presented as educational technology. By the time children are adults, constant neural monitoring is normalized. The next generation doesn't perceive it as a rights violation.

**G8: The inference gap.** The proposal protects "neural data." But what about behavioral inference systems that don't use BCIs? AI that infers emotional state from facial expressions, voice patterns, and body language achieves similar results to neural monitoring without any BCI. Is this "neural data" or just sophisticated behavioral observation?

**G9: The foreign BCI.** A foreign government requires its BCI-equipped citizens traveling in the US to maintain active neural monitoring. The US cannot compel foreign removal of BCIs, but the foreign government now has neural surveillance capability on US soil. Does this section apply to foreign government actions affecting persons on US territory?

**G10: The posthumous loophole.** A person dies while wearing a BCI. Their stored neural data contains thoughts, memories, and intentions. Can this data be accessed without a warrant since the Fourth Amendment rights of the deceased are uncertain? The proposal doesn't address posthumous neural privacy.

**G11: The "not a BCI" relabeling.** As neurotechnology advances, the line between a BCI and a wearable sensor blurs. A smartwatch measures brain-adjacent electrical activity through the skull. An earpiece detects neural signals through the ear canal. A "smart pillow" monitors brain activity during sleep. If the proposal only covers "brain-computer interfaces," these adjacent devices may escape regulation.

---

## 6. Verification Questions

**V1: Does Art IV §7 (Acquisition Shield) already cover government purchase of neural data from commercial providers, making §(c)(iv) partially redundant?**

**V2: Does Art IV §10 (Digital Papers Protection) already extend Fourth Amendment protection to neural data held by BCI companies as "health data held by medical devices" (§10(d)(vi))?**

**V3: Does Art III §7 (Digital Habeas Corpus) already classify neural biometric data as "biometric records" that are "property of the individual" under §7(a)?**

**V4: Does the "absolute mental privacy" in §(d) conflict with the Medical Fitness Panel (Art II §20) that requires neurological and cognitive assessment of the President?**

**V5: Does §(e)'s private sector restriction conflict with the general principle that constitutional rights restrain government, not private actors, absent enabling legislation?**

---

## 7. Proposed Draft Text

The gap analysis proposes the following text (corrected to Art III §8):

> **(a) Neural Privacy as Fundamental Right.** The right of the people to be secure in their mental integrity and neural data shall not be violated. This right encompasses:
>
> - (i) all electrical, chemical, or biological patterns of brain activity;
> - (ii) data derived from brain-computer interfaces, neural implants, or neuroimaging;
> - (iii) inferences about thoughts, emotions, intentions, or beliefs derived from neural data;
> - (iv) any technology that reads, interprets, or influences brain activity.
>
> **(b) Prohibition on Compelled Neural Access.** No government may:
>
> - (i) compel the use of brain-computer interfaces as a condition of employment, licensure, or public benefit;
> - (ii) require neural monitoring for any purpose, including safety;
> - (iii) condition any right, privilege, or benefit on submission to neural data collection;
> - (iv) create incentive structures that effectively coerce neural monitoring.
>
> **(c) Warrant Requirement.** Government access to neural data requires:
>
> - (i) a warrant issued upon probable cause of a specific completed physical crime;
> - (ii) the warrant must describe with particularity the neural data sought;
> - (iii) "pre-crime" prediction or ideological screening may never justify neural access;
> - (iv) neural data may not be obtained through third-party doctrine or employer cooperation.
>
> **(d) Absolute Mental Privacy.** Notwithstanding any other provision of law:
>
> - (i) thoughts, beliefs, and intentions — as distinct from actions — may not be criminalized;
> - (ii) neural patterns may not be used as evidence of intent for any crime;
> - (iii) "pre-crime" interventions based on neural prediction are prohibited;
> - (iv) the contents of the mind are absolutely private from government intrusion.
>
> **(e) Private Sector Limitations.** Private employers and insurers may not:
>
> - (i) require neural monitoring as a condition of employment or coverage;
> - (ii) use neural data for hiring, firing, or coverage decisions;
> - (iii) share neural data with government without warrant;
> - (iv) create databases of neural patterns accessible to government.
>
> **(f) Enforcement.** Violation of this section:
>
> - (i) renders any evidence obtained through neural surveillance inadmissible;
> - (ii) creates civil cause of action with statutory damages of $100,000 per violation;
> - (iii) subjects officials to personal liability for willful violations;
> - (iv) authorizes injunctive relief against ongoing neural monitoring programs.

---

## 8. Review Instructions

Please provide:

1. **Findings** (numbered, with severity: HIGH/MEDIUM/LOW)
2. **Recommendations for each design question** (D1-D12)
3. **Additional design questions** not covered above
4. **Additional gaming vectors** not covered above
5. **Verification answers** (V1-V5) if you can determine them
6. **Draft text** improvements or concerns with the proposed language

Focus especially on:

- Whether "absolute mental privacy" should truly be absolute or have narrow exceptions
- The relationship to existing Art IV §§7/10 (avoid duplication while maintaining distinct substantive right)
- Whether private sector restrictions belong in constitutional text or should be statutory
- The evidentiary asymmetry problem (D10) — neural data as defense but not prosecution evidence
- The cognitive manipulation gap (D8) — reading vs. writing to the brain
- The "metadata, not thoughts" defense (G3) and the "not a BCI" relabeling (G11)
- Medical/therapeutic exception scope (D4)
- The hard dollar amount in enforcement (D6) — should use FPU or ratio
