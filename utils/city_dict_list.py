from datetime import datetime, timedelta, timezone

from config import API_KEY
from .api_request import api_request

def create_city_dict(city_name:str):
    data_dict = api_request(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={city_name}&appid={API_KEY}&lang=ua")
    geo_dict = api_request(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
    translated_city_name = geo_dict[0]["local_names"]["uk"]

    utc_now = datetime.now(timezone.utc)
    city_tz = timezone(timedelta(seconds = data_dict["timezone"]))
    time = utc_now.astimezone(city_tz)

    temp = f"{int(data_dict["main"]["temp"])}°"
    weather = data_dict["weather"][0]["description"]
    min_temp = f"{int(data_dict["main"]["temp_min"])}°"
    max_temp = f"{int(data_dict["main"]["temp_max"])}°"

    city_dict = {
        "search_name": city_name,
        "name": translated_city_name,
        "time": time.strftime('%H:%M'),
        "temp": temp,
        "weather": weather,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    return city_dict


city_name_list = [
            "Kyiv",
            "Dnipro",
            "Lviv",
            "Rome"
        ]
