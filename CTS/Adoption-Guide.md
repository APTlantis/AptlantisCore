# CTS Adoption Guide

Use CTS for tools that are launched from a shell, called by scripts, or used in automation pipelines.

## Steps

1. Create a command contract for every public command.
2. Define exit codes.
3. Separate human output from machine-readable output.
4. Add examples for common automation workflows.
5. Add a release checklist before distributing the tool.
6. Assign command stability levels before scripts depend on command names, flags, fields, or exit codes.
7. Document preview, confirmation, and recovery behavior for destructive commands.

## SFDS Relationship

Use SFDS to maintain CTS as a standard suite.
Use CTS to govern command behavior, contracts, exit codes, output stability, and automation compatibility.
