# D:\ Drive — Development Environment Index

`D:\INDEX.md` is the human-readable map of the `D:\` development drive: it explains the drive's purpose, operating principles, root-level conventions, shared governance, infrastructure, reference material, and—later—its project areas.

> **Current scope:** This document covers the hidden foundation directories and the governed `WDS`, `BASIC`, `CTS`, `DATA`, and `DRS` portfolio roots. Later root-directory groups remain intentionally deferred.

## Contents

1. [Purpose of the drive](#1-purpose-of-the-drive)
2. [Operating model and goals](#2-operating-model-and-goals)
3. [Root-level contract](#3-root-level-contract)
4. [Central documents](#4-central-documents)
5. [Central concepts](#5-central-concepts)
6. [Hidden foundation directories](#6-hidden-foundation-directories)
   - [`D:\.city_hall`](#61-dcity_hall--governance-and-standards)
   - [`D:\.dpw`](#62-ddpw--shared-infrastructure-and-caches)
   - [`D:\.library`](#63-dlibrary--shared-reference-and-documentation-library)
   - [`D:\.sonar`](#64-dsonar--sonarscanner-cli-runtime)
7. [Known documentation and manifest drift](#7-known-documentation-and-manifest-drift)
8. [`D:\BASIC` — QB64 workshop and incubator](#8-dbasic--qb64-workshop-and-incubator)
9. [`D:\DRS` — desktop application portfolio](#9-ddrs--desktop-application-portfolio)
10. [`D:\CTS` — command tools and automation](#10-dcts--command-tools-and-automation)
11. [`D:\DATA` — shared datasets and source snapshots](#11-ddata--shared-datasets-and-source-snapshots)
12. [`D:\WDS` — websites and web applications](#12-dwds--websites-and-web-applications)
13. [Scope boundary](#13-scope-boundary)

---

## 1. Purpose of the drive

`D:\` is a 2 TB Western Digital Blue SATA SSD used as the primary formal development and project-creation drive. Development can happen elsewhere on the computer, but work moves here when it needs a durable home, clearer structure, shared resources, governance, repeatable workflows, or a path toward becoming a maintained project.

The drive is therefore more than a collection of repositories. It is an operator-managed development environment containing:

- Governance standards and reusable project conventions.
- Shared documentation, schemas, templates, styles, and reference assets.
- Local service data, model caches, SDK archives, and tool runtimes.
- Project workspaces and supporting datasets.
- Release, provenance, integrity, evaluation, and preservation records.
- Local copies of material that should remain usable without depending entirely on hosted services.

The structure is intentionally practical rather than purely taxonomic. Directories are grouped according to how they are used, maintained, recovered, and understood by the operator.

---

## 2. Operating model and goals

The drive is designed to make serious local work easier to start, understand, maintain, and recover.

### 2.1 Primary goals

1. **Give formal work a stable home.** Projects that move beyond experiments should have an intentional location, identity, and lifecycle.
2. **Keep shared dependencies local.** Large caches, models, installers, documentation, and common resources should not be duplicated inside every project.
3. **Make context recoverable.** Manifests, READMEs, standards, release notes, and evaluation records should explain what a directory is and how it is meant to be used.
4. **Support repeatable delivery.** Build, validation, hashing, provenance, packaging, and release evidence belong to the workflow rather than being afterthoughts.
5. **Remain useful offline.** Important tools and references should continue to work when a hosted service, package registry, or upstream website is unavailable.
6. **Separate projects from supporting infrastructure.** Runtime data and caches belong in shared service areas; canonical standards belong in governance areas; reusable references belong in the library.
7. **Stay navigable by both people and agents.** A future operator or agent should be able to begin at this index, follow the manifests, and identify authoritative material before changing anything.

### 2.2 High-level layout

```text
D:\
├── AGENTS.md                        Drive-wide operational constitution
├── Development.manifest.toml        Machine-readable drive identity and root registry
├── INDEX.md                         Human-readable drive map
├── .city_hall\                      Governance, standards, and framework archive
├── .dpw\                            Shared infrastructure, caches, models, and installers
├── .library\                        Shared documents, references, evals, clones, and media
├── .sonar\                          Self-contained SonarScanner CLI runtime
├── BASIC\                           QB64 tools, local runtimes, and early project ideas
├── DRS\                             Desktop applications governed by the DRS
├── CTS\                             Command tools, pipelines, generators, and utilities
├── DATA\                            Shared datasets, temporal snapshots, and source exports
├── WDS\                             Websites and web applications governed by WDS
└── ...                              Project and other directory groups documented later
```

The leading-dot directories form the drive's hidden foundation layer. They support work across projects but are not ordinary project workspaces themselves.

---

## 3. Root-level contract

Three governance files are intentionally maintained directly at the root of `D:\`:

| File | Role |
| --- | --- |
| `D:\AGENTS.md` | Short operational constitution defining precedence, inheritance, required records, naming, change safety, and release rules. |
| `D:\Development.manifest.toml` | Authoritative machine-readable identity, policy, standard registry, and governed-root registry for the development drive. |
| `D:\INDEX.md` | Primary human-readable overview and navigation document for the drive. |

Everything else should be grouped into a directory with a clear operational purpose. Reusable templates live under `D:\.city_hall\WGS\templates`, not loose at the drive root.

### 3.1 Governance record contract

The permanent entity-named convention is:

- Governed portfolio or container: `AGENTS.md` and `[DirectoryName].manifest.toml`.
- Individual project or project group: `AGENTS.md`, `[ProjectName].manifest.toml`, and `Project-README.md`.
- Optional ecosystem-facing documentation: `README.md`.

The manifest filename matches its containing directory exactly, preserving casing and punctuation. Superseded generic and duplicate manifests are preserved in dated City Hall migration archives rather than left beside the canonical record. Canonical governance links resolve to `D:\.city_hall`; standards are not copied or exposed through Windows shortcuts.

### 3.2 Maintenance commands

The WGS tooling is dry-run or read-only by default where mutation is possible:

```powershell
python D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\
python D:\.city_hall\WGS\tools\governance_scaffold.py --help
python D:\.city_hall\WGS\tools\snapshot_root_governance.py --workspace-root D:\
```

The inventory command never rewrites manifests. Scaffolding requires `--apply`, refuses existing targets, creates entity-named records, and registers the child with its parent. The root snapshot is a hash-indexed recovery copy inside the City Hall Git repository; the drive-root files remain authoritative.

---

## 4. Central documents

The current shared document set lives in `D:\.library\core_aptlantis`. These are convenient central copies and templates. The maintained standard suites under `D:\.city_hall` should be consulted when current governance authority matters.

| Document | Purpose | Location |
| --- | --- | --- |
| `aptlantis.dataset.v1.2.0.toml` | Canonical template/schema for describing a produced dataset, including identity, description, provenance, contents, and related metadata. | `D:\.library\core_aptlantis\aptlantis.dataset.v1.2.0.toml` |
| `Command Tool Standard.md` | Compact command-line tool standard covering CLI contracts, output rules, JSON envelopes, exit-code bands, compatibility, destructive operations, and release blockers. | `D:\.library\core_aptlantis\Command Tool Standard.md` |
| `Desktop Application Release Standard.md` | Detailed desktop release reference covering versioning, artifacts, hashes, verification, manifests, documentation, release gates, withdrawals, migrations, changelogs, SBOMs, and provenance. | `D:\.library\core_aptlantis\Desktop Application Release Standard.md` |
| `DIRECTORY.two-four.manifest.toml` | Concrete APTlantis Entity Manifest v2.4 directory example, currently modeled around a governed `980-DATA` root. | `D:\.library\core_aptlantis\DIRECTORY.two-four.manifest.toml` |
| `DirectoryName.manifest.toml` | Entity-named directory manifest template for portfolios and containers. | `D:\.city_hall\WGS\templates\DirectoryName.manifest.toml` |
| `NeonInk-v0.1.md` | Early NeonInk visual-language specification: semantic colors, typography, layout, components, dataset surfaces, SESM integration, voice, collateral, and validation. | `D:\.library\core_aptlantis\NeonInk-v0.1.md` |
| `PPS.md` | Compact copy of the Project Proposal Standard used to define a project's intent, limits, risks, success, and failure before broad implementation. | `D:\.library\core_aptlantis\PPS.md` |
| `ProjectName.manifest.toml` | Entity-named project and project-group manifest template. | `D:\.city_hall\WGS\templates\ProjectName.manifest.toml` |
| `Project-README.md` | Internal project orientation and handoff template. | `D:\.city_hall\WGS\templates\Project-README.md` |
| `AGENTS.*.md` | Root, directory, and project instruction templates. | `D:\.city_hall\WGS\templates` |
| `SESM-v0.2.md` | Early SVG Embedded Semantic Metadata specification covering the metadata model, embedding rules, validation, privacy, provenance, integrity, agent behavior, and implementation guidance. | `D:\.library\core_aptlantis\SESM-v0.2.md` |
| `StandardName.manifest.toml` | Reusable manifest template for an APTlantis standard suite. | `D:\.library\core_aptlantis\StandardName.manifest.toml` |
| `styles.css` | Shared stylesheet/reference implementation for the Aptlantis/NeonInk visual language. | `D:\.library\core_aptlantis\styles.css` |

---

## 5. Central concepts

Aptlantis work generally follows these principles:

- **Local-first by default** — useful without depending on hosted services.
- **Metadata matters** — files, datasets, commands, and outputs should explain themselves.
- **Operator-centered design** — tools should fit real workflows and expose trustworthy state.
- **Integrity is a feature** — hashes, manifests, release notes, provenance, and verification belong to the product.
- **Preservation over polish** — durable and recoverable artifacts matter more than trend-chasing.
- **Repeatability wins** — pipelines, schemas, manifests, logs, and checklists turn one-off work into reusable systems.
- **Small tools can be serious tools** — a focused utility can remove more friction than a much larger platform.
- **Authority should be identifiable** — templates, archives, reference copies, and active standards must not be mistaken for one another.
- **Context should survive handoff** — a project should remain understandable after time has passed or a different human or agent takes over.
- **Shared infrastructure should stay shared** — caches, runtimes, models, and references should be centralized where that improves portability and reduces duplication.

---

## 6. Hidden foundation directories

### 6.1 `D:\.city_hall` — governance and standards

#### Role

`D:\.city_hall` is a local archive and working reference for the Aptlantis governance framework. It contains standards for workspace structure, project proposals, delivery, integrity, agent work, analysis, visual semantics, and related development concerns.

City Hall is useful even when the full framework is not being applied to a project. It provides established language, checklists, schemas, and decision boundaries that can be consulted selectively instead of recreated from scratch.

#### Start here

1. `D:\.city_hall\010-CITY-HALL.manifest.toml`
2. `D:\.city_hall\README.md`
3. `D:\.city_hall\WORKSHOP-MAP.md`
4. `D:\.city_hall\WGS\README.md` for workspace governance
5. `D:\.city_hall\SFDS\README.md` for standard-suite development
6. `D:\.city_hall\PPS\README.md` before creating or reviving a governed project

#### Standard and framework map

| Folder | Name | Current role |
| --- | --- | --- |
| `AADR` | Application as Data Representation Standard | Describes application-as-data records, component maps, relationships, schemas, compatibility, and validation limits. |
| `AAMHS` | Aptlantis Archive Multi-Hash Standard | Defines integrity records and validation procedures for preserved archives. |
| `AAS` | Aptlantis Analysis Standard | Defines analysis manifests, evaluation records, metrics, comparisons, and interpretation boundaries. |
| `ARHS` | APTlantis Release Hashing Standard | Defines minimum release-artifact hashing and hash records, including SHA-256, BLAKE3, and KangarooTwelve evidence. |
| `ATS` | Agent Task Standard | Defines replayable task records, handoffs, validation summaries, blockers, and agent-work context. |
| `CTS` | Command Tool Standard | Defines CLI contracts, streams, structured output, exit codes, compatibility, and safety for command tools. |
| `DDS` | Dataset Development Standard | Defines dataset provenance, licensing, splits, validation, integrity, schemas, and release readiness. |
| `DRS` | Desktop Application Release Standard | Reference suite for desktop release notes, manifests, artifacts, hashes, verification, and release evidence. |
| `NeonInk` | NeonInk | Defines semantic color, themes, UI language, visual intent, and SESM-aligned visual metadata. |
| `PPS` | Project Proposal Standard | Defines project mission, boundaries, constraints, risks, roadmap, success, and failure before broad implementation. |
| `SESM` | SVG Embedded Semantic Metadata | Defines portable semantic metadata embedded in SVG assets, including safe use, privacy, validation, and tooling. |
| `SFDS` | Standards Framework Development Standard | Governs how standards are structured, validated, versioned, adopted, and preserved. |
| `SIS` | Service and Infrastructure Standard | Governs local services, daemons, APIs, health checks, ports, logs, resource bounds, and recovery. |
| `WDS` | Website Development Standard | Governs websites and web apps, including manifests, deployment, accessibility, routes, rollback, and monitoring. |
| `WGS` | Workspace Governance Standard | Acts as the workspace constitution for roots, manifests, lifecycle, services, responsibilities, and agent orientation. |

Every listed standard directory currently has both a `README.md` and an entity-named manifest. Many also contain specifications, changelogs, adoption guidance, validation checklists, examples, templates, schemas, or preserved references.

#### Governance routing

Use the standard that owns the question:

- **Where does this live, and how is it registered?** → WGS
- **Why should this project exist?** → PPS
- **How should a standard suite be built?** → SFDS
- **What kind of deliverable is shipping?** → DRS, CTS, SIS, WDS, or DDS
- **What integrity or evidence record is needed?** → ARHS or AAMHS
- **How should agent or analysis work be recorded?** → ATS or AAS
- **How should visual meaning or embedded metadata work?** → NeonInk, SESM, or AADR

#### Repository and workspace metadata

- The directory is a Git working tree and includes `.git`, `.gitignore`, and `.gitattributes`.
- IDE metadata is present under `.idea`.
- The City Hall README identifies `git@github.com:APTlantis/CityHall.git` as its canonical repository.
- City Hall is a governance/reference area; ordinary project creation should not happen directly inside it.

---

### 6.2 `D:\.dpw` — shared infrastructure and caches

#### Role

`D:\.dpw` is the drive's “Public Works” area: shared local infrastructure that supports development but is not itself the main project collection. It centralizes large or machine-managed data so that the development environment is more portable and project workspaces remain cleaner.

The directory should generally be treated as service state, caches, installers, and tool-managed storage. Contents may be large, frequently updated, or unsafe to reorganize while the owning application is running.

#### Resource map

| Path | Purpose | Operational notes |
| --- | --- | --- |
| `D:\.dpw\DockerDesktopWSL` | Docker Desktop WSL storage. | Currently contains `disk` and `main`. Treat as application-managed runtime data; stop Docker Desktop and use its supported migration/backup process before moving or editing it. |
| `D:\.dpw\HF` | Hugging Face local cache and authentication state. | Contains the Hub cache under `hub`, update-check state, `HF.manifest.toml`, and local token files. Token-bearing files are sensitive and must not be published, indexed into documentation, or copied into repositories. |
| `D:\.dpw\JetBrains` | Local storage for JetBrains IDE installations or managed application data. | Contains product-specific directories for Air, CLion, DataSpell, Gateway, GoLand, IntelliJ IDEA, PyCharm, Rider, RubyMine, RustRover, and WebStorm; several products have side-by-side suffixed directories. |
| `D:\.dpw\LMStudio` | LM Studio model storage. | The visible top-level payload is `models`. Expect large model files and let LM Studio manage its internal layout where possible. |
| `D:\.dpw\Ollama` | Ollama model store. | Contains content-addressed `blobs`, model `manifests`, and `Ollama.manifest.toml`. Back up blobs and manifests together; neither side alone fully describes the installed model set. |
| `D:\.dpw\Python` | Local mirror/archive of official Python release material. | Contains 270 top-level version and archive-support directories, spanning historical releases and auxiliary areas such as `binaries-*`, `contrib`, `devtest`, `pymanager`, and `pythonwin`. This is broader than a normal installed-Python directory. |

#### Management rules

- Do not treat cache presence as proof that a dependency is permanently available; record important model or package identities elsewhere when reproducibility matters.
- Do not commit credentials, tokens, machine IDs, or private cache metadata.
- Stop the owning application before manually moving application-managed storage.
- Prefer supported relocation/export mechanisms for Docker Desktop, model managers, and IDEs.
- Preserve paired content/manifest structures together.
- Projects may consume resources here, but source code and project-specific release artifacts should live in their governed project directories.

---

### 6.3 `D:\.library` — shared reference and documentation library

#### Role

`D:\.library` is the shared knowledge and reference layer for the drive. It contains reusable Aptlantis documents, documentation sites, evaluation outputs, selected Git clones, visual assets, and occasional media. Unlike `.dpw`, which is primarily tool/service state, `.library` contains material intended to be read, reused, compared, cited, or incorporated into documentation workflows.

#### Resource map

| Path | Purpose | Current contents |
| --- | --- | --- |
| `D:\.library\core_aptlantis` | Shared Aptlantis reference copies, schemas, templates, and style material. | Useful references, but canonical standards and current governance templates live under `D:\.city_hall`. |
| `D:\.library\docusaurus` | Local Docusaurus documentation publishing workspace. | Two site trees, shared/reference assets, a Caddy configuration, a Phase 2 roadmap PDF, logo assets, and CSS. |
| `D:\.library\evals` | Local copies of project evaluations produced by `AnalyzeProjects`. | JSON evaluation records for projects including Aegis, FileCabinet, CloneCratesio, Structra, SESM, Training, and others. These are snapshots/evidence, not live project state. |
| `D:\.library\ghclones` | Selected local Git repository clones used for source study or reuse. | Current top-level clones include `agents.md`, `iced`, `liboqs-rust`, `slint`, and `terminal`. A clone is not automatically an Aptlantis project or canonical upstream. |
| `D:\.library\images` | Shared visual-reference collection. | Current visible files include light/dark screenshots for completion procedures, table-to-XML conversion, and new-topic options. |
| `D:\.library\misc` | Miscellaneous reference collection. | Material not yet assigned to a more specific library class; provenance and retention should be reviewed before reuse. |
| `D:\.library\youtube` | Optional local storage for YouTube-related reference media. | Present but currently lightly used and empty at the top level. |

#### Docusaurus sites

| Path | Role |
| --- | --- |
| `D:\.library\docusaurus\docs.aptlantis.studio` | Docusaurus site for Aptlantis projects and standards documentation. Includes source docs, static assets, generated `.docusaurus` state, and a built site. |
| `D:\.library\docusaurus\docs.localhost` | Docusaurus site for personal and miscellaneous local project documentation. It has the same basic source/build layout as the Aptlantis site. |
| `D:\.library\docusaurus\refactor-refs` | Visual and project reference material used while refactoring documentation, including project screenshots, SVG/logo assets, style references, and grouped source material. |

Both site directories currently include `package.json`, `package-lock.json`, and `pnpm-lock.yaml`. Before installing or updating dependencies, choose the intended package manager deliberately and avoid casually regenerating both lockfile families.

#### Library usage rules

- Treat `core_aptlantis` as a convenient shared reference layer; consult `.city_hall` for the maintained standard suite when versions or authority differ.
- Treat `evals` as point-in-time analytical evidence. Verify conclusions against the current project before acting on them.
- Treat `ghclones` as reference/source checkouts unless a separate manifest identifies a clone as governed work.
- Keep generated Docusaurus output (`build`, `.docusaurus`) distinguishable from authored source (`docs`, `src`, `static`).
- Preserve source attribution and licensing when material moves from a clone, screenshot collection, video, or other external reference into a project.
- Avoid placing credentials, private tokens, or uncontrolled binaries in the library.

---

### 6.4 `D:\.sonar` — SonarScanner CLI runtime

#### Role

`D:\.sonar` is a self-contained Windows SonarScanner CLI installation used to submit source-analysis jobs to a SonarQube-compatible server. It is shared tooling, not an analysis project or a repository containing scan results.

#### Installed layout

| Path | Purpose |
| --- | --- |
| `D:\.sonar\bin\sonar-scanner.bat` | Main Windows launcher. It derives `SONAR_SCANNER_HOME` from this directory and starts the scanner CLI. |
| `D:\.sonar\bin\sonar-scanner-debug.bat` | Debug launcher for troubleshooting scanner execution. |
| `D:\.sonar\conf\sonar-scanner.properties` | Global scanner configuration template. The example `sonar.host.url` is currently commented out. |
| `D:\.sonar\jre` | Bundled Java runtime used by the launcher when an external Java home is not selected. |
| `D:\.sonar\lib\sonar-scanner-cli-8.0.1.6346.jar` | SonarScanner CLI implementation; the filename identifies version `8.0.1.6346`. |
| `D:\.sonar\.sonar.manifest.toml` | Canonical shared-runtime record. It records the verified CLI version, entrypoint, governance, current path, and remaining consumer-registration gap. |

#### Typical invocation

From a project that has an appropriate `sonar-project.properties` file or equivalent command-line properties:

```powershell
& 'D:\.sonar\bin\sonar-scanner.bat'
```

To confirm the installed scanner and Java runtime before a scan:

```powershell
& 'D:\.sonar\bin\sonar-scanner.bat' --version
```

Project identity, source paths, exclusions, server URL, and authentication should be supplied through the project's scan configuration and secure environment/credential handling. Tokens must not be written into this index or committed to source control.

#### Operational boundaries

- `.sonar` is a shared tool runtime; project-specific scan configuration belongs with the project.
- Analysis output and evaluation records belong in an appropriate project/evaluation area, not in the scanner installation.
- Upgrading the scanner should replace the runtime as a coherent unit and update the manifest/version record.
- Do not publish server tokens or private endpoint details in global configuration.
- Verify server compatibility and scanner release notes before upgrading.

---

## 7. Known documentation and manifest drift

The July 7–8 governance rollout established `D:\AGENTS.md`, `D:\Development.manifest.toml`, entity-named manifests, canonical WGS templates, portfolio/root instructions, project/group records, holding rules, and repeatable scaffold/inventory/audit tooling.

The drift below describes historical evidence or remaining project-specific verification work. Superseded live manifests were moved to `D:\.city_hall\WGS\migration-notes\Legacy-Live-Manifests-20260708`.

The following discrepancies were observed during the July 7, 2026 documentation pass. They are recorded here so that navigation remains honest; this pass does not silently rewrite the individual manifests.

| Area | Observed drift | Recommended correction |
| --- | --- | --- |
| `D:\.city_hall` | `010-CITY-HALL.manifest.toml` still records the directory path as `D:\010-CITY-HALL`. Its `children` list omits the existing `ARHS` directory. The README also refers to the former non-hidden path. | Update the City Hall manifest and explanatory docs if `.city_hall` is now the permanent canonical location; add `ARHS` to the manifest relationship list. |
| `D:\.dpw` | Earlier root and child records retained `D:\015-DPW` paths and incomplete inventories. | Resolved: `.dpw.manifest.toml` registers all six resources; each resource has local instructions and an entity-named manifest. |
| `D:\.library` | The former root record described an unrelated `DocHub` project at `E:/DocHub`. | Resolved: `.library.manifest.toml` now classifies the seven current reference collections; the old record is archived. |
| `D:\.sonar` | The former record described an analysis project at `D:\970-EVALS\sonar-scanner` with version `0.0.0`. | Resolved: `.sonar.manifest.toml` records the current shared runtime and verified SonarScanner CLI `8.0.1.6346`. |
| Root documentation | Earlier notes described loose manifest templates at the drive root. | Resolved: templates now live under `D:\.city_hall\WGS\templates`; `Development.manifest.toml` is the authoritative drive record. |
| `D:\BASIC` | Earlier root and child manifests retained former paths. | Resolved structurally: `BASIC.manifest.toml` and child entity manifests now use current paths; prior records are archived. Project execution evidence remains incremental. |
| `D:\DRS` | Earlier manifests described `D:\100-DRS` and the former numbered taxonomy. | Resolved structurally: `DRS.manifest.toml` registers current projects, FileCabinet, WSL, and holding. Project release evidence remains project-specific. |
| DRS project manifests | Several manifests retain former paths under `D:\100-DRS`, and some generated records report placeholder `0.0.0` versions and zero completion despite substantial source trees. | Review each manifest against its current project documentation and built artifacts before using it for portfolio reporting. |
| `D:\DRS\WSL` | `clearlinux\PROCESS.md` and other build material still cite former `D:\100-DRS\160-UTILITIES\WSL` paths. The requested `aptlantis` child is not currently present on disk. | Update process paths when the workspaces settle; add `aptlantis` only when an actual directory or governed record exists. |
| `D:\CTS` | Earlier manifests recorded `D:\200-CTS` and the former numbered taxonomy. | Resolved structurally: `CTS.manifest.toml` registers current direct projects, groups, Llama, utilities, and holding. |
| CTS project manifests | Several generated manifests retain former `D:\200-CTS\...` locations or placeholder versions/completion values that disagree with substantial current implementations and READMEs. | Reconcile each manifest with current source, documentation, tests, and release artifacts before portfolio reporting. |
| `D:\DATA` | Earlier root and child manifests retained former paths. | Resolved structurally: `DATA.manifest.toml` registers current datasets, Winget group, and root ISO artifact; dataset provenance verification remains incremental. |
| DATA documentation | The crates.io and Node.js dataset manifests point to nonexistent root-level `README.md`/`PROJECT.md` files and report placeholder `0.0.0`/0% metadata despite large, documented outputs. | Make the snapshot/output READMEs authoritative or add dataset-root orientation documents, then align manifest state with reproducible evidence. |
| `D:\DATA\winget` | Earlier duplicate directory/dataset records retained numbered paths and a phantom child. | Resolved structurally: `winget.manifest.toml` is the sole local entity authority and registers `WingetExport` as its child project. |

Until these records are normalized, the physical paths documented in this index reflect the observed July 7, 2026 layout, while the embedded historical manifest values remain evidence of the earlier numbered-directory organization.

---

## 8. `D:\BASIC` — QB64 workshop and incubator

### 8.1 Role

`D:\BASIC` is the drive's QB64 and QuickBASIC-oriented workshop. It combines local development-tool copies with a small group of QB64 application ideas and experiments. Most of the project concepts are in an initial planning or scaffolding phase; `QB-Winget` is the clear functional exception.

The directory is deliberately lighter-weight than `D:\DRS`. It is a place to preserve the language toolchain, explore compact desktop utilities, and develop ideas far enough to decide whether they should mature into governed releases.

### 8.2 Directory map

| Path | Classification | Purpose and current state |
| --- | --- | --- |
| `D:\BASIC\Inform` | Local development tool/reference | Local copy of **InForm**, a WYSIWYG GUI designer and event-driven UI engine for QB64. Its designer exports a `.frm` form definition and a `.bas` program file where application event logic is added. A Windows `UiEditor.exe`, source tree, setup scripts, README, license, and manifest are present. |
| `D:\BASIC\QB64` | Local language/runtime reference | Local copy of the original QB64 ecosystem. The visible root contains a nested `qb64` distribution plus `QB64.manifest.toml`. Keep it as tool/reference material rather than treating it as an Aptlantis-authored project. |
| `D:\BASIC\QB64PE` | Local language/runtime reference | Local copy of **QB64 Phoenix Edition**, the maintained QB64 offshoot that retains QB4.5/QBasic compatibility and compiles native Windows, Linux, and macOS binaries. The directory includes `qb64pe.exe`, compiler/source internals, settings, licenses, build files, and a local manifest. |
| `D:\BASIC\QB-Winget` | Functional QB64 application | Retro-styled QB64 GUI wrapper for Windows Package Manager. It supports package discovery, installation, list handling, and package-management workflows. The repository contains source/form files, an InForm integration, a compiled `WingettingQB64.exe`, assets, documentation, captured command output, an evaluation record, and a project manifest. |
| `D:\BASIC\QB-Veracrypt` | Pending application concept | Intended to explore a QB64 front end for encryption/VeraCrypt workflows, conceptually similar to the Winget wrapper. At present it contains a project manifest and `VeraCrypt-master.zip`; it is not yet a working QB64 application. |
| `D:\BASIC\QB-7Zip` | Pending application concept/reference | Intended to explore a QB64 front end for compression/7-Zip workflows. The current `7-zip` child is a Maven-based source tree rather than a QB64 application or a simple 7-Zip binary bundle, so the project premise and dependency source should be reviewed before implementation. |
| `D:\BASIC\BASIC.manifest.toml` | Canonical root governance record | Registers all current children, classifies `Inform`/`QB64`/`QB64PE` as external sources, and classifies the three QB utility directories as projects. |

### 8.3 `QB-Winget` — working reference project

`QB-Winget` demonstrates the practical shape that the other QB utility ideas could eventually take:

- QB64/BASIC source and InForm-generated UI definitions.
- A compiled Windows executable for direct testing.
- A project manifest and README describing identity, dependencies, capabilities, and status.
- Captured Winget search/install output for integration development.
- Saved package lists and supporting assets.
- A Git repository linked to [APTlantis/WingettingQB64](https://github.com/APTlantis/WingettingQB64).

Its current manifest identifies version `1.0.0`, active development, approximately 75% completion, and mostly stable behavior. Those values should be reverified before the next formal release rather than treated as an automatic release claim.

### 8.4 Toolchain relationships

```text
QB64 / QB64PE
    └── compile BASIC source into native applications

