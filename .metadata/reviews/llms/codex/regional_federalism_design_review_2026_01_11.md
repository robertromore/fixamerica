**Findings**
- High: The elections design still treats presidential selection as "national popular vote or proportional regional vote," but the constitution mandates national popular vote and explicitly prohibits regional allocation/weighting; this is a direct cross-document conflict (`plans/regional-federalism/02-design/02-elections.md:301`, `plans/regional-federalism/02-design/09-constitution.md:211`).
- High: The armed-forces design allows multiple two-key authorization combinations (including Congress or judicial certification), while the constitution defines a specific two-key pair and fallback (President + supermajority of Regional Governors; Chief Justice fallback); the mismatch creates operational ambiguity for domestic deployment (`plans/regional-federalism/02-design/06-armed-forces.md:282`, `plans/regional-federalism/02-design/09-constitution.md:397`).
- Medium: Judiciary timelines are specified as 30/30/30 days in the design doc, but the constitution only says "constitutionally defined timeframes" without defining them or pointing to an implementation act; enforcement timelines are therefore undefined at the constitutional layer (`plans/regional-federalism/02-design/07-judiciary.md:199`, `plans/regional-federalism/02-design/09-constitution.md:367`).
- Medium: Legislative process is underspecified: the constitution keeps a bicameral Congress yet strips the Senate of routine veto power, and the institutions doc limits Senate powers without clarifying how ordinary federal statutes are enacted (House-only vs limited Senate concurrence); this is a core mechanism gap (`plans/regional-federalism/02-design/03-institutions.md:98`, `plans/regional-federalism/02-design/09-constitution.md:150`).

**Open Questions**
- Should the elections design be updated to match the constitution’s national popular vote requirement, or should the constitution be revised to permit regional proportional selection?
- Should the two-key rule be narrowed in the armed-forces design to the constitutional keyholders, or should Article XII be expanded to allow alternative authorization pairs?
- Where should judicial timeframes and default triggers be formally defined: in Article XI itself or in the Implementation Act referenced in Article XVII?
- What is the intended legislative path for ordinary federal statutes under the "no routine Senate veto" rule (House-only passage, delayed Senate review, or category-limited Senate concurrence)?

**Suggested Improvements**
- Update `plans/regional-federalism/02-design/02-elections.md` Section 9.2 to remove the proportional regional vote option or add a note stating it is not adopted under the current constitution.
- Update `plans/regional-federalism/02-design/06-armed-forces.md` Section 9 to mirror Article XII’s exact keyholders and fallback, or explicitly flag the difference as a rejected alternative.
- Add explicit judicial deadlines to Article XI or add a sentence in Article XVII assigning timelines to the implementation act so the 30-day rule has constitutional anchoring.
- Add a short "Federal Lawmaking Procedure" subsection in `plans/regional-federalism/02-design/03-institutions.md` or Article IV to specify how ordinary federal legislation passes under the narrowed Senate role.
