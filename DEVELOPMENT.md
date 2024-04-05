# Development

This project uses the src layout (see [Python Packaging User Guide: src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)).

For that reason, in development you must use an "editable install": [Setup Tools: Development Mode (a.k.a. "Editable Installs")](https://setuptools.pypa.io/en/latest/userguide/development_mode.html).

TL;DR:

```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

```
pip uninstall import-proto
```