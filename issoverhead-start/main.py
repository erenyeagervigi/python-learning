import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 12.996140
MY_LONG = 77.672310
MY_EMAIL = "[test@gmail.com]"
PASSWORD =  "[password]"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid" : "Asia/kolkata"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

while True:
    time.sleep(60)
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        if hour >= sunset or hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password= PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg= "Subject: international space station\n\n look up!!!")



