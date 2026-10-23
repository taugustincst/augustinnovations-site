# CSeed — Product Sheet

**AugustInnovations LLC** · **Current version:** 1.0.1 (Windows)

## What CSeed does

CSeed de-identifies clinical documents and seeds realistic synthetic data in place of the real identifiers — preparing clinical documents for software testing, demos, training, and workflow development. It runs **entirely on the user's own Windows machine**: no cloud, no uploads, no data ever leaves the workstation.

## Key facts

| | |
|---|---|
| **Platform** | Windows (single self-contained application) |
| **Input formats** | DOCX, PDF (including OCR of scanned pages via bundled Tesseract), TXT, CSV, HL7, FHIR |
| **Consistency** | The same person maps to the same fake identity across every document in a batch — names, dates, MRNs, addresses, and contacts stay internally consistent |
| **Crosswalk** | The real↔fake mapping is saved only as an AES-256-GCM encrypted file under a per-batch passphrase chosen by the user |
| **Leak check** | Every run is verified against the source identifiers before output is released; output that does not pass verification is stamped FAILED and blocked from sharing |
| **Dates** | Dates are shifted consistently, preserving intervals and document chronology |
| **Review flags** | Low-confidence OCR regions are flagged for human review rather than passed silently |

## License terms (summary — the license file controls)

- Per-organization, perpetual license for CSeed v1.x
- Up to **5 workstations** owned or controlled by the purchasing organization
- No redistribution, resale, sublicensing, or sharing outside the purchasing organization
- All v1.x updates included while v1 is current
- **14-day refunds**, for any reason, via the storefront
- Support by email

## Validation

Version 1.0.1 passed a 364-test automated suite and a full validation run on a 55-page real-world-format EHR test document with zero leaked identifier kinds. Validation notes are available on request.

## Pricing

Pricing and licensing are provided on request: **info@suds.systems**.
