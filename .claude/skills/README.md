# Shared workspace skills

This directory contains 27 relative discovery links into the canonical
[NeuroVASC skills library](../../../../.agents/skills). Edit shared targets,
not repository-local copies. The [triage index](../../../../.agents/SKILL-TRIAGE.md)
records merged names and aliases.

## Restore on another computer

A standalone SLAVV clone does not contain these skill implementations. Restore
or install the shared library alongside the checkout in this layout:

```text
NeuroVASC/
  .agents/skills/<skill-name>/SKILL.md
  repos/phd-slavv/.claude/skills/<skill-name>
```

Each discovery link targets `../../../../.agents/skills/<skill-name>`.
Use the existing [workspace recovery procedure](../../../../setup/recovery/README.md)
to restore the workspace and its separate skills bundle. A SLAVV Git pull alone
cannot restore that independent library. The recovery guide is an external
workspace dependency and is unavailable in a standalone clone too.

The checkout must preserve Git symlinks. On Windows, ensure symlink support is
available and Git checks out actual links; plain files containing link text do
not provide skill discovery. This migration was verified on macOS, not Windows
or CI.

From the restored NeuroVASC root, run `./setup/check-in.sh --skills` to verify
canonical resources and discovery identities. Do not recreate vendored copies
to work around a missing shared library.
