# Location Tracking: Actions

## What Individuals Can Do

### Protect Your Own Location Data

**Audit Your Phone's Location Permissions**

- Review all apps with location access: on iPhone, go to Settings > Privacy & Security > Location Services; on Android, go to Settings > Location > App location permissions
- Change apps from "Always" to "While Using" or "Never" for location access unless continuous tracking is essential (e.g., fitness tracking during a run)
- Delete apps that collect location data without a clear need for the service you use
- Disable "precise location" where available (iOS 14+ allows apps to receive approximate rather than precise location)
- Turn off WiFi and Bluetooth scanning when not in use (these reveal location even when not connected to networks)

**Manage Your Advertising ID**

- On iPhone: Settings > Privacy & Security > Tracking > toggle off "Allow Apps to Request to Track"; also Settings > Privacy & Security > Apple Advertising > toggle off Personalized Ads
- On Android: Settings > Privacy > Ads > "Delete advertising ID" (Android 12+) or "Opt out of Ads Personalization"
- Resetting or deleting your advertising ID breaks the link between your device and historical location data held by brokers

**Limit Connected Vehicle Tracking**

- Review your vehicle's privacy settings in the infotainment system and associated mobile apps
- Opt out of data sharing programs (e.g., GM OnStar Smart Driver, Ford Driving Insights)
- Contact your automaker in writing to request deletion of collected driving and location data
- Ask your auto insurer whether they use telematics or connected vehicle data in your premium calculation
- Review LexisNexis Consumer Disclosure report (consumer.risk.lexisnexis.com) to see what driving data insurers have access to

**Use Privacy-Protective Tools**

- Use a VPN to mask your IP address-based location (does not prevent GPS or cell tower tracking)
- Use privacy-focused browsers (Brave, Firefox with Enhanced Tracking Protection) to limit web-based location tracking
- Use Signal or other end-to-end encrypted messaging for sensitive communications about location
- Consider using a Faraday bag when you need to prevent all wireless tracking (blocks GPS, cell, WiFi, and Bluetooth signals)
- Use cash or privacy-focused payment methods when location of purchase is sensitive

**Protect Against Tracker Abuse**

- Regularly check for unknown AirTags or Tile trackers: iPhone automatically alerts to unknown AirTags; Android users can download "Tracker Detect" app
- If you are a domestic violence survivor, contact the National Network to End Domestic Violence's Safety Net project (nnedv.org/content/technology-safety) for guidance on device safety
- Be aware that shared phone plans allow account holders to view location; consider an independent phone plan if location privacy is a safety concern

---

## What Communities Can Do

### Organize Locally

- Form or join community privacy advocacy groups focused on location surveillance
- Host educational events about location tracking risks, especially for immigrant communities, domestic violence survivors, and activists
- Partner with legal aid organizations that handle location privacy complaints
- Connect with local ACLU and EFF chapters for location surveillance awareness campaigns
- Engage faith communities concerned about religious practice being revealed by location data

### Engage Local Government

