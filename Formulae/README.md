# Formulae

This folder contains example scripts that fetch metadata and simple analytics
for Homebrew formulae (https://formulae.brew.sh).

Files:
- `core.py` — fetches formula list and writes `package_analytics.json`. Contains helpers and a script entry point.
- `get.py` — small helper to fetch and inspect a single package's analytics.

How to run:

```powershell
python "Formulae/core.py"
```

Notes:
- Scripts are educational and may hit rate limits; be polite to the API.
- Prefer importing functions for unit testing instead of running scripts directly.
