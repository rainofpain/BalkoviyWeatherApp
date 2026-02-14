import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg

from .main_container_components.widget_base import WidgetBase

from utils import *

class MainContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
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

        self.LAYOUT.addWidget(self.WEATHER_WIDGET)

        self.CLOCK_WIDGET = WidgetBase(parent = self)
        self.CLOCK_WIDGET.setObjectName("ClockWidget")
       
        self.CLOCK_WIDGET_HEADER_TITLE_LABEL = qt_widgets.QLabel(text = "Сьогодні", parent = self.CLOCK_WIDGET.HEADER_TITLE)
        self.CLOCK_WIDGET_HEADER_TITLE_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")
        self.CLOCK_WIDGET.HEADER_TITLE_LAYOUT.addWidget(self.CLOCK_WIDGET_HEADER_TITLE_LABEL)

        self.LAYOUT.addWidget(self.CLOCK_WIDGET)