import requests
import json

base_url = "https://formulae.brew.sh/api/formula.json"

def get_response(url):
    response = requests.get(url)
    return response.json()


data = get_response(base_url)


def parse_data(data):
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
    my_dump = json.dumps(data, indent=x)
    return my_dump


package_str = into_json(data, 4)


#print(data[0])


#analytics_url = f"https://formulae.brew.sh/api/formula/{name}.json"

def get_name(data):
    new_data = data[0]
    name = new_data.get('name')
    return name


def get_analytics(name):
    analytics_url = f"https://formulae.brew.sh/api/formula/{name}.json"
    analytics_data = get_response(analytics_url)
    return analytics_data


package_data = get_analytics(get_name(data))
#print(into_json(package_data, 4))
#print(type(data))

for key, values in package_data.items():
    pass
    #print(f"{key}: {values}")

name_analytics = package_data.get('name')

analytics = {
    '1 Month': package_data.get('analytics', {}).get('install_on_request', {}).get('30d').get(name_analytics),
    '3 Months': package_data.get('analytics', {}).get('install_on_request', {}).get('90d').get(name_analytics),
    '1 Year': package_data.get('analytics', {}).get('install_on_request', {}).get('365d').get(name_analytics)
}

for key, values in package_data.items():
    print(package_data['name'])