# TEST_INFRA — E2E Test Infrastructure for phd-slavv uv Migration

## Overview

This document specifies the architecture, execution model, sandboxing, and quality gating framework for the End-to-End (E2E) Test Suite created for the `phd-slavv` `uv` build backend and workflow migration.

The E2E test suite adheres to a requirement-driven, opaque-box testing methodology across four rigorous tiers to guarantee that all functional, boundary, compositional, and real-world lifecycle requirements (R1–R4) are validated.

---

## 4-Tier Test Architecture

The test suite is implemented in `tests/e2e/test_uv_migration_e2e.py` and organized into 4 distinct verification tiers:

```
tests/e2e/
├── __init__.py
└── test_uv_migration_e2e.py
    ├── TestTier1Feature1BuildSystem          (R1: Hatchling build-backend, PEP 621 metadata)
    ├── TestTier1Feature2UvLock               (R1: uv.lock generation, schema, lock check)
    ├── TestTier1Feature3UvSyncExtras         (R2: 12 optional-dependency groups sync)
    ├── TestTier1Feature4DevTooling           (R3: CLI entrypoint, ruff, mypy, pytest via uv run)
    ├── TestTier1Feature5CIWorkflows          (R4: CI YAML schema validity & setup-uv)
    ├── TestTier2Boundary1GitAndLockfile      (B1: uv.lock untracked/ignored boundaries)
    ├── TestTier2Boundary2LockTampering       (B2: Lock drift detection on pyproject mutation)
    ├── TestTier2Boundary3ExtrasComposition   (B3: Unknown extra errors, multiple composition)
    ├── TestTier2Boundary4PipCompatibility    (B4: Pip editable dry-run, wheel packaging integrity)
    ├── TestTier2Boundary5DocsAndErrorResilience (B5: Docs command sanitization, failure handling)
    ├── TestTier3CrossFeatureCombinations     (T3: Pairwise sync+ruff, lock+build, sync+pytest, etc.)
    └── TestTier4RealWorldScenarios           (T4: Clean onboarding, CI emulation, release flow)
```

---

## Test Execution

### Prerequisites
- **Python**: `>= 3.11`
- **uv**: `>= 0.11.0` (installed on `PATH`)
- **Git**: Working tree initialized

### Canonical Test Runner Commands

Run the full E2E test suite with verbose output:
```bash
uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -v
```

Run specific tiers:
```bash
# Tier 1: Core Feature Verification
uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -k "TestTier1" -v

# Tier 2: Boundary & Corner Cases
uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -k "TestTier2" -v

# Tier 3: Pairwise Combinations
uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -k "TestTier3" -v

# Tier 4: Real-World Scenarios
uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -k "TestTier4" -v
```

---

## Sandboxing & Isolation Guarantees

To ensure that tests remain strictly isolated and do not mutate the developer's working directory or dirty the git state:

1. **Non-Destructive Extras Validation**:
   Tests asserting dependency resolution across individual or combined optional dependency groups (`app`, `ml`, `notebooks`, `dicom`, `sitk`, `cupy`, `zarr`, `napari`, `accel`, `workspace`, `tui`, `all`) execute `uv sync --dry-run` to verify resolution without altering `.venv`.

2. **Isolated Tamper Sandboxing**:
   Tests verifying `uv lock --check` behavior upon dependency drift copy `pyproject.toml` and `uv.lock` into an isolated `pytest` `tmp_path` fixture, mutate the configuration in the sandbox, and assert failure without touching the root configuration.

3. **Isolated Build Directory**:
   Tests asserting `uv build` packaging and wheel artifact inspection specify `--out-dir` pointing to `tmp_path` to avoid generating uncommitted artifacts in `dist/`.

4. **Cross-Device Cache Link Resilience**:
   Subprocess invocations run with `--link-mode=copy` or `UV_LINK_MODE=copy` compatibility where required to seamlessly operate across external drives (`/Volumes/LoveSSD`) and home caches.

---

## Milestone Verification Gating

| Milestone | Target Scope | E2E Gating Tests | Expected Status |
| :--- | :--- | :--- | :--- |
| **M1** | Build system, `uv.lock`, extras, dev tooling | `TestTier1Feature1-4`, `TestTier2Boundary1-4`, `TestTier3` (core), `TestTier4` (build/sync) | **PASS (100%)** |
| **M2** | Docs & scripts sanitization (`uv run`) | `TestTier2Boundary5DocsAndErrorResilience` | **PASS upon M2 completion** |
| **M3** | CI workflow migration (`setup-uv`, `uv sync`) | `TestTier1Feature5CIWorkflows`, `test_t3_pairwise_git_tracking_and_ci_setup_uv` | **PASS upon M3 completion** |
| **M4** | Final unified E2E sign-off | Full suite (`61` test methods) | **ALL GREEN (100%)** |
