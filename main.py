from modules import app_obj, main_window, desktop_widget


def main():
    try:
        desktop_widget.show()
        main_window.show()
        app_obj.exec()
    except Exception as error:
        print("\n", f"Помилка під час запуску проєкту: {error}", "\n")


if __name__ == '__main__':
    main()
