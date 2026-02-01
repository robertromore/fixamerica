# Briefing: Gap 226 — Citizenship Void (Who Are "We"?)

## For External Review — Multi-LLM Gap Resolution Protocol, Step 2

---

## 1. Problem Statement

The Regional Federal constitutional framework references "citizens" throughout but **never defines who is a citizen**. The current Fourteenth Amendment defines citizenship through birthright: "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens." If this framework replaces or supersedes the existing Constitution without explicitly incorporating this definition, a dangerous void emerges.

**Why this matters in the RF context:**

- Article I §8 grants "all citizens" freedom of movement — but who counts?
- Article VII §1(d) restricts voting to "natural persons who are citizens" — but who qualifies?
- Article XIV-RF §5 grants standing to "any citizen" — but who has standing?
- Article II §1 lists "immigration and citizenship" as a federal power, and §1(e)(1)(iv) makes "immigration and naturalization" exclusively federal — but neither defines citizenship itself

The constitution allocates citizenship as a federal power and grants rights based on citizenship, yet the foundational question — who is a citizen? — is left undefined.

**The attack vector:** A political faction could argue that "citizens under this Constitution" requires affirmative consent, registration, or oath — enabling mass disenfranchisement of populations that did not actively participate in constitutional adoption. Naturalized citizens could be argued to hold "lesser" citizenship. Residents of non-consenting states could face citizenship uncertainty.

**Severity:** Critical | **Priority:** P1 (Immediate — foundational to every other provision)

---

## 2. Existing Provisions

### 2.1 Citizenship as Federal Power

**Article II, Section 1 — Enumerated Federal Powers** (02-powers-and-rights.md):

> Federal authority is limited to powers expressly enumerated herein, including:
> - immigration and citizenship,

**Article II, Section 1(e)(1)(iv) — Exclusive Federal Domains**:

> (1) Exclusive Federal Domains. The following domains are exclusively federal, and no Regional or State law may operate within them:
> - (iv) Immigration and naturalization;

*Analysis:* Citizenship is allocated as a federal power and naturalization as an exclusive federal domain, but neither provision defines who is a citizen or how citizenship is established.

### 2.2 Provisions That Reference "Citizens"

**Article I, Section 8(a) — Freedom of Movement** (01-regional-structure.md line 621):

> All citizens of the United States shall have the right to:
> - travel freely between and within Regions,
> - establish residence in any Region,
> - seek employment in any Region,
> - access public services on equal terms with residents after establishing residence.

**Article VII, Section 1(d) — Natural Person Franchise Exclusivity** (election-reform.md):

> The right to vote in any election conducted under this Constitution is held exclusively by natural persons who are citizens of the United States. No State or Region may grant, extend, or recognize voting rights to corporations, artificial entities, or automated systems, or weight votes by property, tax contribution, or wealth.

**Article XIV-RF, Section 5(a) — Constitutional Standing** (09-judiciary.md):

> Any citizen of the United States shall have standing to bring an action in federal court to:
> (1) enjoin ultra vires acts by any branch of the Federal Government, any Region, or any State [...]

**Article IV, Section 6 — Census** (03-regional-governance.md line 373):

> (2) unadjusted for citizenship status, incarceration, or other factors that might be manipulated;

*Analysis:* At least 4 articles reference "citizens" without defining the term. The census provision implicitly distinguishes citizens from non-citizens for apportionment. Each provision depends on a citizenship definition that does not exist in the constitutional text.

### 2.3 "Any Person" vs. "Citizen" Design Choice

**Article III, Section 4 — The Unwaivable Core** (Design Rationale, 02-powers-and-rights.md line 1531):

> **Why "Any Person" Rather Than "Citizen" in the Unwaivable Core?**
>
> Section 4 uses "any person" rather than "citizen" deliberately. Adhesion contracts, forced arbitration clauses, and class action waivers affect all persons within U.S. jurisdiction — non-citizen workers, lawful residents, tourists, and visitors are equally subject to terms-of-service extraction. Limiting protection to citizens would create a two-tier rights regime where non-citizens face even greater contractual coercion. The Fourteenth Amendment's Due Process and Equal Protection Clauses already protect "any person," and Section 4 follows this established scope.

*Analysis:* This is the only reference to the Fourteenth Amendment in the entire design. The design consciously distinguishes "any person" protections (Article III §4) from "citizen" protections (Article I §8, Article VII, Article XIV-RF §5), but never defines the threshold between them. This design rationale entry itself acknowledges the Fourteenth Amendment as the source of "any person" scope — yet the Fourteenth Amendment's citizenship clause is not incorporated anywhere.

### 2.4 The Critical Conflict: Citizenship Stripping

**Article XI-RF, Section 1(e) — Foreign Operations** (10-armed-forces.md line 241):

