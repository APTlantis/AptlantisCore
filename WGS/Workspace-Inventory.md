# D:\ Workspace Inventory

Last reviewed: 2026-07-08

## Authority

`D:\Development.manifest.toml` is the machine-readable root registry. `D:\AGENTS.md` is the operational constitution. `D:\INDEX.md` is the human-readable map.

Canonical local manifests are entity-named: the exact containing directory name plus `.manifest.toml`. Superseded records are preserved under `migration-notes/Legacy-Live-Manifests-20260708`, not beside current authority.

## Verified roots

| Root | Canonical manifest | Registered children | Inventory state |
| --- | --- | ---: | --- |
| `D:\WDS` | `WDS.manifest.toml` | 5 | pass |
| `D:\BASIC` | `BASIC.manifest.toml` | 6 | pass |
| `D:\CTS` | `CTS.manifest.toml` | 10 | pass |
| `D:\DATA` | `DATA.manifest.toml` | 3 | pass |
| `D:\DRS` | `DRS.manifest.toml` | 13 | pass |
| `D:\.dpw` | `.dpw.manifest.toml` | 6 | pass |
| `D:\.library` | `.library.manifest.toml` | 7 | pass |
| `D:\.sonar` | `.sonar.manifest.toml` | 4 | pass |

Registered and physical direct-child counts match for every listed root. `D:\.agents` is absent and intentionally not registered.

## Holdings

`.wds_holding`, `.cts_holding`, and `.drs_holding` each have local instructions and entity manifests. Their children are preserved but excluded from active project reporting. Reactivation requires an explicit task and a lifecycle review.

## Project metadata state

Active project/group records use evidence-backed versions or `not-versioned` and explicit lifecycle classifications: `active`, `paused`, `reference`, `experimental`, or `blocked`. Each record carries a `[verification]` boundary.

Metadata reconciliation did not execute every project's build, tests, artifact, or release flow. Those booleans remain false until a project-specific verification pass supplies current evidence. No project is declared release-ready merely because governance files exist.

## Foundation state

- `.dpw` classifies Docker Desktop WSL, HF, JetBrains, LM Studio, Ollama, and Python as shared services, caches, or runtimes.
- `.library` classifies current reference, evaluation, clone, image, miscellaneous, and media collections without treating them as governance authority.
- `.sonar` is a shared runtime; SonarScanner CLI `8.0.1.6346` was verified on 2026-07-08.

## Repeatable commands

```powershell
python D:\.city_hall\WGS\tools\workspace_inventory.py --workspace-root D:\
python D:\.city_hall\WGS\tools\city_hall_audit.py --root D:\.city_hall --workspace-root D:\
python D:\.city_hall\WGS\tools\governance_scaffold.py --help
python D:\.city_hall\WGS\tools\snapshot_root_governance.py --workspace-root D:\
```

`workspace_inventory.py` is read-only and returns nonzero when it finds drift. `governance_scaffold.py` is dry-run by default and refuses existing targets. `snapshot_root_governance.py` compares SHA-256 hashes unless `--apply` explicitly refreshes the non-authoritative City Hall recovery snapshot.

## Remaining work

- Perform project-specific build/release verification when each project is next active.
- Register DPW consumers and resource-specific retention/backup policy.
- Review library collection provenance and retention.
- Decide long-term ownership of the DATA-root Windows ISO.
