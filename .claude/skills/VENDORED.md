# Vendored skills

These 27 skill directories under `.claude/skills/` are **real copies** of the
shared NeuroVASC agent-skills library, vendored into this repository so a fresh
clone (or CI, or another machine) has them without needing the external library
restored alongside the checkout. They previously existed as relative symlinks
into `../../../../.agents/skills/`, which dangle on any clone that is not two
levels under that shared tree.

- **Source path:** `/Volumes/LoveSSD/NeuroVASC/.agents/skills/<name>/`
- **Vendored on:** 2026-11-15
- **Copy rules:** `rsync -rL` (nested symlinks dereferenced to real files; no
  symlinks remain inside). Excluded: `__pycache__/`, `*.pyc`, `.DS_Store`,
  `.pytest_cache/`, `.git/`. No files larger than 5 MB and no secret-looking
  files (`.env`, keys, tokens) were present or copied.

## Vendored skills (27)

1. addressing-pr-review-comments
2. check-compiler-errors
3. consolidate-concepts
4. control-cli
5. control-ui
6. deslop
7. diagnosing-bugs
8. finalizing-pr
9. find-skills
10. fix-ci
11. grilling
12. improve-codebase-architecture
13. make-interfaces-feel-better
14. make-pr-easy-to-review
15. matlab-performance-optimizer
16. pr-review-canvas
17. resolving-merge-conflicts
18. run-smoke-tests
19. self-improving-agent
20. slavv-parity-workflow
21. solution-note-generator
22. thermo-nuclear-code-quality-review
23. translation-paper-author
24. verify-this
25. work-summary
26. workflow-from-chats
27. workspace-hygiene

## Re-sync from the shared library

When the shared library changes, refresh one skill (dereferencing any nested
symlinks, removing files deleted upstream):

```bash
rsync -rL --delete \
  --exclude='__pycache__/' --exclude='*.pyc' --exclude='.DS_Store' \
  --exclude='.pytest_cache/' --exclude='.git/' \
  /Volumes/LoveSSD/NeuroVASC/.agents/skills/<name>/ .claude/skills/<name>/
```

Replace `<name>` with the skill directory. Repeat per skill, or loop over the
list above.
