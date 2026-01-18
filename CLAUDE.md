# CLAUDE.md - Project Guide for AI Assistants

## Project Overview

**FixAmerica** is a comprehensive policy research and advocacy project that documents problems in American society, analyzes their root causes, and proposes evidence-based solutions across 23 major policy domains. The project produces structured markdown documentation that can serve as a resource for advocates, policymakers, researchers, and citizens.

## Project Structure

### Top-Level Directories

```
FixAmerica/
├── analysis/           # Problem analysis across 23 policy domains
├── policies/           # Policy proposals and recommendations
├── implementations/    # System implementations and simulations
│   ├── foreign-examples/              # Existing international models
│   ├── current-system-simulations/    # Simulations of current US systems
│   └── alternative-system-simulations/ # Simulations of proposed alternatives
├── plans/              # Action plans and implementation strategies
├── docs/               # Project documentation and guides
├── scripts/            # Utility scripts
└── .metadata/          # LLM collaboration artifacts
    ├── protocols/      # Collaboration protocols
    ├── templates/      # Tracker templates
    ├── reviews/        # Initial reviews and active trackers
    ├── review-responses/ # LLM response files
    └── changelog/      # Implementation changelogs
```

### Analysis Directory (`analysis/`)

Contains 23 policy domain folders, each analyzing problems, history, stakeholders, and solutions:

| Directory | Description |
|-----------|-------------|
| `analysis/political/` | Electoral systems, campaign finance, congressional reform (PRIMARY - foundational) |
| `analysis/justice/` | Criminal justice, policing, courts |
| `analysis/economic/` | Inequality, taxation, labor markets |
| `analysis/healthcare/` | Healthcare access, costs, and outcomes |
| `analysis/education/` | K-12, higher education, workforce development |
| `analysis/environment/` | Climate, pollution, conservation |
| `analysis/housing/` | Affordability, homelessness, zoning |
| `analysis/immigration/` | Border policy, legal immigration, integration |
| `analysis/infrastructure/` | Transportation, broadband, utilities |
| `analysis/technology/` | AI, privacy, antitrust |
| `analysis/defense/` | Military, foreign policy, veterans |
| `analysis/drugs/` | Drug policy, addiction, decriminalization |
| `analysis/mental-health/` | Mental health access and treatment |
| `analysis/privacy/` | Data privacy, surveillance |
| `analysis/social/` | Social safety net, poverty |
| `analysis/labor/` | Workers' rights, unions, gig economy |
| `analysis/media/` | Press freedom, local journalism |
| `analysis/science/` | Research funding, scientific integrity |
| `analysis/aging/` | Social Security, Medicare, elder care |
| `analysis/veterans/` | VA services, veteran support |
| `analysis/disability/` | ADA, accessibility, benefits |
| `analysis/tribal/` | Native American issues, sovereignty |
| `analysis/agriculture/` | Farm policy, food systems |

### Policies Directory (`policies/`)

Consolidated policy proposals extracted from analysis, organized for implementation.

### Implementations Directory (`implementations/`)

| Subdirectory | Purpose |
|--------------|---------|
| `foreign-examples/` | Documentation of existing systems in other countries |
| `current-system-simulations/` | Models and simulations of how current US systems work |
| `alternative-system-simulations/` | Models and simulations of proposed alternative systems |

### Plans Directory (`plans/`)

Action plans, implementation strategies, and campaign roadmaps.

### Supporting Directories

- `docs/` - Project-wide documentation and guides
- `docs/templates/` - Template files for new content
- `scripts/` - Utility scripts for maintenance

### Subtopic Structure

Fully developed topics have detailed subtopics:

**`analysis/political/`** (27 subtopics): electoral-reform, redistricting, primary-reform, voting-rights, electoral-college, election-security, campaign-finance, lobbying, congressional-reform, executive-reform, judicial-reform, federalism-reform, local-democracy, administrative-reform, war-powers, budget-process, statehood-representation, census-apportionment, direct-democracy, constitutional-amendment-process, party-systems, democratic-innovation, government-transparency, ethics-accountability, media-and-information, civic-education, political-violence

