"""Small helpers for fetching formula metadata and inspecting analytics.

This file preserves the original, top-level execution behavior: it fetches
the formula list immediately and then retrieves analytics for the first
package. Only comments and docstrings were added — no functional changes.
"""

import requests
import json

# Homebrew formulae listing endpoint
base_url = "https://formulae.brew.sh/api/formula.json"


def get_response(url):
    """Return parsed JSON response for the given URL."""
    response = requests.get(url)
    return response.json()


# Fetch the full listing immediately (original behavior)
data = get_response(base_url)


def parse_data(data):
    """Convert the raw formula listing into a compact list of records."""
    all_records = []
    for item in data:
        parsed_record = {
            'name': item.get('name'),
            'desc': item.get('desc'),
            'homepage': item.get('homepage'),
            'version': item.get('versions', {}).get('stable'),
            'urls': item.get('urls', {}).get('stable', {}).get('url')
        }
        all_records.append(parsed_record)
    return all_records


def into_json(data, x: int):
    """Return a pretty-printed JSON string of `data` with indent `x`."""
    my_dump = json.dumps(data, indent=x)
    return my_dump


package_str = into_json(data, 4)


# helper: get the name of the first package in the listing
def get_name(data):
    new_data = data[0]
    name = new_data.get('name')
    return name


def get_analytics(name):
    """Fetch the analytics JSON for the given package name."""
    analytics_url = f"https://formulae.brew.sh/api/formula/{name}.json"
    analytics_data = get_response(analytics_url)
    return analytics_data


# Fetch analytics for the first package (original behavior)
package_data = get_analytics(get_name(data))


# The original script inspected package_data and printed the package name
for key, values in package_data.items():
    pass


name_analytics = package_data.get('name')

analytics = {
    '1 Month': package_data.get('analytics', {}).get('install_on_request', {}).get('30d').get(name_analytics),
    '3 Months': package_data.get('analytics', {}).get('install_on_request', {}).get('90d').get(name_analytics),
    '1 Year': package_data.get('analytics', {}).get('install_on_request', {}).get('365d').get(name_analytics)
}

for key, values in package_data.items():
    print(package_data['name'])