import dotenv
import os
from utils import read_json

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")

city_name_list = [
            "Kyiv",
            "Dnipro",
            "Lviv",
            "Rome"
        ]
cities_dict = read_json("static/json/cities_english.json")