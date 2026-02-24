---
last_updated: 2026-02-20
status: current
confidence: high
---

# Educational Privacy: Current State

## EdTech Landscape

### Market Overview

| Metric | Value | Source |
|--------|-------|--------|
| US EdTech market size | $123 billion (2024) | HolonIQ "Global EdTech Market" (2024) |
| EdTech apps per school district | Average 1,400 distinct applications | LearnPlatform/Instructure EdTech Top 40 Report (2024) |
| K-12 devices per student | 1.5 devices on average (many districts 1:1) | CoSN "State of EdTech Leadership" (2024) |
| Google Workspace for Education users | 170+ million students and educators globally | Google for Education (2024) |
| Canvas LMS market share (higher ed) | 35%+ | HolonIQ / Instructure (2024) |
| Student Information System market | $5.2 billion | Mordor Intelligence (2024) |

### Major EdTech Platforms and Data Practices

| Platform | Users | Data Collected | Concerns |
|----------|-------|---------------|----------|
| Google Workspace for Education | 170M+ globally | Email, documents, browsing (on managed devices), location, usage patterns | Advertising ecosystem integration; data retention policies |
| Microsoft 365 Education | 100M+ | Documents, communications, Teams activity, device telemetry | Telemetry data collection; third-party sharing |
| Canvas (Instructure) | 30M+ | Assignment submissions, grades, login patterns, discussion posts | Acquired by private equity (Thoma Bravo); data monetization concerns |
| Clever | 95,000+ schools | SSO authentication data, app usage, student roster information | Central data hub connecting multiple vendors |
| ClassDojo | 51M+ students | Behavioral data, parent communications, attendance, student portfolios | Behavioral profiling of young children |
| Turnitin | 15,000+ institutions | Student writing, plagiarism analysis, AI detection scores | Permanent retention of student work; AI training |
| PowerSchool | 45M+ students | Grades, attendance, behavior incidents, health records, demographics | 2024 data breach affecting millions |
| GoGuardian | 27M+ students | Web browsing, screen content, location, keystrokes | Real-time monitoring of student devices |
| Gaggle | 5M+ students | Email, documents, chat, social media activity | Automated flagging of student content including LGBTQ+ topics |

### Data Collection Categories

| Category | Examples | Frequency | Sensitivity |
|----------|----------|-----------|-------------|
| **Academic performance** | Grades, test scores, assignments, learning analytics | Continuous | High |
| **Behavioral data** | Disciplinary records, classroom behavior points, reward/penalty systems | Continuous | Very high |
| **Attendance and location** | Check-ins, bus tracking, movement within school | Daily | High |
| **Digital activity** | Web browsing, app usage, search queries, file creation | Continuous | Very high |
| **Communications** | Email, chat, discussion posts, video calls | Continuous | Very high |
| **Biometric data** | Facial recognition, fingerprint (lunch), voice | Varies | Very high |
| **Health and wellness** | Mental health assessments, counselor notes, disability accommodations | As generated | Very high |
| **Demographic data** | Race, ethnicity, gender, income (free lunch status), home language | Annually | High |
| **Social connections** | Group memberships, peer interactions, collaboration patterns | Continuous | Medium-high |

## School Surveillance Systems

### Surveillance Technology Adoption

| Technology | Adoption Rate | Purpose | Primary Vendors |
|------------|--------------|---------|-----------------|
| Security cameras | 91% of public schools | Physical security | Verkada, Avigilon, Milestone |
| Social media monitoring | 80%+ of large districts | Threat assessment, bullying | Gaggle, Bark, Social Sentinel, Securly |
| Web filtering and monitoring | 98% of K-12 schools | CIPA compliance, safety | GoGuardian, Lightspeed, Securly, Bark |
| Student device monitoring | 85%+ of 1:1 districts | Classroom management, safety | GoGuardian, Securly, Lightspeed, Hapara |
| Facial recognition | 10-15% of districts (piloted or deployed) | Access control, identification | Verkada, Clearview AI, RealNetworks (SAFR) |
| Gunshot detection | 5-10% of schools | Active shooter response | ZeroEyes, Evolv Technology |
| Predictive threat assessment | Growing adoption | Identify at-risk students | Bark, Gaggle, Navigate360 |
| License plate readers | Common in high schools | Campus security | Flock Safety, Motorola |

### Social Media and Content Monitoring

