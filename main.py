from modules import app_obj, main_window
from utils import api_request

api_request("Dnipro")

def main():
    try:
        main_window.show()
        app_obj.exec()
    except Exception as error:
        print("\n", f"Помилка під час запуску проєкту: {error}", "\n")


if __name__ == '__main__':
    main()
