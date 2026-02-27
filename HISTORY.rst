=======
History
=======

0.6.0 (2026-02-27)
------------------

* Migrated from setup.py to pyproject.toml (setuptools backend)
* Minimum Python version now 3.10
* Added numpy and cycler as explicit dependencies
* Fixed 9+ bugs across palette.py, colorclass.py, decors.py, plutils.py, colors.py
* Refactored Color_utils class to module-level functions in cutils.py
* Made Color.__repr__ pure (no side effects); added Color.display() for terminal output
* Color.__mul__ no longer mutates the original; returns a new Color
* Renamed ``type`` parameter to ``palette_type`` to avoid shadowing builtin
* Added type hints throughout the codebase
* Added comprehensive test suite (pytest)
* Added GitHub Actions CI (Python 3.10–3.13)
* Replaced flake8 with ruff for linting
* Added 4 colorblind-friendly palettes: Okabe–Ito, Tableau 10, Tol Bright, Tol Muted
* Colorblind palettes importable as plain dicts (``from pychromatic import okabe_ito``)
* Default branch renamed from master to main
* Updated README with features, palette table, colorblind palette docs
* Expanded usage docs with full examples for every major feature
* Updated all GitHub URLs from srmnitc to pyscal org

0.5.15 (2021-xx-xx)
-------------------

* Last release before modernization

0.1.0 (2019-09-17)
------------------

* First release on PyPI.
