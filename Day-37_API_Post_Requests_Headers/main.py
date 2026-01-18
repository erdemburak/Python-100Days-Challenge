import requests
from datetime import datetime

USERNAME = "elessar"
TOKEN = "CFj0s%R4kBR%hq"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Pixela üzerinde kullanıcı oluşturduk 
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Dk",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Bu adım pixela api ile verdiğimiz config verilerine göre graph oluşturuyor
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
today = datetime(year=2026, month=1, day=17)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "22",
}

# istediğimiz spesifik bir tarihe veri giriyoruz 
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "50"
}

# Verdiğimiz tarihteki veriyi güncelliyoruz
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response)