import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from datetime import datetime, timezone, timedelta

from .components import WeatherCard, TopFrameScroll
from .....containers_utils import city_name_message, WeatherLoader
from config import API_KEY
from utils import *

class TopFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        city_name_message.message.connect(self.request_by_name)
        self.setObjectName("TopFrame")
        self.setFixedSize(788, 157)
        self.LAYOUT = create_layout(
            orientation = "v",
            spacing = 16,
            content_margins = (16, 16, 16, 16),
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)

        self.TITLE_FRAME = qt_widgets.QFrame(parent = self)

        self.LAYOUT.addWidget(self.TITLE_FRAME)

        self.TITLE_FRAME.setFixedSize(756, 27)
        self.TITLE_FRAME_LAYOUT = create_layout(
            orientation = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.TITLE_FRAME.setLayout(self.TITLE_FRAME_LAYOUT)

        self.TITLE_FRAME_LABEL = qt_widgets.QLabel(text = "Погода до кінця дня", parent = self.TITLE_FRAME)
        self.TITLE_FRAME_LAYOUT.addWidget(self.TITLE_FRAME_LABEL)

        self.TITLE_FRAME_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.TITLE_FRAME_LAYOUT.addWidget(self.LINE_FRAME)
        self.LINE_FRAME.setFixedSize(756, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
        
        self.CONTENT_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.CONTENT_FRAME)
        self.CONTENT_FRAME.setFixedSize(756, 82)
        self.CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "h",
            spacing = 14,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)


        self.LEFT_SCROLL_BUTTON = qt_widgets.QPushButton(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.LEFT_SCROLL_BUTTON)
        self.LEFT_SCROLL_BUTTON.setFixedSize(40, 82)
        self.LEFT_SCROLL_BUTTON.setStyleSheet("padding-right: 24px;")
        self.LEFT_SCROLL_BUTTON.setIcon(qt_gui.QIcon("media/chevrones/chevron_left.svg"))

        self.LEFT_SCROLL_BUTTON.clicked.connect(lambda: self.SCROLL.setValue(self.SCROLL.minimum()))

        self.SCROLL_CONTAINER = TopFrameScroll(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.SCROLL_CONTAINER)
 
        self.RIGHT_SCROLL_BUTTON = qt_widgets.QPushButton(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.RIGHT_SCROLL_BUTTON)
        self.RIGHT_SCROLL_BUTTON.setFixedSize(40, 82)
        self.RIGHT_SCROLL_BUTTON.setStyleSheet("padding-left: 24px;")
        self.RIGHT_SCROLL_BUTTON.setIcon(qt_gui.QIcon("media/chevrones/chevron_right.svg"))

        self.RIGHT_SCROLL_BUTTON.clicked.connect(lambda: self.SCROLL.setValue(self.SCROLL.maximum()))

        self.SCROLL = self.SCROLL_CONTAINER.SCROLL_AREA.horizontalScrollBar()
    
    def wheelEvent(self, event: qt_gui.QWheelEvent):
       
        delta = event.angleDelta().y()
    
        step = self.SCROLL.singleStep() * (delta // 120) # 120 - mouseWheel step value 

        self.SCROLL.setValue(self.SCROLL.value() - step)
        
        event.accept()
    
    def create_content(self, data: dict):
        self.SCROLL.setValue(self.SCROLL.minimum())
        clear_layout(self.SCROLL_CONTAINER.SCROLL_FRAME_LAYOUT)
        number = 1
        for hourly_forecast in data["list"]:
            card = WeatherCard(parent = self.SCROLL_CONTAINER.SCROLL_FRAME)
            dt_utc = datetime.fromtimestamp(hourly_forecast['dt'], tz=timezone.utc)
            local_time = dt_utc + timedelta(seconds = data["city"]["timezone"])
            hour = local_time.hour
            card.TIME_LABEL.setText(f"{hour}")
           
            card.ICON.load(f"media/scroll_icons/{hourly_forecast["weather"][0]["icon"]}.svg")
            card.TEMPERATURE_LABEL.setText(f"{int(hourly_forecast["main"]["temp"])}°")
            self.SCROLL_CONTAINER.SCROLL_FRAME_LAYOUT.addWidget(card)
            number += 1

    def request_by_name(self, city_name):
        self.HOURLY_FORECAST = WeatherLoader(
            api_request_link = f"https://api.openweathermap.org/data/2.5/forecast/hourly?units=metric&q={city_name}&mode=json&appid={API_KEY}&cnt=24"
            )
        self.HOURLY_FORECAST.received_dict.connect(self.create_content) 
        self.HOURLY_FORECAST.start()

            