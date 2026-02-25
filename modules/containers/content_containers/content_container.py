import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from . import MainContainer, FooterContainer, HeaderContainer


class ContentContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setObjectName("ContentContainer")
        self.setFixedSize(828, 800)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 20, 
            content_margins = (20, 20, 20, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)
        
        self.HEADER = HeaderContainer(parent = self)
        self.HEADER.setObjectName("Header")
        self.LAYOUT.addWidget(self.HEADER)

        self.WEATHER_INFO_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.WEATHER_INFO_FRAME)
        self.WEATHER_INFO_FRAME.setFixedSize(788, 677)
        self.WEATHER_INFO_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.WEATHER_INFO_FRAME.setLayout(self.WEATHER_INFO_FRAME_LAYOUT)
       
        
        self.MAIN = MainContainer(parent = self.WEATHER_INFO_FRAME)
        self.MAIN.setObjectName("Main")
        self.WEATHER_INFO_FRAME_LAYOUT.addWidget(self.MAIN)

        self.FOOTER = FooterContainer(parent = self.WEATHER_INFO_FRAME)
        self.FOOTER.setObjectName("Footer") 
        self.WEATHER_INFO_FRAME_LAYOUT.addWidget(self.FOOTER)

        