InForm
    └── design event-driven QB64 interfaces and generate .frm + .bas files

QB-Winget
    └── working example of a QB64/InForm Windows utility

QB-Veracrypt and QB-7Zip
    └── early concepts that may follow the same wrapper pattern
```

### 8.5 Working rules

- Preserve `Inform`, `QB64`, and `QB64PE` as identifiable upstream tool/reference copies; do not imply Aptlantis authorship.
- Keep generated forms and the hand-edited application logic distinguishable so InForm regeneration does not overwrite custom work.
- Do not describe `QB-Veracrypt` or `QB-7Zip` as functional until a runnable implementation and verification evidence exist.
- Treat encryption and archive operations as potentially destructive: preview inputs/outputs, avoid silent overwrites, and make command execution visible.
- Verify the provenance, license, and intended role of the current Maven tree under `QB-7Zip\7-zip` before building against it.
- Move a project into the release discipline of `D:\DRS` when it is expected to ship as a maintained desktop application.

---

## 9. `D:\DRS` — desktop application portfolio

### 9.1 Role and governing standard

`D:\DRS` is the portfolio root for desktop applications governed by the **Desktop Application Release Standard (DRS)**. Projects may be Windows-specific or cross-platform underneath, but they are grouped here because their intended deliverable is a desktop application, desktop package, or desktop-operated system.

The active root governance files are:

| File | Role |
| --- | --- |
| `D:\DRS\AGENTS.md` | Portfolio-specific operational rules inheriting the drive constitution. |
| `D:\DRS\DRS.manifest.toml` | Canonical directory record for current projects, FileCabinet, the WSL project group, and the holding area. |
| `D:\.city_hall\DRS` | Canonical Desktop Application Release Standard suite. |

Canonical DRS guidance resolves to `D:\.city_hall\DRS` through the manifest and Markdown links. No portfolio-local standard copy or shortcut is authoritative.

The standard's core posture is that a release is a verifiable bundle of understanding, artifact, and evidence—not merely a compiled file. In practical terms:

- The release note is the human promise.
- The manifest is the machine-readable record.
- The artifact hash binds the promise and record to the actual build.
- Destructive behavior must be detected and explained before mutation.
- Documentation and verification evidence ship with the release.
- A passing build alone does not establish release readiness.

### 9.2 Active portfolio map

| Project | Purpose | Current evidence and posture |
| --- | --- | --- |
| `AptlantisConsole` | Local-first DevOps/operator console combining a Next.js interface with a Tauri 2 Windows shell. | Version `1.0.8` is documented. Live areas include Docker, Git, system monitoring, MongoDB, DuckDB, networking, SSH/FTP, Winget, editor tools, terminals, settings, screenshots, and a command builder. `docs\CurrentAndPlannedFeatures.md` is the detailed live/partial/planned feature ledger. |
| `Chat` | **ChatArchive**, a local-first desktop archive for exported AI conversations. | Tauri 2 + React reader with a Rust OpenAI importer, SQLite state, filesystem-backed normalized conversations and assets, structured search, artifact explorers, and Markdown export. It handles both single and sharded OpenAI conversation exports. Its README states that the Phase 2 release gate remains blocked on a clean-baseline Windows installer lifecycle rerun despite other major checks passing. |
| `ChromeArchivalPlugin` | Chrome/Chromium extension tailored to the operator's page-capture and archival workflow. | Captures page/link lists, metadata, JSON-LD, readable Markdown, full-page content, screenshots, and paginated PDFs into local download structures. It combines familiar archival capabilities in one preferred workflow rather than claiming a novel category of browser extension. |
| `ClipboardFilter` | Local clipboard extraction, embedding, indexing, and lookup pipeline. | Uses staged `1-Input`, `2-Embed`, `3-Database`, and `4-Lookup` areas, Python processing scripts, DuckDB, local embeddings/Ollama, and a web lookup UI. The manifest describes version `2.0.0`, mostly-stable status, and an atomic-entry TOML processing model. |
| `CommandWizard` | Schema-driven WinUI desktop application for constructing CLI commands through a guided interface. | Release `v1.0.0` is locally packaged as a signed MSIX. The release record reports a successful Release build, 11/11 tests, a valid local signature, successful installation, and launch. Its development certificate is suitable for local/trusted testing—not public trust. |
| `DataVisualizers` | Early Tauri/React/TypeScript data-visualization workspace. | The source tree and Tauri structure exist, but the README is still the starter template and the generated manifest reports placeholder `0.0.0`/0% metadata. Treat it as experimental until its actual mission and supported formats are documented. |
| `FileCabinet` | Local-first Windows desktop vault for retaining, cataloging, previewing, verifying, and recovering technical artifacts. | Version `1.7.3` is supported by the project file, README, release notes, and historical verification records. The current checkout does not contain the documented MSI, so governance classifies it as paused rather than release-ready until build, tests, installer, hash, installation, and launch are rerun. |
| `Partitioning` | Safety-first Windows disk planning and migration application. | .NET/WPF client with a privileged native C++ engine design, durable plan/evidence records, authenticated named-pipe protocol, and a “Plan first. Execute second. Record everything.” rule. Physical-disk mutation and VSS migration are intentionally disabled pending disposable-VHD and bootable-VM qualification. |
| `Structra` | Interactive structure and layout visualization tool for architectures and organizational systems. | React/Tauri workspace with export support, docs, evaluation record, and a manifest identifying version `1.0.0`, mostly-stable status, and roughly 85% completion. Verify those generated status fields before release reporting. |
| `Tauri-IT` | Desktop packaging/adaptation of the upstream **IT-Tools** web application. | Not an original Aptlantis application concept. It is a local Tauri 2 desktop bundle of [CorentinTh/it-tools](https://github.com/CorentinTh/it-tools), retained because many of its developer and IT utilities are useful without repeatedly starting a web development server. Preserve upstream license and attribution. |
| `WinTrim` | Long-running Windows environment and installation-curation research project. | Originated in deliberate NTLite-based Windows ISO customization with a strong emphasis on understanding and documenting each removal instead of trusting opaque debloat scripts. Current material includes a large annotated removal manifest, component-removal documentation, machine/config data, a documentation architecture, and a Windows 11 ISO. The planned revival should focus on transparent desired state, evidence, and reproducibility. |
| `WSL` | Workspace for adapting Linux distributions into locally packaged WSL environments. | Contains active/recent distro experiments, rootfs artifacts, ISOs, MSIX packaging scripts, launchers, logos, inventories, and process notes. This area is artifact-heavy and currently less normalized than the other DRS projects. See the dedicated map below. |

### 9.3 Project detail and read-first documents

#### AptlantisConsole

Read in this order:

1. `D:\DRS\AptlantisConsole\AptlantisConsole.manifest.toml`
2. `D:\DRS\AptlantisConsole\README.md`
3. `D:\DRS\AptlantisConsole\docs\CurrentAndPlannedFeatures.md`
4. `D:\DRS\AptlantisConsole\AptlantisConsoleVersionMilestoneTimeline.md`

The feature ledger is especially important because it separates live behavior from partial areas, known gaps, proposals, and planned work across each operator-console surface.

#### ChatArchive

Start with `D:\DRS\Chat\README.md`, then consult `docs\Phase2-QA-Report.md` for the current release gate. The README is unusually specific about importer compatibility, local storage, artifacts, tests, privacy, and limitations; it should remain the primary orientation document until a project manifest is added.

#### ClipboardFilter

```text
1-Input      Raw clipboard/export inputs
2-Embed      Extracted entries and embedding-stage material
3-Database   DuckDB-backed indexed corpus
4-Lookup     Query/interaction layer
└── web      Web UI for searching and interacting with the database
scripts      Extraction, ingestion, and embedding utilities
```

Key scripts currently include `embed.py`, `extract_checked.py`, `extract_raw.py`, and `ingest.py`. Inputs, generated/intermediate records, the authoritative database, and the lookup interface should remain clearly separated.

#### CommandWizard

`D:\DRS\CommandWizard\RELEASE-v1.0.0.md` is the clearest release summary. It records the local MSIX path, certificate posture, install flow, validation commands, and verified results. The repository also contains the WinUI project, tests, schemas, packaging scripts, assets, and built output.

#### Partitioning

Read `Partition Wizard v1.md` for the architecture and product contract, then `README.md` for current safety status and build/test instructions. The key trust boundary is explicit: the current native service performs an authenticated handoff and recorded safe stop, but it does **not** silently fall back to DiskPart, PowerShell mutation, or physical-disk writes.

#### Structra

Read `README.md`, `Structra.manifest.toml`, and `Structra-AI-EVALUATION.json` together. The README describes intent and capabilities; the manifest provides structured status; the evaluation is analytical evidence and may age independently of the code.

#### WinTrim

The most useful current records are:

- `COMPONENTS_REMOVED.md` — detailed removal knowledge.
- `RemovalManifest_Annotated.xml` — structured annotated removal record.
- `DOCUMENTATION_ARCHITECTURE.md` — plan for standalone toolkit/GUI documentation and a unified booklet.
- `PHASE1_CLEANUP_SUMMARY.md` — completed cleanup and next documentation work.
- `README-Rules.md` — local documentation conventions.

Because the directory contains a multi-gigabyte Windows ISO, redistribution, licensing, provenance, and hash handling must be deliberate. The ISO should not be mistaken for an ordinary source artifact.

### 9.4 WSL workspace

#### Purpose

`D:\DRS\WSL` is a rapid-development workshop for converting, adapting, validating, and packaging Linux distributions for WSL. Some children are complete enough to include signed local MSIX packages and launchers; others are only source media, extracted payloads, rootfs archives, or planning documents.

The area also contains large shared source artifacts at its root. These include Clear Linux and Nitrux ISOs, Clear Linux archives, a raw disk, Debian Wheezy package indexes, logos, and a very large Clear Linux bundle archive. These files should be inventoried and hashed before deduplication or relocation.

#### Distro/workspace map

| Path | Current on-disk state |
| --- | --- |
| `WSL\antix` | antiX 26 Core ISO plus a substantial `antiX-WSL.md` process/planning document. |
| `WSL\brunson` | `BrunsonLabs-WSL.md` planning/process document; no packaged rootfs is visible at the top level. |
| `WSL\cbpp` | CrunchBang++ ISO, assets, AppX manifest, launcher, local development certificate, and MSIX build script. |
| `WSL\clear-43540-live-server` | Extracted Clear Linux live-server ISO layout with EFI, images, bootloader, kernel, and loader trees. |
| `WSL\clearlinux` | The most heavily documented Clear Linux experiment: frozen baselines, inventory outputs, smoke-test and `swupd` records, a large WSL rootfs tar, and `PROCESS.md`. The work explores not only import but the practical limits of maintaining Clear Linux as a WSL-oriented fork/environment. |
| `WSL\crunchbang` | CrunchBang ISO, rootfs tar, local MSIX releases, launcher, packaging script, overrides, and detailed investigation notes. `CRUNCHBANG_APT_CASE_STUDY.md` distinguishes the fixed missing `apt` command from deeper vintage Debian/Wheezy instability. |
| `WSL\feren` | Feren OS image/rootfs material, Windows launcher, AppX manifest, build script, local certificate, and README. |
| `WSL\nitrux` | Nitrux ISO only at present; no local packaging or process document is visible at the top level. |
| `WSL\peppermint` | Peppermint OS ISO, multiple rootfs tar iterations, local MSIX builds, launcher, manifests, assets, staging data, and packaging script. This is a built-artifact workspace, not merely a distro note. |
| `WSL\solus` | A `solus-rootfs.tar` artifact is present. Additional process documentation is not visible in the current top level and should be restored or linked if it lives elsewhere. |

The requested `D:\DRS\WSL\aptlantis` directory is not currently present and is therefore not documented as an existing workspace.

#### WSL handling rules

- Verify the real image chain for each distro; ISO layouts and package managers differ materially.
- Do not assume every rootfs is Debian/Ubuntu-based or that `apt` is available.
- Extract Linux filesystems on a filesystem that preserves permissions, links, devices, and metadata; NTFS-mounted extraction can break hardlinks and modes.
- Keep source media, extracted rootfs, normalized tar, staged package, signed package, and verification evidence distinguishable.
- Record hashes for large source and release artifacts.
- Treat local `.pfx` development certificates as sensitive release infrastructure; do not publish private-key material.
- Test imports under a distinct disposable WSL name before replacing a working distro.
- Preserve a known-good baseline before experimental pruning or package-manager changes.
- Document whether a distro is a proof of import, a maintained WSL adaptation, or an intended fork; these are very different maintenance commitments.

### 9.5 `.drs_holding` — excluded and dormant work

`D:\DRS\.drs_holding` is the quarantine/incubator area for ideas, starts, dormant projects, and incomplete work that should not appear in normal project evaluations or active-portfolio reporting.

| Path | Current role |
| --- | --- |
| `.drs_holding\Aegis` | Holds `Aegis-CPP` and `Aegis-Rust`. A separate top-level `D:\DRS\Aegis` was observed briefly during the audit but was no longer present at final verification; the holding location is the current physical state. |
| `.drs_holding\Hubris` | Contains an Aptlantis Hubris concept document, concept art, NeonInk reference, manifest, and a nested implementation tree. The generated manifest's “active” label should not override its holding-area classification. |
| `.drs_holding\ProjectTracking` | Early project/tool tracking material plus a generated manifest retaining an older path. |
| `.drs_holding\Tauri-Visualizers` | Experimental Tauri visualization bundle containing Mermaid and JSONCrack-related material, source, dependencies, build output, and a minimal README. |

Rules for the holding area:

- Exclude it from default evaluations, release dashboards, and active-project counts.
- Do not infer abandonment; “holding” means intentionally outside the active reporting surface.
- A project should leave holding only after its identity, purpose, current state, documentation, and destination are reviewed.
- Update generated manifests when promotion occurs; moving a directory alone does not make its old status/path metadata true.

### 9.6 Portfolio-level maintenance rules

- Read the project-specific manifest and current README before broad changes.
- Apply the DRS release gates in proportion to the artifact and its risk.
- Keep source, generated output, installer/package artifacts, and verification evidence distinct.
- Never report a project as release-ready solely because it builds.
- Preserve upstream attribution and license boundaries for adapted third-party projects such as IT-Tools.
- Treat disk-management, encryption, OS-image, WSL-rootfs, and installer work as elevated-risk operations requiring explicit verification.
- Exclude `.drs_holding` from ordinary active-portfolio analysis.
- Reconcile project docs, manifests, versions, and actual artifacts before publishing portfolio metrics.

---

## 10. `D:\CTS` — command tools and automation

### 10.1 Role and governing standard

`D:\CTS` is the portfolio root for command-line tools, automation utilities, generators, data-processing pipelines, and other operator-facing programs governed primarily by the **Command Tool Standard (CTS)**.

CTS exists to make command behavior dependable for both people and automation. It governs command contracts, help and version output, stdout/stderr behavior, structured output, exit codes, pipeline integration, destructive-operation safeguards, compatibility, and release verification. It does not replace the standards governing workspace placement, project intent, datasets, websites, or desktop packaging.

The current root governance files are:

| File | Role |
| --- | --- |
| `D:\CTS\AGENTS.md` | Portfolio-specific command-tool rules inheriting the drive constitution. |
| `D:\CTS\CTS.manifest.toml` | Canonical current-path manifest registering direct projects, project groups, Llama, utilities, and the holding area. |
| `D:\.city_hall\CTS` | Canonical Command Tool Standard suite. |

Canonical CTS guidance resolves to `D:\.city_hall\CTS` through the manifest and Markdown links. No portfolio-local standard copy or shortcut is authoritative.

### 10.2 CTS operating contract

A CTS-governed tool should make the following behavior explicit before its public command surface is considered stable:

- Command purpose and invocation pattern.
- Required and optional inputs.
- Normal stdout and diagnostic stderr behavior.
- Machine-readable output mode and stable fields.
- Documented exit codes.
- Human and automation examples.
- Stability level for commands, flags, and output fields.
- Preview, confirmation, recovery, or `--dry-run` behavior for destructive actions.
- Accurate `--help` and `--version` output.

CTS uses these default exit-code bands:

| Code | Meaning |
| --- | --- |
| `0` | Success. |
| `1` | General failure. |
| `2` | Invalid command usage or arguments. |
| `3` | Input file, path, or resource missing. |
| `4` | Validation failed. |
| `5` | External dependency unavailable. |
| `10+` | Tool-specific failure documented in the command contract. |

Normal data belongs on stdout; warnings, progress, diagnostics, and errors belong on stderr. A JSON mode must not mix prose progress into its stdout payload. A stable command is one that a script can invoke, parse, and respond to without reading prose logs.

### 10.3 Active portfolio map

| Project | Purpose | Current evidence and posture |
| --- | --- | --- |
| `AnalyzeProjects` | AI-assisted multi-project assessment and classification tool. | Python implementation that samples project trees, filters generated/dependency content, sends structured prompts to an Ollama-compatible model endpoint, validates JSON results, and produces per-project summaries plus aggregate statistics. It supports local or cloud-hosted models, configurable concurrency, retry/backoff, context limits, and recent-result skipping. |
| `AptlantisLogos` | Centralized visual-asset generation pipeline. | Converts AI-generated source PNG logos into standardized PNG, ICO, and SVG derivatives, extracts 16-color palettes with ImageMagick/Pillow-based tooling, emits metadata, and builds a local HTML palette/logo atlas. Its palettes directly feed `LangThemeGenerator`. |
| `CloneCratesio` | High-performance crates.io mirroring and metadata pipeline. | Go command tools with a Python orchestration wrapper. Downloads `.crate` archives from a local crates.io index, supports loose and rolling `tar.zst` storage, writes JSONL/sidecar metadata, restores bundles, and exposes Prometheus/pprof telemetry. The README records a June 11, 2026 full-registry run with 2,490,647 successes and zero final errors. |
| `ConversionTools` | Small, opinionated local media-conversion suite. | Groups Rust/FFmpeg audio and video converters with a CPU-oriented Python Whisper transcription utility. Input conventions and common settings are intentionally preselected for the operator's usual workflows. |
| `DatasetPipelines` | Emerging home for repeatable dataset-production pipelines. | Introduces a formal Rust-oriented pipeline model in which the dataset, provenance, validation, training splits, model metadata, reports, and reusable pipeline are all products. Current children are `Winget` and `TinyLlama-HolyC`; their implementation maturity differs. |
| `FH-RefToolkit` | Flathub catalog/ref acquisition toolkit. | Python tools for AppStream parsing, catalog querying, list generation, and `.flatpakref` download. It works, but its documentation, structure, command contracts, and generated status records lag behind the current quality bar and should be revisited before being presented as a current production example. |
| `LangThemeGenerator` | Palette-to-theme generator linked to `AptlantisLogos`. | Converts 16-color ecosystem palettes into themes for VS Code, Notepad++, JetBrains IDEs, and terminals. Includes generated theme trees, palette inputs, documentation, screenshots such as `project_images\jb-zig.png`, and a manifest. Generated themes have also been exposed through the main website for download. |
| `Llama` | HolyC dataset-generation and model-preparation project group. | Contains the Rust `create-dataset` producer and Python-oriented `layer-one` workspace with substantial JSONL corpora. Governance now identifies the children explicitly; provenance, regeneration, schemas, hashes, and training boundaries remain the next verification priorities. |
| `UTILITIES` | Collection of narrowly scoped supporting command tools. | Contains seven small converters, mappers, metadata processors, and search/copy tools. These should remain separately understandable even though they share one portfolio directory. |

### 10.4 `AnalyzeProjects`

#### Purpose

`D:\CTS\AnalyzeProjects` is a project-intelligence tool for quickly extracting useful metadata from many local codebases. It is used for classification, sorting, progress assessment, missing-piece discovery, next-step suggestions, and creative upgrade ideas.

Its model connection is Ollama-compatible, which permits the same workflow to use either:

- A local model hosted through Ollama.
- A cloud-hosted model exposed through an Ollama-compatible endpoint.

Cloud models are often preferred for speed and stronger project inference, while local models remain useful when privacy, offline operation, or cost control is more important.

#### Processing model

```text
Configured project roots
    ↓
