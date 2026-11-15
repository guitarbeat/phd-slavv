---
name: find-skills
description: Find, evaluate, adapt and maintain shared workspace skills; route repository-specific
  writing and engineering tasks.
---


# Find Skills

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Search this workspace's shared library before installing or creating another skill. Match the actual task, repository and invocation policy; do not select skills just because their descriptions contain a keyword. Check available connectors/tools for service capabilities. Review external source bodies and permissions before recommending an install, and use external search only when it helps the requested task. Shared additions belong in NeuroVASC/.agents/skills; repository discovery folders contain links, not forks. Preserve upstream attribution and scope-specific procedures. In phd-dissertation the optional writing sequence is fragments -> agreed terminology -> academic-writing -> optional rhetorical-compression -> optional deslop-prose; do not run every stage by default or substitute Nature-paper conventions for NIH proposal prose. Candidate scanners propose improvements; their output does not authorize new files, rules or launches.

## Choose by task

- **Find an existing workflow:** search shared names and descriptions first, resolve retired names with `../../skill-aliases.json`, and use [the inventory helper](scripts/find_local_skills.py) when a local search helps. It detects the enclosing Git repository from any nested folder. Pass `--repo-root` to select another repository, or `--root` to choose a different skills library. Outside a checkout, it searches all repository modes unless `--repo-root` is supplied.
- **Assess SLAVV work for a reusable gap:** read [SLAVV discovery and candidate review](references/modes/phd-slavv-discovery/workflow.md). It uses the shared helpers; its parity/TODO signals are specific to SLAVV.
- **Route dissertation writing or evaluate a dissertation skill:** read [NIH writing and skill maintenance](references/modes/phd-dissertation-find-skills/workflow.md). Preserve the manuscript owners and optional writing stages.
- **Choose an engineering workflow by development phase:** read [phase-based selection](references/modes/phd-research-using-agent-skills/workflow.md) only when the task needs that map. It does not require running every phase.
- **Evaluate an external skill:** read [external discovery](references/modes/phd-research-find-skills/workflow.md) only when the shared library does not cover the need or the user requests an external option.

The local Python helpers require PyYAML; use an existing workspace or repository environment that supplies it. Their output is advisory, not authorization to install skills or change repository state.
