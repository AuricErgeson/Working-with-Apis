import requests
import json

names_url = "https://restcountries.com/v3.1/all?fields=name"

#### Get Response Function ####
def get_response(url):
  response = requests.get(url, timeout=10)
  return response.json()

# Get country names and store in a list

names = get_response(names_url)

name_list = []
for item in names:
  name = item['name']['common']
  name_list.append(name)


### Get country details and parse required information

data_countries = []

for name_str in name_list:

    filter_url = f"https://restcountries.com/v3.1/name/{name_str}"
    details = get_response(filter_url)

    for item in details:
        name = item['name']['common']
        languages = item.get('languages', {})
        capital = item.get('capital', [])
        currencies = item.get('currencies', {})
        population = item['population']

        countries = {
            'Name': name,
            'Capital': capital,
            'Languages': languages,
            'Population': population,
            'Currencies': currencies
        }

        data_countries.append(countries)

# Store data in JSON file
with open('countries_data.json', 'w') as f:
    json.dump(data_countries, f, indent=2)
