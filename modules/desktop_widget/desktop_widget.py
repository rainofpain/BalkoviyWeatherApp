import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtSvgWidgets as svg_widgets

from config import API_KEY, path_to_image_list

from ..app import app_obj

from utils import *

class DesktopWidget(qt_widgets.QWidget):

    def __init__(self, w, h):
        super().__init__()
        
        self.WINDOW_MOVING = False
        self.CURRENT_CITY_DICT = {}

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
            self.WINDOW_WIDTH + 10,
            self.WINDOW_HEIGHT + 10
        )

        shadow = qt_widgets.QGraphicsDropShadowEffect()
        
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        
        shadow.setBlurRadius(5)
        
        shadow.setColor(qt_gui.QColor(0, 0, 0))
        
        self.CENTRAL_WIDGET = qt_widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setObjectName("CentralWidget")
        self.CENTRAL_WIDGET.setProperty("style", "dark")
        self.CENTRAL_WIDGET.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.CENTRAL_WIDGET.setGraphicsEffect(shadow)
        
        self.CENTRAL_WIDGET_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 6, 
            content_margins = (14, 14, 14, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
        )
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)

        self.HEADER = qt_widgets.QFrame(parent = self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.HEADER)

        self.HEADER_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignVCenter
        )
        self.HEADER.setLayout(self.HEADER_LAYOUT)

        self.HEADER.setFixedSize(220, 31)

        self.HEADER_LABEL_FRAME = qt_widgets.QFrame(parent = self.HEADER)
        self.HEADER_LAYOUT.addWidget(self.HEADER_LABEL_FRAME, alignment = core.Qt.AlignmentFlag.AlignLeft)

        self.HEADER_LABEL_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 7, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.HEADER_LABEL_FRAME.setLayout(self.HEADER_LABEL_FRAME_LAYOUT)

        self.HEADER_LABEL_FRAME.setFixedSize(108, 19)

        self.ARROW = svg_widgets.QSvgWidget("media/navigation.svg", parent = self.HEADER_LABEL_FRAME)
        self.HEADER_LABEL_FRAME_LAYOUT.addWidget(self.ARROW)
        self.ARROW.setFixedSize(11, 11)

        self.HEADER_LABEL_TEXT = qt_widgets.QLabel(parent = self.HEADER_LABEL_FRAME)
        self.HEADER_LABEL_FRAME_LAYOUT.addWidget(self.HEADER_LABEL_TEXT)

        self.HEADER_LABEL_TEXT.setStyleSheet("font-size: 11px; font-weight: 500;")
        self.HEADER_LABEL_TEXT.setText("Поточна позиція")

        self.UPDATE_BUTTON = qt_widgets.QPushButton(parent = self.HEADER)

        self.HEADER_LAYOUT.addWidget(self.UPDATE_BUTTON, alignment = core.Qt.AlignmentFlag.AlignRight)

        self.UPDATE_BUTTON.setIcon(qt_gui.QIcon("media/reload.svg"))
        self.UPDATE_BUTTON.setFixedSize(31, 31)
        self.UPDATE_BUTTON.setIconSize(core.QSize(17, 17))
        self.UPDATE_BUTTON.setStyleSheet("border-radius: 6px; background-color: rgba(0, 0, 0, 0.2);")
        self.UPDATE_BUTTON.clicked.connect(self.update_widget)

        self.CONTENT_FRAME = qt_widgets.QFrame(parent = self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CONTENT_FRAME)

        self.CONTENT_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 17, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.CONTENT_FRAME.setLayout(self.CONTENT_FRAME_LAYOUT)

        self.CONTENT_FRAME.setFixedSize(189, 180)

        self.CITY_NAME = qt_widgets.QLabel(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.CITY_NAME)
        self.CITY_NAME.setStyleSheet("font-size: 31px; font-weight: 500;")

        self.CURRENT_WEATHER_FRAME = qt_widgets.QFrame(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.CURRENT_WEATHER_FRAME)
        self.CURRENT_WEATHER_FRAME_LAYOUT = create_layout(
            orientation = "h", 
            spacing = 6, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignVCenter
        )
        self.CURRENT_WEATHER_FRAME.setLayout(self.CURRENT_WEATHER_FRAME_LAYOUT)
        self.CURRENT_WEATHER_FRAME.setFixedSize(140, 62)

        self.WEATHER_ICON = svg_widgets.QSvgWidget(parent = self.CURRENT_WEATHER_FRAME)
        self.CURRENT_WEATHER_FRAME_LAYOUT.addWidget(self.WEATHER_ICON)
        self.WEATHER_ICON.setFixedSize(54, 54)

        self.CURRENT_TEMP_LABEL = qt_widgets.QLabel(parent = self.CURRENT_WEATHER_FRAME)
        self.CURRENT_WEATHER_FRAME_LAYOUT.addWidget(self.CURRENT_TEMP_LABEL)
        self.CURRENT_TEMP_LABEL.setStyleSheet("font-size: 52px; font-weight: 500;")

        self.WEATHER_DETAILS_FRAME = qt_widgets.QFrame(parent = self.CONTENT_FRAME)
        self.CONTENT_FRAME_LAYOUT.addWidget(self.WEATHER_DETAILS_FRAME)

        self.WEATHER_DETAILS_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 7, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.WEATHER_DETAILS_FRAME.setLayout(self.WEATHER_DETAILS_FRAME_LAYOUT)

        self.WEATHER_DETAILS_FRAME.setFixedSize(189, 47)

        self.WEATHER_DESCRIPTION_LABEL = qt_widgets.QLabel(parent = self.WEATHER_DETAILS_FRAME)
        self.WEATHER_DETAILS_FRAME_LAYOUT.addWidget(self.WEATHER_DESCRIPTION_LABEL)
        self.WEATHER_DESCRIPTION_LABEL.setStyleSheet("font-size: 17px; font-weight: 500;")

        self.MAX_MIN_TEMP_LABEL = qt_widgets.QLabel(parent = self.WEATHER_DETAILS_FRAME)
        self.WEATHER_DETAILS_FRAME_LAYOUT.addWidget(self.MAX_MIN_TEMP_LABEL)
        self.MAX_MIN_TEMP_LABEL.setStyleSheet("font-size: 17px; font-weight: 500;")

    def update_widget(self):
        self.CENTRAL_WIDGET.style().unpolish(self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET.style().polish(self.CENTRAL_WIDGET)
        try:
            from ..window import main_window
            self.APP_LANGUAGE = main_window.APP_LANGUAGE

            self.WEATHER_LOADER = WeatherLoader(
                language = self.APP_LANGUAGE,
                api_request_link = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={self.CURRENT_CITY_DICT["search_name"]}&appid={API_KEY}&lang={self.APP_LANGUAGE}"
            )
            self.WEATHER_LOADER.filtered_dict.connect(self.update_data) 
            self.WEATHER_LOADER.start()
        except:
            print("no data to update")

    def update_data(self, new_data):
        self.CURRENT_CITY_DICT = new_data
        self.CITY_NAME.setText(new_data["name"])
        self.CURRENT_TEMP_LABEL.setText(new_data["temp"])
        self.WEATHER_ICON.load(f"{path_to_image_list[0]}/{new_data["weather_icon"]}.svg")
        self.WEATHER_DESCRIPTION_LABEL.setText(new_data["weather"].capitalize())

        if self.APP_LANGUAGE == "uk":
            self.MAX_MIN_TEMP_LABEL.setText(f"Макс.:{new_data["max_temp"]}, мін.:{new_data["min_temp"]}")
        elif self.window().APP_LANGUAGE == "en":
            self.MAX_MIN_TEMP_LABEL.setText(f"Max.:{new_data['max_temp']}, min.:{new_data['min_temp']}")

    def mousePressEvent(self, event: qt_gui.QMouseEvent):
        
        if event.button() == core.Qt.MouseButton.LeftButton:
            self.CLICK_POSITION = event.position().toPoint()
    
    def mouseMoveEvent(self, event: qt_gui.QMouseEvent):
        
        mouse_move = event.position().toPoint() - self.CLICK_POSITION
        
        self.WINDOW_MOVING = True
        self.move(
            self.x() + mouse_move.x(),
            self.y() + mouse_move.y(),
        )
    
    def mouseReleaseEvent(self, event):
        if event.button() == core.Qt.MouseButton.LeftButton:
            
            if not self.WINDOW_MOVING:
                from ..window import main_window
                main_window.showNormal()
    
            self.WINDOW_MOVING = False

desktop_widget = DesktopWidget(w = 250, h = 250)