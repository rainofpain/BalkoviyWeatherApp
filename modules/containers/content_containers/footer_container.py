import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class FooterContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)
        
        self.setFixedSize(788, 364)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.setStyleSheet('background-color: gray; ')
        self.setLayout(self.LAYOUT)
        
        self.TOP_FRAME = qt_widgets.QFrame(parent = self)
        self.TOP_FRAME.setFixedSize(788, 157)
        self.LAYOUT.addWidget(self.TOP_FRAME)
        
        self.DOWN_FRAME = qt_widgets.QFrame(parent = self)
        self.DOWN_FRAME.setStyleSheet("background-color: green; ")
        self.DOWN_FRAME.setFixedSize(788, 197)
        self.DOWN_FRAME_LAYOUT = create_layout(
            orientation = "v",
            content_margins = (16, 16, 16, 16),
            spacing = 16,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.DOWN_FRAME.setLayout(self.DOWN_FRAME_LAYOUT)
        self.LAYOUT.addWidget(self.DOWN_FRAME)
        
        
        self.FORECAST_LABEL = qt_widgets.QLabel(parent = self.DOWN_FRAME, text = "Прогноз на 12 годин")
        self.FORECAST_LABEL.setStyleSheet("font-size: 16px; font-weight: 500; color: #FFF; ")
        self.DOWN_FRAME_LAYOUT.addWidget(self.FORECAST_LABEL)
        
        
        self.GRAPH_CONTENT_FRAME = qt_widgets.QFrame(parent = self.DOWN_FRAME)
        self.GRAPH_CONTENT_FRAME.setFixedSize(758, 130)
        self.GRAPH_CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "v",
            content_margins = (0, 0, 0, 0),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.GRAPH_CONTENT_FRAME.setLayout(self.GRAPH_CONTENT_FRAME_LAYOUT)
        self.DOWN_FRAME_LAYOUT.addWidget(self.GRAPH_CONTENT_FRAME)
        
        
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
        self.LEFT_FRAME.setStyleSheet(f"background: url({graph_bg_path}); ")
        self.LEFT_FRAME.setFixedSize(755, 106)
        self.LEFT_FRAME_LAYOUT = create_layout(
            orientation = "h",
            content_margins = (0, 0, 0, 0),
            spacing = 3,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.LEFT_FRAME.setLayout(self.LEFT_FRAME_LAYOUT)
        self.GRAPH_FRAME_LAYOUT.addWidget(self.LEFT_FRAME)
        
        data_dict = api_request("Dnipro")
        
        for col in data_dict["list"]:
            temp = int(col["main"]["temp"])
        
        
        self.RIGHT_FRAME = qt_widgets.QFrame(parent = self.GRAPH_FRAME)
        self.RIGHT_FRAME.setFixedSize(22, 106)
        self.RIGHT_FRAME_LAYOUT = create_layout(
            orientation = "v",
            content_margins = (0, 0, 0, 0),
            spacing = 0,
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.RIGHT_FRAME.setLayout(self.RIGHT_FRAME_LAYOUT)
        self.GRAPH_FRAME_LAYOUT.addWidget(self.RIGHT_FRAME)
