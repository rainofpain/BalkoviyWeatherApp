import PyQt6.QtCore as core

class CityNameMessage(core.QObject):
    message = core.pyqtSignal(str)
    city_name = core.pyqtSignal(str)

    def __init__(self):
        super().__init__()

city_name_message = CityNameMessage()