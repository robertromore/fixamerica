# Briefing: Gap 180 — The Extradition Standoff (Sanctuary Warfare)

**Prepared for:** External reviewer (Step 2 of Multi-LLM Gap Resolution Protocol)
**Date:** 2026-02-01
**Gap severity:** High
**Source file:** `04-meta/gaps/13-intergovernmental.md`, line 5193

---

## 1. Problem Statement

A Region refuses to extradite a fugitive charged with a serious felony in another Region, claiming the requesting Region's justice system is "corrupt," "inhumane," or "politically motivated." The Constitution already mandates extradition for serious crimes (Art I §12(b)) and prohibits sanctuary status (Art I §12(f)(2)), but provides no federal enforcement mechanism when a Region simply refuses. The fugitive remains free, and the requesting Region cannot retrieve them without invoking military force.

**Key distinction from Gap 240 (resolved):** Gap 240 addressed extradition *abuse* — Regions demanding extradition for conduct lawful where performed. Gap 180 is the mirror image — Regions *refusing* legitimate extradition for genuine felonies.

## 2. Existing Provisions (Overlap ~60-65%, MODERATE-HIGH)

### 2.1 Provisions that address the concern

| Provision | What it covers | Line |
|---|---|---|
| **Art I §12(a)** — Cooperation requirement | Cooperation mandatory through extradition, hot pursuit, mutual legal assistance | 1330 |
| **Art I §12(b)** — Mandatory extradition | Mandatory for violence, harm to minors, fraud, public corruption; limited exceptions | 1332 |
| **Art I §12(c)** — No shielding | No policies shielding individuals from prosecution for violence/fraud/harm to minors | 1334 |
| **Art I §12(f)(2)** — Sanctuary prohibition | No "sanctuary" status shielding from civil or regulatory enforcement | 1345 |
| **Art I §12(j)** — Limited grounds for refusal | Only 4 grounds: rights floor violation, constitutional protections, pretextual/politically motivated, constitutionally protected conduct | 1366-1371 |
| **Art I §12(k)** — Federal mediation | ARB binding determination within 60 days; fiscal penalties for persistent non-cooperation | 1373-1377 |
| **Art IV §9(h)** — Valid extradition preserved | Extradition Shield does NOT prohibit extradition for conduct criminal in both Regions, conduct within demanding Region, direct harmful effects, universally recognized crime | 573-578 |
| **Art IV §9(i)** — Federal court enforcement | Injunctive relief, removal to federal court, costs/fees, damages from officials | 580-585 |

### 2.2 What is MISSING

| Gap | Why it matters |
|---|---|
| **No federal arrest authority** | Art I §12 mandates extradition but doesn't empower anyone to physically arrest and transport when a Region refuses. ARB can rule and impose fiscal penalties, but the fugitive remains free. |
| **No custody pending review** | When a Region challenges extradition, where does the fugitive wait? Current text doesn't specify. If asylum Region has custody, the fugitive may be released on favorable terms or simply allowed to disappear. |
| **No obstruction definition** | "Non-cooperation" is grounds for fiscal penalties, but no enumeration of what constitutes active obstruction (warning fugitives, interfering with federal officers, providing escape resources). |
| **No counter-charge protection** | Region B can file retaliatory charges against Region A's officers who attempt to arrest the fugitive, creating legal risk that deters all enforcement. |
| **No pattern escalation** | Current text treats each refusal independently. No mechanism to escalate when a Region systematically refuses extradition as policy. |
| **No expedited timeline for criminal extradition** | ARB's 60-day mediation period is appropriate for civil/regulatory disputes but too slow for a fugitive who may flee during delay. |

## 3. Proposed Placement

**Primary option:** Amend Art I §12 with new subsections (r)-(v) after the existing (q) Savings Clause

- Pro: Keeps all extradition/cooperation provisions together in one section
- Pro: Art I §12 already has the mandatory extradition rule; adding enforcement to the same section is logical
- Con: §12 is already dense (17 subsections a-q)

