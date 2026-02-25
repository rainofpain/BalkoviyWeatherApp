import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *
from config import city_name_list
from .components import SearchFrame
from ...containers_utils import search_field_text
from ...left_container import InfoCard

class HeaderContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.CHECK_RESULT = {}
        self.LEFT_CONTAINER_SCROLL = self.window().findChild(qt_widgets.QFrame, "LeftContainerScroll")

        self.setFixedSize(788, 36)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignVCenter
        )

        self.setLayout(self.LAYOUT)
        self.SETTINGS_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.SETTINGS_FRAME)
        self.SETTINGS_FRAME.setFixedSize(144, 36)
        self.SETTINGS_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.SETTINGS_FRAME.setLayout(self.SETTINGS_FRAME_LAYOUT)
        self.SETTINGS_BUTTON = qt_widgets.QPushButton(parent = self.SETTINGS_FRAME)
        self.SETTINGS_BUTTON.setFixedSize(36, 36)
        self.SETTINGS_BUTTON.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0.2); 
            border-radius: 4px; 
            image: url(media/settings_icon.svg);
            padding: 10px;
            """
            )
        
        self.SETTINGS_FRAME_LAYOUT.addWidget(self.SETTINGS_BUTTON)

        self.SETTINGS_LABEL = qt_widgets.QLabel(text = "Налаштування", parent = self.SETTINGS_FRAME)
        self.SETTINGS_LABEL.setStyleSheet("font-size: 14px; font-weight: 500;")
        self.SETTINGS_FRAME_LAYOUT.addWidget(self.SETTINGS_LABEL)

        self.SEARCH_GROUP_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.SEARCH_GROUP_FRAME, alignment = core.Qt.AlignmentFlag.AlignRight)
        self.SEARCH_GROUP_FRAME.setFixedSize(368, 36)
        self.SEARCH_GROUP_FRAME_LAYOUT =  create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignVCenter
        )
        self.SEARCH_GROUP_FRAME.setLayout(self.SEARCH_GROUP_FRAME_LAYOUT)

        self.ADD_CITY_BUTTON = qt_widgets.QPushButton(parent = self.SEARCH_GROUP_FRAME)
        self.SEARCH_GROUP_FRAME_LAYOUT.addWidget(self.ADD_CITY_BUTTON)
        self.ADD_CITY_BUTTON.setObjectName("AddCityButton")
        self.ADD_CITY_BUTTON.setFixedSize(97, 36)
        self.ADD_CITY_BUTTON.setText(" Додати")
        self.ADD_CITY_BUTTON.setIcon(qt_gui.QIcon("media/add_btn.svg"))
        self.ADD_CITY_BUTTON.setStyleSheet(
            """
            QPushButton{
            background-color: rgba(0, 0, 0, 0.2); 
            border-radius: 4px;
            color: rgba(255, 255, 255, 1);
            font-size: 17px;
            }
            """
            )
        self.ADD_CITY_BUTTON.clicked.connect(self.add_city)
        self.ADD_CITY_BUTTON.hide()

        self.SEARCH_INPUT_FRAME = SearchFrame(parent = self.SEARCH_GROUP_FRAME)
        self.SEARCH_GROUP_FRAME.layout().addWidget(self.SEARCH_INPUT_FRAME, alignment = core.Qt.AlignmentFlag.AlignRight)
    
    def check_data(self, data):
        self.CHECK_RESULT = data
        if len(self.CHECK_RESULT) > 0 and data["name"] not in city_name_list: 
            city_name_list.append(data["name"])
            self.CARD.CLICKED = True
            self.CARD.ARROW.show()
            self.CARD.setStyleSheet(
                """
                *{
                background-color: transparent;
                }

                #Card {
                background-color: rgba(0, 0, 0, 0.2); 
                border-radius: 8px;
                }
                """
                )
            self.LEFT_CONTAINER_SCROLL.layout().addWidget(self.CARD, alignment = core.Qt.AlignmentFlag.AlignRight)
        self.SEARCH_INPUT_FRAME.SEARCH_FIELD.setText("")

    def add_city(self):

        city_name = self.SEARCH_INPUT_FRAME.SEARCH_FIELD.text().capitalize()
        
        self.CARD = InfoCard(
                parent = self.LEFT_CONTAINER_SCROLL,
                search_city_name = city_name
                )
        self.CARD.load_weather()
        self.CARD.WEATHER_LOADER.filtered_dict.connect(self.check_data)   

        
        