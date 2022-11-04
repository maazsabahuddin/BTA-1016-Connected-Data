# Python imports
import requests
import json


def notify_iss():
    """
    This function use to notify and return lat lon
    :return:
    """
    response = requests.get("http://api.open-notify.org/iss-now.json")
    _data = json.loads(response.text)

    return _data["iss_position"]["latitude"], _data["iss_position"]["longitude"]