> (e) **Foreign Operations.** U.S. persons may not:
>
> - (1) serve in foreign private military organizations;
> - (2) provide military training or services to foreign governments without State Department license;
> - (3) participate in combat operations for any entity other than the United Regions armed forces.
>
> Violation strips U.S. citizenship and creates permanent ineligibility for any government employment or contract.

*Analysis:* This is the **only denaturalization provision** in the entire constitutional framework. It strips citizenship for unauthorized foreign military service — a penalty that directly conflicts with Gap 226's proposed §(c), which limits citizenship loss to voluntary renunciation and treason conviction only. This conflict must be resolved: either §1(e) survives as an exception, or §226(c) supersedes it.

---

## 3. Proposed Resolution (As Written in Gap File)

**Original Proposed Placement:** Article I-RF, Section 14

**Placement Error Analysis — TRIPLE ERROR:**

| Error | Detail |
|-------|--------|
| 1. Invalid suffix | "-RF" suffix is invalid for Article I. Article I IS the RF core article — it does not have a separate RF supplement |
| 2. Section occupied | Article I, Section 14 is occupied by Professional Credential Protection (immunity for federal officers' professional licenses) |
| 3. Wrong article | Citizenship definition is not a regional structure provision. Article I covers regional establishment, boundaries, inter-regional relations, and commerce |

**Corrected Placement:** Article III, Section 5

**Rationale for Article III §5:**

- Article III is the Bill of Rights / Individual Rights article
- §§1-4 establish rights principles (Floors Not Ceilings, Subsidiarity, Hierarchy of Law, The Unwaivable Core)
- Citizenship is the foundational status upon which the rights framework operates
- §5 would define who the primary rights-holders are, logically preceding any rights enforcement
- The "any person" vs. "citizen" distinction already noted in §4's design rationale makes this placement especially logical — §5 would clarify the line between universal protections and citizenship-dependent rights
- Follows the pattern of the current 14th Amendment being part of the Bill of Rights

### Proposed Text (5 subsections, as written)

**(a) Birthright Citizenship** — jus soli: "All persons born within the territory of the United States, regardless of parentage." Plus naturalized citizens.

**(b) Continuity Provision** — All persons who held citizenship under "the Constitution of 1787" retain citizenship without oath/registration/consent.

**(c) Non-Severability** — Citizenship may only be lost through: (1) voluntary written renunciation (90-day waiting period, mandatory counseling); or (2) criminal conviction for treason, following jury trial and exhaustion of appeals.

**(d) Equal Citizenship** — No distinction between birth and naturalized citizens. No deportation of citizens.

**(e) Prohibition on Citizenship Conditions** — No oath, registration, or consent required to exercise citizenship rights.

---

## 4. Design Questions

### D1: Placement

The proposal targets Article I-RF §14 (triple error). Corrected to Article III §5. Do reviewers agree, or is there a better location?

- **A:** Article III §5 (Bill of Rights, next available — foundational status for rights framework)
- **B:** Article I §25 (next available in Regional Structure — near Freedom of Movement §8)
- **C:** New standalone amendment (citizenship warrants its own article)
- **D:** Other placement

### D2: Jus Sanguinis (Children Born Abroad)

The proposal covers only jus soli (born on U.S. soil) and naturalization. It is silent on children born abroad to U.S. citizen parents — currently covered by statute (8 U.S.C. §1401), not constitutional right.

- **A:** Constitutional jus sanguinis — children born abroad to at least one citizen parent are citizens by right
- **B:** Statutory delegation — Congress determines jus sanguinis scope (status quo)
- **C:** Constitutional jus sanguinis with congressional adjustment authority (constitutional floor, statutory detail)

### D3: "Subject to the Jurisdiction Thereof"

The current 14th Amendment includes "and subject to the jurisdiction thereof." The proposal drops this entirely ("regardless of parentage"). This phrase has been debated regarding children of undocumented immigrants, diplomats, and invading forces.

- **A:** Drop entirely (as proposed) — all births on U.S. soil confer citizenship regardless
- **B:** Retain with narrow exceptions — exclude only children of accredited diplomats and hostile occupying forces
- **C:** Retain verbatim — preserve current 14th Amendment language and its judicial interpretations
- **D:** Replace with functional language ("excluding only persons with diplomatic immunity from U.S. jurisdiction")

### D4: Territorial Scope

"Born within the territory of the United States" — does this include territories? American Samoa currently does NOT grant birthright citizenship (residents are "nationals" but not "citizens"). The proposal does not address this.

- **A:** All territories included — birthright citizenship in all U.S. territories (changes American Samoa status)
- **B:** States and Regions only — territories addressed separately per Article XX
- **C:** Constitutional principle + statutory designation — "territory" includes any area under U.S. sovereignty, but Congress may designate procedures for territories with special status
- **D:** Explicit enumeration — name all included territories

### D5: Article XI-RF §1(e) Denaturalization Conflict

The only existing denaturalization provision strips citizenship for unauthorized foreign military service. Gap 226 §(c) limits citizenship loss to voluntary renunciation and treason only.

- **A:** §226 supersedes — only voluntary renunciation and treason (XI-RF §1(e) penalty reduced to permanent ineligibility and criminal prosecution, not denaturalization)
- **B:** Add military conduct as third exception — expand §(c) to include unauthorized foreign military service
- **C:** Treat as voluntary renunciation equivalent — unauthorized foreign military service constitutes constructive renunciation
- **D:** Supersede with carve-out — §226 controls generally, but Congress may provide for loss of citizenship upon conviction (not administrative finding) for unauthorized foreign combat

### D6: Dual Citizenship

The proposal is silent on dual citizenship. Currently, the U.S. tacitly permits dual citizenship but does not formally recognize it.

- **A:** Explicit recognition — dual citizenship permitted; no person may be required to renounce foreign citizenship as condition of U.S. citizenship
- **B:** Silent (status quo) — leave to statute
- **C:** Constitutional non-interference — "citizenship under this Constitution is not affected by citizenship in another nation"
- **D:** Prohibition — U.S. citizenship is exclusive (not recommended but should be considered)

### D7: Office-Holding Requirements

The current Constitution requires the President to be a "natural-born citizen." This framework may or may not preserve that requirement. If birthright and naturalized citizenship are constitutionally equal (§(d)), does the natural-born requirement survive?

- **A:** Abolish — equal citizenship means equal eligibility; no natural-born requirement
- **B:** Preserve explicitly — "notwithstanding subsection (d), the requirement that the President be a citizen by birth is preserved"
- **C:** Delegate to Article IV or Article VIII — address office-holding requirements in governance or executive provisions
- **D:** Modify — require citizenship for minimum duration (e.g., 20 years) rather than birth

### D8: Regional Citizenship

Article I §8 allows citizens to "establish residence in any Region" but does not discuss Regional citizenship. Is a person a citizen of both the United States and a Region?

- **A:** No Regional citizenship — citizenship is exclusively national; Regional residency determines service access
- **B:** Automatic Regional citizenship through domicile — established by residence, terminated by departure
- **C:** Constitutional silence — leave to Regional constitutions within federal framework
- **D:** Explicit domicile-based membership — "persons domiciled within a Region are members of that Region for purposes of representation, taxation, and services"

### D9: Statelessness Prevention

Should there be an explicit prohibition on rendering any person stateless?

- **A:** Explicit prohibition — no act of renunciation or denaturalization shall take effect if it would render the person stateless
- **B:** Implicit through renunciation procedures — 90-day waiting period and counseling provide safeguard
- **C:** Unnecessary — constitutional right to citizenship already prevents statelessness for citizens

### D10: Renunciation Details

§(c)(1) allows voluntary renunciation with a 90-day waiting period and "mandatory counseling." Questions:

- Minimum age for renunciation?
- Is mandatory counseling paternalistic? Should it be "offered" rather than "mandatory"?
- Must the person have or obtain alternative citizenship first?

Options:

- **A:** As proposed — 90 days, mandatory counseling, no age minimum, no alternative citizenship requirement
- **B:** Add safeguards — 18+ age minimum, alternative citizenship required (anti-statelessness), counseling offered not mandatory
- **C:** Minimal — voluntary before a magistrate with notice of consequences; no waiting period or counseling mandate
- **D:** Modified — 90-day waiting period, counseling offered (not mandatory), 18+ age minimum

### D11: Continuity Provision Precision

§(b) references "the Constitution of 1787." Issues: (1) the Constitution was ratified in 1788 and took effect in 1789; (2) citizenship was also conferred by treaties (Louisiana Purchase, Alaska Purchase, Treaty of Guadalupe Hidalgo) and statutes.

- **A:** Broaden — "All persons who held United States citizenship under any law, treaty, or constitutional provision in effect immediately prior to the adoption of this Constitution"
- **B:** As proposed with correction — fix date reference to "prior Constitution" rather than "Constitution of 1787"
- **C:** Universal — "All persons who are United States citizens at the time of adoption of this Constitution shall remain citizens"

### D12: Non-Citizen Resident Rights

Citizenship definition raises the question of non-citizen rights. Article III §4 already extends "any person" protections. Should this section include an explicit statement on non-citizen rights?

- **A:** Include — "Nothing in this section diminishes the rights of non-citizens under other provisions of this Constitution"
- **B:** Unnecessary — Article III §4 design rationale already addresses this
- **C:** Cross-reference — "Rights extended to 'any person' under this Constitution are not conditioned on citizenship"

### D13: Deportation Prohibition Scope

§(d) states "No citizen shall be subject to deportation, removal, or territorial exclusion." Should this also address exile and banishment?

- **A:** As proposed — deportation, removal, territorial exclusion
- **B:** Expand — add "exile, banishment, or involuntary transfer to foreign jurisdiction"
- **C:** Comprehensive — "No citizen may be expelled from or denied entry to the territory of the United States, or compelled to reside in or excluded from any part thereof, except pursuant to lawful criminal sentence"

---

## 5. Verification Questions

**V1:** Are there any other provisions in the design that reference "citizen" or "citizenship" beyond those identified in Section 2? (Verify no orphaned references.)

**V2:** Does any existing provision in the design define or imply a citizenship definition that might conflict with the proposed §(a)?

**V3:** Does Article XXIII (Indigenous Sovereignty Preservation) contain any citizenship-related provisions for tribal members that interact with this proposal?

**V4:** Are there office-holding eligibility requirements elsewhere in the design (President, Senators, House members, ARB members) that depend on citizenship status?

---

## 6. Gaming Vectors

| # | Vector | Mechanism | Pre-existing or New |
|---|--------|-----------|-------------------|
| G1 | Consent theory revival | Argue citizenship under new Constitution requires affirmative adoption or oath | Pre-existing (core gap vulnerability) |
| G2 | Territorial exclusion | Narrow "territory of the United States" to exclude certain areas | Pre-existing |
| G3 | Selective recognition | Apply citizenship uncertainty to disfavored groups | Pre-existing |
| G4 | Coerced renunciation | Pressure individuals into "voluntary" renunciation through threats or deprivation | New |
| G5 | Treason expansion | Broaden treason definition to enable mass denaturalization | New (if treason exception retained) |
| G6 | Administrative delay | Stall naturalization processing indefinitely | Pre-existing |
| G7 | Naturalization freeze | Argue naturalization procedures under old Constitution are invalid during transition | Pre-existing |
| G8 | Equal citizenship erosion | Create de facto birthright/naturalized distinction through residence requirements, security clearances | New |
| G9 | Parental status manipulation | Argue "regardless of parentage" creates vulnerabilities or doesn't apply to specific categories | Low probability |
| G10 | Diplomatic status gaming | Claim diplomatic immunity for children born in U.S. to avoid citizenship conferral | Low probability, existing under current law |

---

## 7. Architectural Context

### Article III Section Map (Bill of Rights)

| Section | Topic | Status |
|---------|-------|--------|
| 1 | Floors Not Ceilings | Existing |
| 2 | Subsidiarity Principle | Existing |
| 3 | Hierarchy of Law | Existing |
| 3-A | Rights Floor Enforcement Constraints | Existing |
| 4 | The Unwaivable Core | Existing (Gap 217) |
| **5** | **[PROPOSED: Citizenship Definition]** | **Gap 226** |

### Provisions Referencing "Citizens" (Dependency Map)

| Provision | Reference | Depends on Definition |
|-----------|-----------|----------------------|
| Article I §8(a) | "All citizens" — freedom of movement | Yes |
| Article I §21 | Universal suffrage guarantee | Yes |
| Article VII §1(d) | "Natural persons who are citizens" — voting | Yes |
| Article XIV-RF §5(a) | "Any citizen" — constitutional standing | Yes |
| Article IV §6 | "Citizenship status" — census adjustment | Indirectly |
| Article XI-RF §1(e) | "U.S. citizenship" — denaturalization | Yes (conflict) |
| Article III §4 | "Any person" — unwaivable core | No (person, not citizen) |

### Existing Citizenship-Related Powers

| Provision | Content |
|-----------|---------|
| Article II §1 | "Immigration and citizenship" — enumerated federal power |
| Article II §1(e)(1)(iv) | "Immigration and naturalization" — exclusive federal domain |

---

## 8. Review Instructions

Please provide:

1. **Findings** — errors, conflicts, or risks in the proposed text (rated HIGH/MEDIUM/LOW)
2. **Design question recommendations** — for each D1-D13, state your preferred option with rationale
3. **Additional design questions** — any questions not covered above
4. **Additional gaming vectors** — any attack vectors not identified
5. **Verification answers** — if you can address V1-V4 from the provided context

Focus on:

- Whether Article III §5 is the correct placement
- How to handle the Article XI-RF §1(e) denaturalization conflict
- Whether the proposal adequately addresses jus sanguinis, territorial scope, and dual citizenship
- Whether the continuity provision is precise enough for a constitutional transition
- Whether "regardless of parentage" (dropping "subject to the jurisdiction thereof") creates vulnerabilities