| Vendor | Schools Served | What Is Monitored | Key Concerns |
|--------|---------------|-------------------|--------------|
| **Gaggle** | 1,500+ districts | School email, documents, chat; flags for self-harm, violence, nudity | Over-flagging of LGBTQ+ content; racial bias in alerts |
| **Bark** | 6,000+ schools | Texts, social media, email on monitored devices | Parental surveillance extension; false positive rates |
| **GoGuardian** | 27M+ students | Real-time screen activity, browsing, search queries | Teacher can view student screens; chilling effect |
| **Securly** | 20,000+ schools | Web activity, social media, device usage | AI-generated wellness alerts shared with administrators |

### Documented Concerns with Monitoring Systems

| Issue | Evidence | Source |
|-------|----------|--------|
| LGBTQ+ student targeting | Monitoring systems flag LGBTQ+ keywords, outing students to parents and administrators | EFF, "Spying on Students" (2023); CDT research (2024) |
| Racial bias | Students of color disproportionately flagged for behavioral concerns | Brennan Center, "School Surveillance" (2023) |
| Disability impact | Students with behavioral health conditions more frequently surveilled | National Disability Rights Network (2023) |
| False positive rates | 95%+ of automated flags are false positives | Gaggle internal data reviewed by *The 74 Million* (2023) |
| Chilling effects | 68% of students report self-censoring online communication | Center for Democracy and Technology, student survey (2024) |
| Lack of evidence for safety | No peer-reviewed study demonstrates that school surveillance prevents mass violence | RAND Corporation, "School Surveillance Review" (2023) |

## Remote Learning and Proctoring

### Post-COVID EdTech Expansion

| Metric | Pre-COVID (2019) | Post-COVID (2024) | Change |
|--------|-----------------|-------------------|--------|
| EdTech tool usage per district | ~700 apps | ~1,400 apps | +100% |
| 1:1 device programs | 60% of districts | 90%+ of districts | +50% |
| Remote proctoring adoption (higher ed) | 15% of institutions | 54% of institutions | +260% |
| Student data volume generated | Baseline | 3-5x baseline | +200-400% |
| Parent awareness of data collection | 42% | 55% | +31% |

### Online Proctoring Concerns

| Platform | Technology | Privacy Issues |
|----------|-----------|----------------|
| Proctorio | AI behavior analysis, eye tracking, screen recording | Webcam access; room scanning; algorithmic bias against disabled students |
| ExamSoft | Facial recognition, keystroke analysis, screen lockdown | Biometric collection without meaningful consent; data retention |
| Respondus | Screen lockdown, webcam monitoring | Limited accommodation for disabled students |
| Honorlock | AI proctoring, phone detection, ID verification | Secondary device detection; network monitoring |

## Regulatory Landscape

### Federal Law

| Law | Year | Scope | Gaps |
|-----|------|-------|------|
| **FERPA** | 1974 | Education records at institutions receiving federal funds | Written pre-internet; no meaningful enforcement; school official exception swallows the rule |
| **COPPA** | 1998 | Commercial websites/apps for children under 13 | Does not apply when schools authorize EdTech; weak enforcement |
| **PPRA** | 1978 | Student surveys and evaluations | Narrow scope; does not address digital data collection |
| **CIPA** | 2000 | Internet filtering in schools receiving E-rate | Mandates filtering/monitoring, potentially increasing surveillance |
| **IDEA** | 1975/2004 | Students with disabilities | Education records provisions; intersection with IEP confidentiality |

### FERPA Limitations

| Issue | Description | Impact |
|-------|-------------|--------|
| **School official exception** | Schools can share records with any contractor deemed a "school official" with "legitimate educational interest" | EdTech vendors access data without parent consent |
| **No private right of action** | Students and parents cannot sue for FERPA violations | Only remedy is Department of Education complaint |
| **Directory information opt-out** | Schools may share name, address, phone, dates unless parent opts out | Military recruiters, commercial entities receive student data |
| **No data minimization** | FERPA imposes no limits on how much data is collected | Schools and vendors collect maximally |
| **No breach notification** | FERPA does not require notification of data breaches | Students unaware when data is exposed |
| **Enforcement mechanism** | Threat of losing federal funding -- never used | No deterrent effect |

### State Laws

| State | Law | Year | Key Provisions |
|-------|-----|------|----------------|
| **California** | SOPIPA (Student Online Personal Information Protection Act) | 2014 | Prohibits EdTech from selling student data or using for non-educational purposes |
| **New York** | Education Law 2-d | 2014/2020 | Data privacy and security standards for education agencies and vendors |
| **Illinois** | SOPPA (Student Online Personal Protection Act) | 2021 | Parental consent for data collection; vendor agreements; data breach notification |
| **Colorado** | Student Data Transparency and Security Act | 2016 | Data governance framework; vendor transparency |
| **Connecticut** | Student Data Privacy Act | 2016 | Vendor prohibitions; security requirements |
| **50 states** | Various student privacy provisions | 2014-2025 | All 50 states have enacted some form of student data privacy law |

