import requests
from smtplib import SMTP

# Credentials for SMS system
# import os
# from twilio.rest import Client
# account_sid = os.environ['']
# auth_token = os.environ['']

MAIL = ""
PASSWORD = ""

URL = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "ddd5823d8829e48f928fb910ed78ab8c"
weather_params = {
    "lat": 23.822350,
    "lon": 90.365417,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(URL, params=weather_params)
response.raise_for_status()
hourly = response.json()["hourly"][0:12]
going_to_rain = False

for hour in hourly:
    if hour["weather"][0]["id"] < 600:
        going_to_rain = True
if going_to_rain:
    # EMAIL SYSTEM
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASSWORD)
        message = "Subject: Rain\n\nIt's going to rain today. Bring an Umbrella with you.\n\nShampad"
        connection.sendmail(from_addr="shampadsh@gmail.com", to_addrs="sompod123@gmail.com", msg=message)
        connection.close()

    # SMS SYSTEM

    # client = Client(account_sid, auth_token)
    # message = client.messages \
    #     .create(
    #     body="It's going to rain today. Bring an UMBRELLA with you.",
    #     from_='+12057549231',
    #     to='+8801521239970'
    # )
    #
    # print(message.status)
