import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from .components import WeatherCard, TopFrameScroll
from utils import *

class TopFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setObjectName("TopFrame")
        self.setFixedSize(788, 157)
        self.LAYOUT = create_layout(
            orientation = "v",
            spacing = 16,
            content_margins = (16, 16, 16, 16),
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)

        self.TITLE_FRAME = qt_widgets.QFrame(parent = self)

        self.LAYOUT.addWidget(self.TITLE_FRAME)

        self.TITLE_FRAME.setFixedSize(756, 27)
        self.TITLE_FRAME_LAYOUT = create_layout(
            orientation = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.TITLE_FRAME.setLayout(self.TITLE_FRAME_LAYOUT)

        self.TITLE_FRAME_LABEL = qt_widgets.QLabel(text = "Погода до кінця дня", parent = self.TITLE_FRAME)
        self.TITLE_FRAME_LAYOUT.addWidget(self.TITLE_FRAME_LABEL)

        self.TITLE_FRAME_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.TITLE_FRAME_LAYOUT.addWidget(self.LINE_FRAME)
        self.LINE_FRAME.setFixedSize(756, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")
        
        self.CONTENT_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.CONTENT_FRAME)
        self.CONTENT_FRAME.setFixedSize(756, 82)
        self.CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "h",
            spacing = 14,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)

        self.LEFT_SCROLL_BUTTON = qt_widgets.QPushButton(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.LEFT_SCROLL_BUTTON)
        self.LEFT_SCROLL_BUTTON.setFixedSize(40, 82)
        self.LEFT_SCROLL_BUTTON.setStyleSheet("padding-right: 24px;")
        self.LEFT_SCROLL_BUTTON.setIcon(qt_gui.QIcon("media/chevrones/chevron_left.svg"))

        self.LEFT_SCROLL_BUTTON.setAutoRepeat(True)
        self.LEFT_SCROLL_BUTTON.setAutoRepeatDelay(0)   
        self.LEFT_SCROLL_BUTTON.setAutoRepeatInterval(15)
        self.LEFT_SCROLL_BUTTON.clicked.connect(lambda: self.make_scroll(-5))

        self.SCROLL_CONTAINER = TopFrameScroll(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.SCROLL_CONTAINER)

        for item in range(30):
            item = WeatherCard(parent = self.SCROLL_CONTAINER.SCROLL_FRAME)
            self.SCROLL_CONTAINER.SCROLL_FRAME_LAYOUT.addWidget(item)
        
        self.RIGHT_SCROLL_BUTTON = qt_widgets.QPushButton(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.RIGHT_SCROLL_BUTTON)
        self.RIGHT_SCROLL_BUTTON.setFixedSize(40, 82)
        self.RIGHT_SCROLL_BUTTON.setStyleSheet("padding-left: 24px;")
        self.RIGHT_SCROLL_BUTTON.setIcon(qt_gui.QIcon("media/chevrones/chevron_right.svg"))

        self.RIGHT_SCROLL_BUTTON.setAutoRepeat(True)
        self.RIGHT_SCROLL_BUTTON.setAutoRepeatDelay(0)  
        self.RIGHT_SCROLL_BUTTON.setAutoRepeatInterval(15) 
        self.RIGHT_SCROLL_BUTTON.clicked.connect(lambda: self.make_scroll(5))
   
    def make_scroll(self, step):
        scroll = self.SCROLL_CONTAINER.SCROLL_AREA.horizontalScrollBar()
        scroll.setValue(scroll.value() + step)