import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg

from utils import *

class WeatherCard(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setObjectName("WeatherCard")
        self.setFixedSize(45, 82)
        self.LAYOUT = create_layout(
            orientation = "v",
            spacing = 10,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignHCenter
        )
        self.setLayout(self.LAYOUT)

        self.TIME_LABEL = qt_widgets.QLabel(parent = self)
        self.LAYOUT.addWidget(self.TIME_LABEL, alignment = core.Qt.AlignmentFlag.AlignTop)
        self.TIME_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")

        self.ICON = qt_svg.QSvgWidget(parent = self)
        self.ICON.setFixedSize(24, 24)
        self.LAYOUT.addWidget(self.ICON)

        self.TEMPERATURE_LABEL = self.TEMPERATURE_LABEL = qt_widgets.QLabel(parent = self)
        self.LAYOUT.addWidget(self.TEMPERATURE_LABEL, alignment = core.Qt.AlignmentFlag.AlignBottom)
        self.TEMPERATURE_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")