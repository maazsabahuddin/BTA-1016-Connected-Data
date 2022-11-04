# Python imports
import requests
import json


def weather_data(lat, lon):
    """
    This function will return the weather using the lat lon.
    :param lat:
    :param lon:
    :return:
    """

    # Local imports
    from main import OPEN_WEATHER_MAP_API_KEY

    # URL f-string
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_MAP_API_KEY}'

    # get the response from the API
    response = requests.get(url).text

    return round(json.loads(response)['main']['temp'] - 273.15, 2)
