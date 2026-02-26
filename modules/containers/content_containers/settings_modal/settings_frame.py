import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *
from .components import SettingsContentArea

class SettingsFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.HEADER_CONTAINER = self.parent()
        self.MAIN_WINDOW = self.window()
        self.setObjectName("SettingsContainer")
        self.setFixedSize(790, 688)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 34, 
            content_margins = (24, 20, 24, 20), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setStyleSheet(
            """
            #SettingsContainer{ 
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
            }
           
            """
            )
        self.setLayout(self.LAYOUT)
        
        self.TITLE_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.TITLE_FRAME)
        self.TITLE_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 550, 
            content_margins = (0, 2, 0, 2), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.TITLE_FRAME.setFixedSize(742, 28)

        self.TITLE_FRAME.setLayout(self.TITLE_FRAME_LAYOUT)

        self.TITLE_LABEL = qt_widgets.QLabel("Налаштування",parent = self.TITLE_FRAME)
        self.TITLE_FRAME_LAYOUT.addWidget(self.TITLE_LABEL)
        self.TITLE_LABEL.setStyleSheet("font-size: 24px; font-weight: 500;")

        self.CROSS_BUTTON = qt_widgets.QPushButton(parent = self.TITLE_FRAME)
        self.TITLE_FRAME_LAYOUT.addWidget(self.CROSS_BUTTON)
        self.CROSS_BUTTON.setIcon(qt_gui.QIcon("media/cross.svg"))
        self.CROSS_BUTTON.clicked.connect(self.close_modal)
        self.CROSS_BUTTON.setFixedSize(24, 24)
        self.CROSS_BUTTON.setIconSize(core.QSize(24, 24))

        self.SETTING_CONTENT_AREA = SettingsContentArea(parent = self)
        self.LAYOUT.addWidget(self.SETTING_CONTENT_AREA)
    
    def close_modal(self):
        self.hide()
        self.HEADER_CONTAINER.WEATHER_INFO_FRAME.show()
        # self.MAIN_WINDOW.SHADOW_MASK_FRAME.hide()