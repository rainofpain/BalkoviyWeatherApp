import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from .components import SettingsContentContainer, SettingsMenuContainer

class SettingsContentArea(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(742, 578)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 24, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)

        self.CONTENT_CONTAINER = SettingsContentContainer(parent = self) # create ContentContainer
        
        self.MENU_CONTAINER = SettingsMenuContainer(parent = self)
        self.LAYOUT.addWidget(self.MENU_CONTAINER)

        self.LAYOUT.addWidget(self.CONTENT_CONTAINER) # add ContentContainer


        

