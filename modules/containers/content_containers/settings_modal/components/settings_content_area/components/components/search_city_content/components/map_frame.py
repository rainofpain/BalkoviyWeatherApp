import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtWebEngineWidgets as web_engine
import folium
import io

from utils import *

class MapFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(289, 256)
        self.setStyleSheet("border-radius: 4px;")
        self.LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setLayout(self.LAYOUT)

        self.MAP = folium.Map(
            location = (51.507408, -0.127699),
            zoom_start = 15,
            zoom_control = False,
            attribution_control = False 
            )
        
        self.WEB_VIEW = web_engine.QWebEngineView(parent = self)

        self.LAYOUT.addWidget(self.WEB_VIEW)

        self.WEB_VIEW.setFixedSize(289, 256)

        self.MARKER = folium.Marker(location = (51.507408, -0.127699), icon = None)
        self.MARKER.add_to(self.MAP)
        
        data = io.BytesIO()
        self.MAP.save(data, close_file = False)
        
        data_value = data.getvalue()
        
        self.WEB_VIEW.setHtml(data_value.decode())

        update_content.coord.connect(self.load_map)

    def load_map(self, coord):
        
        self.MAP.location = coord
        self.MARKER.location = coord

        data = io.BytesIO()
        self.MAP.save(data, close_file = False)
        
        data_value = data.getvalue()
        
        self.WEB_VIEW.setHtml(data_value.decode())
        

        
        