File filtering and bounded sampling
    ↓
Structured project-analysis prompt
    ↓
Local or cloud Ollama-compatible model
    ↓
JSON validation and retry handling
    ↓
Per-project JSON + aggregate Markdown/statistics
```

The current implementation includes configurable roots, explicit standalone projects, directory exclusions, file/character limits, three-worker concurrency by default, exponential retry behavior, seven-day result skipping, progress logging, and schema validation.

#### Read first and security

1. `D:\CTS\AnalyzeProjects\README.md`
2. `D:\CTS\AnalyzeProjects\config.toml`
3. `D:\CTS\AnalyzeProjects\Summarizer.py`
4. `D:\CTS\AnalyzeProjects\PromptTemplate.py`
5. `D:\CTS\AnalyzeProjects\ModelClient.py`

The local Git remote identifies [APTlantis/AnalyzeProjects](https://github.com/APTlantis/AnalyzeProjects) as the upstream repository.

Model API keys must not be committed. Prefer environment variables or another secret store, and remember that selecting a cloud model sends sampled project content outside the machine. Sensitive repositories require an explicit privacy decision before analysis.

### 10.5 `AptlantisLogos` and `LangThemeGenerator`

These projects form one connected visual pipeline:

```text
Programming-language or ecosystem concept
    ↓
