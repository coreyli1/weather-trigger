import requests as req
from requests_toolbelt.utils import dump
import json
import pprint


def main():
    latitude = 33.0198
    longitude = -96.6989
    res = req.get(f'https://api.weather.gov/points/{latitude},{longitude}',)
    res_obj = (json.loads(res.content.decode('utf-8')))
    location = {
        'gridX':res_obj['properties']['gridX'], 
    'gridY':res_obj['properties']['gridY'], 
    'office':res_obj['properties']['cwa'],
    
    }
    office = location['office']
    gridX = location['gridX']
    gridY = location['gridY']

    res = req.get(f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast')
    res_obj = json.loads(res.content.decode('utf-8'))
    weather = res_obj['properties']['periods']




if __name__ == "__main__":
    main()