**`analysis/justice/`** (21 subtopics): policing, courts, prosecutors, sentencing, prisons, parole-and-probation, reentry, juvenile-justice, wrongful-convictions, civil-rights-enforcement, restorative-justice, death-penalty, forensics, victims-rights, fines-and-fees, mental-health-crisis, immigration-detention, asset-forfeiture, solitary-confinement, prison-labor, surveillance-technology

**`analysis/economic/`** (14 subtopics): taxation, inequality, antitrust, financial-regulation, monetary-policy, fiscal-policy, trade, corporate-governance, public-investment, wages, small-business, economic-mobility, consumer-debt, automation

## File Naming Convention

Each topic/subtopic uses a numbered file structure:

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
| `11-legislation.md` | Draft legal text, constitutional amendments, model legislation |
| `12-perspectives.md` | Political perspectives analysis with scoring and compromise proposals |

## Writing Guidelines

### Style

- **Objective tone**: Present facts and analysis without partisan framing
- **Evidence-based**: Support claims with citations
- **Accessible**: Write for educated general audience, not specialists
- **Actionable**: Focus on what can be done, not just what's wrong
- **No emojis**: Unless explicitly requested

### Markdown Standards

The project uses `markdownlint` with configuration in `.markdownlint.json`:

- ATX-style headers (`#`, `##`, etc.)
- Dash-style lists (`-`)
- 4-space indentation for nested lists
- No line length limit (MD013 disabled)
- Fenced code blocks with backticks
- Asterisk emphasis (`*italic*`, `**bold**`)

### Legal Text Format

For `11-legislation.md` files:

**Federal Bills:**

```text
SEC. 1. SHORT TITLE.
This Act may be cited as the "[Name] Act".

SEC. 2. [SUBSTANTIVE PROVISION].
(a) IN GENERAL.—[Main requirement]
(b) DEFINITIONS.—[Key terms]
```

**State Model Legislation:**

```text
SECTION 1. SHORT TITLE.
This Act may be cited as the "[State] [Name] Act".

SECTION 2. [PROVISION]
```

**Constitutional Amendments:**

```text
Section 1. [Substantive provision]

Section 2. Congress shall have the power to enforce this article
by appropriate legislation.

Section 3. This article shall take effect [timing].
```

### Citation Format

See `docs/citation-guide.md` for full details. Key formats:

- U.S. Code: `52 U.S.C. § 10301`
- Court cases: `*Shelby County v. Holder*, 570 U.S. 529 (2013)`
- Academic: Author last, first. "Title." *Journal* vol (year): pages.

## Key Guides

- `docs/legislation-guide.md` - How to write legislation files, including loopholes analysis
- `docs/citation-guide.md` - Citation formatting standards
- `docs/templates/11-legislation.md` - Template for legislation files
- `docs/templates/12-perspectives.md` - Template for perspectives analysis files
- `.metadata/protocols/llm-review-protocol.md` - LLM collaboration protocol

## Important Sections in Legislation Files

Each `11-legislation.md` must include:

1. **Overview** - Legislative approach for the topic
2. **Constitutional Amendments** - If needed, with draft text
3. **Federal Legislation** - Bills with Purpose, Draft Text, Explanation, Challenges, Refinements
4. **State Model Legislation** - Adaptable state-level bills
5. **Regulatory Framework** - Administrative implementation
6. **Legal Considerations** - Constitutional issues, preemption, enforcement
7. **Loopholes, Shortcomings, and Rectification** - Analysis of weaknesses with:
   - Potential Loopholes table (Loophole | Description | Severity)
   - Shortcomings table (Issue | Impact | Root Cause)
   - Rectification Procedures (numbered list of fixes)
   - General Implementation Concerns
8. **References** - Citations to law, cases, academic sources
9. **Related Topics** - Cross-references to other files
10. **Document Navigation** - Links to previous/next files

## Political Perspectives Analysis

Each `12-perspectives.md` evaluates the topic through 9 political viewpoints:

**Perspectives:** Conservative, Liberal, Progressive, Libertarian, Constitutionalist, Populist, Centrist, Religious Right, Democratic Socialist

**For each perspective:**

- **Engagement Consistency (1-5)**: Assessment of how reliably stated positions align with principles
    - 5 = Highly Consistent (positions stable when concerns addressed)
    - 1 = Unpredictable (positions driven by opposition dynamics)
