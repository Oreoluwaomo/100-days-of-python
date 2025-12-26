import requests
from twilio.rest import Client
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"

api_key = "ad0c2163327c3d2b732230ce21fafdd0"
account_sid = "ACe5974cdcff4f3cc32b5ef2b429455648"
auth_token = "612a2dff5d48c7bb1272d306bafc5c62"
weather_params = {
    "lat" : 6.612773,
    "lon" : 3.390033,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MG78872534159a3a6e01f805038096bde8',
        body="It's going to rain today,remember to bring an umbrella ☔",
        to='+2349030095489')
    print(message.status)