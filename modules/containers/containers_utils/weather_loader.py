import PyQt6.QtCore as core
from utils import *

class WeatherLoader(core.QThread):
    filtered_dict = core.pyqtSignal(dict)
    recieved_dict = core.pyqtSignal(dict)

    def __init__(self, api_request_link: str = ""):
        super().__init__()
        self.api_request_link = api_request_link
    def run(self):
        data = api_request(self.api_request_link)
        self.recieved_dict.emit(data)

        filtered_data = create_city_dict(data)
        if filtered_data is not None:
            self.filtered_dict.emit(filtered_data)
    