- **Position Scores (1-10)**: Agreement with current state analysis, root causes, solutions, legislation
- **Alternative Proposals**: What they would support instead
- **Coalition Potential**: Natural allies and potential bridges

**Summary sections:**

- Master comparison table (all perspectives, all dimensions)
- Solution support matrix
- Engagement consistency distribution

**Compromise proposals** identify reforms that could bridge multiple perspectives, mapping how each addresses different concerns and what each side concedes.

**Generate with:** `/analyze-perspectives <domain>/<subtopic>`

## Common Tasks

### Adding a New Subtopic

1. Create directory under appropriate parent topic
2. Copy template files or create files 01-11 following naming convention
3. Add `11-legislation.md` following `docs/templates/11-legislation.md`
4. Run `/analyze-perspectives <domain>/<subtopic>` to generate 12-perspectives.md
5. Run `npx markdownlint-cli path/to/*.md` to verify formatting

### Updating Legislation Files

1. Read existing file completely before making changes
2. Follow established format for that file
3. Include loopholes analysis for any new legislation
4. Verify markdownlint compliance

### Running Linting

```bash
# Check specific files
npx markdownlint-cli analysis/political/**/*.md

# Check all markdown
npx markdownlint-cli **/*.md
```

### Finding Uncited Claims

```bash
./scripts/find-uncited-claims.sh path/to/file.md
```

### LLM Review Collaboration

This project uses a formal protocol for multi-LLM document review cycles (e.g., Claude and Codex reviewing each other's work).

**Quick start:** Use the `/llm-review` command:

- `/llm-review` - Show options and active reviews
- `/llm-review start <topic>` - Start a new review
- `/llm-review continue` - Continue a review where you're the next actor
- `/llm-review status` - Show status of all active reviews

**Key files:**

- `.claude/commands/llm-review.md` - The `/llm-review` skill definition
- `.metadata/protocols/llm-review-protocol.md` - Full protocol definition
- `.metadata/templates/review-tracker-template.md` - Template for new reviews
- `.metadata/reviews/active/` - Active review trackers

**Core rules (when participating in a review):**

1. **Single source of truth**: The tracker file is authoritative
2. **Append-only outputs**: Do not edit other LLM's output files
3. **Ownership rule**: Only mark your own steps as `done`
4. **Date format**: Use `YYYY_MM_DD` in file names (snake_case)
5. **Single actor handoff**: `Next` field must specify exactly one actor
6. **Cite locations**: Reference specific file paths and line numbers

**Issue IDs**: Use `ISSUE-XX` format (e.g., `ISSUE-01`) for unambiguous references.

**To start a new review:**

1. Copy template to `.metadata/reviews/active/{topic}-tracker.md`
2. Fill in Meta section (topic, target, created, last_updated, status, participants)
3. Provide tracker path to reviewer LLM with handoff prompt from template

**To continue an existing review:**

1. Read the tracker at `.metadata/reviews/active/{topic}-tracker.md`
2. Find the step with status `planned`
3. Use the handoff prompt from the tracker's "Handoff Prompts" section

**When you are the next actor:**

1. Read the input file specified in your step
2. Perform the action (review, response, implement, verify, or fix)
3. Write your output file to the appropriate location
4. Update the tracker:
   - Mark your step `done` with Output and Summary filled in
   - Add next step with status `planned`
   - Update Current State section
   - Update Issues table and Agreements Log as needed
   - Update `Last updated` date in Meta section

## Cross-References

When referencing other topics, use relative paths:

```markdown
See [Campaign Finance: Legislation](../campaign-finance/11-legislation.md)
```

## Project Philosophy

1. **Political reform is foundational** - Other policy domains cannot be fixed without fixing democratic dysfunction first
2. **Non-partisan analysis** - Present facts that challenge both parties' narratives
3. **Practical solutions** - Focus on achievable reforms, not utopian visions
4. **Implementation focus** - Include draft legislation, not just policy ideas
5. **Acknowledge opposition** - Understand and address counterarguments

## Do NOT

- Add README.md or other documentation files unless explicitly requested
- Create new top-level directories without confirmation
- Use emojis in content
- Make partisan statements or attacks
- Ignore the established file structure
- Skip the loopholes/shortcomings analysis in legislation files
- Edit another LLM's output files during review collaboration (append-only)
