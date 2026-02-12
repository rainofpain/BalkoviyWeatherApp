import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg
import PyQt6.QtGui as qt_gui

from utils import *

class InfoCard(qt_widgets.QFrame):
    def __init__(self, parent, search_city_name: str, city_name: str, time: str, temp: str, weather: str, min_temp: str, max_temp: str):
        super().__init__(parent = parent)

        self.CLICKED = False
        self.SEARCH_NAME = search_city_name
        self.NAME = city_name
        self.TIME = time
        self.TEMP = temp
        self.WEATHER = weather
        self.MIN_TEMP = min_temp
        self.MAX_TEMP = max_temp
        
        self.setObjectName("Card")
        self.setFixedSize(330, 90)
        self.setStyleSheet("background-color: transparent; ")

        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (8, 8, 8, 8), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )

        self.setLayout(self.LAYOUT)

        self.TOP_FRAME = qt_widgets.QFrame(parent = self)
        self.TOP_FRAME.setFixedSize(314, 52)
       
        self.TOP_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )

        self.TOP_FRAME.setLayout(self.TOP_FRAME_LAYOUT)

        self.CITY_FRAME = qt_widgets.QFrame(parent = self.TOP_FRAME)
        self.CITY_FRAME.setFixedSize(247, 52)
        

        self.CITY_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 6, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.CITY_FRAME.setLayout(self.CITY_FRAME_LAYOUT)

        self.CITY_NAME_FRAME = qt_widgets.QFrame(parent = self.CITY_FRAME)

        self.CITY_NAME_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CITY_NAME_FRAME.setFixedSize(247, 28)
        self.CITY_NAME_FRAME.setLayout(self.CITY_NAME_FRAME_LAYOUT)

       
        self.ARROW = qt_widgets.QFrame(parent = self.CITY_NAME_FRAME)
        self.ARROW.setFixedSize(16, 16)
        self.ARROW.setObjectName("Arrow")
        
        self.CITY_NAME_FRAME_LAYOUT.addWidget(self.ARROW)
        self.ARROW.hide()

        self.CITY_NAME = qt_widgets.QLabel(text = self.NAME, parent = self.CITY_NAME_FRAME)
        self.CITY_NAME.setStyleSheet("font-size: 24px")
                                      
                                     
                                     

        self.CITY_NAME_FRAME_LAYOUT.addWidget(self.CITY_NAME)

        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_NAME_FRAME)
        
        self.CITY_TIME = qt_widgets.QLabel(text = self.TIME, parent = self.CITY_FRAME)
        self.CITY_TIME.setFixedSize(247, 18)
        self.CITY_TIME.setStyleSheet("font-size: 12px;")

        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_TIME)


        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_FRAME)

        self.CITY_TEMP_FRAME = qt_widgets.QFrame(parent = self.TOP_FRAME)
        self.CITY_TEMP_FRAME.setFixedSize(67, 52)

        self.CITY_TEMP_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.CITY_TEMP_FRAME.setLayout(self.CITY_TEMP_FRAME_LAYOUT)

        self.CITY_TEMP_LABEL = qt_widgets.QLabel(text = self.TEMP, parent = self.CITY_TEMP_FRAME)
        self.CITY_TEMP_LABEL.setFixedSize(67, 44)
        self.CITY_TEMP_LABEL.setStyleSheet("font-size: 44px;")

        self.CITY_TEMP_FRAME_LAYOUT.addWidget(self.CITY_TEMP_LABEL)

        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_TEMP_FRAME)

        self.LAYOUT.addWidget(self.TOP_FRAME)

        self.BOT_FRAME = qt_widgets.QFrame(parent = self)
        self.BOT_FRAME.setFixedSize(314, 14)

        self.BOT_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )

        self.BOT_FRAME.setLayout(self.BOT_FRAME_LAYOUT)

        self.CITY_WEATHER = qt_widgets.QLabel(text = self.WEATHER, parent = self.BOT_FRAME)
        self.CITY_WEATHER.setFixedSize(216, 14)
        self.CITY_WEATHER.setStyleSheet("font-size: 12px;")

        self.BOT_FRAME_LAYOUT.addWidget(self.CITY_WEATHER)

        self.MIN_AND_MAX_TEMP = qt_widgets.QLabel(
            text = f"Макс.:{self.MAX_TEMP}, мін.:{self.MIN_TEMP}",
            parent = self.BOT_FRAME
            )
        
        self.MIN_AND_MAX_TEMP.setFixedSize(98, 14)
        self.MIN_AND_MAX_TEMP.setStyleSheet("font-size: 12px;")

        self.BOT_FRAME_LAYOUT.addWidget(self.MIN_AND_MAX_TEMP)

        self.LAYOUT.addWidget(self.BOT_FRAME)

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.LINE_FRAME.setFixedSize(314, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")

        self.LAYOUT.addWidget(self.LINE_FRAME)

    def mousePressEvent(self, event: qt_gui.QMouseEvent):

        button = event.button()
    
        if button == core.Qt.MouseButton.LeftButton:

            if self.CLICKED == False:

                left_container = self.parent().parent().parent().parent()
                left_container.reset_card_click()
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
                new_data = create_city_dict(self.SEARCH_NAME)
                self.CITY_TIME.setText(f"{new_data["time"]}")
                self.CITY_TEMP_LABEL.setText(new_data["temp"])
                self.CITY_WEATHER.setText(new_data["weather"].capitalize())
                self.MIN_AND_MAX_TEMP.setText(f"Макс.:{new_data["max_temp"]}, мін.:{new_data["min_temp"]}")
                
            elif self.CLICKED == True:

                self.CLICKED = False
                self.ARROW.hide()
                self.setStyleSheet("background-color: transparent; ")