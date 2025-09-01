import requests
import datetime as dt
pixela_endpoint= "https://pixe.la/v1/users"
TOKEN = name
USERNAME = username
ID =  "graph1"
# parameters = {
#     "token": ,
#     "username": ,
#     "agreeTermsofService" : "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url,json=parameters)
# print(response.text)
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# parameters = {
#     ,
#     "name": "coding Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "momiji",
# }
headers = {
    "X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=parameters, headers= headers)
# print(response.text)

time = dt.datetime.now()
date = time.strftime("%Y%m%d")
# parameters = {
#     "date" : time.strftime("%Y%m%d"),
#     "quantity": "10",
# }
graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# response = requests.put(url = graph_post_endpoint, headers=headers, json=parameters)
# print(response.text)


paramerters = {
    "quantity" : "3"
}
graph_put_endpoint = f"{graph_post_endpoint}/{date}"
response = requests.delete(url = graph_put_endpoint,headers=headers)

print(response.text)
