import requests
from config import API_KEY

def api_request(city_name: str):
    
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}")
    data_dict = response.json()
    
    print(data_dict)
    