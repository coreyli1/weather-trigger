import requests as req
import json




# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def daily(request):
    """HTTP Cloud Function.
    Args:
        the request object
    Returns:
        the response object
    """
    twilio()
    request_json = request.get_json()
    args = request.args
    print(request_json, '\n', args,'\n', request)

    if request.args and 'lat' in request.args and 'long' in request.args:
        latitude = float(request.args.get('lat'))
        longitude = float(request.args.get('long'))
    else:
        return json.dumps({
            'error': 'provide a lat and long'
        }, indent=2)
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


def twilio():

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACa4baaeb3fc51126fa67758dea02f6b7c'
    auth_token = '8c53626cbd6d6ab0765cdc51c1369d83'
    client = Client(account_sid, auth_token)

    res = req.get('https://us-central1-weather-271603.cloudfunctions.net/function-1', params={
        'lat': 33.0198,
        'long': -96.6989,
    })

    res_obj = json.loads(res.content.decode('utf-8'))

    print(res.content)

    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            messaging_service_sid='MG07da65e431342e7fa18631063d993b6a',
            to='+19729716345'
        )

    print(message.sid)

