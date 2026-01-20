import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class MainContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setFixedSize(788, 303)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setStyleSheet('background-color: gray')
        self.setLayout(self.LAYOUT)
