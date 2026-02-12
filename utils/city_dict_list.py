from datetime import datetime, timedelta, timezone
from .write_json import write_json

from .api_weather_request import api_weather_request
from .api_geo_request import api_geo_request

def create_city_dict(city_name:str):
    data_dict = api_weather_request(city_name, "ua")
    write_json(data_dict, f"static/json/{city_name}.json")
    geo_dict = api_geo_request(data_dict["name"])
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
# city_dict_list =[]

# for city_name in city_name_list:

#     city_dict = create_city_dict(city_name = city_name)

#     city_dict_list.append(city_dict)