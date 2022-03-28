from email import header
import json
import requests
from datetime import datetime

pixela_endpoint  = "https://pixe.la/v1/users" 

USERNAME = 'otwoma'
TOKEN = "zaphdev254tracker*"
GRAPH_ID = 'graph1'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "my coding graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response_post = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2022, month=3, day=28)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "8"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
