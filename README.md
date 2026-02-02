# Working-with-APIs

![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

A small collection of example scripts that demonstrate fetching, parsing, and saving data from public APIs. The repository contains short, focused Python scripts that retrieve data from the Formulae (Homebrew), Nobel Prize, and Rest Countries APIs and store results as JSON or CSV files.

**What this project does**
- Fetches and parses data from multiple public APIs.
- Produces simple data exports (JSON / CSV) for analysis or further processing.

**Key features**
- `Formulae/` — scripts to download Homebrew formulae metadata and analytics (outputs `package_analytics.json`).
- `Nobel Prize/` — script to fetch Nobel Prize records and export `nobel_prizes.csv`.
- `Rest Countries/` — script to fetch country details and export `countries_data.json`.

**Prerequisites**
- Python 3.11 or newer recommended.
- Install runtime dependencies from `requirements.txt`.

**Setup**
1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or Command Prompt
.\.venv\Scripts\activate.bat
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Usage examples**

- Run the Formulae data fetcher:

```bash
python "Formulae/get.py"
# or
python "Formulae/core.py"
```

Outputs: `package_analytics.json` (in the `Formulae/` directory or repository root depending on current working directory).

- Run the Nobel Prize data exporter:

```bash
python "Nobel Prize/apirequest.py"
```

Outputs: `nobel_prizes.csv` in the `Nobel Prize/` folder.

- Run the Rest Countries script:

```bash
python "Rest Countries/countries request.py"
```

Outputs: `countries_data.json` in the `Rest Countries/` folder.

**Project structure (high level)**
- `Formulae/` — `core.py`, `get.py`, `package_analytics.json`
- `Nobel Prize/` — `apirequest.py`, `nobel_prizes.csv`
- `Rest Countries/` — `countries request.py`, `countries_data.json`
- `requirements.txt` — Python dependencies
- `LICENSE` — repository license

**Where to get help**
- Open an issue on the repository for bugs or feature requests.
- For general questions, add an issue titled "Support / Question" and include reproduction steps and environment details.

**Maintainers & Contributing**
- Maintainer: project owner (see repository settings).
- For contribution guidelines, add a `CONTRIBUTING.md` file; for now, open issues or fork and submit pull requests. Keep changes small and include tests or usage notes where applicable.

**Notes & recommendations**
- Scripts are intentionally small and educational — feel free to refactor into reusable modules or add CLI options.
- Avoid running all scripts repeatedly without accounting for API rate limits.

**License**
- See `LICENSE` for license details.
