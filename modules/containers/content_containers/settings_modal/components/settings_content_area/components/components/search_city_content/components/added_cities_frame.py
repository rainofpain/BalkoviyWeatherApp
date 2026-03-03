import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from config import city_name_list
from .city_card import CityCard
from .........containers_utils import update_content

class AddedCitiesFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        update_content.update_settings_container.connect(self.update_content)

        self.setFixedSize(544, 160)
        self.setObjectName("AddedCitiesContainer")

        self.setStyleSheet(
            """
            #AddedCitiesContainer{
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 8px;
            }
            """
            )

        self.LAYOUT = create_layout(
                    orientation = "v", 
                    spacing = 0, 
                    content_margins = (16, 16, 16, 16), 
                    alignment = core.Qt.AlignmentFlag.AlignCenter
                )
        self.setLayout(self.LAYOUT)

        self.SCROLL_AREA = qt_widgets.QScrollArea(parent = self)
        self.SCROLL_AREA.setWidgetResizable(True)
        self.SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.SCROLL_AREA.setStyleSheet("border: none;")
        
        self.LAYOUT.addWidget(self.SCROLL_AREA)
        
        self.SCROLL_FRAME = qt_widgets.QFrame(parent = self.SCROLL_AREA)
        
        self.SCROLL_FRAME.setFixedWidth(512)

        self.LAYOUT.addWidget(self.SCROLL_FRAME)
        
        self.SCROLL_AREA.setWidget(self.SCROLL_FRAME)
        
        self.SCROLL_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)

        for city in city_name_list:
                city_card = CityCard(parent = self.SCROLL_FRAME, city_name = city)
                self.SCROLL_FRAME_LAYOUT.addWidget(city_card)

    def update_content(self, update_signal):
        if update_signal == True:
            clear_layout(self.SCROLL_FRAME_LAYOUT)
            for city in city_name_list:
                city_card = CityCard(parent = self.SCROLL_FRAME, city_name = city)
                self.SCROLL_FRAME_LAYOUT.addWidget(city_card)
    


    

    

        
