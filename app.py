from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
import requests as req
from requests_toolbelt.utils import dump
import json
import pprint



def main():
    lat, long = find_location('1713 Snowmass Drive', 'Plano', 'Texas')
    pprint.pprint(weather(lat, long))
    return 'fuck you'



    
def find_location(address, city, state):

    address = '+'.join(address.split(' '))
    city = '+' + '+'.join(city.split(' '))
    state = '+' + state

    MAPS_API = 'AIzaSyAkZeNLI9Brl60rekMMPD-dgVir86iggGM'

    get_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address},{city},{state}&key={MAPS_API}'
    res = req.get(get_url)
    res_obj = json.loads(res.content.decode('utf-8'))
    lat = res_obj['results'][0]['geometry']['location']['lat']
    lng = res_obj['results'][0]['geometry']['location']['lng']
    print(lat,lng)
    # pprint.pprint(res_obj)

    return lat, lng

def weather(lat, long):
    latitude = lat
    longitude = long
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
    daily = res_obj['properties']['periods']

    res = req.get(f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast/hourly')
    res_obj = json.loads(res.content.decode('utf-8'))
    hourly = res_obj['properties']['periods']

    return {
        'daily': daily,
        'hourly': hourly,
    }

if __name__ == "__main__":
    main()
