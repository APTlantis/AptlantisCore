# Standards Evaluation Backlog

## Purpose

This backlog translates the 2026-07-30 standards evaluation notes from `C:\Users\Administrator\Desktop\StaandardsEvals.md` into staged work packages.
It is the working backlog for detailed standards follow-up. `Standards-Backlog.md` remains the high-level standards roadmap, and `Documentation-Suite-Roadmap.md` remains the maturity/status tracker.

This pass organizes work only. It does not complete the individual standards, add validators, change schemas, or promote maturity states.

## Priority Model

| Tier | Focus | Standards |
| --- | --- | --- |
| Tier 1 | Foundation governance gaps | WGS, SFDS |
| Tier 2 | Near-completion polish | DRS, SESM |
| Tier 3 | Automation and example deepening | PPS, CTS, WDS, AAMHS |
| Tier 4 | Maturity evidence | LDS |

## Tier 1 - Foundation Governance Gaps

### WGS

**Path:** `D:\.library\aptlantis_core\WGS`

**Current status:** active | **Completion:** 92% | **Priority tier:** Tier 1

**Blocking gaps:**
- Formal workspace-audit dashboard data specification is complete in `Workspace-Audit-Dashboard-Spec.md`.
- A dedicated `Agent-Closeout-Procedure.md` artifact is complete and registered in the WGS suite.

**Next implementation slice:**
- Author `Agent-Closeout-Procedure.md` with exact update steps for direct and extended documentation on agent task completion. Status: complete in first WGS slice.
- Define a dashboard or metrics schema that converts inventory and audit outputs into machine-readable records, such as JSONL or DuckDB-ready tables. Status: complete in first WGS slice.
- Add structured output modes to `city_hall_audit.py` and `workspace_inventory.py`. Status: complete in WGS structured audit output slice.
- Define where periodic audit and snapshot outputs should be recorded under governed audit history. Status: complete in WGS audit history convention slice.
- Add one additional filled `Workspace-Health-Record` example for another root. Status: complete with `examples/Library-Root-Health-Record.md`.
- Map manifest fields to dashboard metrics and register that mapping in `Documentation-Suite-Roadmap.md`. Status: complete in WGS audit history convention slice.

**Optional improvements:**
- Add stricter machine schema exports for manifest v2.4.
- Add CI or scheduled audit snippets for structural regression checks.
- Add manifest-diff and link-integrity tooling.
- Publish a reference query store for entity manifests, such as DuckDB or SQLite.
- Add a minimal static dashboard front end for workspace health signals.

**Dependency notes:**
- This should lead the first implementation wave because WGS defines workspace orientation, closeout behavior, manifest truth, and audit/dashboard expectations used by later standards work.

### SFDS

**Path:** `D:\.library\aptlantis_core\SFDS`

**Current status:** Production | **Completion:** 90% | **Priority tier:** Tier 1

**Blocking gaps:**
- SFDS-specific manual validation procedures are documented in `SFDS-Validation-Guidance.md` and registered as validation support.
- `validators` and `governance_notes` are populated in `SFDS.manifest.toml`.

**Next implementation slice:**
- Author and register explicit SFDS suite-conformance validation guidance. Status: complete in SFDS validation guidance slice.
- Reference validation guidance from `Validation-Checklist.md`. Status: complete in SFDS validation guidance slice.
- Populate governance notes with decision history or policy clarifications and register them in the manifest. Status: complete in SFDS validation guidance slice.
- Add one or two additional adopter example suites beyond DRS. Status: complete with `examples/WGS-Candidate-Suite.md`.
- Clarify compatibility policy in the primary specification. Status: complete in SFDS validation guidance slice.
- Record known adopters in the manifest or adoption guide as adoption begins. Status: complete in `SFDS/Adoption-Guide.md`.

**Optional improvements:**
- Add a lightweight executable validator for required suite files and `STANDARD.manifest.schema.toml` conformance.
- Add local, GitHub Actions, or Azure CI snippets for SFDS validation.
- Tighten manifest schema enums for maturity, status, and promotion state.
- Add machine-readable compatibility rules or a compatibility matrix.
- Add a minimal non-DRS adopter manifest example.

