# Project Proposal Standard (PPS)

![Standard](https://img.shields.io/badge/project%20standard-PPS%20v0.2.2-blue)
![Manifest](https://img.shields.io/badge/manifest-TOML-orange)
![Purpose](https://img.shields.io/badge/purpose-project%20clarity-green)
![Templates](https://img.shields.io/badge/templates-proposal-purple)
![Status](https://img.shields.io/badge/status-candidate-lightgrey)

PPS governs project creation before code boundaries are drawn. It is the north star standard for project intent: problem, mission, boundaries, success, failure, constraints, risks, and roadmap.

## Document Suite

| File | Purpose |
| --- | --- |
| `PPS.md` | Existing primary PPS draft. |
| `Project Proposal Standard.md` | Formal SFDS-shaped specification wrapper. |
| `PPS.manifest.toml` | Standard manifest for PPS. |
| `ProjectProposal.manifest.schema.toml` | Machine-readable proposal manifest shape. |
| `templates/Project-Proposal.md` | Proposal template. |
| `templates/PROJECT.manifest.toml` | Generic v2.4 project-manifest template; real projects use entity-named manifests. |
| `examples/Example-CLI-Project-Proposal.md` | Filled proposal example for a CTS-governed CLI tool. |
| `Adoption-Guide.md` | How new projects adopt PPS. |
| `Validation-Checklist.md` | Manual proposal readiness check. |
| `CHANGELOG.md` | PPS version history. |

## SFDS Suite Model

`PPS.manifest.toml` describes PPS as a standard suite.
`ProjectProposal.manifest.schema.toml` and the templates in `templates/` describe proposal and project records governed by PPS.

## Governance Role

WGS decides where a project lives and how it is registered.
PPS decides whether the project intent is clear enough to create, revive, expand, or resume.
DRS, CTS, SIS, WDS, DDS, and other delivery standards govern execution after PPS has frozen the intent boundary.

## Validation Posture

PPS is currently operational through its proposal template, filled examples, adoption guide, schema, and manual validation checklist. Automated proposal validation is a future maturity item, not a blocker for using PPS today.

The `validators` list in `PPS.manifest.toml` is intentionally empty until a real validator exists. Reviews should treat that as backlog work unless PPS starts claiming executable validation.

```mermaid
flowchart LR
    Spark["Project spark"]
    Proposal["PPS proposal"]
    Boundary{"Intent boundary clear?"}
    Register["WGS registration"]
    Execute["Delivery standard"]
    Rework["Revise mission, scope, risks"]

    Spark --> Proposal --> Boundary
    Boundary -- yes --> Register --> Execute
    Boundary -- no --> Rework --> Proposal
```
