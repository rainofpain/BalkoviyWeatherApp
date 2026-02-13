import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtWebEngineWidgets as web_engine

import folium
import io

from .app import app_obj
from utils import *
from .containers import LeftContainer, ContentContainer
from .title_bar import TitleBar


class MainWindow(qt_widgets.QMainWindow):
    def __init__(self, w, h):
        super().__init__()
        
        self.setWindowFlags(core.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(core.Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.WINDOW_WIDTH = w
        self.WINDOW_HEIGHT = h
        
        
        screen = app_obj.primaryScreen()
        screen_size = screen.size()
        
        self.SCREEN_WIDTH = screen_size.width()
        self.SCREEN_HEIGHT = screen_size.height()
        
        self.CENTER_X = (self.SCREEN_WIDTH // 2) - (self.WINDOW_WIDTH // 2)
        self.CENTER_Y = (self.SCREEN_HEIGHT // 2) - (self.WINDOW_HEIGHT // 2)
        
        
        self.setGeometry(
            self.CENTER_X, 
            self.CENTER_Y, 
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT + 40
        )
        self.setWindowTitle("Weather forecast")
        
        self.CENTRAL_WIDGET = qt_widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setObjectName("CentralWidget")

        self.CENTRAL_WIDGET.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT + 40)
        
        self.CENTRAL_WIDGET_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)
        
        self.TITLE_BAR = TitleBar(parent = self.CENTRAL_WIDGET, window_width = self.WINDOW_WIDTH)

        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.TITLE_BAR)

        self.CONTENT_FRAME = qt_widgets.QFrame(parent= self.CENTRAL_WIDGET)

        self.CONTENT_FRAME.setObjectName("ContentFrame")
        
        self.CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CONTENT_FRAME)

        
        self.LEFT_CONTAINER = LeftContainer(parent = self.CONTENT_FRAME)
        self.LEFT_CONTAINER.setObjectName("LeftContainer")
        self.CONTENT_FRAME_LAYOUT.addWidget(self.LEFT_CONTAINER)
        
        self.CONTENT_CONTAINER = ContentContainer(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.CONTENT_CONTAINER)
        
        
       
    
    
    def button_click(self):
        
        # Shadow modal
        self.SHADOW_MODAL = qt_widgets.QWidget(parent = self)
        self.SHADOW_MODAL.setGeometry(
            (self.WINDOW_WIDTH // 2) - 395, 
            (self.WINDOW_HEIGHT // 2) - 344, 
            790, 
            688
        )
        self.SHADOW_MODAL.setStyleSheet("background-color: none; ")
        
        # Shadow
        shadow = qt_widgets.QGraphicsDropShadowEffect()
        
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        
        shadow.setBlurRadius(25)
        
        shadow.setColor(qt_gui.QColor(0, 0, 0))
        
        self.SHADOW_MODAL.setGraphicsEffect(shadow)
        
        self.SHADOW_MODAL.show()
        
        # Main modal
        self.MODAL = qt_widgets.QWidget(parent = self)
        self.MODAL.setGeometry(
            (self.WINDOW_WIDTH // 2) - 395, 
            (self.WINDOW_HEIGHT // 2) - 344, 
            790, 
            688
        )
        self.MODAL.setStyleSheet("background-color: #FFF; border-radius: 10px; ")
        self.MODAL.show()
        
        self.MODAL_LAYOUT = create_layout(
            orientation = "v",
            spacing = 34,
            content_margins = (24, 24, 24, 24),
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        
        self.MODAL.setLayout(self.MODAL_LAYOUT)
        
        self.HEADER = qt_widgets.QFrame(parent = self.MODAL)
        self.HEADER.setFixedSize(core.QSize(742, 28))
        self.HEADER_LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignRight
        )
        self.HEADER.setLayout(self.HEADER_LAYOUT)
        
        self.MODAL_LAYOUT.addWidget(self.HEADER)
        
        self.CROSS_BUTTON = qt_widgets.QPushButton(parent = self.HEADER)
        
        cross_icon = qt_gui.QIcon()
        cross_icon.addFile("media/cross.svg")
        self.CROSS_BUTTON.setIcon(cross_icon)
        self.CROSS_BUTTON.clicked.connect(self.close_modal)
        
        self.HEADER_LAYOUT.addWidget(self.CROSS_BUTTON)
        
        
        self.MAIN = qt_widgets.QFrame(parent = self.MODAL)
        self.MAIN.setFixedSize(core.QSize(742, 578))
        self.MAIN_LAYOUT = create_layout(
            orientation = "h",
            spacing = 24,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        self.MAIN.setLayout(self.MAIN_LAYOUT)
        
        self.MODAL_LAYOUT.addWidget(self.MAIN)
        
        # Minimap
        map = folium.Map(location = (50.45205145776175, 30.50042416456522))
        
        web_view = web_engine.QWebEngineView(parent = self.MAIN)
        web_view.setFixedSize(289, 256)
        self.MAIN_LAYOUT.addWidget(web_view)
        
        data = io.BytesIO()
        map.save(data, close_file = False)
        
        data_value = data.getvalue()
        
        web_view.setHtml(data_value.decode())
    
    
    def close_modal(self):
        self.MODAL.hide()
        self.SHADOW_MODAL.hide()
    
    

main_window = MainWindow(w = 1200, h = 800)

