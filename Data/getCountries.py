import requests
import json
from API_KEY import *

headers = api_header

r = requests.get('https://covid-19-data.p.rapidapi.com/help/countries', headers=headers)


print(r)
j = json.loads(r.content)

with open('countries.json', 'w') as fp:
    json.dump(j, fp)
