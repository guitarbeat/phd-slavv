---
name: workspace-hygiene
description: "Organize, archive, or remove workspace files and source-layout clutter within a requested cleanup scope. Trace active consumers and preserve research evidence. Use consolidate-concepts for merging equivalent definitions and architectural-analysis for a read-only codebase audit."
metadata:
  keywords:
  - archive sprint
  - cleanup repo
  - dead code
  - docs cleanup
  - remove artifacts
  - repo cleanup
  - test cleanup
  - unused dependencies
  file_patterns:
  - '**/archive/**'
  - '**/cleanup/**'
  - '**/deprecated/**'
  - '**/legacy/**'
  confidence: 0.82
---


# Workspace Hygiene

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Inventory the selected workspace and its active consumers before changing layout. Distinguish source, original data, numerical results, installed dependencies, rebuildable caches and disposable scratch. Trace duplicate bytes and current callers before removing copies. Preserve dirty work, canonical inputs, raw histories, oracles, receipts and software paths. Use the user's explicit cleanup scope; a folder named cache, backup, or quarantine alone does not establish disposability. Keep one canonical owner, update affected links/configuration, and verify retained consumers. Use the static-analysis mode only for an authorized source/dependency cleanup; do not turn ordinary tidying into broad architecture work.

## Choose by cleanup scope

- **Ordinary file, documentation, or test cleanup:** read [scoped cleanup](references/modes/phd-research-repo-cleanup/workflow.md).
- **Source/dependency restructuring that needs static analysis:** read [tool-assisted consolidation](references/modes/phd-research-workspace-corral/workflow.md). Use only the tools relevant to the requested source scope.
- **SLAVV cleanup involving parity runs or evidence:** read [SLAVV preservation and cleanup](references/modes/phd-slavv-cleanup/workflow.md). Preserve its oracle, run-state, and scientific evidence rules.
