import PyQt6.QtWidgets as qt_widgets

from utils import *

class SettingsContentContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(544, 578)
        self.LAYOUT = create_layout(
            orientation  = "g",
            spacing = 0,
            content_margins = (0, 0, 0, 0)
        )
        self.setLayout(self.LAYOUT)
