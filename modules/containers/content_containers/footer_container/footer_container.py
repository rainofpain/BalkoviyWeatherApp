import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from .footer_container_components import BottomFrame, TopFrame

from utils import *

class FooterContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setFixedSize(788, 364)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setLayout(self.LAYOUT)
        
        self.TOP_FRAME = TopFrame(parent = self)
        
        self.LAYOUT.addWidget(self.TOP_FRAME)
        
        self.BOTTOM_FRAME = BottomFrame(parent = self)

        self.LAYOUT.addWidget(self.BOTTOM_FRAME)
        
        
        