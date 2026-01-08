import json

from .create_abspath import create_abspath

def read_json(path: str):
    try:
        with open(file = create_abspath(path), mode = "r") as file:
            return json.load(file)
    except Exception as error:
        print("\n", f"Помилка під час отримання контенту файлу {path}: {error}", "\n")
