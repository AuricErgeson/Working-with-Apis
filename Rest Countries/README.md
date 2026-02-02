# Rest Countries

Examples showing how to fetch country metadata from the Rest Countries API
and export the results as JSON.

Files:
- `countries_request.py` — fetches names, requests details per-country, and writes `countries_data.json`.

How to run:

```powershell
python "Rest Countries/countries_request.py"
```

Notes:
- The original file name had a space; this copy uses snake_case to improve importability.
- Consider adding caching or limiting requests to avoid long runtime.
