import PyQt6.QtWidgets as widgets
from .app import app_obj


screen = app_obj.primaryScreen()
screen_size = screen.size()

screen_width = screen_size.width()
screen_height = screen_size.height()

center_x = (screen_width // 2) - (screen_width // 4)
center_y = (screen_height // 2) - (screen_height // 4)


main_window = widgets.QMainWindow()

main_window.setGeometry(center_x, center_y, screen_width // 2, screen_height // 2)
main_window.setWindowTitle("Weather forecast")
main_window.setStyleSheet("background-color: red; ")