Source: Student Privacy Compass / Data Quality Campaign State Policy Tracker (January 2025).

## Higher Education Data Practices

### Learning Analytics

| Institution Type | Adoption Rate | Data Used | Concerns |
|-----------------|--------------|-----------|----------|
| Large public universities | 75%+ | LMS activity, grades, demographics, financial aid | Predictive models may reinforce inequities |
| Community colleges | 50%+ | Registration, course completion, early alerts | Data-driven interventions may stigmatize |
| Private universities | 60%+ | Applications, enrollment, retention metrics | Commercial partnerships with data firms |
| For-profit institutions | 80%+ | Lead generation data, enrollment, completion | Data shared with marketing partners |

### Student Data in Admissions

| Practice | Description | Privacy Concern |
|----------|-------------|-----------------|
| Social media screening | Colleges reviewing applicants' social media | No disclosure requirements; bias potential |
| Demonstrated interest tracking | Email opens, campus visits, web browsing tracked | Students unaware of tracking influence on admissions |
| Data broker purchases | Colleges purchasing student lists from ACT/SAT/College Board | Students' test registration data sold for marketing |
| Algorithmic admissions | AI tools used for initial screening | Opaque decision-making; bias amplification |

## Data Breaches and Security

### K-12 Breach Statistics

| Metric | Value | Source |
|--------|-------|--------|
| Total K-12 breaches (2016-2024) | 2,691 publicly reported incidents | K12 SIX Incident Map |
| Student records exposed | 37+ million | Comparitech K-12 breach analysis (2024) |
| Average cost per breach | $3.5 million (education sector) | IBM Cost of a Data Breach Report (2024) |
| Ransomware attacks on schools (2023-2024) | 100+ per year | CISA K-12 cybersecurity reports |
| Districts with dedicated cybersecurity staff | Less than 25% | CoSN "State of EdTech Leadership" (2024) |

### Notable Breaches

| Year | Entity | Records Affected | Data Exposed |
|------|--------|-----------------|--------------|
| 2024 | PowerSchool | Estimated millions of student records | Names, SSNs, grades, medical information |
| 2023 | MOVEit (affecting multiple districts) | Hundreds of thousands | Student and employee PII |
| 2022 | Illuminate Education | Millions | Student demographics, grades, behavior |
| 2021 | Pearson | Millions of students | Names, email addresses, dates of birth |
| 2020 | Blackbaud | Multiple universities | Donor and student data |

## The Gap

| What Exists | What Is Needed | Current Status |
|-------------|----------------|----------------|
| FERPA (1974) | Modernized federal student privacy law | No comprehensive update since 1974 |
| School official exception | Strict vendor accountability requirements | Vendors access data with minimal oversight |
| No private right of action | Enforceable individual rights | Students and parents have no legal remedy |
| Voluntary EdTech pledges | Mandatory data minimization and purpose limitation | Industry self-regulation inadequate |
| Surveillance expansion | Evidence-based assessment of surveillance effectiveness | No systematic evaluation of school surveillance |
| Patchwork state laws | Federal floor with state innovation | Inconsistent protections across states |
| Minimal breach notification | Mandatory breach notification and security standards | Most states lack education-specific breach requirements |

## Sources

- Center for Democracy and Technology, "Online and Observed: Student Privacy Implications of School-Issued Devices and Student Activity Monitoring Software" (2024)
- CoSN (Consortium for School Networking), "State of EdTech Leadership" (2024)
- Brennan Center for Justice, "School Surveillance Infrastructure" (2023)
- Electronic Frontier Foundation, "Spying on Students: School-Issued Devices and Student Privacy" (2023)
- HolonIQ, "Global EdTech Market" (2024)
- IBM Security, "Cost of a Data Breach Report" (2024)
- K12 Security Information Exchange, "K-12 Cyber Incident Map" (2024)
- LearnPlatform/Instructure, "EdTech Top 40 Report" (2024)
- RAND Corporation, "School Security Technologies" (2023)
- Student Privacy Compass, "State Student Privacy Laws" (January 2025)

## Related Topics

- [Children's Privacy](../childrens-privacy/01-overview.md) - COPPA and children's online protections
- [Commercial Surveillance](../commercial-surveillance/01-overview.md) - EdTech as commercial surveillance
- [Privacy Overview](../01-overview.md) - Broader privacy context

## Document Navigation

- Previous: [Overview](01-overview.md)
- Next: [History](03-history.md)
