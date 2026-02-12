import json

from .create_abspath import create_abspath


def write_json(content, path: str):
    try:
        with open(file = create_abspath(path), mode = "w", encoding = "utf-8") as file:
            json.dump(fp = file, obj = content, indent= 4, ensure_ascii= False)
    except Exception as error:
        print("\n", f"Помилка під час запису до файлу {path}: {error}", "\n")
