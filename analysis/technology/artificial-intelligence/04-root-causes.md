# Artificial Intelligence: Root Causes

## Overview

The challenges in AI governance—from safety risks to economic disruption to democratic threats—stem from deep structural factors: misaligned incentives, inadequate institutions, power concentration, and the fundamental difficulty of governing rapidly evolving technology. Understanding these root causes is essential for designing effective solutions.

## Primary Root Causes

### 1. Speed Mismatch

**The problem**: AI capability advances faster than governance can adapt.

| Domain | Typical Timeline |
|--------|------------------|
| Major AI capability advance | 6-18 months |
| Agency rulemaking | 2-5 years |
| Federal legislation | 5-10+ years |
| International agreements | 10+ years |

**Why this happens:**
- Technology is exponential, policy is linear
- Democratic deliberation is slow by design
- Expertise takes time to develop
- Stakeholder consultation required
- Legal challenges delay implementation

**Consequences:**
- Governance always reactive
- Harms occur before rules exist
- Industry sets de facto standards
- Regulatory capture easier

### 2. Misaligned Incentives

**Commercial incentives:**

| Actor | Primary Incentive | Safety Tension |
|-------|-------------------|----------------|
| AI companies | Growth, valuation | Speed vs. safety |
| Investors | Returns | Reward speed |
| Researchers | Publications, prestige | Novel capabilities vs. safety |
| Engineers | Ship features | Launch vs. evaluate |

**Competitive dynamics:**
- First-mover advantages are large
- Safety investment is costly
- Competitors may not invest in safety
- Market rewards capability, not safety
- "Move fast and break things" culture

**Result**: Race to deploy, underinvestment in safety

### 3. Information Asymmetries

**What companies know vs. what others know:**

| Information | Companies | Government | Public |
|-------------|-----------|------------|--------|
| Model capabilities | Full | Limited | Minimal |
| Training data | Full | None | None |
| Safety testing | Internal | Limited disclosure | None |
| Deployment risks | Some | Limited | After harm |
| Future plans | Full | None | None |

**Why asymmetries persist:**
- Trade secrets protection
- No disclosure requirements
- Complexity barriers
- Rapid change
- Limited government expertise

**Consequences:**
- Regulators cannot assess risks
- Public cannot evaluate claims
- Policy based on incomplete information
- Industry controls narrative

### 4. Power Concentration

**Compute concentration:**
- 3 cloud providers control most AI compute
- NVIDIA dominates AI chips
- Training runs require massive resources
- Barriers to entry enormous

**Talent concentration:**
- Small number of top researchers
- Big Tech attracts talent
- Academic labs disadvantaged
- Geographic concentration (SF, Seattle)

**Data concentration:**
- Internet platforms have unique data
- Training data requires scale
- Data moats create advantages
- Privacy limits alternatives

**Capital concentration:**
- Frontier models cost $100M+
- Only large companies can afford
- VC concentrated in few firms
- Returns compound concentration

**Result**: Few actors control AI development

### 5. Governance Fragmentation

**Federal level:**
- No lead AI agency
- Multiple agencies with partial authority
- Coordination challenges
- Expertise scattered

**Agency overlap:**

| Agency | AI Authority |
|--------|--------------|
| FTC | Consumer protection, competition |
| EEOC | Employment discrimination |
| FDA | Medical AI |
| NHTSA | Autonomous vehicles |
| SEC | Financial AI |
| CFPB | Consumer financial AI |

**Federalism:**
- States experimenting
- Patchwork emerging
- Preemption questions
- Industry prefers federal

**International:**
- No global governance body
- Competing frameworks (US, EU, China)
- Race to bottom concerns
- Coordination difficulties

### 6. Technical Opacity

**Why AI is hard to govern:**

| Challenge | Description |
|-----------|-------------|
| Black box problem | Cannot fully explain model decisions |
| Emergent capabilities | Behaviors not anticipated by developers |
| Generality | Same model, many applications |
| Continuous learning | Systems change after deployment |
| Scale | Billions of parameters |

**Interpretability gap:**
- Researchers don't fully understand models
- Safety evaluation incomplete
- Harms hard to predict
- Accountability difficult

### 7. Externalized Harms

**Who bears costs:**

| Harm | Who Bears Cost |
|------|----------------|
| Job displacement | Workers, communities |
| Discrimination | Affected individuals |
| Misinformation | Society, democracy |
| Privacy violations | Individuals |
| Safety incidents | Victims, taxpayers |

**Who captures benefits:**

| Benefit | Who Captures |
|---------|--------------|
| Productivity gains | Shareholders, consumers |
| Innovation | Companies, early adopters |
| Market power | Dominant platforms |

**Result**: Costs socialized, benefits privatized

### 8. Inadequate Safety Research

**Funding imbalance:**

