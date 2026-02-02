# Working-with-APIs

![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

A small collection of example scripts that demonstrate fetching, parsing, and saving data from public APIs. The repository contains short, focused Python scripts that retrieve data from the Formulae (Homebrew), Nobel Prize, and Rest Countries APIs and store results as JSON or CSV files.

What this repository provides
- Small, focused scripts that fetch data from public APIs and export it for analysis.
- Each major folder now includes a `README.md` that explains the purpose and how to run the scripts inside it.

Prerequisites
- Python 3.11 or newer recommended.
- Install runtime dependencies from `requirements.txt`.

Setup (example, PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Usage examples

- Run the Formulae data fetcher:

```powershell
python "Formulae/core.py"
```

Outputs: `package_analytics.json` in the `Formulae/` folder.

- Run the Nobel Prize data exporter:

```powershell
python "Nobel Prize/api_request.py"
```

Outputs: `nobel_prizes.csv` in the `Nobel Prize/` folder.

- Run the Rest Countries script:

```powershell
python "Rest Countries/countries_request.py"
```

Outputs: `countries_data.json` in the `Rest Countries/` folder.

Project structure (high level)
- `Formulae/` — `core.py`, `get.py`, `package_analytics.json`, see folder README
- `Nobel Prize/` — `api_request.py`, `nobel_prizes.csv`, see folder README
- `Rest Countries/` — `countries_request.py`, `countries_data.json`, see folder README
- `requirements.txt` — Python dependencies
- `LICENSE` — repository license

Where to get help
- Open an issue on the repository for bugs or feature requests.

Maintainers & Contributing
- Maintainer: project owner (see repository settings).

Notes & recommendations
- Scripts are intentionally small and educational — feel free to refactor into reusable modules or add CLI options.
- Avoid running all scripts repeatedly without accounting for API rate limits.

License
- See `LICENSE` for license details.
