# FixAmerica

A comprehensive policy research and advocacy project documenting problems across 23 American policy domains with evidence-based solutions and draft legislation.

**Core Philosophy:** Political reform is foundational—other policy domains cannot be fixed without first fixing democratic dysfunction.

## Project Structure

```
FixAmerica/
├── analysis/           # Problem analysis across 23 policy domains
├── policies/           # Consolidated policy proposals
├── implementations/    # System models and simulations
├── plans/              # Action plans and implementation strategies
├── docs/               # Project documentation and guides
└── scripts/            # Utility scripts
```

## Current Scale

| Component | Files | Lines | Description |
|-----------|-------|-------|-------------|
| **Analysis** | 967 | 270K+ | Research across 23 domains |
| **Legislation** | 62 | 57K | Draft bills, amendments, regulations |
| **Plans** | 49 | 65K+ | Implementation strategies and proposals |
| **Simulations** | 15 | 4K+ | Electoral and fiscal modeling code |

## Policy Domains

### Primary Domains (with detailed subtopics)

**Political Reform** (27 subtopics)

- Electoral reform, redistricting, primary reform, voting rights
- Electoral college, election security, campaign finance, lobbying
- Congressional reform, executive reform, judicial reform
- Federalism, local democracy, administrative reform
- War powers, budget process, statehood/representation
- Census/apportionment, direct democracy, constitutional amendments
- Party systems, democratic innovation, government transparency
- Ethics/accountability, media/information, civic education, political violence

**Criminal Justice** (21 subtopics)

- Policing, courts, prosecutors, sentencing, prisons
- Parole/probation, reentry, juvenile justice, wrongful convictions
- Civil rights enforcement, restorative justice, death penalty
- Forensics, victims' rights, fines/fees, mental health crisis
- Immigration detention, asset forfeiture, solitary confinement
- Prison labor, surveillance technology

**Economic Policy** (14 subtopics)

- Taxation, inequality, antitrust, financial regulation
- Monetary policy, fiscal policy, trade, corporate governance
- Public investment, wages, small business, economic mobility
- Consumer debt, automation

### Standard Domains (12 files each)

| Domain | Domain | Domain |
|--------|--------|--------|
| Aging | Agriculture | Defense |
| Disability | Drugs | Education |
| Environment | Healthcare | Housing |
| Immigration | Infrastructure | Labor |
| Media | Mental Health | Privacy |
| Science | Social | Technology |
| Tribal | Veterans | |

## File Structure

Each topic uses a standardized 12-file structure:

| File | Purpose |
|------|---------|
| `01-overview.md` | Executive summary and scope |
| `02-current-state.md` | Present-day conditions and data |
| `03-history.md` | Historical context and evolution |
| `04-root-causes.md` | Systemic analysis of why problems exist |
| `05-stakeholders.md` | Who is affected and who has power |
| `06-opposition.md` | Who opposes reform and why |
| `07-solutions.md` | Proposed reforms and interventions |
| `08-roadmap.md` | Implementation timeline and sequencing |
| `09-resources.md` | Further reading and citations |
| `10-actions.md` | What citizens can do |
| `11-legislation.md` | Draft legal text and model legislation |
| `12-perspectives.md` | Political perspectives analysis and compromise mapping |

## Implementation Plans

**[Regional Federalism](plans/constitutional-amendments/comprehensive/regional-federalism/README.md)** - A comprehensive constitutional redesign proposal (49 documents):

- Constitutional text with 7-region structure
- Stress-testing against policy conflicts, economic tensions, and authoritarian scenarios
- Safeguards playbook and transition legislation
- 24 proposal documents covering interregional cooperation, elections, rights, boundaries, and emergencies
- Policy application guides for healthcare and housing

**[Regional Federalism Simulations](implementations/alternative-system-simulations/regional-federalism/README.md)** - Data-driven validation of the Regional Federalism proposal:

- Presidential election simulations (EC vs NPV+RCV) for 2016, 2020, 2024
- House proportional representation model (D'Hondt method)
- Senate regional composition model (14 seats + DC)
- Fiscal equalization calculator and 20-year convergence projections

## Documentation

- [Citation Guide](docs/citation-guide.md) - Citation formatting standards
- [Legislation Guide](docs/legislation-guide.md) - How to write legislation files
- [Templates](docs/templates/) - Templates for new content

## Perspectives Analysis

The project includes a political perspectives analysis system that evaluates each topic from 9 distinct viewpoints: Conservative, Liberal, Progressive, Libertarian, Constitutionalist, Populist, Centrist, Religious Right, and Democratic Socialist.

Each perspective receives:

- **Faith Level (1-5)**: Assessment of good faith engagement with evidence citations
- **Position Scores (1-10)**: Agreement with current state, root causes, solutions, and legislation
- **Alternative Proposals**: What each perspective would prefer instead
- **Coalition Potential**: Natural allies and potential bridges

The analysis concludes with compromise proposals identifying common ground across perspectives.

### Quick Start (Claude Code)

```bash
/analyze-perspectives political/campaign-finance
/analyze-perspectives political/electoral-reform --perspective Conservative
/analyze-perspectives political/campaign-finance --compromises-only
```

## LLM Review Collaboration

This project uses a formal protocol for multi-LLM document review cycles. You can request reviews of any document or plan using this system.

### Quick Start (Claude Code)

Use the `/llm-review` command:

- `/llm-review` - Show options and active reviews
- `/llm-review start <topic>` - Start a new review
- `/llm-review continue` - Continue a review where you're the next actor
- `/llm-review status` - Show status of all active reviews

### Manual Process

**Starting a new review:**

1. Copy the template:

   ```bash
   cp .metadata/templates/review-tracker-template.md .metadata/reviews/active/{topic}-tracker.md
   ```

2. Fill in the tracker with your topic, target path, and assign reviewer/implementer roles

3. Provide this prompt to the reviewer LLM:

   ```text
   Read the review tracker at .metadata/reviews/active/{topic}-tracker.md

   Your current task is step 01 with status "planned". Review the target documents,
   create your review file, then update the tracker per the protocol.

   Protocol: .metadata/protocols/llm-review-protocol.md
   ```

**Continuing an existing review:**

1. Open the tracker at `.metadata/reviews/active/{topic}-tracker.md`
2. Find the step with status `planned`
3. Copy the handoff prompt from the tracker's "Handoff Prompts" section
4. Provide that prompt to the appropriate LLM

### Active Reviews

| Topic | Status | Next Actor |
|-------|--------|------------|
| [Regional Federalism](.metadata/reviews/active/regional-federalism-tracker.md) | closed | - |

### Protocol Details

- [Full Protocol](.metadata/protocols/llm-review-protocol.md) - Complete collaboration rules
- [Tracker Template](.metadata/templates/review-tracker-template.md) - Starting point for new reviews

## Development

### Markdown Linting

```bash
# Check specific files
npx markdownlint-cli analysis/political/**/*.md

# Check all markdown
npx markdownlint-cli **/*.md
```

### Utility Scripts

```bash
# Find claims without citations
./scripts/find-uncited-claims.sh path/to/file.md

# Fix markdown formatting
./scripts/fix-markdown.sh
```

## Contributing

This project uses:

- ATX-style headers (`#`, `##`, etc.)
- Dash-style lists (`-`)
- 4-space indentation for nested lists
- Fenced code blocks with backticks
- Asterisk emphasis (`*italic*`, `**bold**`)

See [CLAUDE.md](CLAUDE.md) for detailed project guidelines.

## License

TBD
