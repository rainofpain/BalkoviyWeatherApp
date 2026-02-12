import requests
from config import API_KEY


def api_forecast_request(city_name: str, language: str):
    
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?units=metric&q={city_name}&appid={API_KEY}&lang={language}")
    data_dict = response.json()
    
    return data_dict