| Category | Funding Level |
|----------|---------------|
| Capability research | $50B+ annually (private) |
| Safety research | <$1B annually (mostly private) |
| Government safety research | Minimal |

**Why underinvestment:**
- Safety is public good
- Private returns limited
- Competitive pressure
- Short-term focus
- Uncertainty about risks

### 9. Democratic Deficits

**Who decides about AI:**
- Tech executives (deployment)
- Researchers (development)
- Investors (funding)
- Lobbyists (policy)

**Who is excluded:**
- Affected workers
- Marginalized communities
- Future generations
- General public

**Why exclusion:**
- Expertise barriers
- Speed of development
- Resources for participation
- Complexity of issues

### 10. International Competition Pressure

**US-China dynamics:**
- Both investing heavily
- Security competition
- Technology decoupling
- Race dynamics

**Effect on governance:**
- "We can't slow down or China wins"
- Security trumps safety
- Coordination difficult
- Export controls partial

## Structural Factors

### Market Structure

```
Compute Layer (NVIDIA, cloud)
          ↓
Foundation Model Layer (OpenAI, Anthropic, Google)
          ↓
Application Layer (many startups)
          ↓
End Users
```

**Power resides at upper layers:**
- Compute providers set terms
- Foundation model companies control access
- Application layer dependent
- Users have limited power

### Institutional Design

**Why existing institutions fail:**

| Institution | Limitation |
|-------------|------------|
| Congress | Expertise gap, slow, polarized |
| Agencies | Limited authority, understaffed |
| Courts | Reactive, slow, case-by-case |
| Universities | Underfunded, talent drain |
| Civil society | Under-resourced |

### Cultural Factors

**Silicon Valley culture:**
- "Move fast and break things"
- Technology as solution
- Libertarian leanings
- Optimism about progress
- Skepticism of government

**Effect on AI development:**
- Speed prioritized
- Safety as constraint
- Self-regulation preferred
- Dismissal of concerns

## Feedback Loops

### Concentration → Capture → Weaker Governance → More Concentration

1. Concentrated industry has resources to lobby
2. Lobbying shapes favorable rules
3. Favorable rules reinforce concentration
4. More concentration, more lobbying power

### Speed → Governance Lag → De Facto Standards → Lock-In

1. Fast deployment creates facts on ground
2. Governance cannot keep pace
3. Industry practices become standards
4. Standards create path dependency
5. Hard to change later

### Information Asymmetry → Weak Regulation → More Asymmetry

1. Companies control information
2. Regulators cannot assess risks
3. Weak or no regulation
4. Less pressure to disclose
5. Asymmetry deepens

## Why Standard Approaches Fail

### Self-Regulation Limits

| Approach | Why Limited |
|----------|-------------|
| Voluntary principles | No enforcement |
| Industry commitments | Competitive pressure |
| Internal ethics teams | Subordinate to business |
| AI ethics boards | Often disbanded or ignored |

### Traditional Regulation Limits

| Approach | Why Limited |
|----------|-------------|
| Notice and comment | Too slow |
| Sector-specific | AI crosses sectors |
| Product-based | AI is general purpose |
| Ex post enforcement | Harm already done |

### International Coordination Limits

| Approach | Why Limited |
|----------|-------------|
| Treaties | Years to negotiate |
| Soft law | Non-binding |
| Export controls | Leaky |
| Standards bodies | Industry-dominated |

## Comparison to Other Technologies

| Technology | Similar Root Causes | Different Factors |
|------------|---------------------|-------------------|
| Nuclear | Speed, competition, concentration | Clearer physical risks |
| Biotech | Speed, dual-use, expertise | Smaller actor pool |
| Internet | Speed, governance lag, concentration | AI more opaque |
| Finance | Complexity, asymmetry, capture | AI more general |

## Root Cause Interactions

```
Speed of Advance ─────► Governance Lag ─────► Reactive Policy
       │                      │                     │
       ▼                      ▼                     ▼
Concentration ───────► Information Asymmetry ───► Capture
       │                      │                     │
       ▼                      ▼                     ▼
Power Imbalance ─────► Democratic Deficit ───► Weak Accountability
```

## Implications for Solutions

Solutions must address:

1. **Speed**: Adaptive, anticipatory governance
2. **Incentives**: Align private and public interests
3. **Information**: Transparency and disclosure
4. **Concentration**: Competition and access
5. **Fragmentation**: Coordination and authority
6. **Opacity**: Interpretability and evaluation
7. **Externalities**: Internalize costs
8. **Safety**: Dedicated investment
9. **Democracy**: Public participation
10. **International**: Cooperation frameworks

---

## Document Navigation

- Previous: [History](03-history.md)
- Next: [Stakeholders](05-stakeholders.md)
- Up: [Overview](01-overview.md)
