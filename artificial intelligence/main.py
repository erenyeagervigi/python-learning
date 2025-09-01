import requests
import datetime


time = datetime.datetime.now()

API_ID = "77f81f14"
API_KEY = "c7476e9d19ce4ab5b1154c8a707a7350"

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = 'https://api.sheety.co/6080f6c2e197e7a78fdb09d4091eff6a/workoutTracking/sheet1'
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    'Content-Type': 'application/json'
}
user_input = input("Tell me which exercises you did: ")
query = {
    "query": user_input
}

response = requests.post(url = url, headers = headers,json=query)
recieved = response.json()
print(recieved)

sheety_headers = {
    "Authorization": "Bearer erenyeager",
    "Content-Type" :"application/json"
}
for exersice in recieved['exercises']:
    parameters = {
        "sheet1":{
            "date": time.strftime("%d/%m/%Y").title(),
            "time":time.strftime("%X"),
            "exercise": exersice['name'].title(),
            "duration": str(round(exersice['duration_min'])),
            "calories": exersice['nf_calories']
        }
    }
    response1 = requests.post(url = sheety_url,json=parameters, headers= sheety_headers)
    print(response1.text)