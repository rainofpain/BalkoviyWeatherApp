import requests
from config import API_KEY


def api_geo_request(city_name: str):
    
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
    data_dict = response.json()
    
    return data_dict