**Alternative:** New Art IV §9-A (Extradition Enforcement) in `03-regional-governance.md`

- Pro: Groups with the existing Extradition Shield (Art IV §9)
- Con: Separates enforcement from the cooperation mandate

## 4. Design Questions

### D1. Placement — Art I §12(r)-(v) or new Art IV §9-A?

Both are defensible. The cooperation mandate and limitations are in Art I §12; the Extradition Shield is in Art IV §9. Enforcement could logically go in either.

### D2. US Marshals authority — constitutional or statutory?

The proposal gives Marshals arrest-and-transport authority upon a Federal Magistrate's probable cause finding. Should this be:

- (A) Constitutional text (ensures it cannot be weakened by statute)
- (B) Statutory implementing legislation (more flexible, less constitutional bloat)
- (C) Constitutional authorization with statutory procedures ("Congress shall establish procedures for federal enforcement of extradition obligations")

### D3. What standard for federal intervention?

When should the federal government bypass Regional law enforcement?

- (A) Automatic upon refusal (any refusal triggers Marshals authority)
- (B) After ARB ruling (Region refuses → ARB rules within 30 days → Marshals enforce)
- (C) Upon Federal Magistrate finding (probable cause + Region has refused/obstructed)
- (D) Only for enumerated serious crimes (violence, terrorism, public corruption)

### D4. Custody pending review — federal or asylum Region?

If the asylum Region challenges extradition:

- (A) Federal custody (US Marshals hold fugitive while Court reviews) — ensures fugitive doesn't disappear
- (B) Asylum Region custody with federal monitoring — less aggressive but risky
- (C) Demanding Region custody (immediate transfer, challenge after) — most aggressive

### D5. Review timeline — 30 days or shorter?

Proposal says 30-day Constitutional Court review. Current ARB mediation is 60 days. For a fugitive in custody, both may be too long. Options:

- (A) 30 days (proposal)
- (B) 14 days (expedited review given liberty interest)
- (C) 72-hour preliminary hearing + 30-day full review

### D6. Pattern non-compliance — automatic federal assumption?

Proposal triggers automatic federal assumption after 3 refusals in 12 months. Is this appropriate?

- (A) Yes — 3 refusals = systematic policy, warranting federal takeover
- (B) Modified — require Constitutional Court finding of pattern before federal assumption
- (C) No automatic assumption — escalating fiscal penalties are sufficient

### D7. Counter-charge protection scope?

How broad should protection for pursuing officers be?

- (A) Full immunity for officers executing valid federal warrants
- (B) Qualified immunity for good-faith enforcement
- (C) Retaliatory-charge dismissal only (Region B charges dismissed if found retaliatory; no blanket immunity)
- (D) Federal preemption of state/Regional charges against officers executing extradition

### D8. Obstruction — criminal offense or civil?

Should active obstruction (warning fugitives, interfering with federal officers) be:

- (A) Federal criminal offense
- (B) Civil liability with removal from office
- (C) Both (criminal for active interference; civil for passive non-cooperation)

### D9. Death penalty / harsh sentence carve-out?

Art I §12(b) already allows declining extradition where "the requesting jurisdiction seeks sentences violating federal rights floors." But what about the death penalty specifically?

- (A) No special carve-out (death penalty is either above or below the rights floor; let the floor determination handle it)
- (B) Explicit carve-out: extradition required but demanding Region must agree not to seek death penalty
- (C) Leave to statutory implementation

### D10. Interaction with Art I §12(d) — pretextual/politically motivated exception?

Art I §12(j)(3) allows declining when the request is "pretextual or politically motivated, as determined by federal court." This is the legitimate defense. But who bears the burden of proof?

- (A) Burden on asylum Region to prove pretext (presumption of good faith for demanding Region)
- (B) Burden on demanding Region to prove non-pretext
- (C) Burden shifts: demanding Region shows probable cause; asylum Region must then show pretext by clear and convincing evidence

