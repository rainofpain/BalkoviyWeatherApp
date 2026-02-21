import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg
import PyQt6.QtGui as qt_gui

from config import API_KEY
from ...containers_utils import WeatherLoader, city_name_message,api_link_message

from utils import *


class InfoCard(qt_widgets.QFrame):
    def __init__(self, parent, search_city_name: str):
        super().__init__(parent = parent)

        self.LEFT_CONTAINER = self.parent().parent().parent().parent()
        self.CLICKED = False
        self.SEARCH_NAME = str(search_city_name)
        self.API_LINK = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={self.SEARCH_NAME}&appid={API_KEY}&lang=ua"
        
        self.setObjectName("Card")
        self.setFixedSize(330, 90)
        self.setStyleSheet("background-color: transparent;")

        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 8, 
            content_margins = (8, 8, 8, 8), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )

        self.setLayout(self.LAYOUT)

        self.TOP_FRAME = qt_widgets.QFrame(parent = self)
        self.TOP_FRAME.setFixedSize(314, 52)
       
        self.TOP_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )

        self.TOP_FRAME.setLayout(self.TOP_FRAME_LAYOUT)
        self.LAYOUT.addWidget(self.TOP_FRAME)

        self.CITY_FRAME = qt_widgets.QFrame(parent = self.TOP_FRAME)
        self.CITY_FRAME.setFixedSize(247, 52)
        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_FRAME)
        

        self.CITY_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 6, 
            content_margins = (0, 0, 0, 4), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.CITY_FRAME.setLayout(self.CITY_FRAME_LAYOUT)

        self.CITY_NAME_FRAME = qt_widgets.QFrame(parent = self.CITY_FRAME)
        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_NAME_FRAME)

        self.CITY_NAME_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CITY_NAME_FRAME.setFixedSize(247, 28)
        self.CITY_NAME_FRAME.setLayout(self.CITY_NAME_FRAME_LAYOUT)

       
        self.ARROW = qt_svg.QSvgWidget("media/navigation.svg",parent = self.CITY_NAME_FRAME)
        self.ARROW.setFixedSize(16, 16)
        self.ARROW.setObjectName("Arrow")
        
        self.CITY_NAME_FRAME_LAYOUT.addWidget(self.ARROW)
        self.ARROW.hide()

        self.CITY_NAME = qt_widgets.QLabel(parent = self.CITY_NAME_FRAME)
        self.CITY_NAME.setStyleSheet("font-size: 24px")
        self.CITY_NAME_FRAME_LAYOUT.addWidget(self.CITY_NAME)
                                      
        self.CITY_TIME = qt_widgets.QLabel(parent = self.CITY_FRAME)
        self.CITY_TIME.setFixedSize(247, 18)
        self.CITY_TIME.setStyleSheet("font-size: 12px;")

        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_TIME)

        self.CITY_TEMP_FRAME = qt_widgets.QFrame(parent = self.TOP_FRAME)
        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_TEMP_FRAME)

        self.CITY_TEMP_FRAME.setFixedSize(67, 52)

        self.CITY_TEMP_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.CITY_TEMP_FRAME.setLayout(self.CITY_TEMP_FRAME_LAYOUT)

        self.CITY_TEMP_LABEL = qt_widgets.QLabel(parent = self.CITY_TEMP_FRAME)
        self.CITY_TEMP_FRAME_LAYOUT.addWidget(self.CITY_TEMP_LABEL)
        self.CITY_TEMP_LABEL.setStyleSheet("font-size: 44px;")
        self.CITY_TEMP_LABEL.setIndent(0)
        self.CITY_TEMP_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignBottom | core.Qt.AlignmentFlag.AlignRight)
    
        self.BOT_FRAME = qt_widgets.QFrame(parent = self)
        self.BOT_FRAME.setFixedSize(314, 14)

        self.BOT_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )

        self.BOT_FRAME.setLayout(self.BOT_FRAME_LAYOUT)

        self.CITY_WEATHER = qt_widgets.QLabel(parent = self.BOT_FRAME)
        self.CITY_WEATHER.setFixedSize(161, 14)
        self.CITY_WEATHER.setStyleSheet("font-size: 12px;")

        self.BOT_FRAME_LAYOUT.addWidget(self.CITY_WEATHER)

        self.MIN_AND_MAX_TEMP = qt_widgets.QLabel(parent = self.BOT_FRAME)
        
        self.MIN_AND_MAX_TEMP.setFixedSize(161, 14)
        self.MIN_AND_MAX_TEMP.setStyleSheet("font-size: 12px;")

        self.BOT_FRAME_LAYOUT.addWidget(self.MIN_AND_MAX_TEMP)
        self.MIN_AND_MAX_TEMP.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        self.MIN_AND_MAX_TEMP.setIndent(4)

        self.LAYOUT.addWidget(self.BOT_FRAME)

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.LINE_FRAME)
        self.LINE_FRAME.setFixedSize(314, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
    
    def update_ui(self, new_data: dict):
        self.CITY_NAME.setText(new_data["name"])
        self.CITY_TIME.setText(f"{new_data['time']}")
        self.CITY_TEMP_LABEL.setText(new_data["temp"])
        self.CITY_WEATHER.setText(new_data["weather"].capitalize())
        self.MIN_AND_MAX_TEMP.setText(f"Макс.:{new_data['max_temp']}, мін.:{new_data['min_temp']}")
    
    def load_weather(self):
        self.WEATHER_LOADER = WeatherLoader(
            api_request_link = self.API_LINK
            )
        
        self.WEATHER_LOADER.filtered_dict.connect(self.update_ui) 
        self.WEATHER_LOADER.start()

    def mousePressEvent(self, event: qt_gui.QMouseEvent):

        button = event.button()
    
        if button == core.Qt.MouseButton.LeftButton:

            if self.CLICKED == False:

                self.LEFT_CONTAINER.reset_card_click()
                self.CLICKED = True
                self.ARROW.show()
                self.setStyleSheet(
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
                self.load_weather()
                api_link_message.message.emit(self.API_LINK)
                city_name_message.message.emit(self.SEARCH_NAME)
                
                
            elif self.CLICKED == True:

                self.CLICKED = False
                self.ARROW.hide()
                self.setStyleSheet("background-color: transparent; ")