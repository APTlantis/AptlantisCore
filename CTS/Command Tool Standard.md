# Command Tool Standard

## Status

Candidate v0.2.1.

## Scope

CTS governs CLI tools, automation utilities, command contracts, exit codes, stdout/stderr behavior, machine-readable output, pipeline integration, and release verification.

## Does Not Govern

CTS does not govern desktop GUI releases, website deployment, dataset provenance, or workspace root placement.

## Core Principles

- Text first.
- Machine-readable when requested.
- Predictable exit codes.
- Stable command names.
- Automation compatibility is a release requirement.
- Destructive commands must support preview or confirmation behavior.
- A command contract is part of the product, not an afterthought.

## Relationship to PPS and WGS

PPS defines why a command tool exists, who it serves, and what success or failure means.
WGS registers the project, lifecycle state, and workspace placement.
CTS governs the command behavior that scripts, agents, and operators depend on.

## Required CLI Artifacts

- Command contract.
- Exit code table.
- Output schema for JSON or structured output.
- Examples.
- Release checklist.
- Project manifest.
- Help output.
- Version output.
- Error examples.

## Command Contract Requirements

Every public command must have a contract before it is treated as stable.

The contract must state:

- Command purpose.
- Invocation pattern.
- Required and optional inputs.
- Normal stdout behavior.
- Diagnostic stderr behavior.
- Machine-readable output mode, if provided.
- Exit codes.
- Examples for human use and automation use.
- Stability notes for names, flags, and output fields.

## Output Rules

- Human-readable output is the default unless the tool is automation-only.
- Machine-readable output must be requested explicitly, usually with `--json`, `--format json`, or a documented equivalent.
- Normal data goes to stdout.
- Diagnostics, warnings, progress, and errors go to stderr.
- Machine-readable output must not include progress text in stdout.
- A field that automation depends on must not be renamed without a breaking-change note.
- Errors in machine-readable mode should use a documented error object or clearly documented fallback behavior.
- `--quiet` must not hide failures.
- `--verbose` must not change machine-readable data shape.

## JSON Output Envelope

CTS-governed tools that emit JSON should either use `CommandOutput.schema.json` or document why their command-specific schema is more appropriate.

The reusable envelope requires:

- `status`
- `tool`
- `version`

It allows:

- `data` for command-specific payloads.
- `warnings` for non-fatal findings.
- `errors` for structured failures.

Stable commands must document which fields inside `data` are automation-safe.

## Exit Code Bands

| Code | Meaning |
| --- | --- |
| 0 | Success. |
| 1 | General failure. |
| 2 | Invalid command usage or arguments. |
| 3 | Input file, path, or resource missing. |
| 4 | Validation failed. |
| 5 | External dependency unavailable. |
| 10+ | Tool-specific failures documented in the command contract. |

## Command Stability Levels

| Level | Meaning |
| --- | --- |
| `experimental` | Command may change without compatibility guarantees. |
| `documented` | Command has a contract, examples, and exit-code behavior. |
| `stable` | Scripts may depend on command name, flags, output fields, and exit codes. |
| `deprecated` | Command still works but has a documented replacement and removal plan. |

Public automation should depend only on `stable` commands.

## Breaking CLI Changes

The following require a major version, a compatibility note, or an explicit migration path:

- Renaming or removing a stable command.
- Renaming or removing a stable flag.
- Changing the meaning of an exit code.
- Moving normal data from stdout to stderr or the reverse.
- Renaming, removing, or changing the type of a stable machine-readable field.
- Changing default destructive behavior.
- Making an offline command require network access.

## Destructive Command Rules

Commands that delete, overwrite, move, publish, mutate, or revoke data must document:

- What will change.
- How the operator can preview the change.
- Whether `--dry-run` is available.
- Whether confirmation is required.
- What rollback or recovery path exists.

Automation-facing destructive commands should support `--dry-run` unless the command contract explains why that is impossible.

## Release Blockers

A CTS-governed tool is blocked from release when:

- Help output is missing or inaccurate.
- Documented exit codes do not match implementation behavior.
- Machine-readable output contains progress text on stdout.
- Stable JSON fields changed without a compatibility note.
- Errors cannot be detected reliably by scripts.
- Destructive commands lack preview, confirmation, or documented recovery behavior.
- Examples cannot be run or adapted by an automation consumer.

## Stability Rule

A command is automation-compatible only when a script can call it, parse the documented output, and respond to documented exit codes without reading prose logs.
