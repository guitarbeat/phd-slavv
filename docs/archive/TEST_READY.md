# TEST_READY — E2E Test Suite Readiness Declaration

## Status: READY FOR VERIFICATION & GATING

The End-to-End (E2E) Acceptance Test Suite for the `phd-slavv` uv migration has been authored and verified against the current repository state.

- **Test Suite Location**: `tests/e2e/test_uv_migration_e2e.py`
- **Framework**: `pytest`
- **Standard Test Command**:
  ```bash
  uv run --extra workspace --extra app pytest tests/e2e/test_uv_migration_e2e.py -v
  ```

---

## 4-Tier Test Coverage Checklist

### Tier 1: Feature Coverage (Requirement-Driven)

#### Feature 1: Build System & Backend Configuration (R1)
- [x] `test_t1_f1_build_backend_is_hatchling`: Pyproject specifies `hatchling.build` as build backend.
- [x] `test_t1_f1_requires_hatchling_in_build_system`: Pyproject specifies `hatchling>=1.24.0` in `build-system.requires`.
- [x] `test_t1_f1_pep621_metadata_fields`: All PEP 621 metadata fields (name, version, description, readme, requires-python) exist.
- [x] `test_t1_f1_pep621_dependencies_declared`: Runtime dependency list exists, non-empty, and includes core scientific stack.
- [x] `test_t1_f1_scripts_entrypoint_declared`: `[project.scripts]` declares `slavv = "slavv_python.interface.cli:main"`.

#### Feature 2: `uv.lock` Generation & Validation (R1)
- [x] `test_t1_f2_lockfile_exists`: `uv.lock` exists at repository root.
- [x] `test_t1_f2_lockfile_schema_version`: `uv.lock` contains valid `version = 1` or higher.
- [x] `test_t1_f2_lockfile_contains_slavv_package`: `uv.lock` registers `slavv_python` local project member.
- [x] `test_t1_f2_lockfile_contains_direct_dependencies`: `uv.lock` pins key direct dependencies (numpy, scipy, scikit-image, etc.).
- [x] `test_t1_f2_uv_lock_check_clean`: `uv lock --check` exits with code 0 on the clean tree.

#### Feature 3: `uv sync` with Optional Dependencies / Extras (R2)
- [x] `test_t1_f3_optional_dependencies_groups_count`: Exactly 12 optional dependency groups declared.
- [x] `test_t1_f3_optional_dependencies_expected_groups`: All 12 required groups (`app`, `ml`, `notebooks`, `dicom`, `sitk`, `cupy`, `zarr`, `napari`, `accel`, `workspace`, `tui`, `all`) exist.
- [x] `test_t1_f3_uv_sync_dry_run_app_extra`: `uv sync --dry-run --extra app` resolves successfully.
- [x] `test_t1_f3_uv_sync_dry_run_workspace_extra`: `uv sync --dry-run --extra workspace` resolves successfully.
- [x] `test_t1_f3_uv_sync_dry_run_all_extras`: `uv sync --dry-run --all-extras` resolves successfully.

#### Feature 4: Developer Workflow Tooling via `uv run` (R3)
- [x] `test_t1_f4_uv_run_cli_help`: `uv run slavv --help` executes and displays usage help.
- [x] `test_t1_f4_uv_run_cli_info`: `uv run slavv info` executes and prints system information.
- [x] `test_t1_f4_uv_run_ruff_check`: `uv run ruff check slavv_python` runs linter cleanly.
- [x] `test_t1_f4_uv_run_mypy_execution`: `uv run mypy --version` executes cleanly.
- [x] `test_t1_f4_uv_run_pytest_execution`: `uv run pytest --version` executes cleanly.

#### Feature 5: CI Workflow Validity & `setup-uv` Integration (R4)
- [x] `test_t1_f5_regression_gate_yaml_valid`: `.github/workflows/regression-gate.yml` is valid YAML.
- [x] `test_t1_f5_matlab_parity_yaml_valid`: `.github/workflows/matlab-random-component-parity.yml` is valid YAML.
- [ ] `test_t1_f5_ci_workflows_declare_setup_uv`: CI workflows specify `astral-sh/setup-uv@v5` *(Gated on M3)*.
- [ ] `test_t1_f5_ci_workflows_use_uv_sync`: CI workflows use `uv sync` for dependency installation *(Gated on M3)*.
- [ ] `test_t1_f5_ci_workflows_use_uv_run`: CI workflow steps execute tools via `uv run` *(Gated on M3)*.

---

### Tier 2: Boundary & Corner Cases

#### Boundary 1: Lockfile Gitignore & Git Tracking
- [x] `test_t2_b1_uv_lock_not_gitignored`: `git check-ignore -v uv.lock` returns non-zero (lockfile is tracked).
- [x] `test_t2_b1_gitignore_file_clean`: `.gitignore` does not ignore `uv.lock`.
- [x] `test_t2_b1_venv_is_gitignored`: `.venv/` is correctly ignored by git.
- [x] `test_t2_b1_dist_is_gitignored`: `dist/` build output directory is ignored by git.
- [x] `test_t2_b1_egg_info_is_gitignored`: Legacy `.egg-info` directories are ignored by git.

