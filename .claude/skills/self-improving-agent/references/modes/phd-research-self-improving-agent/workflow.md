> Shared-library adaptation: use NeuroVASC/.agents/skills for reusable skill edits. Older repository installation/storage examples below are historical; do not create another copy or override the selected repository’s current instructions.

# Self-Improving Agent

Use this skill to convert validated experience into durable instructions without distracting from the user's primary task.

## Core Rule

Only capture learnings that are durable, project-relevant, and validated. Do not record preferences, guesses, one-off mistakes, or unresolved theories.

## Four-Phase Loop & Slash Commands

- **`/self-improve capture`**: Record an observation with symptom, root cause ("why", not "what"), and glob scope as a behavioral directive.
- **`/self-improve promote`**: Elevate verified patterns into their canonical home (see targets below). Compress project-wide rules to one line when promoting to `AGENTS.md`.
- **`/self-improve prune`**: Review rules in `AGENTS.md` and learning docs, removing obsolete or redundant entries.
- **`/self-improve review`**: Scan the active session for user corrections, dead ends, or backtracking; extract candidate learnings.

## Repository Learning Targets

Choose the smallest durable target:

- Existing [`documentation/standards/`](../../../../../../repos/phd-research/documentation/standards) for
  verified cross-idea workflow rules; promote reproducible findings into their
  live owners and use Git history for retired supporting drafts.
  Use `/ce-compound` when available for reproducible troubleshooting capture,
  and preserve its required metadata without creating a competing root home.
- [`applications/vascular-structure/vascular-structure-speckle-modeling/research/learnings/`](../../../../../../repos/phd-research/applications/vascular-structure/vascular-structure-speckle-modeling/research/learnings/README.md) for STP-specific traps after `/ce-compound` or when writing directly.
- `AGENTS.md` for agent-operational rules that should run before or during future work, such as test commands, environment workarounds, login requirements, or data-root handling.
- `.agents/skills/<skill-name>/SKILL.md` for reusable agent behavior that applies across a class of tasks.
- Existing planning or operation docs only when the learning changes an established runbook, roadmap, or operator workflow.
- Existing repository standards, such as `documentation/standards/meeting-records.md`,
  when a cross-idea workflow already has a canonical owner. Inspect the current
  tree before choosing a target; do not create a missing root learning directory
  just because it appears in this skill's examples.

## Capture Workflow

1. Finish or stabilize the user's requested task first.
2. Identify the learning in one sentence: what failed, what proved true, and when it applies.
3. Verify with the smallest concrete command, test, code reference, or documentation source available.
4. Check for an existing home before creating a new file:

```powershell
rg -n "<keyword>|<module>|<failure phrase>" .agents/AGENTS.md documentation/standards documentation/archive/audits applications/vascular-structure/vascular-structure-speckle-modeling/research/learnings .agents/skills
```

5. Write the learning in the smallest place that future agents will naturally read.
6. Report what changed and what validation supports it.

## Generative STP Loop

Use this loop for STP operator or training improvements. For a meeting, documentation
or other cross-idea workflow audit, inspect that workflow's real artifacts and
canonical owners instead; do not run unrelated STP state/quality commands. Choose
the current host's interpreter and commands rather than copying Windows examples
on macOS. Apply the promotion and validation rules to the actual changed surface.

1. Use the active STP Python. On this Windows workstation, prefer activation or the known environment interpreter when plain `python` resolves to old Anaconda:

```powershell
. .\infrastructure\activation\windows.ps1
# or: D:\envs\idea-2p2s-dl\Scripts\python.exe -m stp ...
```

2. Read the current operator state:

```powershell
python -m two_photon_to_speckle workflow status
python -m two_photon_to_speckle self-supervised-learning status
python -m two_photon_to_speckle documentation search "stale workflow benchmark registration encoder" --limit 8
```

3. Compare the state against local memory surfaces:

```powershell
rg -n "stale|blocked|deferred|manual|accepted subset|current encoder|data root|cache|workflow check" documentation/standards documentation/archive/audits applications/vascular-structure/vascular-structure-speckle-modeling/research/learnings .agents/AGENTS.md .agents/skills
```

4. Generate candidate improvements as one of:
   - a new project-local skill for a recurring workflow,
   - an update to an existing skill,
   - an existing canonical standard update with dated audit evidence for a verified cross-idea trap,
   - an STP learnings index row for STP-specific traps,
   - an `AGENTS.md` update for a required future first-check.
5. Apply the promotion rules below before editing.
6. Validate skill edits with the skill-creator quick_validate script when available.
7. Validate documentation edits with:

```powershell
python -m two_photon_to_speckle documentation check
```

The best generative output is usually a small, named skill or solution note that removes one repeated decision from future agents.

## Solution Note Shape

For a reproducible troubleshooting note in the appropriate existing learning or
audit home, use a focused structure like this (record a date for audit evidence):

```markdown
---
module: two_photon_to_speckle.<area>
tags: [workflow, testing]
problem_type: agent-learning
---

# Short Specific Title

## Problem

One paragraph describing the recurring failure mode.

## Cause

The verified cause, with concrete paths or commands.

## Solution

The durable fix or workflow. Include exact STP commands when useful.

## Validation

The smallest command or test that proved the fix.
```

## Promotion Rules

- Promote to `AGENTS.md` only when future agents need the instruction before choosing commands or edits.
- Promote to a skill when the lesson is a repeatable procedure, not a single fact.
- Promote verified cross-idea workflow fixes to their existing canonical standard;
  retain dated supporting evidence in `documentation/archive/audits/` rather than
  turning a historical audit into a second live rulebook.
- Promote to STP [`research/learnings/`](../../../../../../repos/phd-research/applications/vascular-structure/vascular-structure-speckle-modeling/research/learnings/README.md) when the lesson is STP-specific and should change operator or training work.
- Leave no durable note when the only lesson is "read the code more carefully" or "a command failed once."

## Self-Review Prompts

Ask these before writing anything:

- Would this have prevented the same mistake in a fresh session?
- Is it specific to STP's Structure-to-Perfusion pipeline, data layout, tests, or docs?
- Is there evidence from a command, file, or user correction?
- Could this note become stale, and if so is the scope/date clear?

## Safety

- Never store secrets, tokens, Box/rclone credentials, Camber credentials, or private data payload details.
- Do not modify broad instruction files while the worktree is dirty unless the change is directly related to the current request.
- Do not add process overhead to every task. Capture only when a durable improvement is obvious and verified.
