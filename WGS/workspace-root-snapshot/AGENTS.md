# D:\ Drive Agent Constitution

## Scope and precedence

This file governs work anywhere under `D:\`. Read applicable instructions from the drive root toward the target directory before changing files.

Rules apply in this order:

1. Explicit operator instructions for the current task.
2. The nearest `AGENTS.md` at or above the target.
3. Parent `AGENTS.md` files, up to this document.
4. Canonical standards under `D:\.city_hall`.
5. Project documentation and manifests.

A child may specialize a parent rule for its own scope but must identify the exception. It may not silently weaken safety, integrity, preservation, or release requirements.

## Canonical governance

`D:\.city_hall` is the canonical governance location. Link to standards there; do not scatter copied standards through portfolios or projects.

- [Workspace Governance Standard](D:/.library/aptlantis_core/WGS/README.md)
- [Project Proposal Standard](D:/.library/aptlantis_core/PPS/README.md)
- [Command Tool Standard](D:/.library/aptlantis_core/CTS/README.md)
- [Desktop Application Release Standard](D:/.library/aptlantis_core/DRS/README.md)
- [Website Development Standard](D:/.library/aptlantis_core/WDS/README.md)
- [Dataset Development Standard](D:/.library/aptlantis_core/WGS/README.md)
- [Service and Infrastructure Standard](D:/.library/aptlantis_core/WGS/README.md)
- [Agent Task Standard](D:/.city_hall/ATS/README.md)

Templates, reference-library copies, migration notes, generated records, and historical manifests are not governing authority unless a canonical standard explicitly says otherwise.

## Required local records

| Entity | Required files |
| --- | --- |
| Governed portfolio or container | `AGENTS.md`, `[DirectoryName].manifest.toml` |
| Individual project | `AGENTS.md`, `[ProjectName].manifest.toml`, `Project-README.md` |
| Project group | `AGENTS.md`, `[GroupName].manifest.toml`, `Project-README.md` |

An ordinary `README.md` may remain the user-facing or ecosystem entry point. `Project-README.md` owns internal project orientation, governance, architecture, operating state, evidence, and handoff context. Link between them instead of duplicating prose.

## Naming and identity

- Use exactly the containing directory name plus `.manifest.toml` for the canonical local manifest; for example, `CTS.manifest.toml` and `CloneCratesio.manifest.toml`.
- Preserve the containing directory's casing and punctuation in the manifest filename.
- Use `Development.manifest.toml` only for the drive root.
- Use Windows absolute paths in manifest path fields.
- Keep exactly one canonical manifest per governed directory. Component/data manifests with another schema must declare a distinct role and must not claim local entity authority.
- Move superseded generic, duplicate, or historical manifests to a documented City Hall migration archive after reconciling useful evidence.
- Expose canonical standards and templates through manifest paths and Markdown links. Windows `.lnk` files, copied standards, and templates are never governance authority.

## Inheritance and classification

Every governed directory declares a class:

- `project`: one independently governed deliverable with its own lifecycle.
- `project-group`: related projects sharing governance and orientation.
- `container`: organization only; it is not independently versioned or released.

Datasets, standards, services, external sources, and archives retain their specific entity kinds but still declare whether the directory behaves as a project, group, or container where needed.

Child manifests inherit parent governance unless they explicitly declare a more specific standard. Local `AGENTS.md` files should contain only local constraints, commands, boundaries, and links needed to specialize the inherited rules.

## Change rules

- Inspect the target, its manifests, documentation, and current version-control state before editing.
- Do not move, rename, delete, archive, or broadly regenerate an entity without explicit operator approval.
- Do not overwrite unrelated or unexplained local changes.
- Record discovered drift; repair it when the task authorizes the affected scope.
- Keep parent and child paths, relationships, and inventories synchronized when structure changes.
- Never convert a template, generated placeholder, or historical copy into authority merely because it is nearby.
- Generated files must identify their generator or source and must not replace hand-maintained authority without an explicit migration.

## Release and integrity rules

- Follow the standard matching the deliverable class and any additional standards named by the manifest.
- Build and verify the actual shipping artifact before claiming readiness.
- Keep versions, hashes, release notes, manifests, and documentation aligned to the artifact.
- State blockers and partial verification plainly; a successful build alone is not a release verdict.
- Preserve provenance and existing evidence unless replacement is intentional and documented.

## Required startup sequence

Before substantial work:

1. Read this file and each nearer `AGENTS.md` down to the target.
2. Read the nearest entity-named manifest matching its containing directory.
3. For a project or group, read its entity-named manifest and `Project-README.md`.
4. Read the canonical governing standards linked by those records.
5. Inspect current source, artifacts, tests, and version-control state appropriate to the task.

If required records are missing, proceed only within the explicit task scope and report or repair the governance gap as appropriate.

The descriptive drive map lives in [INDEX.md](D:/INDEX.md). Do not turn this file into a second inventory.
