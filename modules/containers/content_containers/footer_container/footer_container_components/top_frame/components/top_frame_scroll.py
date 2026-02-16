import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class TopFrameScroll(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setFixedSize(648, 82)
        self.setLayout(self.LAYOUT)
        self.setStyleSheet("border: none;")

        self.SCROLL_AREA = qt_widgets.QScrollArea(parent = self)
        self.LAYOUT.addWidget(self.SCROLL_AREA)
        self.SCROLL_AREA.setWidgetResizable(True)
        self.SCROLL_AREA.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.SCROLL_FRAME = qt_widgets.QFrame(parent = self.SCROLL_AREA)
        self.SCROLL_FRAME.setFixedHeight(82)

        self.LAYOUT.addWidget(self.SCROLL_FRAME)
        
        self.SCROLL_AREA.setWidget(self.SCROLL_FRAME)
        
        self.SCROLL_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 17, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)