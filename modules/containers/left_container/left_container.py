import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from .components import InfoCard, LeftContainerHeader
from config import city_name_list, API_KEY, app_language

from utils import *


class LeftContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        language_change.message.connect(self.change_language)
        update_content.update_left_container.connect(self.update_content)
        self.setFixedWidth(375)
        self.setMinimumHeight(800)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (20, 0, 20, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setStyleSheet("border: none")
        
        self.setLayout(self.LAYOUT)

        self.HEADER = LeftContainerHeader(parent = self)

        self.LAYOUT.addWidget(self.HEADER)

        self.SCROLL_AREA = qt_widgets.QScrollArea(parent = self)
        self.SCROLL_AREA.setWidgetResizable(True)
        self.SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.LAYOUT.addWidget(self.SCROLL_AREA)
        
        self.SCROLL_FRAME = qt_widgets.QFrame(parent = self.SCROLL_AREA)
        self.SCROLL_FRAME.setObjectName("LeftContainerScroll")
        
        self.SCROLL_FRAME.setFixedWidth(330)

        self.LAYOUT.addWidget(self.SCROLL_FRAME)
        
        self.SCROLL_AREA.setWidget(self.SCROLL_FRAME)
        
        self.SCROLL_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        

        for city in city_name_list:

            card = InfoCard(
                parent = self.SCROLL_FRAME,
                search_city_name = city
                )
            card.load_weather()
                
            self.SCROLL_FRAME_LAYOUT.addWidget(card, alignment = core.Qt.AlignmentFlag.AlignRight)
        

    def change_language(self):
        for index in range(self.SCROLL_FRAME_LAYOUT.count()):
            item = self.SCROLL_FRAME_LAYOUT.itemAt(index)
            widget = item.widget()
            if widget.CLICKED == True:
                api_link = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={widget.SEARCH_NAME}&appid={API_KEY}&lang={app_language[0]}"
                api_link_message.message.emit(api_link)
                break

    def reset_card_click(self):
        for index in range(self.SCROLL_FRAME_LAYOUT.count()):
            item = self.SCROLL_FRAME_LAYOUT.itemAt(index)
            widget = item.widget()
            widget.CLICKED = False
            widget.ARROW.hide()
            widget.setStyleSheet("background-color: transparent; ")

    def update_content(self, update_signal):
        if update_signal == True:
            clear_layout(self.SCROLL_FRAME_LAYOUT)
            for city in city_name_list:
                card = InfoCard(
                    parent = self.SCROLL_FRAME,
                    search_city_name = city
                    )
                card.load_weather()
                    
                self.SCROLL_FRAME_LAYOUT.addWidget(card, alignment = core.Qt.AlignmentFlag.AlignRight)
        

    
        
            