AI-generated Aptlantis source PNG
    ↓
AptlantisLogos
    ├── normalized PNG derivatives
    ├── ICO assets
    ├── SVG assets
    ├── extracted color palettes
    ├── logos.json metadata
    └── local HTML atlas / palette board
              ↓
       LangThemeGenerator
              ├── VS Code themes
              ├── Notepad++ themes
              ├── JetBrains themes
              └── terminal themes
```

The source logo is inspired by a programming language's syntax or ecosystem identity, but its colors are not necessarily that language's official brand colors. They may reflect the image model's composition and should be labeled as Aptlantis interpretations rather than official language branding.

`AptlantisLogos` currently contains separate `png`, `ico`, `svg`, `palettes`, `themes`, and `scripts` trees plus `logos.json` and a large generated `palette-atlas.html`. The atlas is a local static board and generated artifact; its approximately 258 MB size makes regeneration and source/derived separation important.

`LangThemeGenerator` consumes the palette layer through `generate_theme.py` and produces multiple IDE/terminal theme families. Its README currently describes “one palette → 5 IDE themes.” Read `README.md`, `LangThemeGenerator.manifest.toml`, `palettes`, and `project_images` before changing mappings or published output.

Repositories:

- [APTlantis/AptlantisLogos](https://github.com/APTlantis/AptlantisLogos)
- The local `LangThemeGenerator` directory did not expose a Git remote during this audit; confirm its canonical publishing location before documenting one.

### 10.6 `CloneCratesio`

`D:\CTS\CloneCratesio` is a production-oriented crates.io mirror system built for large captures, offline Rust development, archival work, and metadata analysis.

#### Architecture

| Component | Role |
| --- | --- |
| `Clone-Index.py` | Outer orchestration layer around the compiled command tools and local index workflow. |
| `cmd\download-crates` | Concurrent crate downloader with retries, integrity behavior, loose/bundle storage modes, progress, and telemetry. |
| `cmd\generate-sidecars` | Generates per-crate JSON or aggregated JSONL sidecar metadata. |
| `cmd\extract-bundles` | Restores rolling bundle contents into the standard crates.io shard layout. |
| `internal` | Shared Go implementation packages. |
| `docs` | Architecture, quick-start, release, air-gap, metrics, and operational evidence. |
| `testdata` | Bounded fixtures for validation and development. |

The README identifies `v1.1.0` as the current documented release and shows the actual large-scale run evidence near the top. Its root manifest still reports `1.0.0`, so release reporting should use the README/release document and reconcile the manifest before the next publish action.

Read first:

1. `D:\CTS\CloneCratesio\README.md`
2. `D:\CTS\CloneCratesio\docs\Architecture.md`
3. `D:\CTS\CloneCratesio\docs\Quickstart-Windows.md`
4. `D:\CTS\CloneCratesio\docs\RELEASE-v1.1.0.md`
5. `D:\CTS\CloneCratesio\CloneCratesio.manifest.toml`

Repository: [APTlantis/Clone-Cratesio](https://github.com/APTlantis/Clone-Cratesio)

### 10.7 `ConversionTools`

`D:\CTS\ConversionTools` groups three task-focused local media tools:

| Path | Implementation | Role |
| --- | --- | --- |
| `ConversionTools\VideoToMP4` | Rust + FFmpeg | Converts common video inputs to MP4 using the operator's usual input and output conventions. Contains a Cargo project, source, built target tree, and help text. |
| `ConversionTools\Audio` | Rust + FFmpeg | Performs common audio conversion work through a small compiled Rust wrapper. Contains an independent Cargo project and target tree. |
| `ConversionTools\CPU-Whisper` | Python + Whisper | CPU-oriented local transcription using small/base/tiny Whisper-class models. Contains `main.py` and a minimal requirements file. |
| `ConversionTools\in` | Shared input staging | Convenience location for source media. Inputs should not be confused with source code or durable release artifacts. |

The suite is intentionally opinionated: it avoids repeatedly reconstructing FFmpeg and transcription commands for common local jobs. That convenience should still be backed by visible input/output paths, overwrite behavior, dependency checks, and meaningful exit codes.

Repository: [APTlantis/SimpleConversionTools](https://github.com/APTlantis/SimpleConversionTools)

### 10.8 `DatasetPipelines`

#### Purpose

`D:\CTS\DatasetPipelines` is a newer effort to replace one-off, project-attached dataset generation with reusable and inspectable pipelines. The governing idea in `Aptlantis Rust Pipeline Template.md` is that a dataset should never simply appear as `train.jsonl`; it should ship with evidence explaining source material, transformations, exclusions, rules, structure, intended model objective, and quality checks.

The target pipeline stack is:

```text
Source material
    ↓