**Dependency notes:**
- SFDS should follow WGS in the first implementation wave because it governs the standard-suite shape used by the remaining backlog.

## Tier 2 - Near-Completion Polish

### DRS

**Path:** `D:\.library\aptlantis_core\DRS`

**Current status:** Production | **Completion:** 95% | **Priority tier:** Tier 2

**Blocking gaps:**
- No explicit blocking gap was identified in the eval notes.

**Next implementation slice:**
- Publish a short CI snippet demonstrating `drs.ps1` usage, such as release checks and hashing. Status: complete in `DRS/docs/CI-Usage.md`.
- Add optional BLAKE3 compute/verify mode to `drs.ps1` and document when to prefer it over SHA-256. Status: complete via `drs hash <path> --blake3` and optional `check-release` verification.
- Provide one fully populated adopter manifest beyond MiniVault, covering non-trivial dependency provenance and data-migration fields. Status: complete with `DRS/examples/FieldDesk/FieldDesk.manifest.toml`.
- Add troubleshooting guidance for common `drs.ps1` failures and expected exit codes. Status: complete in `DRS/docs/Troubleshooting.md`.
- Record exact PowerShell runtime compatibility and either sign `drs.ps1` or provide script-signature guidance. Status: complete in `DRS/docs/Troubleshooting.md`.

**Optional improvements:**
- Tighten manifest schema patterns and add machine-readable release-note metadata.
- Add companion validators for BLAKE3 and signature verification.
- Add structured release-note metadata export, such as JSON-LD.
- Publish CI workflows for continuous release gating.
- Add a minimal GUI verifier for release folders.

**Dependency notes:**
- DRS remains the reference implementation pattern for validators and examples; use it to inform SFDS, CTS, WDS, and AAMHS automation style.

### SESM

**Path:** `D:\.library\aptlantis_core\SESM`

**Current status:** In Progress | **Completion:** 90% | **Priority tier:** Tier 2

**Blocking gaps:**
- No explicit blocking gap was identified in the eval notes, but spec filename/version visibility needs reconciliation before adopters rely on it.

**Next implementation slice:**
- Reconcile canonical spec filename and version visibility, especially `SESM-v0.2.md` versus suite version `0.3.0`. Status: complete in `SESM/Specification-Version-Note.md`.
- Publish validator JSON exit-code matrix and a small JSON example output. Status: complete in `SESM/VALIDATOR-RULES.md` and `SESM/examples/validator-json-basic-safe.json`.
- Add a lightweight conformance test harness example for `Validate-SESM-Safe.py` and fixtures. Status: complete in `SESM/tests/CONFORMANCE-HARNESS.md`.
- Document recommended sanitizer or pipeline steps for pairing SESM safe-profile checks with independent SVG sanitization. Status: complete in `SESM/SANITIZER-PIPELINE.md`.
- Add cross-version compatibility fixtures showing `0.2.0` to `0.3.0` migration behavior. Status: complete in `SESM/fixtures/compatibility/`.

**Optional improvements:**
- Add a language-agnostic extraction/parsing library example in Rust, Go, or JavaScript.
- Add optional signature or integrity endorsements for SESM blocks.
- Automate validator tests in CI and publish JSON reports.
- Define a stricter ingestion profile for metadata size, remote references, and `llm` field limits.
- Add a JSON-LD mapping guide for structured-data interoperability.

**Dependency notes:**
- SESM work should stay aligned with its existing validator, fixtures, safe profile, and NeonInk-related references.

## Tier 3 - Automation and Example Deepening

### PPS

**Path:** `D:\.library\aptlantis_core\PPS`

**Current status:** active | **Completion:** 85% | **Priority tier:** Tier 3

**Blocking gaps:**
- No explicit blocking gap was identified in the eval notes.

