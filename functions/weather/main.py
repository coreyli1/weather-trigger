import requests as req
import json


def daily(request):
    """HTTP Cloud Function.
    Args:
        the request object
    Returns:
        the response object
    """
    request_json = request.get_json()
    args = request.args
    if request.args and 'lat' in request.args and 'long' in request.args:
        latitude = float(request.args.get('lat'))
        longitude = float(request.args.get('long'))
    else:
        return {
            'error': 'provide a lat and long'
        }
    res = req.get(f'https://api.weather.gov/points/{latitude},{longitude}',)
    res_obj = (json.loads(res.content.decode('utf-8')))
    location = {
        'gridX': res_obj['properties']['gridX'],
        'gridY': res_obj['properties']['gridY'],
        'office': res_obj['properties']['cwa'],

    }
    office = location['office']
    gridX = location['gridX']
    gridY = location['gridY']

    res = req.get(
        f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast')
    res_obj = json.loads(res.content.decode('utf-8'))
    daily = res_obj['properties']['periods']

    res = req.get(
        f'https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast/hourly')
    res_obj = json.loads(res.content.decode('utf-8'))
    hourly = res_obj['properties']['periods']

    return json.dumps({
        'daily': daily,
        'hourly': hourly,
    }, indent=2)
