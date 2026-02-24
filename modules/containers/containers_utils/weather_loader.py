import PyQt6.QtCore as core
from utils import *

class WeatherLoader(core.QThread):
    filtered_dict = core.pyqtSignal(dict)
    received_dict = core.pyqtSignal(dict)

    def __init__(self, api_request_link: str = ""):
        super().__init__()
        self.api_request_link = api_request_link
    def run(self):
        data = api_request(self.api_request_link)
        self.received_dict.emit(data)

        filtered_data = create_city_dict(data)
        if isinstance(filtered_data, dict):
            self.filtered_dict.emit(filtered_data)
        else:
            self.filtered_dict.emit({"cod": filtered_data})

