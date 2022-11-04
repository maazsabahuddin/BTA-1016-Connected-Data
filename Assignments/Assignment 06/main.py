# Python imports
import requests
import json

# Package imports
from twilio.rest import Client

# Local imports
from weather_api import weather_data
from space_station import notify_iss

jsonObject = open("./key.json")
data = json.load(jsonObject)

OPEN_WEATHER_MAP_API_KEY = data['OPEN_WEATHER_MAP_API_KEY']
TWILIO_ACCOUNT_SID = data["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = data["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = data["TWILIO_PHONE_NUMBER"]
SENDING_TO_NUMBER = data["SENDING_TO_NUMBER"]  # Your own number


def send_message(phone_number, message):
    """
    This function will send message to the given verified phone number.
    :param phone_number:
    :param message:
    :return:
    """
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    print(f"Message sent successfully with message id: {message.sid}")


latitude, longitude = notify_iss()
weather = weather_data(lat=latitude, lon=longitude)
send_message(phone_number=SENDING_TO_NUMBER, message=f"Space station latitude and longitude is {latitude}, {longitude}"
                                                     f" and the weather is {weather}°C.")
