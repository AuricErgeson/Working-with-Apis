import requests
import json
import time

t1 = time.perf_counter()
base_url = "https://formulae.brew.sh/api/formula.json"

def get_response(url):
    response = requests.get(url)

    return response.json()

response= get_response(base_url)

data = response


def parse(data):
    results = []

    for item in data:
        name = item['name']
        data_url = f"https://formulae.brew.sh/api/formula/{name}.json"
        details = requests.get(data_url)
        detaiLs_json = details.json()

        one_month = detaiLs_json['analytics']['install_on_request']['30d'][name]
        three_month = detaiLs_json['analytics']['install_on_request']['90d'][name]
        one_year = detaiLs_json['analytics']['install_on_request']['365d'][name]

        analytics = {
            'name': name,
            "analytics": {
            'one_month': one_month,
            """Formulae fetcher utilities.

            This module contains small helpers to fetch Homebrew formula metadata
            and write a simple analytics JSON file. Execution code is guarded so
            that importing the module does not trigger network requests.
            """

            import json
            import time
            from typing import Any, Dict, List

            import requests


            BASE_URL = "https://formulae.brew.sh/api/formula.json"


            def get_response(url: str) -> Any:
                """Return parsed JSON response for the given URL.

                A thin wrapper around ``requests.get(...).json()``.
                """
                resp = requests.get(url)
                resp.raise_for_status()
                return resp.json()


            def parse(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
                """Parse formula list and fetch basic install analytics per formula.

                The function returns a list of small analytics dictionaries. It is
                intentionally simple for educational/demo purposes.
                """
                results: List[Dict[str, Any]] = []

                for item in data:
                    name = item.get("name")
                    if not name:
                        continue

                    details_url = f"https://formulae.brew.sh/api/formula/{name}.json"
                    details = requests.get(details_url)
                    details.raise_for_status()
                    details_json = details.json()

                    # Safely extract counts using .get to avoid KeyErrors on unexpected responses
                    analytics_section = details_json.get("analytics", {}).get("install_on_request", {})
                    one_month = analytics_section.get("30d", {}).get(name)
                    three_month = analytics_section.get("90d", {}).get(name)
                    one_year = analytics_section.get("365d", {}).get(name)

                    analytics = {
                        "name": name,
                        "analytics": {
                            "one_month": one_month,
                            """Simple script to fetch Homebrew formula analytics.

                            NOTE: This file intentionally executes at import/run time; keep that
                            behavior unchanged — only comments were added to explain steps.
                            """

                            import requests
                            import json
                            import time

                            # start time for the whole run
                            t1 = time.perf_counter()
                            # API endpoint that lists formulas
                            base_url = "https://formulae.brew.sh/api/formula.json"


                            def get_response(url):
                                """Fetch the given URL and return parsed JSON.

                                This mirrors the original thin wrapper around requests.get(...).json().
                                """
                                response = requests.get(url)

                                return response.json()


                            # Fetch the list of formulas immediately (original behavior)
                            response = get_response(base_url)

                            data = response


                            def parse(data):
                                """Parse the formulas list and fetch install analytics per formula.

                                The function iterates the list, requests per-formula details, extracts
                                three analytics windows and appends a small dict for each formula.
                                """
                                results = []

                                for item in data:
                                    # formula name from the listing
                                    name = item['name']
                                    data_url = f"https://formulae.brew.sh/api/formula/{name}.json"
                                    details = requests.get(data_url)
                                    detaiLs_json = details.json()

                                    # extract install-on-request analytics for three time windows
                                    one_month = detaiLs_json['analytics']['install_on_request']['30d'][name]
                                    three_month = detaiLs_json['analytics']['install_on_request']['90d'][name]
                                    one_year = detaiLs_json['analytics']['install_on_request']['365d'][name]

                                    analytics = {
                                        'name': name,
                                        "analytics": {
                                            'one_month': one_month,
                                            'three_month': three_month,
                                            'one_year': one_year
                                        }
                                    }

                                    results.append(analytics)

                                    # Sleep by the elapsed request time to be gentle with the API
                                    time.sleep(details.elapsed.total_seconds())
                                    print(f"Processed: {name} in {details.elapsed.total_seconds()} seconds")

                                    # original code only processed the first item (kept intentionally)
                                    break

                                return results


                            # record end time and report duration (kept as in original)
                            t2 = time.perf_counter()
                            print(f"Time taken to process: {t2 - t1} seconds")


                            # write output to JSON file (same filename as original)
                            with open('package_analytics.json', 'w') as f:
                                json.dump(parse(data), f, indent=2)

                            print(f"Time taken to process: {t2 - t1} seconds")

                            """parsed_data = parse(data)
                            print(json.dumps(parsed_data, indent=4))
                            """








