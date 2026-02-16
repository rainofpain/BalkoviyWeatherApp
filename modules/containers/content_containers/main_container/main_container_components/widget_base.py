import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class WidgetBase(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(390, 303)
        
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 16, 
            content_margins = (16, 16, 16, 16), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.setLayout(self.LAYOUT)
    
        self.HEADER = qt_widgets.QFrame(parent = self)
        self.HEADER.setFixedSize(358,27)
        self.HEADER_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 8, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
            )
        self.HEADER.setLayout(self.HEADER_LAYOUT)

        self.HEADER_TITLE = qt_widgets.QFrame(parent = self.HEADER)
        self.HEADER_TITLE.setFixedSize(152, 19)
        self.HEADER_TITLE_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 6, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
            )
        self.HEADER_TITLE.setLayout(self.HEADER_TITLE_LAYOUT)
        
        self.HEADER_LAYOUT.addWidget(self.HEADER_TITLE)

        self.HEADER_LINE_FRAME = qt_widgets.QFrame(parent = self.HEADER)
        self.HEADER_LINE_FRAME.setFixedSize(358, 1)
        self.HEADER_LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
        self.HEADER_LAYOUT.addWidget(self.HEADER_LINE_FRAME)

        self.LAYOUT.addWidget(self.HEADER)
