import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class InfoCard(qt_widgets.QFrame):
    def __init__(self, parent, city_name: str, time: str, temp: str, weather: str, min_temp: str, max_temp: str):
        super().__init__(parent = parent)

        self.setFixedSize(330, 90)
        self.setStyleSheet("background-color: transparent; ")

        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 8, 
            content_margins = (0, 0, 0, 0), 
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

        self.CITY_NAME = qt_widgets.QLabel(text = city_name, parent = self.CITY_FRAME)
        self.CITY_NAME.setFixedSize(247, 28)
        self.CITY_NAME.setStyleSheet("""
                                     color: white;
                                     font-size: 24px;
                                     font-weight: 500;
                                     """)

        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_NAME)

        self.TIME = qt_widgets.QLabel(text = time, parent = self.CITY_FRAME)
        self.TIME.setFixedSize(247, 18)
        self.TIME.setStyleSheet("""
                                     color: white;
                                     font-size: 12px;
                                     font-weight: 500;
                                     """)

        self.CITY_FRAME_LAYOUT.addWidget(self.TIME)

        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_FRAME)

        self.TEMP_FRAME = qt_widgets.QFrame(parent = self.TOP_FRAME)
        self.TEMP_FRAME.setFixedSize(67, 52)

        self.TEMP_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.TEMP_FRAME.setLayout(self.TEMP_FRAME_LAYOUT)

        self.TEMP = qt_widgets.QLabel(text = temp, parent = self.TEMP_FRAME)
        self.TEMP.setFixedSize(67, 44)
        self.TEMP.setStyleSheet("""
                                     color: white;
                                     font-size: 44px;
                                     font-weight: 500;
                                     """)

        self.TEMP_FRAME_LAYOUT.addWidget(self.TEMP)

        self.TOP_FRAME_LAYOUT.addWidget(self.TEMP_FRAME)

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

        self.WEATHER = qt_widgets.QLabel(text = weather, parent = self.BOT_FRAME)
        self.WEATHER.setFixedSize(216, 14)
        self.WEATHER.setStyleSheet("""
                                     color: white;
                                     font-size: 12px;
                                     font-weight: 500;
                                     """)

        self.BOT_FRAME_LAYOUT.addWidget(self.WEATHER)

        self.MIN_AND_MAX_TEMP = qt_widgets.QLabel(
            text = f"Макс.:{max_temp}, мін.:{min_temp}",
            parent = self.BOT_FRAME
            )
        
        self.MIN_AND_MAX_TEMP.setFixedSize(98, 14)
        self.MIN_AND_MAX_TEMP.setStyleSheet("""
                                     color: white;
                                     font-size: 12px;
                                     font-weight: 500;
                                     """)

        self.BOT_FRAME_LAYOUT.addWidget(self.MIN_AND_MAX_TEMP)

        self.LAYOUT.addWidget(self.BOT_FRAME)

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.LINE_FRAME.setFixedSize(314, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")

        self.LAYOUT.addWidget(self.LINE_FRAME)