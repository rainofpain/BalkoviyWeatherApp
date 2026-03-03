import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtWebEngineWidgets as web_engine
import folium
import io

from .........containers_utils import update_content
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

        update_content.coord.connect(self.load_map)

    def load_map(self, coord):

        clear_layout(self.LAYOUT)

        map = folium.Map(
            location = coord,
            zoom_start = 10,
            zoom_control = False,
            attribution_control = False 
            )
        
        web_view = web_engine.QWebEngineView(parent = self)

        self.LAYOUT.addWidget(web_view)

        web_view.setFixedSize(289, 256)

        path = qt_gui.QPainterPath()
        path.addRoundedRect(0, 0, 289, 256, 4, 4)
        region = qt_gui.QRegion(path.toFillPolygon().toPolygon())
        web_view.setMask(region)
        
        data = io.BytesIO()
        map.save(data, close_file = False)
        
        data_value = data.getvalue()
        
        web_view.setHtml(data_value.decode())
        