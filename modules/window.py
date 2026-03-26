import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtWebEngineWidgets as web_engine

import folium
import io

from .app import app_obj

from utils import *
from .containers import LeftContainer, ContentContainer, SearchDropdownMenu
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
            0, 
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT + 40
        )

        self.CENTRAL_WIDGET = qt_widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setObjectName("CentralWidget")
        self.CENTRAL_WIDGET.setProperty("style", "dark")
        self.CENTRAL_WIDGET.setMinimumSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT + 40)
        
        self.CENTRAL_WIDGET_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)

        self.SEARCH_DROPDOWN_MENU = SearchDropdownMenu(parent = self)

        self.SEARCH_DROPDOWN_MENU.move(self.WINDOW_WIDTH - 280, 96)
        self.SEARCH_DROPDOWN_MENU.setProperty("style", "dark")
        self.SEARCH_DROPDOWN_MENU.hide()


        self.TITLE_BAR = TitleBar(parent = self.CENTRAL_WIDGET, window_width = self.WINDOW_WIDTH)

        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.TITLE_BAR)

        self.CONTENT_FRAME = qt_widgets.QFrame(parent= self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CONTENT_FRAME)

        self.CONTENT_FRAME.setObjectName("ContentFrame")
        
        self.CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft| core.Qt.AlignmentFlag.AlignTop
        )
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CONTENT_FRAME)

        
        self.LEFT_CONTAINER = LeftContainer(parent = self.CONTENT_FRAME)
        self.LEFT_CONTAINER.setObjectName("LeftContainer")
        self.CONTENT_FRAME_LAYOUT.addWidget(self.LEFT_CONTAINER)
        
        self.CONTENT_CONTAINER = ContentContainer(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.CONTENT_CONTAINER)

main_window = MainWindow(w = 1200, h = 800)

