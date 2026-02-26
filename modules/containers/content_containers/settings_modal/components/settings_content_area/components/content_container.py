import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class SettingsContentContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(544, 578)
        