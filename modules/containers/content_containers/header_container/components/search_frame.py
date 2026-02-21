import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtSvgWidgets as qt_svg

from utils import *


class SearchFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(261, 36)
        self.setObjectName("SearchFrame")
        self.LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (8, 6, 8, 7),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)
        self.setStyleSheet(
            """
            #SearchFrame {
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
            }
            """
        )
        self.ICON_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.ICON_FRAME)
        self.ICON_FRAME_LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.ICON_FRAME.setLayout(self.ICON_FRAME_LAYOUT)
        self.ICON_FRAME.setFixedSize(25, 22)
        self.ICON_FRAME.setStyleSheet("padding-left: 3px; padding-top: 1px; margin-top: 1px;")
        self.ICON = qt_svg.QSvgWidget("media/search_icon.svg", parent = self.ICON_FRAME)
        self.ICON_FRAME_LAYOUT.addWidget(self.ICON)
        self.ICON.renderer().setAspectRatioMode(core.Qt.AspectRatioMode.KeepAspectRatio)

        self.SEARCH_FIELD = qt_widgets.QLineEdit(parent = self)
        self.SEARCH_FIELD.setStyleSheet("border:none; font-size: 16px; color: rgba(255, 255, 255, 1);")
        self.LAYOUT.addWidget(self.SEARCH_FIELD)
        self.SEARCH_FIELD.setFixedSize(220, 22)
        self.SEARCH_FIELD.setPlaceholderText("Пошук")
        self.SEARCH_FIELD.textChanged.connect(self.show_clear_button)

        self.CLEAR_BUTTON = qt_widgets.QPushButton(parent = self)
        self.LAYOUT.addWidget(
            self.CLEAR_BUTTON, 
            alignment = core.Qt.AlignmentFlag.AlignAbsolute| core.Qt.AlignmentFlag.AlignRight
            )
        self.CLEAR_BUTTON.hide()
        self.CLEAR_BUTTON.setIcon(qt_gui.QIcon("media/clear.svg"))
        self.CLEAR_BUTTON.setFixedSize(20, 22)
        self.CLEAR_BUTTON.setStyleSheet("margin-top: 2px; border: none;")
        
        self.CLEAR_BUTTON.clicked.connect(self.clear_search)

    def show_clear_button(self):
        if self.SEARCH_FIELD.text() != "":
            self.CLEAR_BUTTON.show()
            self.CLEAR_BUTTON.clicked.connect(self.clear_search)
        else:
            self.CLEAR_BUTTON.hide()
    
    def clear_search(self):
        self.SEARCH_FIELD.setText("")
        self.CLEAR_BUTTON.hide()
       