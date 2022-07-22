import requests

USER_NAME = "futa"
TOKEN = "dfgfgrthfghtrtfg"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# responsee = requests.post(url=pixela_endpoint,json= user_params)
# print(responsee.text)

graphs_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "my coding graph",
    "unit": "hours",
    "type": "float",
    "color":"sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graphs_endpoint,json=graph_config,headers=headers)
# print(response.text)
import datetime
today = datetime.datetime.now()
print(today.strftime('%Y%m%d'))
pixel_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'
pixel_params = {
    "date":today.strftime('%Y%m%d'),
    "quantity":"10",
}
# response = requests.post(url=pixel_endpoint,headers=headers,json =pixel_params)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_params = {
    "quantity":"4"
}
#
# response = requests.put(url=update_endpoint,json=update_params,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

responsse = requests.delete(url=delete_endpoint,headers=headers)
print(responsse.text)
