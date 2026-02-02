"""Fetch Nobel Prize records and export CSV.

This preserves the original top-level execution: functions are defined and
then the script immediately queries the API, pages through results, and
writes `nobel_prizes.csv`. Only comments were added — no logic changes.
"""

import math
import requests
import pandas as pd


base_url = "https://api.nobelprize.org/2.1/"
endpoint = 'nobelPrizes'


def get_main_request(base_url, endpoint):
    """Perform a GET for the provided endpoint and return JSON."""
    r = requests.get(base_url + endpoint)
    return r.json()


def get_pages(response):
    """Compute number of pages from response meta (count / limit)."""
    pages = math.ceil(response['meta']['count'] / response['meta']['limit'])
    return pages


def parse_respsonse(response):
    """Parse a single API page into simplified records.

    Note: the function name retains the original spelling to avoid changing
    any callers in the repository.
    """
    parse_list = []
    for item in response['nobelPrizes']:
        if 'laureates' in item:
            n = len(item['laureates'])
        else:
            n = 0
        r_data = {
            'awardYear': item['awardYear'],
            'category': item['category']['en'],
            'laureates': n
        }
        parse_list.append(r_data)

    return parse_list


data = get_main_request(base_url, endpoint)

main_data = []
for x in range (get_pages(data)):
    offset = x * data['meta']['limit']

    main_data.extend(parse_respsonse(
        get_main_request(base_url, endpoint + f'?offset={offset}')
    )
    )

df = pd.DataFrame(main_data)
df.to_csv('nobel_prizes.csv', index=False)