### D11. Hot pursuit — cross-Regional authority?

Art I §12(a) mentions "hot pursuit" but doesn't define it. Should the new text clarify?

- (A) Yes — define hot pursuit with geographic/time limits and reporting requirements
- (B) No — leave to statutory implementation
- (C) Only clarify that hot pursuit by federal officers is unrestricted

## 5. Gaming Vectors

### From the proposal (4)

| # | Vector | Mechanism |
|---|---|---|
| G1 | "Human Rights" Shield | Claim requesting Region violates human rights; refuse on "humanitarian" grounds |
| G2 | "Corrupt Prosecution" Defense | Claim charges politically motivated; demand evidence review; delay indefinitely |
| G3 | "Legal Limbo" | Challenge in Regional courts; appeal endlessly; years pass |
| G4 | Counter-Charge Gambit | Charge pursuing officers with harassment; create legal risk deterring enforcement |

### Additional gaming vectors (6)

| # | Vector | Mechanism |
|---|---|---|
| G5 | The "Slow Walk" | Technically comply but process extradition requests over months; fugitive uses time to disappear or flee abroad |
| G6 | The "Bail Release" | Accept extradition request but immediately release fugitive on nominal bail; fugitive "fails to appear" and Region claims no responsibility |
| G7 | The "Procedural Fortress" | Create elaborate Regional extradition procedures with dozens of required hearings, filings, waiting periods — technically lawful, functionally impossible |
| G8 | The "Gubernatorial Pardon" | Governor pardons fugitive for the underlying offense under Regional law; claims extradition mooted because no charge exists |
| G9 | The "Mutual Refusal Pact" | Allied Regions agree never to extradite to each other's political opponents; creates ideological safe zones within the Union |
| G10 | The "Evidence Standard" Escalation | Demand trial-level evidence for extradition (beyond probable cause); require depositions, expert testimony, discovery — convert extradition hearing into mini-trial |

## 6. Verification Questions

### V1. Does the new text provide a federal enforcement mechanism that works even when the asylum Region's government actively obstructs?

The core gap — all existing provisions assume eventual cooperation or are limited to fiscal penalties. The new text must enable physical enforcement.

### V2. Does the new text protect against the counter-charge gambit (G4)?

Officers attempting to enforce extradition must not face retaliatory criminal charges from the asylum Region.

### V3. Does the new text prevent the "slow walk" (G5) and "procedural fortress" (G7)?

Time limits must apply to Regional processing, not just federal review.

### V4. Does the new text address the gubernatorial pardon problem (G8)?

Can a Governor effectively grant asylum by pardoning the underlying offense?

### V5. Does the new text preserve the legitimate defenses in Art I §12(j)?

Rights floor violations, pretextual prosecution, and constitutionally protected conduct must remain valid defenses — the goal is to prevent abuse of these defenses, not eliminate them.

---

## 7. Draft Text Direction

The amendments should:

1. **Authorize federal arrest** — US Marshals authority upon Federal Magistrate probable cause finding when Region refuses extradition
2. **Mandate federal custody** pending review when extradition is challenged
3. **Set expedited timeline** — 14-30 day Constitutional Court review, not 60-day ARB mediation
4. **Define obstruction** — enumerate specific acts constituting extradition obstruction
5. **Protect pursuing officers** — preempt retaliatory charges for good-faith enforcement
6. **Establish pattern escalation** — automatic federal assumption after systematic refusal
7. **Prevent slow-walking** — maximum timeline for Regional processing of extradition requests
8. **Address gubernatorial pardon** — Regional pardon does not moot federal extradition obligation
9. **Preserve legitimate defenses** — rights floor, pretext, protected conduct remain available but with burden allocation
10. **Set consequences** — removal from office for officials who knowingly obstruct

Recommended structure: Art I §12(r)-(w) adding federal enforcement, obstruction definition, officer protection, pattern escalation, processing deadlines, and gubernatorial pardon limitation.
