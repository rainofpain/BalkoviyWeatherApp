import dotenv
import os
from utils import read_json

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")

path_to_image_list = ["media/weather_icons/set_1"]

city_name_list = []
cities_dict = read_json("static/json/cities_english.json")
countries_and_cities_dict = read_json("static/json/countries_and_cities.json")