Rust pipeline
    ↓
Normalized corpus
    ↓
High-signal dataset
    ↓
Training splits
    ↓
Model/fine-tune metadata
    ↓
Evaluation and validation reports
    ↓
Published dataset bundle
```

#### Current children

| Path | Current state |
| --- | --- |
| `DatasetPipelines\Winget` | Existing Winget-manifest conversion work being drawn toward the formal pipeline model. The current directory is mixed Go/Python rather than a completed Rust pipeline and includes a compiled converter plus a roughly 533 MB `winget_manifests-6.1.jsonl` artifact. Treat this as migration/prototype work, not proof that the Rust pipeline standard is already complete. |
| `DatasetPipelines\TinyLlama-HolyC` | Rust/Cargo pipeline workspace with `src`, build output, transcripts, and both `aptlantis.pipeline.toml` and `aptlantis.dataset.toml`. This more closely reflects the intended repeatable pipeline shape. |

The root `DatasetPipelines.manifest.toml` describes an active `0.1.0` framework at roughly 75% completion, but those generated status fields should be reviewed alongside actual pipeline validation and reproducibility.

### 10.9 `FH-RefToolkit`

`D:\CTS\FH-RefToolkit` is the current home of the Flathub reference toolkit. Its working purpose is to:

- Parse Flathub AppStream/catalog data.
- Query application metadata.
- Generate lists of Flatpak references.
- Download `.flatpakref` files for deployment or package-management workflows.
- Support both packaged Python code and standalone scripts.

The directory contains `src`, `StandAloneScripts`, build output, `Download.py`, `Query.py`, a Dockerfile, Python project metadata, and two manifests: `FH-RefToolkit.manifest.toml` for the current container and `FlathubRefs.manifest.toml` for the underlying project identity.

Its current README still presents a polished “production/95%” FlathubRefs snapshot while the container manifest describes an experimental `0.0.0` command tool. This contradiction is exactly why the project needs a deliberate revisit: establish the canonical name, command surface, packaging model, tests, current Flathub API assumptions, and release evidence before updating status.

### 10.10 `UTILITIES`

`D:\CTS\UTILITIES` collects narrow tools that are useful enough to preserve but do not need a large top-level project presence.

| Utility | Purpose and current shape |
| --- | --- |
| `appstream_to_jsonl` | Python converter for AppStream XML/catalog data into JSONL/Flatpak-ref-oriented records. Includes source and generated data, schema, README, and manifests. The checked-in XML and JSONL outputs are data artifacts and should be versioned intentionally. |
| `dir_mapper` | Directory/ecosystem mapping and graph-visualization experiments. Includes Python conversion, large graph JSON, DOT/SVG output, Linux genealogy datasets, crates data, and local HTML force-graph viewers. |
| `extract_winget_manifests` | Python iterations for converting Winget YAML manifests into JSON/JSONL, with conversion status, help text, and encoder tests. Overlaps materially with `DatasetPipelines\Winget` and should eventually have a documented source-of-truth relationship. |
| `JSON-JSONL` | Small Go converter between JSON and JSONL-oriented records, with sample crate and package-manifest inputs and a compiled executable. |
| `platform_views` | Rust-based generated/static platform view project with `site`, `src`, build output, and project manifest. Its exact supported views and command contract need deeper documentation. |
| `search_and_copy` | Minimal Go search-and-copy utility with source, module file, and help text. |
| `svg_metadata` | Python tool for applying or managing structured SVG metadata using an asset schema, override file, and sample assets. It should stay aligned with SESM expectations where applicable. |

Utility rules:

- Each tool should have its own help text or README, explicit inputs/outputs, and failure behavior.
- Generated datasets and compiled binaries should be distinguishable from source.
- Overlapping tools should name the authoritative implementation and migration path.
- A utility that gains a stable external command contract can be promoted into a first-class CTS project without changing the meaning of its existing commands casually.

### 10.11 `.cts_holding` — excluded and dormant work

`D:\CTS\.cts_holding` is the non-active reporting area for projects that should not appear in ordinary CTS evaluations, portfolio counts, or release dashboards.

| Path | Current role |
| --- | --- |
| `.cts_holding\EpicVideos` | Media-production pipeline with Python package structure, tests, examples, output, and a manifest. Although its manifest calls it active/mostly stable, its physical holding classification is authoritative for portfolio inclusion. |
| `.cts_holding\GithubAcquisition` | PowerShell-based ecosystem/repository acquisition work with workflow, schema, examples, and generated manifests. Retains an older `D:\200-CTS` manifest path. |
| `.cts_holding\PythonDocs` | Preserved Python documentation project/material, including `python-complete-6-1`, README, and manifests. Currently concept-classified. |
| `.cts_holding\Training` | Training/dataset experiments including `RustForSmallModels` and `RustTrainingGemma4`. Its manifest describes a completed Rust Corpus Forge dataset tool, but holding placement means it is excluded from current active reporting until reviewed. |
| `.cts_holding\ScriptWriters` | Local LLM podcast/script generation system using Ollama and XTTS, with Python package code, tests, configuration, CPU/CUDA requirements, outputs, and a generated production-status manifest. It remains intentionally outside the active CTS surface. |

`EpicVideos` was listed separately in the planning notes, but the current physical location is `.cts_holding\EpicVideos`; it is documented only as held work.

Holding rules mirror `.drs_holding`:

- Physical holding placement excludes a project from default evaluations even when an older manifest says `active` or `production`.
- Holding does not mean abandoned; it means intentionally outside the current active portfolio.
- Promotion requires a review of purpose, source state, documentation, command contract, tests, manifest, destination, and release posture.
- Generated completion percentages do not override operator classification.

### 10.12 Portfolio relationships and maintenance rules

The main CTS relationships are:

```text
AptlantisLogos palettes ───────→ LangThemeGenerator themes

