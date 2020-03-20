
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests as req
import json


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
