import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *


class HeaderContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setFixedSize(788, 36)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 383, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )

        self.setLayout(self.LAYOUT)
        self.SETTINGS_FRAME = qt_widgets.QFrame(parent = self)
        self.SETTINGS_FRAME.setFixedSize(144, 36)
        self.SETTINGS_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.SETTINGS_FRAME.setLayout(self.SETTINGS_FRAME_LAYOUT)
        self.SETTINGS_BUTTON = qt_widgets.QPushButton(parent = self.SETTINGS_FRAME)
        self.SETTINGS_BUTTON.setFixedSize(36, 36)
        self.SETTINGS_BUTTON.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0.2); 
            border-radius: 4px; 
            image: url(media/settings_icon.svg);
            padding: 10px;
            """
            )
        
        self.SETTINGS_FRAME_LAYOUT.addWidget(self.SETTINGS_BUTTON)

        self.SETTINGS_LABEL = qt_widgets.QLabel(text = "Налаштування", parent = self.SETTINGS_FRAME)
        self.SETTINGS_LABEL.setStyleSheet("font-size: 14px; font-weight: 500;")
        self.SETTINGS_FRAME_LAYOUT.addWidget(self.SETTINGS_LABEL)


        self.LAYOUT.addWidget(self.SETTINGS_FRAME)

        self.SEARCH_WIDGET = qt_widgets.QLineEdit(parent = self)
        self.SEARCH_WIDGET.setFixedSize(261, 36)
        self.SEARCH_WIDGET.setStyleSheet(
            """
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
            font-size: 17px;
            """
            )
        self.SEARCH_WIDGET.setPlaceholderText("Пошук")
        self.SEARCH_WIDGET.addAction(qt_gui.QIcon("media/search_icon.svg"), qt_widgets.QLineEdit.ActionPosition.LeadingPosition)
        self.LAYOUT.addWidget(self.SEARCH_WIDGET)