Winget source manifests ───────→ extract_winget_manifests
                         └──────→ DatasetPipelines\Winget

Flathub AppStream data ────────→ FH-RefToolkit
                         └──────→ UTILITIES\appstream_to_jsonl

Local project trees ───────────→ AnalyzeProjects evaluations

crates.io index ───────────────→ CloneCratesio mirror + metadata
```

Portfolio rules:

- Treat the Command Tool Standard as the command-behavior authority.
- Read the project README, manifest, help output, and examples before changing a public command.
- Verify generated status/completion fields against real tests and artifacts.
- Keep model/API credentials out of repositories and document when source material is sent to a cloud model.
- Preserve upstream attribution, data licensing, and source provenance.
- Record reproducible inputs, transformations, validations, and outputs for dataset pipelines.
- Avoid mixing human progress text into machine-readable stdout.
- Require previews or explicit confirmation for destructive copy, overwrite, publish, delete, or mutation commands.
- Exclude `.cts_holding` from active portfolio reporting.
- Keep large generated assets and datasets reproducible where practical; do not let a 258 MB HTML atlas or 533 MB JSONL file become the only surviving form of its source data.

---

## 11. `D:\DATA` — shared datasets and source snapshots

### 11.1 Role and governance

`D:\DATA` is the drive's shared dataset and source-snapshot store. It separates durable, reusable data products from the command tools and pipelines that produce, transform, validate, or consume them.

The distinction matters:

- `D:\CTS` contains executable pipelines and tooling.
- `D:\DATA` contains their large data inputs, temporal snapshots, processed outputs, and reusable reference exports.
- A dataset is not considered reproducible merely because its output files exist; its source, transformation, schema, statistics, dates, and validation evidence must remain identifiable.

`D:\DATA\DATA.manifest.toml` is the canonical root record. It establishes DDS as primary, registers the three current children, classifies `crates.io` and `node.js` as datasets and `winget` as a project group, and records the root ISO as an artifact.

### 11.2 Root map

| Path | Role | Current contents |
| --- | --- | --- |
| `D:\DATA\crates.io` | Temporal crates.io ecosystem datasets. | January through April 2026 snapshots containing document-level and version-level JSONL, Parquet, source dumps, README documentation, and build statistics. |
| `D:\DATA\node.js` | Processed Node.js API documentation dataset. | A single `output` tree containing document-level and granular JSONL, granular Parquet, README documentation, and statistics. |
| `D:\DATA\winget` | Windows Package Manager catalog/reference snapshots. | Three large dated JSON exports, a local copy of Winget Export, and both directory- and dataset-level manifests. |
| `D:\DATA\Win11_25H2_English_x64.iso` | Uncategorized source artifact. | A 7,736,125,440-byte Windows 11 ISO currently stored directly at the DATA root. Its intended dataset/project relationship is not documented and should be reviewed. |
| `D:\DATA\DATA.manifest.toml` | Canonical root governance record. | Current-path APTlantis Entity Manifest v2.4 record with registered classifications and explicit verification gaps. |

### 11.3 `crates.io` temporal datasets

#### Purpose

`D:\DATA\crates.io` preserves monthly views of the evolving Rust package ecosystem. The datasets are derived from crates.io index data and retain both normal and yanked releases. That makes them useful for:

- Supply-chain and dependency analysis.
- Ecosystem growth and evolution studies.
- Resolver and version-history research.
- Yanked-version and security-oriented analysis.
- Retrieval, model-training, and code-intelligence experiments.
- Reproducible comparison of the registry at different points in time.

The root `cratesio.manifest.toml` classifies the material as a DDS-governed data project but still points to the former `D:\980-DATA\981-CRATESIO\cratesio` location and nonexistent root documentation files.

#### Data views

Each documented snapshot provides two complementary logical views:

| View | Unit | Intended use |
| --- | --- | --- |
| **Documents / macro** | One record per crate, aggregating its release history. | Package lifecycle, maintenance, ecosystem context, and broader model context. |
| **Granular / micro** | One record per crate version. | Dependency resolution, version-specific analysis, feature/checksum inspection, yanked-release research, and fine-grained retrieval. |

The granular data is supplied as JSONL for streaming workflows and as Parquet for efficient columnar filtering and analytical queries. Document records preserve the full version history in a crate-level representation.

#### Snapshot inventory

| Snapshot | Source/build date | Unique crates | Versions | Yanked versions | Principal files |
| --- | --- | ---: | ---: | ---: | --- |
| `jan-2026` | Statistics generated February 5, 2026 from `crates-1-29.26.jsonl`. | 222,152 | 1,934,833 | 92,972 | `crates_documents.jsonl`, `crates_granular.jsonl`, `crates_granular.parquet` |
| `feb-2026` | February 14 source snapshot; statistics generated March 22, 2026. | 227,133 | 1,980,440 | 93,534 | `Cratesio.2-14-26.jsonl`, documents/granular JSONL, granular Parquet |
| `mar-2026` | March 15 source snapshot; statistics generated March 22, 2026. | 238,012 | 2,071,078 | 95,933 | `Cratesio.03-15-26.jsonl`, documents/granular JSONL, granular Parquet |
| `apr-2026` | April 17, 2026 snapshot/build. | 254,393 | 2,211,049 | 98,778 | `crates_04-17-26.jsonl`, dated documents/granular JSONL, dated Parquet |

The April statistics report a 4.47% yanked-version share. Directory names represent the intended temporal snapshot, while each `STATS.md` records the actual generation time and source filename; both should be retained because processing can occur after the source month.

#### Snapshot files and storage posture

Individual JSONL files are large—roughly 3.7 GB to 5.0 GB each—while the Parquet files are hundreds of megabytes. These should be treated as dataset artifacts rather than ordinary source files.

Each snapshot currently includes:

- A README describing provenance, methodology, schema, and intended use.
- `STATS.md` with exact record counts and source/build information.
- A crate-level documents JSONL view.
- A version-level granular JSONL view.
- A granular Parquet view.
- For February through April, a dated/raw or precursor JSONL source artifact in the same snapshot directory.

January also contains a `.git` directory. That makes it the only monthly snapshot currently carrying repository metadata and should be a deliberate choice rather than an accidental difference between snapshots.

#### Relationship to CTS tooling

The datasets are closely related to `D:\CTS\CloneCratesio` and the emerging dataset-pipeline work:

```text
crates.io index / mirror metadata
    ↓
