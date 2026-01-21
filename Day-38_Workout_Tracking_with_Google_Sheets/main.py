import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
NUT_EX_BASE_ENDPOINT = "https://app.100daysofpython.dev"
SHEETY_URL = os.getenv("SHEETY_ENDPOINT")

headers = {
    "x-app-id" : os.getenv("X-APP-ID"),
    "x-app-key" : os.getenv("X-APP-KEY")
}

nut_ex_example_data = {
    "query": input("Tell me which exercises you did? "),
    "weight_kg": 71,
    "height_cm": 170,
    "age": 30,
    "gender": "male"
}

nut_ex_example = f"{NUT_EX_BASE_ENDPOINT}/v1/nutrition/natural/exercise"
response = requests.post(url=nut_ex_example, json=nut_ex_example_data, headers=headers)
exercise_data = response.json()["exercises"][0]

print(exercise_data)
# Sheety kullanımı
today = datetime.now()

headers = {
    "Authorization": os.getenv("SHEETY_AUTH_KEY")
}

sheety_data = {
    "sayfa1" : {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_data["name"].title(),
        "duration": exercise_data["duration_min"],
        "calories": exercise_data["nf_calories"]
    }
}

print(sheety_data)

requests.post(url=SHEETY_URL, json=sheety_data, headers=headers)