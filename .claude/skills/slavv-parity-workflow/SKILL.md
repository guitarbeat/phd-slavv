---
name: slavv-parity-workflow
description: Inspect or run SLAVV MATLAB-to-Python parity checks with preflight, protected
  roots and evaluated spatial proof bars.
---


# Slavv Parity Workflow

Repository paths and commands are relative to the selected working repository. Read its AGENTS.md and the shared library guidance; load only the procedure that matches the task.

Use only in phd-slavv. Read `docs/reference/core/EXACT_PROOF_FINDINGS.md` and ADR 0011/0012 before choosing roots or reporting status. Check writer leases/PIDs, parameter fingerprints, input identity, memory and the current host's CLI. Keep float64 and Fortran [Y,X,Z] ordering. Follow the cheap ladder: unit/synthetic, crop, full non-writer re-selection, then a new writer only when needed. Never overwrite protected claim/oracle roots, including canonical_full_v18 and crop_M_exact_v3. Create a new destination for a requested computation; an old example with source=destination is not permission to rewrite a baseline. Inspect saved proof JSON with `slavv parity inspect-proof --path <report> --require-evaluated` or load_proof_record. Edges/network require evaluated ADR0012 spatial ownership/multiset bars and passed=true; raw edge-pair overlap is insufficient. Compare raw with raw and final with final. Report actual per-field failures and missing evidence without launching new computation merely to fill a report.