**Next implementation slice:**
- Register PPS suite location and lifecycle mapping in WGS. Status: complete with `PPS/WGS-Lifecycle-Mapping.md`.
- Publish a lightweight proposal generator that creates proposal and entity-manifest skeletons from templates. Status: complete with `PPS/tools/pps_new.py`.
- Document PPS readiness-level mapping to WGS lifecycle transitions. Status: complete in `PPS/WGS-Lifecycle-Mapping.md`.
- Add a worked example showing proposal adoption and delivery-standard handoff. Status: complete in `PPS/examples/Proposal-To-Delivery-Handoff.md`.
- Record archival proposal snapshots to demonstrate provenance and drift detection. Status: complete in `PPS/examples/proposal-snapshots/`.

**Optional improvements:**
- Add an optional reference validator for required manifest fields and structured diagnostics.
- Add schema enumerations for status, readiness, and operational personas.
- Add local lint or CI examples for checklist execution.
- Define a simple JSONL export format for proposal metadata.
- Add normative PPS-to-delivery-standard mapping examples for DRS, CTS, SIS, WDS, and DDS.

**Dependency notes:**
- PPS should use WGS lifecycle language and SFDS suite conventions after those foundation gaps are clarified.

### CTS

**Path:** `D:\.library\aptlantis_core\CTS`

**Current status:** In Progress | **Completion:** 85% | **Priority tier:** Tier 3

**Blocking gaps:**
- No explicit blocking gap was identified in the eval notes.

**Next implementation slice:**
- Publish a small reference validator prototype for help output, exit-code table presence, and JSON envelope conformance. Status: complete with `CTS/tools/cts_validate.py`.
- Add complete human and JSON command-output examples for adopter tools. Status: complete with manifest-audit contract plus JSON success/error examples.
- Document semantic versioning and migration notes for command-contract field changes. Status: complete in `CTS/Command-Versioning-Migration-Notes.md`.
- Add a CI snippet showing validation-checklist execution. Status: complete in `CTS/CI-Usage.md`.
- Clarify `data` payload expectations in `CommandOutput.schema.json` or provide command-specific schema guidance. Status: complete in `CTS/JSON-Data-Payload-Guidance.md`.

**Optional improvements:**
- Tighten `CommandOutput.schema.json` with recommended data-shape guidance and common error-code mappings.
- Add machine-checkable JSON fixtures.
- Add cross-language reference implementation examples.
- Add a command-contract linter for instability risks.
- Add compatibility notes for progress output so machine output stays parseable.

**Dependency notes:**
- CTS validator and output-envelope work should borrow from the DRS reference style where practical.

### WDS

**Path:** `D:\.library\aptlantis_core\WDS`

**Current status:** In Progress | **Completion:** 80% | **Priority tier:** Tier 3

**Blocking gaps:**
- Automated WDS validator tooling is complete with lightweight manifest, route, and accessibility smoke-check tools.
- Runnable route-check and accessibility smoke-check implementations are complete and registered.

**Next implementation slice:**
- Implement an executable validator that consumes `SiteManifest.schema.toml` and checklist expectations. Status: complete with `WDS/tools/wds_validate.py`.
- Add a runnable route-check script and accessibility smoke-check wrapper referenced by deployment templates. Status: complete with `WDS/tools/route_check.py` and `WDS/tools/accessibility_smoke.py`.
- Add CI or local examples showing validation on deploy and `Deployment-Record.md` emission. Status: complete in `WDS/templates/Deployment-Record.md`.
- Expand `SiteManifest.schema.toml` with concrete example values and edge-case constraints. Status: complete in `WDS/SiteManifest.schema.toml`.
- Document WGS registration flow and publication approval steps before a site is marked `published`. Status: complete in `WDS/Publication-Approval-Flow.md`.

**Optional improvements:**
- Add a reference CLI that fills deployment records from CI artifacts and commit metadata.
- Add JSON-LD metadata examples.
- Add reusable preview/production route-check harnesses.
- Add optional monitoring integration fields.
- Define a minimal conformance test suite and example validator outputs.

