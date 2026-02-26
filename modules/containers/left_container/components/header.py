import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui


from modules import app_obj

from utils import *

class LeftContainerHeader(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        self.MAIN_WINDOW = self.window()
        self.SWITCH = False

        self.setFixedSize(330, 44)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 10, 0, 10), 
            alignment = core.Qt.AlignmentFlag.AlignRight
        )

        self.setLayout(self.LAYOUT)

        self.SWITCH_BUTTON = qt_widgets.QToolButton(parent = self)

        self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_dark.svg")
        
        self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
        self.SWITCH_BUTTON.setStyleSheet("border: none")

        icon_size = core.QSize(52,24)
        self.SWITCH_BUTTON.setIconSize(icon_size)

        self.SWITCH_BUTTON.clicked.connect(self.switch)

        self.LAYOUT.addWidget(self.SWITCH_BUTTON)

    def switch(self):
        if self.SWITCH == False:
            self.SWITCH = True
            self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_light.svg")
            self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.setProperty("style", "light")
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.style().unpolish(self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU)
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.style().polish(self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU)
            self.MAIN_WINDOW.CENTRAL_WIDGET.setProperty("style", "light")
            self.MAIN_WINDOW.CENTRAL_WIDGET.style().unpolish(self.MAIN_WINDOW.CENTRAL_WIDGET)
            self.MAIN_WINDOW.CENTRAL_WIDGET.style().polish(self.MAIN_WINDOW.CENTRAL_WIDGET)

        elif self.SWITCH == True:
            self.SWITCH = False
            self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_dark.svg")
            self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.setProperty("style", "dark")
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.style().unpolish(self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU)
            self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.style().polish(self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU)
            self.MAIN_WINDOW.CENTRAL_WIDGET.setProperty("style", "dark")
            self.MAIN_WINDOW.CENTRAL_WIDGET.style().unpolish(self.MAIN_WINDOW.CENTRAL_WIDGET)
            self.MAIN_WINDOW.CENTRAL_WIDGET.style().polish(self.MAIN_WINDOW.CENTRAL_WIDGET)
          


