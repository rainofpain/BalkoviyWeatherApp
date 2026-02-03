import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *


class TitleBar(qt_widgets.QFrame):
    def __init__(self, parent, window_width: int):
        super().__init__(parent = parent)
        
        self.setFixedSize(window_width, 40)
        
        self.LAYOUT = create_layout(
            orientation = "h",
            content_margins = (10, 0, 10, 0),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)
        
        self.setStyleSheet("background-color: #FFF; ")
        
        
        self.WINDOW = self.window()
        
        self.CROSS_BUTTON = qt_widgets.QToolButton(parent = self)
        cross_icon = qt_gui.QIcon("media/title_bar/Close_Button.svg")
        self.CROSS_BUTTON.setIcon(cross_icon)
        self.CROSS_BUTTON.setStyleSheet("border: none")
        self.CROSS_BUTTON.setFixedSize(24, 24)
        self.CROSS_BUTTON.clicked.connect(self.WINDOW.close)
        
        self.LAYOUT.addWidget(self.CROSS_BUTTON)
        
        
        self.MINIMIZE_BUTTON = qt_widgets.QToolButton(parent = self)
        cross_icon = qt_gui.QIcon("media/title_bar/Minimize_Button.svg")
        self.MINIMIZE_BUTTON.setIcon(cross_icon)
        self.MINIMIZE_BUTTON.setStyleSheet("border: none")
        self.MINIMIZE_BUTTON.setFixedSize(24, 24)
        self.MINIMIZE_BUTTON.clicked.connect(self.WINDOW.showMinimized)
        
        self.LAYOUT.addWidget(self.MINIMIZE_BUTTON)
        
        
        self.MAXIMIZE_BUTTON = qt_widgets.QToolButton(parent = self)
        cross_icon = qt_gui.QIcon("media/title_bar/Maximize_Button.svg")
        self.MAXIMIZE_BUTTON.setIcon(cross_icon)
        self.MAXIMIZE_BUTTON.setStyleSheet("border: none")
        self.MAXIMIZE_BUTTON.setFixedSize(24, 24)
        self.MAXIMIZE_BUTTON.clicked.connect(self.WINDOW.showMaximized)
        
        self.LAYOUT.addWidget(self.MAXIMIZE_BUTTON)
    
    
    def mousePressEvent(self, event: qt_gui.QMouseEvent):
        if event.button() == core.Qt.MouseButton.LeftButton:
            self.CLICK_POSITION = event.position().toPoint()
    
    
    def mouseMoveEvent(self, event: qt_gui.QMouseEvent):
        
        mouse_move = event.position().toPoint() - self.CLICK_POSITION
        
        self.WINDOW.move(
            self.WINDOW.x() + mouse_move.x(),
            self.WINDOW.y() + mouse_move.y(),
        )
