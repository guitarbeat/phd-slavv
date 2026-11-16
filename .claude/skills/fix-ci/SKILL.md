---
name: fix-ci
description: Diagnose failing pull-request checks, apply focused fixes, and monitor
  the check set when requested.
---


# Fix Ci

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Use `gh pr checks` for all PR-attached checks; `gh run list` covers only GitHub Actions. Inspect the first actionable failure and logs or the external check link, apply a focused fix, and run its local equivalent. Monitor pending checks in bounded waits; after an authorized push, refresh the full check set. Retry a suspected flake once with evidence. Do not bypass hooks or claim a pass from pending checks. Commit/push only within existing authorization. Read the detailed CI mode when log analysis needs it; upstream Streamlit build commands apply only inside streamlit/streamlit.

## Select the relevant procedure

- [phd-research: fixing-streamlit-ci (general technique; repository-specific commands remain scoped)](references/modes/phd-research-fixing-streamlit-ci/workflow.md). Read only when this procedure matches the task.
- [phd-slavv: fix-ci](references/modes/phd-slavv-fix-ci-agents/workflow.md). Read only when this procedure matches the task.
- [phd-slavv: loop-on-ci](references/modes/phd-slavv-loop-on-ci-agents/workflow.md). Read only when this procedure matches the task.
