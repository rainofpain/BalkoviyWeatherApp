import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg

from .main_container_components.widget_base import WidgetBase
from ..weather_loader import WeatherLoader
from ..city_name_message import city_name_message

from utils import *

class MainContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        city_name_message.message.connect(self.get_name)
        self.setFixedSize(788, 303)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.setLayout(self.LAYOUT)

        self.WEATHER_WIDGET = WidgetBase(parent = self)
        self.WEATHER_WIDGET.setObjectName("WeatherWidget")

        self.ARROW = qt_svg.QSvgWidget("media/navigation.svg", parent = self.WEATHER_WIDGET.HEADER_TITLE)
        self.ARROW.setFixedSize(16, 16)
        self.WEATHER_WIDGET.HEADER_TITLE_LAYOUT.addWidget(self.ARROW)

        self.WEATHER_WIDGET_HEADER_TITLE_LABEL = qt_widgets.QLabel(text = "Поточна позиція", parent = self.WEATHER_WIDGET.HEADER_TITLE)
        self.WEATHER_WIDGET_HEADER_TITLE_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")
        self.WEATHER_WIDGET.HEADER_TITLE_LAYOUT.addWidget(self.WEATHER_WIDGET_HEADER_TITLE_LABEL)

        self.WEATHER_WIDGET_CONTENT = qt_widgets.QFrame(parent = self.WEATHER_WIDGET)
        self.WEATHER_WIDGET_CONTENT.setFixedSize(358, 228)
        self.WEATHER_WIDGET_CONTENT_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 16, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.WEATHER_WIDGET_CONTENT.setLayout(self.WEATHER_WIDGET_CONTENT_LAYOUT)

        self.CITY_NAME_LABEL = qt_widgets.QLabel(parent = self.WEATHER_WIDGET_CONTENT)
        self.CITY_NAME_LABEL.setStyleSheet("font-size: 44px; font-weight: 500;")
        self.WEATHER_WIDGET_CONTENT_LAYOUT.addWidget(self.CITY_NAME_LABEL, alignment= core.Qt.AlignmentFlag.AlignCenter)

        self.TEMP_FRAME = qt_widgets.QFrame(parent = self.WEATHER_WIDGET_CONTENT)
        self.TEMP_FRAME.setFixedSize(197, 87)
        self.TEMP_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 8, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
            )
        self.TEMP_FRAME.setLayout(self.TEMP_FRAME_LAYOUT)

        self.TEMP_FRAME_ICON = qt_svg.QSvgWidget(parent = self.TEMP_FRAME)
        self.TEMP_FRAME_ICON.setFixedSize(76, 76)
        self.TEMP_FRAME_LAYOUT.addWidget(self.TEMP_FRAME_ICON)

        self.TEMP_FRAME_LABEL = qt_widgets.QLabel(parent = self.TEMP_FRAME)
        self.TEMP_FRAME_LABEL.setStyleSheet("font-size: 74px; font-weight: 500;")
        self.TEMP_FRAME_LAYOUT.addWidget(self.TEMP_FRAME_LABEL)

        self.WEATHER_WIDGET_CONTENT_LAYOUT.addWidget(self.TEMP_FRAME, alignment= core.Qt.AlignmentFlag.AlignCenter)

        self.WEATHER_SUMMARY_FRAME = qt_widgets.QFrame(parent = self.WEATHER_WIDGET_CONTENT)
        self.WEATHER_SUMMARY_FRAME.setFixedSize(259, 57)
        self.WEATHER_SUMMARY_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        
        self.WEATHER_SUMMARY_FRAME.setLayout(self.WEATHER_SUMMARY_FRAME_LAYOUT)

        self.WEATHER_DESCRIPTION_LABEL = qt_widgets.QLabel(parent = self.WEATHER_SUMMARY_FRAME)
        self.WEATHER_DESCRIPTION_LABEL.setStyleSheet("font-size: 24px; font-weight: 500;")
        self.WEATHER_DESCRIPTION_LABEL.setFixedHeight(28)
        self.WEATHER_SUMMARY_FRAME_LAYOUT.addWidget(self.WEATHER_DESCRIPTION_LABEL, alignment= core.Qt.AlignmentFlag.AlignCenter)

        self.MIN_MAX_TEMP_LABEL = qt_widgets.QLabel(parent = self.WEATHER_SUMMARY_FRAME)
        self.MIN_MAX_TEMP_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")
        self.WEATHER_SUMMARY_FRAME_LAYOUT.addWidget(self.MIN_MAX_TEMP_LABEL, alignment= core.Qt.AlignmentFlag.AlignCenter)

        self.WEATHER_WIDGET_CONTENT_LAYOUT.addWidget(self.WEATHER_SUMMARY_FRAME, alignment= core.Qt.AlignmentFlag.AlignCenter)


        self.WEATHER_WIDGET.LAYOUT.addWidget(self.WEATHER_WIDGET_CONTENT)

        self.LAYOUT.addWidget(self.WEATHER_WIDGET)

        self.CLOCK_WIDGET = WidgetBase(parent = self)
        self.CLOCK_WIDGET.setObjectName("ClockWidget")
       
        self.CLOCK_WIDGET_HEADER_TITLE_LABEL = qt_widgets.QLabel(text = "Сьогодні", parent = self.CLOCK_WIDGET.HEADER_TITLE)
        self.CLOCK_WIDGET_HEADER_TITLE_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")
        self.CLOCK_WIDGET.HEADER_TITLE_LAYOUT.addWidget(self.CLOCK_WIDGET_HEADER_TITLE_LABEL)

        self.CLOCK_WIDGET_CONTENT = qt_widgets.QFrame(parent = self.CLOCK_WIDGET)
        self.CLOCK_WIDGET_CONTENT.setFixedSize(358, 228)
        self.CLOCK_WIDGET_CONTENT_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 16, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.CLOCK_WIDGET_CONTENT.setLayout(self.CLOCK_WIDGET_CONTENT_LAYOUT)

        self.DATE_FRAME = qt_widgets.QFrame(parent = self.CLOCK_WIDGET_CONTENT)
        self.DATE_FRAME.setFixedSize(358, 44)
        self.DATE_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 116, 
            content_margins = (8, 0, 8, 0), 
            alignment = core.Qt.AlignmentFlag.AlignJustify
            )
        self.DATE_FRAME.setLayout(self.DATE_FRAME_LAYOUT)

        self.DAY_LABEL = qt_widgets.QLabel(parent = self.DATE_FRAME)
        self.DAY_LABEL.setStyleSheet("font-size: 24px; font-weight: 500;")
        self.DATE_FRAME_LAYOUT.addWidget(self.DAY_LABEL)

        self.DATE_LABEL = qt_widgets.QLabel(parent = self.DATE_FRAME)
        self.DATE_LABEL.setStyleSheet("font-size: 24px; font-weight: 500;")
        self.DATE_FRAME_LAYOUT.addWidget(self.DATE_LABEL)

        self.CLOCK_WIDGET_CONTENT_LAYOUT.addWidget(self.DATE_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)

        self.WATCH_FRAME = qt_widgets.QFrame(parent = self.CLOCK_WIDGET_CONTENT)
        self.WATCH_FRAME.setFixedSize(168, 168)
        self.WATCH_FRAME.setStyleSheet(
            """
            border-radius: 84px; 
            background-color: rgba(0, 0, 0, 0.2); 
            background-image: url(media/ticks.svg); 
            background-repeat: no-repeat;
            background-position: center;
            """
            )
        self.WATCH_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
            )
        self.WATCH_FRAME.setLayout(self.WATCH_FRAME_LAYOUT)

        self.TIME_LABEL = qt_widgets.QLabel(parent = self.WATCH_FRAME)
        self.TIME_LABEL.setStyleSheet("font-size: 29px; font-weight: 500; background-color: transparent;")
        self.WATCH_FRAME_LAYOUT.addWidget(self.TIME_LABEL)
        self.WATCH_FRAME.hide()

        self.CLOCK_WIDGET_CONTENT_LAYOUT.addWidget(self.WATCH_FRAME, alignment = core.Qt.AlignmentFlag.AlignCenter)


        self.CLOCK_WIDGET.LAYOUT.addWidget(self.CLOCK_WIDGET_CONTENT)

        self.LAYOUT.addWidget(self.CLOCK_WIDGET)
    
    def show_data(self, data):
        self.CITY_NAME_LABEL.setText(data["name"])
        self.TEMP_FRAME_LABEL.setText(f"{data["temp"]}")
        self.TEMP_FRAME_ICON.load(f"media/weather_icons/{data["weather_icon"]}.svg")
        self.WEATHER_DESCRIPTION_LABEL.setText(data["weather"].capitalize())
        self.MIN_MAX_TEMP_LABEL.setText(f"Макс.:{data["max_temp"]}, мін.:{data["min_temp"]}")
        self.DAY_LABEL.setText(data["day"])
        self.DATE_LABEL.setText(data["date"])
        self.TIME_LABEL.setText(data["time"])
        self.WATCH_FRAME.show()
        
        

    def get_name(self, city_name):
        self.WEATHER_LOADER = WeatherLoader(city_name = city_name)
        self.WEATHER_LOADER.finished.connect(self.show_data) 
        self.WEATHER_LOADER.start()
