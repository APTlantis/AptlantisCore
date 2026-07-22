# SESM Changelog

## 0.3.0 - 2026-06-11

- Promoted the public-review candidate profile to v0.3.0 after the `llm.interpretation_hints` vocabulary change.
- Added privacy considerations, conformance rules, submission pitch, contribution guidance, code of conduct, and license.
- Added `Validate-SESM-Safe.py` as the safe-profile validator.
- Added valid, invalid, and warning fixtures for safe-profile validation.
- Expanded tests to cover safe-profile validator behavior.
- Clarified schema compatibility for both `0.2.0` historical metadata and `0.3.0` public-review metadata.
- Updated security support and schema wording for the 0.3.x candidate profile.

## 0.2.3 - 2026-06-11

- Renamed the LLM hint field to `llm.interpretation_hints` before external review to reduce agent authority confusion.
- Updated SESM schema, specification, README, and threat model language to frame LLM-facing fields as non-authoritative interpretation context.

## 0.2.2 - 2026-06-11

- Added external-review documents: explainer, safe profile, threat model, security policy, validator rules, and reference implementation map.
- Clarified that SESM metadata is untrusted input and does not make arbitrary SVG safe.
- Registered the public review documents in the SESM suite manifest.

## 0.2.1 - 2026-06-10

- Added SFDS two-layer suite metadata to the SESM standard manifest.
- Added a SESM suite map example.
- Clarified README, adoption, and validation language for suite conformance versus SVG metadata readiness.

## 0.2.0 - 2026-06-10

- Added WGS/SFDS governance wrapper.
- Preserved existing SESM spec, schema, tools, and tests as authoritative.