CloneCratesio acquisition and sidecar tools
    ↓
dataset transformation / flattening
    ↓
D:\DATA\crates.io\<monthly snapshot>
    ├── documents JSONL
    ├── granular JSONL
    ├── granular Parquet
    ├── README
    └── STATS.md
```

The monthly READMEs reference earlier processing locations such as `src/process_crates.py` and `scripts/cmd`. Those scripts are not present inside the current snapshot roots, so the canonical pipeline repository and exact command/version used for each build should be linked explicitly during normalization.

### 11.4 `node.js` API dataset

#### Purpose

`D:\DATA\node.js\output` contains a structured dataset derived from the official Node.js API documentation JSON. It flattens a large hierarchical documentation source into two model- and analysis-friendly views:

| File | Unit and purpose | Size |
| --- | --- | ---: |
| `nodejs_documents.jsonl` | Module-level records preserving high-level API context and nested content. | 723,690,415 bytes |
| `nodejs_granular.jsonl` | Individual functions, properties, events, and other API items for retrieval or instruction-oriented work. | 694,821,483 bytes |
| `nodejs_granular.parquet` | Columnar form of the granular dataset for DuckDB/Pandas-style filtering and analysis. | 153,811,230 bytes |
| `README.md` | Provenance, methodology, schemas, and use cases. | Documentation |
| `STATS.md` | Build date, source path, counts, and output inventory. | Documentation |

The February 2, 2026 statistics record:

- 26,883 module/document records.
- 570,380 granular function/property/event records.

The document view supports broad conceptual association—for example, keeping related `fs` APIs together—while the granular view supports retrieval of a specific method, property, signature, or event. Parquet enables analytical questions such as filtering by stability classification or comparing API shapes across modules.

#### Provenance gaps

`output\README.md` records the original source as `datasets/raw/nodejs.all.json` and the processor as `src/process_nodejs.py`, but neither the raw source nor the processor is present under the current `D:\DATA\node.js` root. The statistics also retain an older source path, `d:/Projects/Datasets/raw/nodejs.all.json`.

To make the dataset independently reproducible, the root should eventually identify:

- Exact Node.js documentation version or commit.
- Source URL and acquisition date.
- Source checksum.
- Canonical processor repository and version.
- Transformation command/configuration.
- Schema version and validation results.
- Licensing and redistribution terms for derived documentation data.

### 11.5 `winget` catalog data

#### Purpose

`D:\DATA\winget` holds dated Windows Package Manager catalog exports plus a local copy of a third-party browsing/export interface. The data is useful for package discovery, manifest inspection, catalog analysis, list generation, ingestion experiments, and feeding Winget-oriented tools or datasets.

#### Snapshot inventory

| File | Date encoded in name | Contents | Size |
| --- | --- | --- | ---: |
| `winget.all-2-23-26.json` | February 23, 2026 | Full package/version/installer-oriented records, including identifiers, versions, installer types, commands, dependencies, release dates, and installer metadata. | 512,771,579 bytes |
| `winget.locale-en-US-2-18-26.json` | February 18, 2026 | English (United States) package locale metadata such as identifiers, package names, publishers, authors, URLs, licenses, descriptions, and related fields. | 192,555,051 bytes |
| `winget.locale-en-US-2-23-26.json` | February 23, 2026 | Later English locale snapshot in the same general record family. | 192,229,285 bytes |

These are JSON arrays rather than JSONL streams. Because each file is hundreds of megabytes, consumers should prefer streaming parsers or conversion to JSONL/Parquet instead of loading the entire array into memory without bounds.

The February 18 and February 23 locale files provide a natural temporal comparison, but the root currently has no `README.md`, `STATS.md`, checksums, record counts, acquisition commands, or schema note explaining exactly how the exports were generated.

#### `WingetExport`

`D:\DATA\winget\WingetExport` is a local clone of [4lrick/winget-export](https://github.com/4lrick/winget-export). The Git remote confirms that upstream identity.

The project provides a browser interface for:

- Searching the Winget package catalog.
- Selecting and reordering packages.
- Exporting selections as Winget JSON, PowerShell, or a command line.
- Importing the generated JSON through `winget import`.
- Rebuilding its local `data\index.json` package index.

It is useful as an upstream reference and operator convenience for grabbing package identifiers, export manifests, and installation lists. It is not an Aptlantis-authored project, and its MIT license and upstream attribution should remain intact.

The clone contains a static frontend, source, local data, a server component, assets, package metadata, a pnpm lockfile, and a GitHub Actions workflow that can update the package index. Its local `WingetExport.manifest.toml` is a generated Aptlantis inventory record, not an assertion of authorship or a replacement for the upstream project metadata.

#### Relationships to local tools

```text
Winget catalog/export data
    ├──→ D:\BASIC\QB-Winget
    ├──→ D:\DRS\AptlantisConsole Winget surface
    ├──→ D:\CTS\DatasetPipelines\Winget
    ├──→ D:\CTS\UTILITIES\extract_winget_manifests
    └──→ D:\DATA\winget\WingetExport
