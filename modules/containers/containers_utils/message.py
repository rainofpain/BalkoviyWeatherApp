import PyQt6.QtCore as core

class Message(core.QObject):
    message = core.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()

city_name_message = Message()
api_link_message = Message()