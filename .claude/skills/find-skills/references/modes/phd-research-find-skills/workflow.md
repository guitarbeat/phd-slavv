# External skill discovery

Use when the shared library lacks the requested capability or the user explicitly wants an external option. A routine request for help does not require installing a skill.

1. State the missing task capability and inspect the closest existing shared skill first.
2. Search an available official registry or source repository. If the Skills CLI is already available, `npx skills find <specific task>` is an optional search route; do not install tools solely to perform this lookup.
3. Read the candidate's SKILL.md and required resources. Check source provenance, task fit, dependencies, side effects, permissions, and current maintenance. Install counts and stars are discovery signals, not correctness evidence.
4. Recommend the smallest suitable option with its source and concrete tradeoffs. If no option fits, complete the task directly when feasible.
5. When installation or adaptation is requested, place reusable workspace instructions under `NeuroVASC/.agents/skills` and add only relevant repository discovery links. Preserve upstream attribution. Do not use bulk updates to overwrite locally adapted skills. Machine-wide installation requires the user's requested scope.
6. Validate adapted metadata/resources with `.agents/scripts/check_skills.py` from the workspace root. Repository-specific scientific, parity, and manuscript policies remain in their existing owners.
