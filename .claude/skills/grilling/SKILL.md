---
name: grilling
description: Run an explicitly requested design interview or grill-with-docs session,
  recording agreed terminology in the repository’s canonical owners.
---


# Grilling

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Use for an explicitly requested design interview or stress test. Investigate discoverable facts yourself; ask the user about decisions. Walk dependencies one at a time, with a recommended answer and concise lettered options, and wait for the answer before dependent choices. A request to consolidate skills is not an invitation to grill the user. In documentation mode, record agreed terms in the repository's existing canonical glossary and qualifying decisions in its ADR home. In phd-dissertation use CONTEXT.md and research/howtos/decisions/; elsewhere inspect the repository's current glossary/ADR owners. Do not overwrite AGENTS.md merely because an upstream example uses it as a glossary. Distinguish resolved decisions from open questions; implement only within the user's requested scope.

Use the [term template](CONTEXT-FORMAT.md) and [ADR template](ADR-FORMAT.md) only when compatible with the selected repository’s existing document owners and formats.
