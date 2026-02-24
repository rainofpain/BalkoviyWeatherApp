from datetime import datetime, timedelta, timezone

from config import API_KEY
from .api_request import api_request

def create_city_dict(city_data: dict):
    try:
        cod = city_data["cod"]
        city_name = city_data["name"]
        geo_dict = api_request(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")

        try:
            translated_city_name = geo_dict[0]["local_names"]["uk"]
        except:
            translated_city_name = geo_dict[0]["name"]

        days = [
            "Понеділок", 
            "Вівторок", 
            "Середа", 
            "Четвер", 
            "П’ятниця", 
            "Субота", 
            "Неділя"
            ]
        
        day = days[datetime.now().weekday()]
        utc_now = datetime.now(timezone.utc)
        city_tz = timezone(timedelta(seconds = city_data["timezone"]))
        time = utc_now.astimezone(city_tz)

        temp = f"{int(city_data["main"]["temp"])}°"
        weather = city_data["weather"][0]["description"]
        min_temp = f"{int(city_data["main"]["temp_min"])}°"
        max_temp = f"{int(city_data["main"]["temp_max"])}°"
        weather_icon = city_data["weather"][0]["icon"]

        city_dict = {
            "search_name": city_name,
            "name": translated_city_name,
            "time": time.strftime("%H:%M"),
            "date": time.strftime("%d.%m.%Y"),
            "day": day,
            "temp": temp,
            "weather": weather,
            "min_temp": min_temp,
            "max_temp": max_temp,
            "weather_icon": weather_icon
        }

        return city_dict
    
    except Exception:
        print("create_city_dict() not able to load data")
        return cod