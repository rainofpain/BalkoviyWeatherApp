import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
from config import API_KEY

from utils import *

class TopFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setObjectName("TopFrame")
        self.setFixedSize(788, 157)