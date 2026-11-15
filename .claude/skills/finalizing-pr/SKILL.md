---
name: finalizing-pr
description: Review and prepare branch changes for a pull request or shipping actions
  already authorized by the user.
---


# Finalizing Pr

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Review the current branch against its target and the user's stated intent. Fix actionable bugs and scope/coverage gaps, simplify noisy diffs when useful, and run repository-appropriate checks. Use a new branch when repository policy or the task requires it. Prepare a reviewable title/body describing behavior and validation. Commit, push, open or update a PR only when the user authorized those actions; do not treat invoking a local review as permission to ship. Keep unrelated work out of the commit and report remaining blockers honestly.

## Select the relevant procedure

- [phd-research: finalizing-pr](references/modes/phd-research-finalizing-pr/workflow.md). Read only when this procedure matches the task.
- [phd-slavv: new-branch-and-pr](references/modes/phd-slavv-new-branch-and-pr-agents/workflow.md). Read only when this procedure matches the task.
- [phd-slavv: review-and-ship](references/modes/phd-slavv-review-and-ship-agents/workflow.md). Read only when this procedure matches the task.