#### Boundary 2: Lock Drift Detection & Tampering
- [x] `test_t2_b2_uv_lock_drift_detection_on_dependency_mutation`: Mutating pyproject dependencies causes `uv lock --check` to fail.
- [x] `test_t2_b2_uv_lock_drift_detection_on_extra_mutation`: Mutating optional dependency groups causes `uv lock --check` to fail.
- [x] `test_t2_b2_uv_lock_tamper_detection_on_lock_edit`: Directly modifying `uv.lock` causes `uv lock --check` to fail.
- [x] `test_t2_b2_uv_lock_reproducibility`: Re-running `uv lock` in temporary directory produces consistent lock content.
- [x] `test_t2_b2_empty_input_protection`: Invalid empty pyproject fails fast with helpful error.

#### Boundary 3: Extras Composition & Unknown Extra Handling
- [x] `test_t2_b3_unknown_extra_fails_gracefully`: `uv sync --extra nonexistent_extra_xyz` fails non-zero.
- [x] `test_t2_b3_pairwise_extras_sync`: Combining multiple extras (`--extra ml --extra notebooks`) resolves cleanly.
- [x] `test_t2_b3_scientific_extras_sync`: Combining scientific extras (`--extra dicom --extra sitk --extra zarr`) resolves cleanly.
- [x] `test_t2_b3_ui_and_dev_extras_sync`: Combining UI and development extras (`--extra app --extra workspace --extra tui`) resolves cleanly.
- [x] `test_t2_b3_all_extra_matches_individual_superset`: `all` extra superset dependency membership matches all individual modules.

#### Boundary 4: Pip Compatibility & Wheel Artifact Packaging
- [x] `test_t2_b4_pip_editable_install_dry_run`: `pip install -e . --dry-run` validates PEP 517/518 build compatibility.
- [x] `test_t2_b4_uv_build_generates_sdist_and_wheel`: `uv build` builds both `.tar.gz` and `.whl` artifacts.
- [x] `test_t2_b4_wheel_contains_package_json_overrides`: Wheel archive contains `matlab_linspace_overrides.json`.
- [x] `test_t2_b4_wheel_contains_matlab_random_reference_json`: Wheel archive contains `matlab_random_linspace_reference.json`.
- [x] `test_t2_b4_wheel_metadata_pep621_fields`: Built wheel METADATA matches pyproject PEP 621 fields.

#### Boundary 5: Docs & Error Resilience
- [ ] `test_t2_b5_readme_no_bare_pip_install_setup`: `README.md` free of bare `pip install -e .` commands *(Gated on M2)*.
- [ ] `test_t2_b5_agents_md_uses_uv_commands`: `AGENTS.md` commands use `uv run` / `uv sync` *(Gated on M2)*.
- [ ] `test_t2_b5_scripts_readme_uses_uv_run`: `scripts/README.md` uses `uv run python` *(Gated on M2)*.
- [x] `test_t2_b5_streamlit_launcher_unit_test_passes`: Interface launcher tests pass under `uv run --extra workspace --extra app pytest`.
- [x] `test_t2_b5_uv_run_invalid_command_fails_gracefully`: Running non-existent commands through `uv run` fails cleanly.

---

### Tier 3: Cross-Feature Combinations (Pairwise Interactions)
- [x] `test_t3_pairwise_sync_workspace_and_ruff_check`: `uv sync --extra workspace` + `uv run ruff check`.
- [x] `test_t3_pairwise_lock_check_and_build`: `uv lock --check` + `uv build`.
- [x] `test_t3_pairwise_sync_workspace_and_pytest`: `uv sync --extra workspace --extra app` + `uv run pytest`.
- [x] `test_t3_pairwise_sync_ci_extras_and_ci_gate_sequence`: `uv sync (app,workspace,zarr)` + `ruff check` + `mypy`.
- [x] `test_t3_pairwise_sync_all_extras_and_cli_entrypoints`: `uv sync --all-extras` + `slavv info` + `slavv --help`.
- [ ] `test_t3_pairwise_git_tracking_and_ci_setup_uv`: `uv.lock` git tracking + CI `setup-uv` workflow config *(Gated on M3)*.

---

### Tier 4: Real-World Application Scenarios (End-to-End Journeys)
- [x] `test_t4_journey_clean_developer_onboarding`: End-to-end clone -> verify lock -> sync -> CLI -> ruff -> fast unit test.
- [x] `test_t4_journey_ci_regression_pipeline_emulation`: Full CI pipeline simulation (workflow YAML -> sync extras -> ruff -> mypy -> pytest).
- [x] `test_t4_journey_release_packaging_distribution`: Full release package build and sdist + wheel inspection in temporary directory.
- [x] `test_t4_journey_lock_sync_all_extras_lifecycle`: Full lifecycle lock generation -> check -> sync --all-extras dry-run -> verify.
- [x] `test_t4_journey_developer_scripts_execution`: Developer probe scripts verify CLI info and tool versions.

---

## Baseline Verification Summary

- **Total Test Cases**: 61
- **Current Milestone (M1) Passing**: 54 / 54 (100%)
- **Pending Milestones (M2 & M3)**: 7 tests (Accurately gating on Docs and CI edits)
