import math
import requests
import pandas as pd

base_url = "https://api.nobelprize.org/2.1/"
endpoint = 'nobelPrizes'
def get_main_request(base_url, endpoint):
    r = requests.get(base_url + endpoint)
    return r.json()

def get_pages(response):
    pages = math.ceil(response['meta']['count'] / response['meta']['limit'])
    return pages

def parse_respsonse(response):
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










