# Improve Codebase Architecture

Find architectural friction and propose implementable deepening opportunities.
Do not depend on external design skills or slash commands.

## Context To Read

1. `AGENTS.md`
2. `CONTEXT.md` (ADR / agent-owned process surfaces)
3. Relevant `research/howtos/decisions/`
4. **[`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md)** — package map + command table (SoT)
5. Package READMEs under `tools/*/README.md` for the subsystem under review
6. `tools/quality/hooks/README.md` when hooks are in scope
7. `planner/README.md` when Gantt tooling is in scope

Do not restate the tools package map in this skill; open the README.

## Review Heuristics

- Prefer deeper modules with small public surfaces over many shallow wrappers.
- Use `infra.filesystem_utils.ProjectLayout` before adding path logic.
- Keep `tools/manage.py` as the user-facing command router; move reusable logic
  into domain modules (`proposal_ops`, `planner_ops`, `cli`, …).
- Preserve Makefile entrypoints when moving scripts.
- Prefer stable package façades when splitting (`from inventory import …`); do not
  keep eternal `helpers` barrels after consumers have moved.
- Treat tests as interface documentation. A refactor that deletes tests without
  replacing coverage is not an improvement.
- Do not re-merge citation audit or build helpers into monoliths without a
  strong reason.
- Skills describe agent process; **do not** move runnable code into
  `.claude/skills/`.

## Output

Produce a short architecture report with:

- Candidate refactor name
- Files involved
- Current friction
- Proposed target shape
- Tests affected or added
- Risk level: strong, worth exploring, or speculative

If a visual report helps, write it outside the repo in `$TMPDIR` and provide the
absolute path. Keep visuals optional; the decision record matters more.

## Verification For Implemented Refactors

Focused tests while iterating. Lint / local-ci / manuscript verify / hooks:
[`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md). Do not propose re-vendoring
nature-skills into git; keep lock + `.agents/` install (`nature-for-phd`).
