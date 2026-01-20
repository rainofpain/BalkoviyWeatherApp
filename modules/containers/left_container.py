import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class LeftContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setFixedSize(370, 800)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setStyleSheet('background-color: gray')
        self.setLayout(self.LAYOUT)
        
        self.SCROLL_AREA = qt_widgets.QScrollArea(parent = self)
        self.SCROLL_AREA.setWidgetResizable(True)
        self.SCROLL_AREA.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.LAYOUT.addWidget(self.SCROLL_AREA)

        self.SCROLL_FRAME = qt_widgets.QFrame(parent = self.SCROLL_AREA)
        
        self.LAYOUT.addWidget(self.SCROLL_FRAME)
        
        self.SCROLL_AREA.setWidget(self.SCROLL_FRAME)
        
        self.SCROLL_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.SCROLL_FRAME.setLayout(self.SCROLL_FRAME_LAYOUT)
        
        for index in range(20):
            card = qt_widgets.QFrame(parent = self.SCROLL_FRAME)
            card.setFixedSize(330, 90)
            card.setStyleSheet("background-color: green; ")
            
            self.SCROLL_FRAME_LAYOUT.addWidget(card)


