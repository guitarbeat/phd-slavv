> Shared-library adaptation: use NeuroVASC/.agents/skills for reusable skill edits. Older repository installation/storage examples below are historical; do not create another copy or override the selected repository’s current instructions.

# Find Skills

**Source of truth for skill routing** in this repository. Other docs list skills
briefly and point here. Prefer local repo conventions over generic upstream
behavior.

## Skill routing matrix

| Need | Primary skill | Notes |
|---|---|---|
| Pre-draft ideation / angle | `writing-fragments` | Piles under `reports/writing-fragments/`; not LaTeX |
| Term / glossary lock | `grill-with-docs` → `domain-modeling` | Writes `CONTEXT.md` |
| NIH proposal / appendix prose | `academic-writing` | Preserve claims, cites, LaTeX; owns readability and jargon |
| Page-limit compression | `rhetorical-compression` | Author-gated; preserve rhetorical anchors and scientific locks |
| Author identity / write-like-me | `identity-profile` | Build or apply `identity/VOICE.md`; protocol in the skill |
| De-AI / voice score | `humanizer` | SoT: `.claude/commands/humanize.md`; author sample: `identity/VOICE.md` |
| Diff-scoped slop (code/docs/prose) | `deslop` | Then humanizer for deep prose |
| Subgroup talks / presentation delivery | `giving-presentations` | Define one memorable arrow, use takeaway titles, add state changes, rehearse with the Accordion Method |
| Evidence-first PPTX composition / supplemental QA | `presentation-skill` | **Keep-as-cache / optional:** guidance-only lab-report grammar + QA if installed under `.agents/skills/presentation-skill/` (upstream `siril9/presentation-skill`). Not in `skills-lock.json`; absence on a fresh clone is OK. Do not vendor the ~68MB body into `.claude/`. Living deck builders + Artifact Tool / bundled `Presentations` remain authoritative |
| LaTeX build, floats, bib, Overleaf | `latex-skills` (+ `references/`) | Router only; not nested skills |
| Paper intake to vault | `fetch-paper` | Lean inventory first |
| Merge duplicates | `consolidate` | Code **or** research track |
| Tool architecture review | `improve-codebase-architecture` | `tools/` map |
| Project CLI diagnostics / commands | `phd-writing-cli` | Start with `phd-writing --json doctor` |
| Ruff / hooks | `python-code-quality` | Commands: `tools/README.md` |
| Nav docs | `project-readme` | One SoT home per domain |
| Nature package | **`nature-for-phd` first** | Install/allowlist lives only in that skill |

### Proposal writing ladder

This is the only writing-order SoT. Other skills point here.

`writing-fragments` → (optional `grill-with-docs`) → `academic-writing` →
optional `rhetorical-compression` → optional `deslop` → optional `humanizer`.
Do not run the whole ladder by default. Commands: [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md).

Do not run academic-writing + nature-writing + researchwrite + humanizer on the
same pass unless the user asked for a multi-lens review.

## Workflow (install / adapt)

1. Clarify the recurring task the skill should support.
2. Check this matrix and existing local skills in `.claude/skills/` before
   searching outside.
3. If a new skill is needed, search with `npx skills find <query>` or inspect a
   user-provided repository.
4. Before recommending or installing, review the skill body for:
   - stale paths or assumptions that conflict with `AGENTS.md`
   - unsafe commands, destructive operations, or hidden network behavior
   - unnecessary token-heavy prose
   - missing validation steps
   - outlet mismatch (Nature CNS paper vs NIH proposal)
5. Install with the user's requested command or `npx skills add ...`.
   Non-interactive: `npx skills add <source> --skill '*' -y` or `--all`.
6. Read the installed `SKILL.md` and decide whether it works as-is or needs a
   repo-specific rewrite / bridge skill (see `nature-for-phd`).
7. Update `skills-lock.json` when the installed skill is tracked or customized.
8. Update `.claude/skills/README.md` and `research/howtos/agents/skills.md` when the
   public skill set changes (short lists only; keep the matrix here).

## Local Policy

- Imported skills are starting points, not source of truth.
- If a skill changes purpose materially, rename it to a project-specific name
  and mark the lockfile entry as local.
- Keep `SKILL.md` concise; move long references into `references/` only when
  they are actually needed (see `latex-skills/references/`).
- Tell the user to restart Codex / Claude / Grok after installing or renaming
  skills.
- **Rule of three:** do not install a skill until wanted in three real sessions
  (bridges that prevent harm are the exception).

## Validation

```bash
python -m json.tool skills-lock.json >/dev/null
npx skills list
```

After editing a **tracked** `SKILL.md`, refresh its lock hash:

```bash
shasum -a 256 .claude/skills/<name>/SKILL.md
# paste lowercase hex into skills-lock.json → skills.<name>.computedHash
# keep "sourceType": "local" for repo-owned skills
```

Prefer updating repo-local tooling skills (`python-code-quality`,
`improve-codebase-architecture`, `project-readme`, `consolidate`, `latex-skills`)
when `tools/` layout or hooks change, rather than installing a parallel generic
plugin skill.
