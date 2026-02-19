import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
from config import API_KEY

from ....containers_utils import city_name_message, WeatherLoader

from utils import *

class BottomFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        city_name_message.message.connect(self.get_name)
        self.setFixedSize(788, 197)
        self.setObjectName("BottomFrame")
        
        self.LAYOUT = create_layout(
            orientation = "v",
            content_margins = (16, 16, 16, 16),
            spacing = 8,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)
        
        
        self.FORECAST_LABEL = qt_widgets.QLabel(parent = self, text = "Прогноз на 12 годин")
        self.FORECAST_LABEL.setStyleSheet("font-size: 16px; font-weight: 500;")
        self.LAYOUT.addWidget(self.FORECAST_LABEL)

        self.LINE_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.LINE_FRAME)
        self.LINE_FRAME.setFixedSize(756, 1)
        self.LINE_FRAME.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);")

        self.GRAPH_CONTENT_FRAME = qt_widgets.QFrame(parent = self)
        self.GRAPH_CONTENT_FRAME.setFixedSize(758, 130)
        self.GRAPH_CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "v",
            content_margins = (0, 0, 0, 0),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.GRAPH_CONTENT_FRAME.setLayout(self.GRAPH_CONTENT_FRAME_LAYOUT)
        self.LAYOUT.addWidget(self.GRAPH_CONTENT_FRAME)
        
        
        self.ICONS_FRAME = qt_widgets.QFrame(parent = self.GRAPH_CONTENT_FRAME)
        self.ICONS_FRAME.setFixedSize(728, 24)
        self.ICONS_FRAME_LAYOUT = create_layout(
            orientation = "h",
            content_margins = (0, 4, 0, 4),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.ICONS_FRAME.setLayout(self.ICONS_FRAME_LAYOUT)
        self.GRAPH_CONTENT_FRAME_LAYOUT.addWidget(self.ICONS_FRAME)
        
        
        self.GRAPH_FRAME = qt_widgets.QFrame(parent = self.GRAPH_CONTENT_FRAME)
        self.GRAPH_FRAME.setFixedSize(755, 106)
        self.GRAPH_FRAME_LAYOUT = create_layout(
            orientation = "h",
            content_margins = (0, 0, 0, 0),
            spacing = 6,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.GRAPH_FRAME.setLayout(self.GRAPH_FRAME_LAYOUT)
        self.GRAPH_CONTENT_FRAME_LAYOUT.addWidget(self.GRAPH_FRAME)
        
        self.LEFT_FRAME = qt_widgets.QFrame(parent = self.GRAPH_FRAME)
        graph_bg_path = create_abspath("media/graph_bg.svg")
        self.LEFT_FRAME.setStyleSheet(
            f"""
            background-image: url({graph_bg_path.replace('\\', '/')}); 
            background-repeat: norepeat;
            """
            )

        self.LEFT_FRAME.setFixedSize(727, 106)
        self.LEFT_FRAME_LAYOUT = create_layout(
            orientation = "h",
            content_margins = (0, 0, 0, 0),
            spacing = 3,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.LEFT_FRAME.setLayout(self.LEFT_FRAME_LAYOUT)
        self.GRAPH_FRAME_LAYOUT.addWidget(self.LEFT_FRAME)
        
        self.RIGHT_FRAME = qt_widgets.QFrame(parent = self.GRAPH_FRAME)
        self.RIGHT_FRAME.setFixedSize(22, 106)
        self.RIGHT_FRAME_LAYOUT = create_layout(
            orientation = "v",
            content_margins = (0, 0, 0, 0),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.RIGHT_FRAME.setLayout(self.RIGHT_FRAME_LAYOUT)

        temp = 25

        for temp_label in range(8):
            temp_label = qt_widgets.QLabel(text = f"{temp}°", parent = self.RIGHT_FRAME)
            temp_label.setStyleSheet("font-size: 12px;")
            self.RIGHT_FRAME_LAYOUT.addWidget(temp_label)
            temp -= 5

        self.GRAPH_FRAME_LAYOUT.addWidget(self.RIGHT_FRAME)

    def get_name(self, city_name):
        
        self.WEATHER_LOADER = WeatherLoader(
            api_request_link = f"https://api.openweathermap.org/data/2.5/forecast/hourly?units=metric&q={city_name}&&mode=json&appid={API_KEY}&cnt=64"
        )
        self.WEATHER_LOADER.received_dict.connect(self.build_graph) 
        self.WEATHER_LOADER.start()

    def build_graph(self, data_dict):

        clear_layout(self.LEFT_FRAME_LAYOUT)
    
        for col in data_dict["list"]: 
            temp = int(col["main"]["temp"])

            if temp < 0:
                height = 30 - ((temp * - 1) * 3)
                
                if temp < -10 or height < 15:
                    height = 15
            elif temp == 0:
                height = 30
            elif temp > 0:
                height = temp * 3 + 30
                if temp > 25:
                    height = 105
          
            graph_frame = qt_widgets.QFrame(parent = self.LEFT_FRAME)
            graph_frame.setStyleSheet("""
                background: qlineargradient(
                    x1: 0 y1: 0,
                    x2: 0 y2: 1,
                    stop:0 rgba(255, 223, 86, 1), stop:1 rgba(135, 206, 250, 1)
                ); 
            """)
            graph_frame.setFixedSize(8, height)
            self.LEFT_FRAME_LAYOUT.addWidget(graph_frame, alignment = core.Qt.AlignmentFlag.AlignBottom)