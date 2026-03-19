import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *
from config import city_name_list, API_KEY

class CityCard(qt_widgets.QFrame):
    def __init__(self, parent, city_name: str):
        super().__init__(parent = parent)

        self.SETTINGS_CONTENT_AREA = self.parent().parent().parent().parent().parent().parent().parent().parent()
        self.NAME = city_name
        self.setFixedSize(512, 32)

        self.setStyleSheet(
            """
           
            CityCard::hover {
            border-radius: 2px;
            background-color: rgba(0, 0, 0, 0.2);
            }
            """
            )

        self.LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignVCenter
            )

        self.setLayout(self.LAYOUT)

        self.LABEL = qt_widgets.QLabel(parent = self)
        self.LABEL.setStyleSheet("font-size: 14px;")
        self.LAYOUT.addWidget(self.LABEL, alignment = core.Qt.AlignmentFlag.AlignLeft)

        self.BUTTON = qt_widgets.QPushButton(parent = self)

        self.LAYOUT.addWidget(self.BUTTON, alignment = core.Qt.AlignmentFlag.AlignRight)

        self.BUTTON.setIcon(qt_gui.QIcon("media/trash.svg"))

        self.BUTTON.setIconSize(core.QSize(16, 16))
        self.BUTTON.setFixedSize(16, 16)

        self.BUTTON.clicked.connect(self.remove_city_from_list)

        self.load_name()

    def load_name(self):
        self.WEATHER_LOADER = WeatherLoader(
            api_request_link = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={self.NAME}&appid={API_KEY}&lang={self.window().APP_LANGUAGE}",
            language = self.window().APP_LANGUAGE
        )
        self.WEATHER_LOADER.filtered_dict.connect(self.set_name)
        self.WEATHER_LOADER.start()

    def set_name(self, city_dict):
        self.LABEL.setText(city_dict["name"])

    def remove_city_from_list(self):
        if city_name_list:
            city_name_list.remove(self.NAME)
            update_content.update_left_container.emit(True)
            self.SETTINGS_CONTENT_AREA.MENU_CONTAINER.show_city_search()
        
