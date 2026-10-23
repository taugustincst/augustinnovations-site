# Rules of Engagement — Web Application Penetration Test

**[TEMPLATE — complete all bracketed fields and have both parties sign before any testing begins. No testing is authorized until the companion Testing Authorization is also signed.]**

**Provider:** AugustInnovations LLC dba Clinical Perimeter ("Clinical Perimeter"), 1347 Meadow Ranch St, Plumas Lake, CA 95961 · hello@clinicalperimeter.com
**Client:** [CLIENT LEGAL NAME] ("Client")
**Engagement reference:** [ENGAGEMENT ID, e.g., CP-2026-___]
**Date:** [DATE]

## 1. Scope

- **Application in scope:** [APPLICATION NAME], staging environment only
- **In-scope URLs / hostnames:** [LIST EVERY HOSTNAME, SUBDOMAIN, AND API BASE URL]
- **In-scope accounts/roles:** [LIST TEST ACCOUNTS AND ROLES TO BE PROVIDED BY CLIENT]
- **Testing approach:** White-box / gray-box (circle or delete one in the executed copy)
- **Explicitly out of scope:** production systems and any system containing real protected health information (PHI); denial-of-service and load testing; social engineering and phishing; physical security; internal-network, wireless, and mobile-application testing; any host, account, or system not listed above; [ADDITIONAL CLIENT-SPECIFIC EXCLUSIONS]

## 2. Testing window

- **Start:** [DATE AND TIME, WITH TIME ZONE]
- **End:** [DATE AND TIME, WITH TIME ZONE]
- Testing occurs only inside this window. Any extension requires written agreement (email is sufficient) from both parties before the original window closes.

## 3. Authorized techniques

Within scope and window, Clinical Perimeter may: probe and enumerate the application and its APIs; attempt authentication and session attacks against test accounts; test authorization boundaries between roles and tenants using test accounts; submit malicious and malformed input to test validation and injection defenses; inspect responses, exports, error messages, and accessible logs for PHI exposure; and use automated scanners and manual techniques consistent with the OWASP Web Security Testing Guide.

## 4. Prohibited actions

Clinical Perimeter will not: access, copy, or retain real PHI (if real PHI is encountered, testing on that path stops immediately and §8 applies); perform denial-of-service, load, or stress testing; attempt social engineering or phishing; test any out-of-scope system; exfiltrate data beyond the minimum evidence needed to document a finding; or make persistent changes to the staging environment beyond what a finding's reproduction requires (any such change is documented and reported the same day).

## 5. Test data and accounts

Client provides test accounts and a staging environment loaded with **synthetic data only**. Client confirms the staging environment contains no real PHI at the start of the window: [CLIENT INITIALS]. Credentials are exchanged through [SECURE CHANNEL — NOT EMAIL] and are rotated or revoked by Client at the end of the engagement.

## 6. Contacts and escalation

- **Client technical contact:** [NAME, EMAIL, PHONE]
- **Client escalation contact (incidents):** [NAME, EMAIL, PHONE]
- **Clinical Perimeter tester:** Taylor Augustin, hello@clinicalperimeter.com, [PHONE]
- Either party may pause testing immediately by contacting the other party's contact above. A pause is confirmed in writing (email is sufficient).

## 7. Handling of findings and evidence

Evidence is captured only as needed to document findings, stored encrypted by Clinical Perimeter, and handled per Clinical Perimeter's evidence-handling procedure. Findings are confidential to Client and are disclosed only to Client's named recipients: [RECIPIENT NAMES/ROLES]. Evidence retention and destruction follow the engagement agreement: [RETENTION PERIOD / DESTRUCTION TERMS, or "per engagement agreement dated [DATE]"].

## 8. Incident procedure

If testing appears to cause instability, data exposure, or any impact beyond the staging environment, the tester stops, preserves minimal evidence, and notifies the Client escalation contact **immediately** by phone and email. Testing resumes only with Client's written approval.

## 9. Deliverables

Full findings report, attestation letter, 60-minute remediation call, and one retest within 30 days of report delivery — per the engagement agreement / service sheet dated [DATE]. Report delivery within 10 business days of the testing window closing.

## 10. Signatures

Agreed and accepted:

**Clinical Perimeter** — AugustInnovations LLC dba Clinical Perimeter
Signature: ______________________________ Name: Taylor Augustin, [TITLE] Date: __________

**Client** — [CLIENT LEGAL NAME]
Signature: ______________________________ Name: [NAME], [TITLE] Date: __________
