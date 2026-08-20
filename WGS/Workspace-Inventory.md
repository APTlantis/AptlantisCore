# D:\ Workspace Inventory

Last reviewed: 2026-08-20

## Authority

`D:\Development.manifest.toml` is the machine-readable root registry. `D:\AGENTS.md` is the operational constitution. `D:\INDEX.md` is the human-readable map. `D:\.library\aptlantis_core` is the active standards and adopted overview library.

Canonical local manifests are entity-named: the exact containing directory name plus `.manifest.toml`. `Development.manifest.toml` remains the drive-root exception.

## Current Inventory Run

The read-only WGS inventory command was rerun on 2026-08-20 after `D:\Development.manifest.toml` was restored from current physical roots and live entity manifests.
The root manifest parses and active standards validate, but several portfolio manifests still have child-list drift against the current filesystem.

| Root | Canonical manifest | Registered children | Physical children | Inventory state |
| --- | --- | ---: | ---: | --- |
| `D:\.city_hall` | `CITY-HALL.manifest.toml` | 18 | 18 | pass |
| `D:\.library` | `.library.manifest.toml` | 4 | 4 | pass |
| `D:\.dpw` | `.dpw.manifest.toml` | 8 | 3 | drift: missing `DockerDesktopWSL`, `Inform`, `Python`, `QB64`, `QB64PE` |
| `D:\.pnpm-store` | `.pnpm-store.manifest.toml` | 3 | 3 | pass |
| `D:\.data` | `.data.manifest.toml` | 3 | 3 | pass |
| `D:\CTS` | `CTS.manifest.toml` | 12 | 8 | drift: missing `.cts_holding`, `FH-RefToolkit`, `HolyC-Llama`, `LangThemeGenerator`, `ScriptWriters`; unregistered `Single-Project Evaluator` |
| `D:\DRS` | `DRS.manifest.toml` | 17 | 7 | drift: missing legacy/renamed children; unregistered `Aptlantis Console`, `Chat Archive`, `Chrome Plugin`, `Command Wizard`, `React Workbench` |
| `D:\LDS` | `LDS.manifest.toml` | 1 | 0 | drift: missing `ReactComponentLibrary` |
| `D:\WDS` | `WDS.manifest.toml` | 3 | 1 | drift: missing `LinuxGenealogy`, `WebsiteTemplate` |

## Reconciliation Notes

- `D:\BASIC`, `D:\DATA`, `D:\.zoning`, and `D:\.sonar` are not registered in the restored root manifest because they were not physically present during the 2026-08-20 restoration pass.
- `D:\LDS` is registered as the governed portfolio for library-first projects, but its child registration currently points to missing `ReactComponentLibrary`.
- `D:\.pnpm-store` is registered as a tool-managed shared PNPM package cache.
- WDS now registers `.wds_holding`, `LinuxGenealogy`, and `WebsiteTemplate`.
- CTS now registers the current direct children, including `ArchiveHasher`, `HolyC-Llama`, and `ScriptWriters`; former `DatasetPipelines`, `Llama`, and `UTILITIES` registrations were removed.
- DRS now registers current physical children, including `CodeNote`, `QB-Winget`, and `WingettingQB64`; former `DataVisualizers` and `PackagerPlugin` registrations were removed.
- DPW now registers `Inform`, `QB64`, and `QB64PE`; `LMStudio` was removed from the current registration because it was not physically present.
- `.library` now registers only physically present collections; missing `images` and `misc` were removed from current registration.
- Strict City Hall audit repairs normalized Blue Slate artifacts, WDS `LinuxGenealogy` and `WebsiteTemplate`, CTS `ArchiveHasher`, `HolyC-Llama`, `ScriptWriters`, HolyC-Llama child layers, DRS `CodeNote`, `QB-Winget`, `WingettingQB64`, and moved DPW runtime parents.

## Repeatable Command

```powershell
python D:\.library\aptlantis_core\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\
```

The inventory command is read-only and returns nonzero when registered roots drift from physical child directories. The City Hall audit additionally checks promoted standards, portfolio children, and foundation records.

## Remaining Work

- Perform project-specific build, test, artifact, deployment, release, and lifecycle verification before making release-readiness claims.
- Review cache/resource retention policies for `.dpw` and `.pnpm-store`.
- Reconcile child lists for `.dpw`, CTS, DRS, LDS, and WDS against current physical directories.
- Refresh root-governance recovery snapshots after root/index/agent instruction edits.
