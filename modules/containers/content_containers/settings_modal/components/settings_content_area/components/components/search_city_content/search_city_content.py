import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from .components import CityInputFrame, AddedCitiesFrame, MapFrame

class SearchCityContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        language_change.message.connect(self.change_language)

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
        self.TOP_FRAME.setFixedSize(544, 320)
        self.TOP_FRAME_LAYOUT = create_layout(
            orientation  = "h",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.TOP_FRAME.setLayout(self.TOP_FRAME_LAYOUT)

        # Create MAP_FRAME
        self.MAP_FRAME = MapFrame(parent = self.TOP_FRAME) 

        # Create CITY_INPUT_FRAME
        self.CITY_INPUT_FRAME = CityInputFrame(parent = self.TOP_FRAME)
        self.TOP_FRAME_LAYOUT.addWidget(self.CITY_INPUT_FRAME)

        # Add MAP_FRAME to Layout
        self.TOP_FRAME_LAYOUT.addWidget(self.MAP_FRAME)
        
        self.BOTTOM_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.BOTTOM_FRAME)
        self.BOTTOM_FRAME.setFixedSize(544, 200)
        self.BOTTOM_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
        )
        self.BOTTOM_FRAME.setLayout(self.BOTTOM_FRAME_LAYOUT)

        self.BOTTOM_FRAME_TITLE = qt_widgets.QLabel(parent = self.BOTTOM_FRAME)
        self.BOTTOM_FRAME_LAYOUT.addWidget(self.BOTTOM_FRAME_TITLE)
        self.BOTTOM_FRAME_TITLE.setStyleSheet("font-size: 18px")

        self.CITIES_FRAME = AddedCitiesFrame(parent = self.BOTTOM_FRAME)
        self.BOTTOM_FRAME_LAYOUT.addWidget(self.CITIES_FRAME)

    def change_language(self, language):
       
        if language == "uk":
            self.BOTTOM_FRAME_TITLE.setText("Додані міста")
        elif language == "en":
            self.BOTTOM_FRAME_TITLE.setText("Added cities")