- Advocate for local government policies restricting use of automated license plate readers (ALPRs)
- Push for municipal contracts with technology vendors to include location privacy requirements
- Support local resolutions calling for state and federal location privacy reform
- Attend city and county hearings on police surveillance technology acquisitions
- Advocate for community control over surveillance technology through local ordinances (model: Seattle's surveillance ordinance)

### Support Affected Communities

- Help immigrant community members understand how ICE/CBP use commercial location data and what protections exist (or do not exist)
- Connect domestic violence survivors with resources on protecting against location-based stalking
- Support activists and protesters in understanding geofence warrant risks and taking protective measures
- Assist LGBTQ+ individuals in understanding risks of location data near sensitive venues

---

## What Advocates Can Do

### Legislative Advocacy

**Federal Level**

- Contact your U.S. senators and representative to support:
    - Fourth Amendment Is Not For Sale Act (warrant requirement for government location data purchases)
    - Geofence warrant reform legislation
    - Comprehensive location privacy legislation with consent requirements and private right of action
    - Connected vehicle privacy legislation
    - Location data broker registration requirements
- Provide testimony at congressional hearings on location privacy and government data purchases
- Submit detailed public comments on FTC location privacy rulemakings
- Meet with legislative staff to share constituent stories about location data misuse

**State Level**

- Support adoption of warrant requirements for law enforcement location data access (Utah model)
- Advocate for geofence warrant restrictions (New York model)
- Push for location privacy consent laws (Illinois model)
- Support state AG enforcement of location data violations
- Testify at state legislative committee hearings on location privacy bills

### Regulatory Engagement

- Submit public comments on all FTC location privacy rulemakings
- Monitor and publicize FTC enforcement actions against location data brokers
- Engage with state AG offices on location privacy enforcement priorities
- Participate in NIST and standards body processes on location data de-identification and privacy

### Legal Action

- Support organizations filing location privacy lawsuits (EFF, ACLU, EPIC)
- Report deceptive location data practices to the FTC (reportfraud.ftc.gov)
- File complaints with state AGs about location privacy violations
- Support class action litigation against location data brokers and companies that share location data without consent
- Support Fourth Amendment challenges to government purchases of commercial location data

---

## What Technology Professionals Can Do

### Build Privacy-Respecting Location Technology

- Implement location data minimization: collect only the precision necessary for the service (e.g., city-level for weather, street-level for navigation)
- Use on-device processing for location-dependent features when possible, avoiding server-side storage
- Implement location permission best practices: request "While Using" rather than "Always" access by default
- Audit third-party SDKs in your apps for location data collection; remove SDKs that harvest location data
- Publish transparent privacy disclosures in plain language about location data collection, sharing, and retention
- Implement automatic deletion of location data after it is no longer needed for the requested service

### Audit and Advocate

- Conduct security and privacy audits of location data systems
- Report location data vulnerabilities responsibly
- Participate in open-source privacy tool development (e.g., tracker detection apps, location privacy tools)
- Advocate within your company for privacy-respecting location data practices
- Refuse to implement surveillance features or location tracking SDKs that lack meaningful consent

### Research and Publish

- Conduct and publish research on location data re-identification to counter industry anonymization claims
- Develop privacy-preserving location analytics methods (differential privacy, k-anonymity, federated learning)
- Analyze RTB bid streams for location data leakage and publish findings
- Contribute to standards development for location data privacy (NIST, W3C, IEEE)

---

## What Journalists Can Do

- Investigate location data broker practices and government purchases using FOIA requests and public records
- Test de-anonymization of commercially available location datasets to demonstrate re-identification risks
- Report on connected vehicle data sharing practices and consumer impact
- Investigate geofence warrant usage in local jurisdictions through court records
- Cover the disparity between industry "anonymization" claims and scientific reality
- Highlight the disproportionate impact of location surveillance on immigrant communities, communities of color, and domestic violence survivors

---

## What Researchers Can Do

- Conduct studies on the re-identification of "anonymized" location datasets to strengthen the empirical basis for regulation
- Publish analysis of the effectiveness of privacy-preserving location analytics methods
- Study the chilling effects of location surveillance on First Amendment activity, health care seeking, and immigrant community participation
- Analyze the effectiveness of state location privacy laws to inform federal legislative efforts
- Develop and evaluate technical standards for location data de-identification
- Advise policymakers on the technical feasibility and limitations of location privacy solutions

---

## Quick Reference: Where to File Complaints

| Issue | Agency | How to File |
|-------|--------|-------------|
| App collecting or sharing location data deceptively | FTC | reportfraud.ftc.gov |
| Location data broker selling your data without consent | FTC | reportfraud.ftc.gov |
| Location data used for stalking or harassment | Local police + FTC | Local police non-emergency number; reportfraud.ftc.gov |
| Unknown AirTag or tracker detected | Local police | File a police report; Apple provides instructions at support.apple.com |
| State location privacy law violation | State AG | Your state AG's consumer complaint portal |
| Government agency accessed your location without a warrant | ACLU or EFF | aclu.org/contact or eff.org/pages/legal-assistance |
| Connected vehicle data shared without consent | FTC + State AG | reportfraud.ftc.gov; state AG complaint portal |
| Geofence warrant affecting you as a bystander | ACLU or public defender | Contact ACLU affiliate or assigned public defender |

## Document Navigation

- Previous: [Resources](09-resources.md)
- Next: [Legislation](11-legislation.md)
- Up: [Overview](01-overview.md)
