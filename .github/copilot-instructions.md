<!-- .github/copilot-instructions.md for the common-sense repo -->
# Guidance for AI coding agents

This project is a small utility library of playful "common sense" helpers in Python. The goal of these instructions is to get an AI coding agent productive quickly by describing the repo layout, conventions, test/build workflows, and project-specific patterns we follow.

- Package root: `common_sense/` — all public helpers are re-exported from `common_sense/__init__.py` using star-imports from module files (e.g. `dates.py`, `debug.py`, `strings.py`, `numbers.py`, `life.py`, `utils.py`). Keep exports stable: prefer adding functions to the module where the concept belongs, and avoid changing the public API names.

- Quick checks and developer workflows
  - Install editable dev deps: the project uses a simple setuptools setup. From the repository root run:

    ```powershell
    pip install -e .
    pip install -r requirements.txt
    ```

  - Run tests with pytest from the repo root:

    ```powershell
    pytest
    ```

  - Packaging uses `setup.py` / `pyproject.toml` (setuptools backend). `setup.py` reads `requirements.txt` and allows local editable installs (`-e .` is expected to be removed by `setup.py` parsing).

- Project-specific patterns and conventions (use these when editing or adding code)
  - Module organization: small, single-file modules grouped by concern (dates, debug, strings, numbers, life, utils). Add new utilities to the most relevant existing module rather than creating many small files.
  - Public API surface: `common_sense/__init__.py` imports * from the main modules — maintain stable names there. Avoid importing heavy third-party packages at top-level to keep import-time cost low.
  - Tests live at project root (top-level `tests/` in this workspace). Tests are simple pytest functions. Follow existing docstring-style examples used across modules (many functions include small doctest-like examples).
  - Minimal side-effects: modules should avoid network calls or runtime I/O during import. Use helper functions (e.g. `safe_import` in `devtools.py`) when conditionally importing optional dependencies.

- Notable implementation examples to reference
  - `common_sense/dates.py` — dozens of small, pure functions (e.g. `is_weekend`, `days_until`, `next_weekday`) that operate on `datetime.date` and `datetime.timedelta`. Prefer clear docstrings and small, testable logic.
  - `common_sense/debug.py` — predicate and introspection helpers (e.g. `is_iterable`, `is_module`, `explain_type`) that return simple primitives; follow the same naming conventions and behavior (no side effects).
  - `common_sense/devtools.py` — contains `timeit`, `bench`, `retry`, and `safe_import`. These utilities show how the project expects small, synchronous helpers to behave; follow similar signatures when adding utilities.

- External dependencies and integration points
  - `requests` and `urllib3` are listed in `requirements.txt` but are not used at import time across core modules — treat them as optional runtime deps for functions that may need network access (search for `net.py` to see usage patterns).
  - The package is small and self-contained; there are no complex service boundaries or microservices.

- How to modify the public API safely
  - Add new function(s) to the most relevant module (for example, date-related helpers in `dates.py`).
  - Add unit tests under `tests/` covering the new behavior and edge cases.
  - Keep top-level import names stable; if you must rename or remove an exported name, add a deprecation wrapper to preserve compatibility for one minor release.

- Testing and quality checks
  - Tests run with `pytest`. Modules include doctest-like examples in docstrings — consider adding matching pytest cases.
  - Keep functions small and pure where possible to simplify testing.

- Safe changes and anti-patterns to avoid
  - Avoid heavy computation or long-running loops at import time.
  - Avoid adding new runtime dependencies unless necessary — prefer `safe_import` for optional features.
  - Do not change `setup.py` behavior that strips `-e .` from `requirements.txt` without verifying install behavior.

If any of the above is unclear or you'd like me to include examples for adding a specific new helper, tell me which area to expand and I will iterate.  