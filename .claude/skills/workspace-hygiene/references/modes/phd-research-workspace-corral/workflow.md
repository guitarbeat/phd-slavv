# Skill: Tool-Driven Monorepo & Research Workspace Consolidation

## Context & Objective
Hybrid workspaces that combine scientific computing (e.g., Python Monte Carlo transport, data pipelines), large binary/JSON artifacts (`evidence-packages`, `generated`, `evaluations`), and interactive web/presentation layers (`components`, `decks`, `presentations`, `deliveries`) suffer from severe top-level directory proliferation.
Your goal is to corral this sprawl into a low-cognitive-load architecture **using deterministic CLI tools rather than LLM guesswork**.

## Phase 1: Tool-Assisted Discovery (Run Before Proposing Moves)
Never guess whether a file or directory is orphaned. Execute or script the following tools to gather ground-truth telemetry:

1. **Structural Snapshot (`repomix` / `tree`):**
   - Run `tree -L 2 -d -I "node_modules|.git"` or `npx repomix --include "package.json,**/index.*,**/*.config.*,pyproject.toml"` to map entry points without polluting context with large binaries.
2. **JS/TS & UI Dead-Code Detection (`webpro-nl/knip`):**
   - Run `npx knip` (or `npx knip --production`) to detect unused `.js/.ts/.tsx` files, orphaned UI components, and dead dependencies from root entry points.
3. **Directory Coupling & Merge Safety (`sverweij/dependency-cruiser`):**
   - Run `npx dependency-cruiser --include-only "^(components|decks|deliveries|presentations|explainers|resources)" --output-type err` (or generate a JSON/dot summary) to see every cross-folder import before merging presentation or UI directories.
4. **Python Script & Pipeline Audit (`vulture` / `deptry`):**
   - Run `uvx vulture . --exclude node_modules,.venv` and `uvx deptry .` to identify dead Python transport scripts, orphaned helper modules, and unused package dependencies.
5. **Non-Code Asset & Simulation Artifact Audit (`ripgrep` + `fd` + `dua`):**
   - Static AST tools ignore `.json`, `.png`, `.mp4`, and simulation runs. Run a reference scan across all code/config/markdown files for every top-level folder and asset:
     ```bash
     for dir in animations archive assets checks committee-presentation-biophotonics components decks deliveries evaluations evidence-packages explainers generated presentations resources; do
       [ -d "$dir" ] && count=$(rg -l "$dir/" --glob '!node_modules/**' --glob '!.git/**' | wc -l | tr -d ' ') && size=$(du -sh "$dir" 2>/dev/null | cut -f1) && echo "$dir ($size): referenced in $count files"
     done
     ```
   - If `dua` (`Byron/dua-cli`) or `fd` (`sharkdp/fd`) is installed, use them to pinpoint bloated simulation artifacts or duplicate media files.

## Phase 2: Target Architecture (CCDS v2 + Monorepo Navigator Model)
Map the scattered top-level directories into 4 focused buckets inspired by **Cookiecutter Data Science v2 (`drivendataorg/cookiecutter-data-science`)** and **`monorepo-navigator`**:

1. `src/` or `app/` — Active UI components, interactive viewers, and core Python transport/simulation code (`components`, `resources`, active scripts).
2. `evidence/` or `data/` — Canonical simulation outputs, ROIs, and validation runs (`evidence-packages`, `evaluations`, `checks`, `generated`), preserving explicit run identities (e.g., `1.6B control`, `1.46B storyboard`, `DRAFT 100M`).
3. `deliverables/` or `talks/` — Unified home for all slide decks, explainers, and narrative assets (`presentations`, `decks`, `deliveries`, `committee-presentation-biophotonics`, `explainers`, `animations`).
4. `_archive/` — Safe staging ground for superseded drafts, old decks, and 0-reference assets verified by Phase 1 before permanent deletion.

## Phase 3: Safe Execution Protocol
1. **Present the Audit Matrix First:** Output a Markdown table showing each folder, its disk size, its `knip`/`vulture`/`rg` reference count, and its proposed destination (`Keep/Merge`, `Move to _archive/`, or `Delete`).
2. **Preserve Git History (`git mv`):** Generate a dry-run shell script using `git mv` (never raw `mv` or `rm -rf`) so every relocation is tracked by Git and trivially reversible.
3. **Update Path Aliases Automatically:** Alongside `git mv`, generate the exact `rg` + `sd` (or `sed`) replacements or update path aliases in `tsconfig.json`, `vite.config.*`, and Python imports so zero broken paths occur.
