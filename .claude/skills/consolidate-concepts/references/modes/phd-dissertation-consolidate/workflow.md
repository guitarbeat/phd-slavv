# Consolidate

Consolidate repository artifacts without losing behavior, citations, history, or
test coverage. Pick the track that matches the work:

| Track | Use when |
|---|---|
| [Code and tooling](#code-and-tooling) | Python modules, scripts, Makefile targets, imports, tests |
| [Research concepts](#research-concepts) | Definitions, terminology, notes, lab dossiers, manuscript claims |

For pure prose polishing without moving concepts, use `academic-writing` or
`latex-skills`. For AI-pattern cleanup, use `deslop` or `humanizer`. Routing:
`find-skills`.

## Code And Tooling

### Workflow

1. Read `AGENTS.md` and every source file in full before editing.
2. Choose the canonical target. Package map:
   [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md). Research layout:
   [`research/README.md`](../../../../../../repos/phd-dissertation/research/README.md). Skills are agent
   process only — do not park runnable code or a second command table there.
3. Move content into the canonical target by preserving public API, citations,
   examples, tests, and user-facing behavior.
4. Update all imports, links, Makefile targets, command docs, tests, and README
   references that pointed at the old files.
5. Delete tracked files with `git rm`; use plain deletion only for untracked
   generated artifacts.
6. After consolidations, run the local-ci gate in
   [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md) and fix failures before
   considering work done.

### Rules

- Do not commit unless the user explicitly asks.
- Do not rewrite from scratch when appending/merging preserves intent.
- Do not touch unrelated dirty worktree changes.
- For Python under `tools/`, keep `PYTHONPATH=tools` on direct module
  invocations.
- Keep public package façades when splitting (`from inventory import …`); migrate
  temporary re-export barrels (e.g. old `helpers.py`) to focused modules.
- On macOS, use BSD-compatible shell commands; `sed -i ''` requires the empty
  string argument.
- After tooling consolidations: [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md)
  (`tools-lint` / local-ci).

## Research Concepts

Use this track when the user wants to merge, deduplicate, or centralize
conceptual material rather than code modules: definitions, theory summaries,
related-work claims, method descriptions, terminology, and cross-module idea
dossiers.

### Repository Model

Layout SoT: [`research/README.md`](../../../../../../repos/phd-dissertation/research/README.md) and
[`AGENTS.md`](../../../../../../repos/phd-dissertation/AGENTS.md). Dossier packets live under
`research/dossiers/<name>/`. Literature intake: `fetch-paper`.

Default destination choices:

- Durable concept definitions usually belong in `research/concepts/`.
- Raw multi-module literature usually belongs under `research/literature/`
  with inventory in `research/concepts/literature-sources.md`.
- Dossier-specific papers belong in `research/dossiers/<name>/literature/` plus
  `research/dossiers/<name>/knowledge/` (or archive, per that dossier's README).
- Module-specific research synthesis usually belongs in
  `research/modules/<module>/README.md`.
- Project process concepts belong in `research/howtos/`.
- Manuscript-ready prose belongs in `proposal/` + `private-appendix/` +
  `latex-shared/`, but only after concept consolidation is complete.
- Generated outputs in `reports/` or `generated/` are usually consumers, not
  canonical homes, unless the user explicitly says otherwise.

### Guiding Principle

Consolidation must preserve the scholarly claim surface. Do not silently change
meaning, citation support, scope, uncertainty, terminology, or evidence level.
The output should create one clearer source of truth and update references to
point there.

When consolidating code-adjacent concepts or moving files, follow `AGENTS.md`:
read all source files fully, update references, and use `git rm` for tracked
deletions. Multi-file gate: [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md).

### Phase 1 — Discover And Read

1. Find candidate files with `rg` and `rg --files`.
2. Read every candidate source file in full before moving content.
3. For each concept, record:
   - Current definitions or descriptions
   - File and section where each appears
   - Citations, source links, source PDFs, figure references, and backlinks
   - Related aliases, abbreviations, and near-duplicate names
   - Whether the material is settled, speculative, generated, or historical
4. Trace references:
   - Markdown links and Obsidian wikilinks
   - LaTeX labels, refs, citations, and includes
   - README links from `research/` modules
   - Tooling or report references if documentation paths are consumed by code

Do not consolidate from generated files unless the generated file is the only
available copy or the user explicitly asks.

### Phase 2 — Decide Canonical Ownership

Pick one canonical home for each concept:

- Use `research/` for reusable domain concepts and literature synthesis.
- Use `research/modules/<module>/README.md` for the public overview of a research module.
- Use module-local documents for experiment-specific details.
- Use `research/howtos/` for process, workflow, or convention concepts.
- Use `proposal/` + `private-appendix/` + `latex-shared/` for final narrative integration, not as the only source of
  reusable background knowledge.

Keep material local when:

- It only applies to a single experiment, figure, or module.
- Moving it would obscure provenance or uncertainty.
- It is a historical report that should remain as an audit trail.
- The apparent duplicate actually has different scope, assumptions, or evidence.

### Phase 3 — Plan Changes

For non-trivial or multi-file changes, present a short plan before editing:

- Canonical target file and why it is the right owner
- Source files being merged from
- Concepts to move, merge, or leave local
- References and links that will be updated
- Verification commands to run

Explicit user confirmation is required before:

- Deleting tracked files
- Moving manuscript prose between chapters or sections
- Collapsing multiple notes into one note when citation provenance is ambiguous
- Making broad changes across more than five source files

For small local consolidations with an obvious target, proceed directly.

### Phase 4 — Execute

When editing:

1. Move or merge concept text into the canonical target.
2. Preserve citations, links, labels, figure references, and source provenance.
3. Prefer appending and integrating over rewriting from scratch.
4. If merging duplicate definitions, keep the strongest supported formulation
   and retain important caveats from all sources.
5. Replace duplicated source text with:
   - A concise pointer to the canonical file, or
   - A short local summary plus a link, when local context still matters.
6. Update all inbound links, backlinks, README references, LaTeX refs, and any
   tooling references affected by renamed or deleted files.
7. Use `git rm <file>` for tracked files that are removed.
8. Do not edit unrelated generated outputs unless the task requires regenerating
   them.

### Phase 5 — Verify

Always verify the kind of change made:

- Markdown-only note consolidation:
  - Run `rg` for old concept names, filenames, headings, and wikilinks.
  - Check links manually where path formats changed.
- Manuscript, tooling, or broad refactors: [`tools/README.md`](../../../../../../repos/phd-dissertation/tools/README.md)
  (build / local-ci as the change requires). Check that citations, labels, and
  refs still resolve.

If a verification command fails, fix the cause and rerun it. If failure is
unrelated to the consolidation, report it clearly with the failing command and
the relevant error.

### Pitfalls

- Do not flatten meaningful distinctions between concepts that only sound
  similar.
- Do not strip citations while deduplicating prose.
- Do not make generated reports the canonical home for living knowledge.
- Do not move manuscript claims into notes without preserving the manuscript's
  citation and argument context.
- Do not delete historical reports just because their conclusions were copied
  into a living note.
- Do not rename or remove files without updating all repo references.

## Report

Summarize canonical targets, merged sources, updated references, deleted files,
and verification commands with pass/fail results.
