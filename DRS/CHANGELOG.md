# DRS Changelog

## Unreleased

- Added CI usage guidance for running `drs.ps1` from local automation and Windows CI.
- Added troubleshooting, PowerShell 7 compatibility, and script trust guidance.
- Added optional BLAKE3 support to `drs.ps1 hash` and `check-release` when `b3sum` or `blake3` is available.
- Added a second filled adopter manifest example, `examples/FieldDesk/FieldDesk.manifest.toml`.

## 1.0.2 - 2026-06-11

- Promoted DRS to SFDS reference maturity after SFDS v1.0 stabilization.
- Updated suite validation language to distinguish DRS folder conformance from adopter desktop release validation.
- Clarified README language so DRS is explicitly the reference implementation for the mature City Hall standard-suite pattern.

## 1.0.1 - 2026-06-10

- Clarified that DRS conforms to SFDS at the standard-suite governance layer while remaining authoritative for desktop release behavior.
- Documented the two-layer manifest model for the DRS suite and DRS adopter project manifests.
- Added SFDS-facing manifest metadata for validators, governance notes, reference examples, and adopter artifacts.
- Clarified that the DRS validation checklist is for release readiness, not SFDS suite conformance.

## 1.0.0 - 2026-06-10

- Registered DRS under WGS/SFDS with a standard manifest.
- Preserved existing DRS specification, schema, templates, examples, and CLI as authoritative.