```

These consumers have different goals. The raw DATA snapshots should remain immutable inputs; transformations, UI-specific indexes, saved package lists, and generated training records should be written to distinct outputs with their own provenance.

### 11.6 Data lifecycle and handling rules

#### Snapshot identity

Every durable dataset snapshot should record:

- Canonical dataset name and schema version.
- Source system, URL/repository, and source version or commit.
- Acquisition date and transformation date.
- Exact input filename and checksum.
- Pipeline/tool version and invocation.
- Record counts, validation results, and known exclusions.
- Output filenames, sizes, and SHA-256 hashes.
- License, redistribution constraints, and attribution.
- Relationship to earlier and later snapshots.

#### Immutability and regeneration

- Treat dated snapshots as immutable once published or consumed by downstream work.
- Corrections should produce a clearly labeled replacement/revision rather than silently mutating a dated artifact.
- Keep generated data reproducible from an identified source plus an identified pipeline version.
- Do not rely on directory timestamps as dataset acquisition dates; preserve explicit dates in manifests and statistics.
- Use streaming tools for multi-gigabyte JSON/JSONL data.
- Prefer Parquet for repeated analytical filtering while retaining JSONL where portability and streaming matter.
- Keep raw/source, normalized, granular, document-level, split, validation, and packaged outputs distinguishable.

#### Storage and integrity

- Large data files should have recorded hashes; filenames and byte sizes alone do not establish identity.
- Avoid copying multi-gigabyte snapshots casually between projects. Consumers should reference the shared DATA location or use a documented derived-data workflow.
- A Git repository is not automatically appropriate for multi-gigabyte generated outputs; use a deliberate large-artifact or dataset publication strategy.
- Verify available disk space before regeneration because pipelines may temporarily require source, intermediate, and final forms simultaneously.
- Preserve README and statistics files with their matching snapshot.
- Do not delete an older snapshot merely because a newer month exists; temporal comparison is part of the value.

### 11.7 Root ISO review item

`D:\DATA\Win11_25H2_English_x64.iso` is not part of the crates.io, Node.js, or Winget datasets. A file with the same name and byte length was observed under `D:\DRS\WinTrim`, but matching name and size are not enough to prove identical content.

Before moving or deduplicating either copy:

1. Compute and compare SHA-256 hashes.
2. Decide which project or source-media archive owns the canonical copy.
3. Update WinTrim documentation/configuration if its expected path changes.
4. Preserve licensing and redistribution boundaries.
5. Use a reference/link or documented shared-source relationship if both workflows need the same ISO.

No hash comparison or file relocation was performed during this documentation pass.

---

## 12. `D:\WDS` — websites and web applications

`D:\WDS` is the governed portfolio for websites and web applications. Its canonical standard is `D:\.city_hall\WDS`.

The active governance records are `D:\WDS\AGENTS.md` and `D:\WDS\WDS.manifest.toml`. Every active direct child is registered and has `AGENTS.md`, an entity-named manifest, and `Project-README.md`. `.wds_holding` is registered and excluded from active reporting.

| Project | Classification | Current shape |
| --- | --- | --- |
| `aptlantis-one` | Project | Vite-based web application with client, server, public assets, and shared styling. |
| `aptlantis-two` | Project group | Contains independently governed `aptlantis` and `webserver` children. |
| `linux-genealogy` | Project | Linux genealogy web/data project with maintained data, reference material, and generated visualization output. |
| `portfolio-website` | Project | Next.js portfolio website with routes, components, data, hooks, styles, and public assets. |

The governance rollout establishes structure and authority, but each project still carries an explicit project-specific verification gap for current build, deployment, version, and lifecycle claims.

---

## 13. Scope boundary

This document currently covers:

1. The purpose, operating model, root contract, central documents, and central principles of `D:\`.
2. The hidden foundation directories: `.city_hall`, `.dpw`, `.library`, and `.sonar`.
3. The QB64 workshop and incubator at `D:\BASIC`.
4. The governed desktop-application portfolio at `D:\DRS`, including its WSL workshop and `.drs_holding` area.
5. The command-tool portfolio at `D:\CTS`, including dataset pipelines, small utilities, and `.cts_holding`.
6. The shared dataset store at `D:\DATA`, including crates.io temporal snapshots, Node.js API outputs, Winget catalog exports, and the uncategorized root ISO review item.
7. The website and web-application portfolio at `D:\WDS`, including the nested `aptlantis-two` project group.

No later root-directory group is documented yet. The next pass should begin from the next explicitly selected section rather than pulling unrelated directories into this one.
