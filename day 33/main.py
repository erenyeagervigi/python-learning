import requests
import datetime as dt
response= requests.get(url ="http://api.open-notify.org/iss-now.json" )
response.raise_for_status()

data = response.json()['iss_position']

longitude = data['longitude']
latitude = data['latitude']

parameters = {
    "lat" : latitude,
    "lng" : latitude,
    "tzid": "Asia/Kolkata",
    "formatted": 0
}
response2 = requests.get(url = 'https://api.sunrise-sunset.org/json', params= parameters)
response2.raise_for_status()
data2 = response2.json()
sunrise = data2['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data2['results']['sunset'].split('T')[1].split(':')[0]

time = dt.datetime.now()
print(time.hour)
print(sunrise)