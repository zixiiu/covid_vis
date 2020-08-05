import requests
import json
import tqdm
import time
from API_KEY import *


def getData():
    with open('Data/countries.json', 'rb') as fp:
        con = json.load(fp)



    headers = api_header
    res = []
    for i in tqdm.tqdm(con):
        data = {
            "format": "json",
            "code": i['alpha2code']
        }
        r = requests.get('https://covid-19-data.p.rapidapi.com/country/code', headers=headers, params = data)

        j = json.loads(r.content)
        res.append(j)
        time.sleep(1.5)



    return res


if __name__ == '__main__':
    res = getData()
    with open('today.json', 'w') as fp:
        json.dump(res, fp)
