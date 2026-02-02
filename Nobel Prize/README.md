# Nobel Prize

Scripts that fetch Nobel Prize data and export a small CSV for analysis.

Files:
- `api_request.py` — queries the public Nobel Prize API and writes `nobel_prizes.csv`.

How to run:

```powershell
python "Nobel Prize/api_request.py"
```

Notes:
- The script pages through the API using the metadata `count`/`limit` values.
- Import the module to reuse helpers; running the file executes the exporter.
