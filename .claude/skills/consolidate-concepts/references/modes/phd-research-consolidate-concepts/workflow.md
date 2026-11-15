# Consolidate Concepts

Fold scattered, duplicated, or drifted definitions of a domain concept into the **one** doc that owns it, then repoint or delete the copies. This is the STP-native version: there is no `.plain`/`template/` module system and no glossary here — concepts live in canonical operating docs, and the old `applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/glossary.md` was deliberately deleted and absorbed into primers. The authority for *where* any concept belongs is [`applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/planning-map.md`](../../../../../../repos/phd-research/applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/planning-map.md) (Source-of-Truth Order, Ownership Map, Promotion Rules). **Read it first.**

## When to Use

- The same term (e.g. "spatial-tile split", "keeper", "held-out spatial correlation", `MaskedDepth3DStem`, "aligned pair") is defined independently in more than one doc.
- Definitions **conflict or have drifted** — one doc describes the current method, another the superseded one (the honesty-relevant case; see the selected repository AGENTS.md evidence rules).
- A canonical fact is stranded in a lower-priority file (dated snapshot, `.agents/specs/`, manuscript draft) and should be **promoted** to its owner.
- A doc split/merge left shared definitions duplicated or awkwardly cross-referenced.

## Guiding Principle

This is an **editorial refactor, not a claim change**. The scientific meaning and facts must remain **identical** — you deduplicate and relocate definitions; you never sharpen a hedged claim, invent a number, or change a result while moving text. Honesty-first per [AGENTS.md](../../../../../../repos/phd-research/.agents/AGENTS.md) / `CLAUDE.md`. Per the planning-map Conflict Checklist: **prefer deletion over footnotes** — a stale definition that still sounds current is more dangerous than a deleted one.

## Input

The concept(s) to consolidate, plus optionally the intended canonical owner. If not specified, ask — or scan for drift by grepping the term (and its `aliases:`) across `research/`, `documentation/`, `.agents/`, and Python docstrings.

## Phase 1 — Locate every definition and usage

1. **Grep the term and its aliases** across markdown and code. Check doc frontmatter `aliases:` lists too — the same concept often hides under a synonym.
2. **Build an inventory.** For each hit record: the file, whether it is a *definition* (authoritative wording) or a *passing reference*, whether the file is canonical or a copy (use the planning-map Ownership Map), and the frontmatter `status`/`canonical` flag.
3. **Flag conflicts.** Note any location whose wording is drifted or describes a superseded method — these are the ones that must be repointed or deleted, not just linked.

## Phase 2 — Choose the canonical owner and plan

Pick the **one** owner using the planning-map Source-of-Truth Order and Ownership Map, e.g.:

- scientific stance / claim boundaries / dataset facts -> `applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/operator-playbook.md`
- what a model inputs/outputs, what exists -> `applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/model-inventory.md`
- a term explainer / definition -> the relevant primer (e.g. `applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/self-supervised-learning-encoder.md`)
- current sprint intent -> `applications/vascular-structure/vascular-structure-speckle-modeling/research/goals.md`; execution order -> `applications/vascular-structure/vascular-structure-speckle-modeling/research/operator-docs/roadmap.md`; a hard-to-reverse decision -> `documentation/decisions/`

Then present the plan and get explicit confirmation:

- the canonical owner (and why, per the Ownership Map),
- for each other location: replace-with-link vs delete,
- confirmation that **no scientific fact, claim, or hedge changes**,
- the promotion (if a fact is moving up the source-of-truth order).

Do not create a new glossary file — this repo puts concepts in their canonical owner, not a separate drawer.

## Phase 3 — Execute

1. **Make the owner definitive.** Ensure the concept's definition in the owner doc is complete and correct; merge in the best wording from the copies, keeping every hedge and scope label.
2. **Repoint or delete the copies.** Replace each scattered definition with a short reference and a markdown link to the owner, or delete it outright when redundant (prefer deletion).
3. **Leave surrounding content alone** — functional prose, results, and claims around a moved definition stay byte-for-byte unless they were the drift being fixed.
4. **Touch at most three places** beyond the owner (planning-map Maintenance Loop): the owner doc, one index if discoverability changed, one dated journal note if the concept was clarified by a run. If a fourth file seems necessary, stop and reconsider.

## Phase 4 — Verify

- `python -m two_photon_to_speckle documentation check` -> **0 issues** (no broken links introduced by the repoint/delete).
- `python -m two_photon_to_speckle documentation index` if discoverability changed.
- **Re-grep the term:** exactly one canonical definition remains; every other hit is a link/reference or gone.
- **No behavioral/claim change:** diff the moved text — meaning identical, hedges and scope labels intact, no invented numbers.
- Optional: `python -m two_photon_to_speckle workflow check --workspace-hygiene` stays clean.
- Read every modified file in full and present the diff for approval.

## Common Pitfalls

- **Consolidating a purely-local term.** If a concept is only used in one doc, moving it adds coupling for no gain — leave it local.
- **Leaving a drifted copy live.** The whole point is the conflicting/superseded definition; link-or-delete it, don't just add a second canonical source.
- **Inventing a glossary.** This repo removed `glossary.md` on purpose — put the concept in its canonical owner.
- **Promoting an unbacked claim.** Promote a fact only when backed by code, a manifest, a run summary, or a deliberate human decision (planning-map Promotion Rules).
- **Footnoting instead of deleting.** Prefer deleting a stale sentence over explaining it.
- **Breaking links.** Always run `documentation check` after repointing.

## Validation Checklist

- [ ] Read `planning-map.md`; canonical owner chosen via Source-of-Truth Order / Ownership Map
- [ ] User confirmed the plan before edits
- [ ] Exactly one definition of the concept remains, in the owner doc
- [ ] All other occurrences are links/references or deleted (prefer deletion)
- [ ] No scientific fact, claim, or hedge was altered; no numbers invented
- [ ] `documentation check` reports 0 issues; index refreshed if discoverability changed
- [ ] At most three files touched beyond the owner (Maintenance Loop)
- [ ] Every modified file read in full and approved by the user
