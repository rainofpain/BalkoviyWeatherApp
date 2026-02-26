import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from .components import CityInputFrame

class SearchCityContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(544, 578)
        self.LAYOUT = create_layout(
            orientation  = "v",
            spacing = 24,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.setLayout(self.LAYOUT)

        self.TOP_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.TOP_FRAME)
        self.TOP_FRAME.setFixedSize(544, 301)
        self.TOP_FRAME_LAYOUT = create_layout(
            orientation  = "h",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.TOP_FRAME.setLayout(self.TOP_FRAME_LAYOUT)


        self.CITY_INPUT_FRAME = CityInputFrame(parent = self.TOP_FRAME)
        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_INPUT_FRAME)
        


        self.BOTTOM_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.BOTTOM_FRAME)
        self.BOTTOM_FRAME.setFixedSize(544, 197)
        self.BOTTOM_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.BOTTOM_FRAME.setLayout(self.BOTTOM_FRAME_LAYOUT)