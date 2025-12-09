import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

from .app import app_obj


class MainWindow(widgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        screen = app_obj.primaryScreen()
        screen_size = screen.size()
        
        self.SCREEN_WIDTH = screen_size.width()
        self.SCREEN_HEIGHT = screen_size.height()
        
        self.MAIN_WINDOW_SIZE = core.QSize(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        
        self.CENTER_X = (self.SCREEN_WIDTH // 2) - (self.SCREEN_WIDTH // 4)
        self.CENTER_Y = (self.SCREEN_HEIGHT // 2) - (self.SCREEN_HEIGHT // 4)
        
        
        self.setGeometry(
            self.CENTER_X, 
            self.CENTER_Y, 
            self.SCREEN_WIDTH // 2, 
            self.SCREEN_HEIGHT // 2
        )
        self.setWindowTitle("Weather forecast")
        self.setStyleSheet("background-color: transparent; ")
        
        
        self.CENTRAL_WIDGET = widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setStyleSheet('background-color: transparent; ')
        self.CENTRAL_WIDGET.setFixedSize(self.MAIN_WINDOW_SIZE)
        
        self.CENTRAL_WIDGET_LAYOUT = widgets.QVBoxLayout()
        self.CENTRAL_WIDGET_LAYOUT.setSpacing(10)
        self.CENTRAL_WIDGET_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CENTRAL_WIDGET_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignRight)
        
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)
        
        self.FRAME1 = widgets.QFrame(parent = self.CENTRAL_WIDGET)
        self.FRAME1.setStyleSheet('background-color: green; ')
        self.FRAME1.setFixedSize(core.QSize(100, 200))
        # self.FRAME1.setSizePolicy(widgets.QSizePolicy.Policy.Expanding, widgets.QSizePolicy.Policy.Fixed)
        
        self.FRAME2 = widgets.QFrame(parent = self.CENTRAL_WIDGET)
        self.FRAME2.setStyleSheet('background-color: red; ')
        self.FRAME2.setFixedSize(core.QSize(100, 200))
        
        self.FRAME3 = widgets.QFrame(parent = self.CENTRAL_WIDGET)
        self.FRAME3.setStyleSheet('background-color: blue; ')
        self.FRAME3.setFixedSize(core.QSize(100, 200))
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.FRAME1)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.FRAME2)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.FRAME3)

main_window = MainWindow()

