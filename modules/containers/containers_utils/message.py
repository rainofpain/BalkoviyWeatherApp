import PyQt6.QtCore as core

class Message(core.QObject):
    message = core.pyqtSignal(str)
    update_left_container = core.pyqtSignal(bool)
    update_settings_container = core.pyqtSignal(bool)
    coord = core.pyqtSignal(tuple)
    def __init__(self):
        super().__init__()


set_property = Message()
city_name_message = Message()
search_field_text = Message()
api_link_message = Message()
update_content = Message()
