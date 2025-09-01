import requests
import os
from twilio.rest import Client

account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

url = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "API_KEY"

params = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()
is_raining = False
# for i in range(4):
#     weather_id = weather_data['list'][i]['weather'][0]['id']
#     if weather_id < 700:
#         is_raining = True

for data in weather_data['list']:
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        is_raining = True

if is_raining:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        from_='whatsapp:NUMBER',
        to='whatsapp: NUMBER',
        body = "weather is kinda cloudy better wear warm clothes 🧥🧥"
    )
    print(message.status)