**Dependency notes:**
- WDS publication states should line up with WGS registration and any SFDS validation conventions.

### AAMHS

**Path:** `D:\.library\aptlantis_core\AAMHS`

**Current status:** In Progress | **Completion:** 85% | **Priority tier:** Tier 3

**Blocking gaps:**
- No explicit blocking gap was identified in the eval notes.

**Next implementation slice:**
- Refine `HashManifest.schema.toml` with item-level file entry types, array item schema, and allowed hash algorithm keys. Status: complete in `AAMHS/HashManifest.schema.toml`.
- Add a concrete `templates/Hash-Manifest.toml` example with actual computed hashes. Status: complete with concrete template fields and `AAMHS/examples/Example-Hash-Manifest.toml`.
- Publish one or two small reference validator scripts for checklist automation and signature verification examples. Status: complete with `AAMHS/tools/aamhs_validate.py` and `AAMHS/tools/aamhs_signature_check.py`.
- Link or embed ARHS reference sections for quick cross-reference. Status: complete in the AAMHS primary specification quick boundary table.
- Record maintainer contact and expected update cadence in the manifest. Status: complete in `AAMHS/AAMHS.manifest.toml`.

**Optional improvements:**
- Add JSON Schema or JSON-LD mapping for broader tool compatibility.
- Add CI or automation snippets for generating and validating hash manifests.
- Add a lightweight validator script or executable and register it as adopter-provided validation support.
- Extend schema for pluggable algorithm lists and versioned hash-suite declarations.
- Add a canonical signed archive integrity record example.

**Dependency notes:**
- AAMHS should coordinate with DRS and ARHS so release hashing and archive preservation hashing stay distinct.

## Tier 4 - Maturity Evidence

### LDS

**Path:** `D:\.library\aptlantis_core\LDS`

**Current status:** candidate-active | **Completion:** 75% | **Priority tier:** Tier 4

**Blocking gaps:**
- Machine-readable schema artifact is registered.
- LDS has completed-interface validation examples for two independent library shapes.
- LDS has a simulated breaking-change cycle example.
- `render-manifest.crate` remains staged because concrete crate artifacts do not yet exist.

**Next implementation slice:**
- Author or register the declared machine-readable schema artifact and reference it in `LDS.manifest.toml`. Status: complete with `LDS/LibraryInterfaceNote.schema.json`.
- Onboard one completed library adopter and produce a filled `Library-Interface-Note`. Status: complete with `LDS/examples/ManifestQuery.Core-Library-Interface-Note.md`.
- Validate LDS against a second independent library adopter. Status: complete with `LDS/examples/HashSuite.Core-Library-Interface-Note.md`.
- Run or simulate a breaking-change cycle with an adopter. Status: complete with `LDS/examples/Breaking-Change-Cycle.md`.
- Decide whether executable validators are desired; if so, author and register lightweight validators. Status: complete with `LDS/tools/lds_validate.py`.
- Promote the `render-manifest.crate` example out of staging once concrete crate artifacts exist. Status: deferred honestly; concrete crate artifacts do not yet exist.

**Optional improvements:**
- Add JSON-LD mapping for `Library-Interface-Note`.
- Add fully filled real-adopter examples showing lifecycle transitions.
- Add optional CI snippets for missing-field checks.
- Add a canonical semver and breaking-change policy template, including Rust MSRV notes.
- Add a short validator-runner example for repository checklist checks.

**Dependency notes:**
- LDS maturity should follow foundation work because its schema and evidence conventions depend on SFDS and WGS patterns.

## Coverage Check

The eval source standards are represented exactly once in this backlog:

- WGS
- SFDS
- DRS
- SESM
- PPS
- CTS
- WDS
- AAMHS
- LDS

Every eval source `Missing Pieces` and `Next Steps` item is captured above. `Potential Improvements` items are captured as optional improvements and should be scheduled only after the next implementation slice for that standard is accepted.
