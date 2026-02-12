import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from .content_containers import MainContainer, FooterContainer, HeaderContainer


class ContentContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setObjectName("ContentContainer")
        self.setFixedSize(828, 800)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 20, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setLayout(self.LAYOUT)

        self.HEADER = HeaderContainer(parent = self)
        self.HEADER.setObjectName("Header")
        self.LAYOUT.addWidget(self.HEADER)

        self.MAIN = MainContainer(parent = self)
        self.MAIN.setObjectName("Main")
        self.LAYOUT.addWidget(self.MAIN)

        self.FOOTER = FooterContainer(parent = self)
        self.FOOTER.setObjectName("Footer") 
        self.LAYOUT.addWidget(self.FOOTER)

