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
            'three_month': three_month,
            'one_year': one_year
           }
        }



        results.append(analytics)
        time.sleep(details.elapsed.total_seconds())
        print(f"Processed: {name} in {details.elapsed.total_seconds()} seconds")

        break


    return results

t2 = time.perf_counter()
print(f"Time taken to process: {t2 - t1} seconds")


with open('package_analytics.json', 'w') as f:
    json.dump(parse(data), f, indent=2)

print(f"Time taken to process: {t2 - t1} seconds")

"""parsed_data = parse(data)
print(json.dumps(parsed_data, indent=4))
"""








