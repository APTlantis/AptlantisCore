# WGS Validation Checklist

This checklist validates workspace governance readiness under WGS. SFDS suite conformance for WGS is tracked by `WGS.manifest.toml` and the WGS suite map.

- [ ] `D:\AGENTS.md` and `D:\Development.manifest.toml` exist.
- [ ] Root inventory is current.
- [ ] Target directory map is separate from current state.
- [ ] Governed portfolios and containers have `AGENTS.md` and `[DirectoryName].manifest.toml`.
- [ ] Projects and project groups have `AGENTS.md`, `[ProjectName].manifest.toml`, and `Project-README.md`.
- [ ] Each governed directory has exactly one canonical entity manifest.
- [ ] Standards have entity-named standard manifests.
- [ ] Governed projects have exactly one lifecycle state or a recorded lifecycle gap.
- [ ] Project classes are recorded closely enough to identify the governing domain standard.
- [ ] Shared services are registered, intentionally excluded, or queued for directory manifests.
- [ ] Metadata records support discovery by purpose, class, lifecycle state, governing standard, or relationship.
- [ ] Agent startup procedure is available.
- [ ] Canonical standard links resolve under `D:\.city_hall`; no copied standard or Windows shortcut is a governance dependency.
- [ ] Manifest physical paths and parent/child relationships match the current filesystem.
- [ ] Agent read-first order is available from manifests or identity docs.
- [ ] Workspace health state is recorded for reviewed roots.
- [ ] Drift between current state and target state is recorded before moves or renames.
- [ ] Next safe action is documented for blocked or drifted roots.
- [ ] Superseded projects link to their successor.
- [ ] Paused or archived projects have enough context to be reactivated or audited later.
