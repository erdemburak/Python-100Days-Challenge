import os
import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

MY_LAT = 40.036263
MY_LON = 32.888898

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

# This part is my solution
# for i in range(0,4):
#     if weather_data["list"][i]["weather"][0]["id"] < 700:
#         print("Take your Unbrella before going out!!!")

# This one from course
will_rain = False
for hour_date in weather_data["list"]:
    condition_code = hour_date["weather"][0]["id"]
    if int(condition_code) < 805:
        will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today, Remember to bring an ☔️",
            from_="+15612589572",
            to="MY_Phone"
        )
    print(message.status)
