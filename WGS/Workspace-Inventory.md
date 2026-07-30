# D:\ Workspace Inventory

Last reviewed: 2026-07-25

## Authority

`D:\Development.manifest.toml` is the machine-readable root registry. `D:\AGENTS.md` is the operational constitution. `D:\INDEX.md` is the human-readable map.

Canonical local manifests are entity-named: the exact containing directory name plus `.manifest.toml`. `Development.manifest.toml` remains the drive-root exception.

## Verified Roots

The read-only WGS inventory command passed for every registered root on 2026-07-25. The stricter City Hall standards audit also passed all 25 scopes on 2026-07-25 after child-level manifest and front-door records were reconciled.

| Root | Canonical manifest | Registered children | Physical children | Inventory state |
| --- | --- | ---: | ---: | --- |
| `D:\.city_hall` | `CITY-HALL.manifest.toml` | 18 | 18 | pass |
| `D:\.zoning` | `.zoning.manifest.toml` | 4 | 4 | pass |
| `D:\LDS` | `LDS.manifest.toml` | 0 | 0 | pass |
| `D:\WDS` | `WDS.manifest.toml` | 3 | 3 | pass |
| `D:\CTS` | `CTS.manifest.toml` | 11 | 11 | pass |
| `D:\.data` | `.data.manifest.toml` | 3 | 3 | pass |
| `D:\DRS` | `DRS.manifest.toml` | 15 | 15 | pass |
| `D:\.dpw` | `.dpw.manifest.toml` | 8 | 8 | pass |
| `D:\.pnpm-store` | `.pnpm-store.manifest.toml` | 3 | 3 | pass |
| `D:\.library` | `.library.manifest.toml` | 5 | 5 | pass |

## Reconciliation Notes

- `D:\BASIC` is no longer registered because the root is not physically present.
- `D:\LDS` is registered as the governed portfolio for library-first projects and is currently empty.
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
- Refresh root-governance recovery snapshots if a snapshot update task is explicitly requested.
