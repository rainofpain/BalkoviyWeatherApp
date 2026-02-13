import PyQt6.QtCore as core
from utils import create_city_dict

class WeatherLoader(core.QThread):
    finished = core.pyqtSignal(dict)  

    def __init__(self, city_name):
        super().__init__()
        self.city_name = city_name

    def run(self):
        
        data = create_city_dict(self.city_name)
        self.finished.emit(data)

