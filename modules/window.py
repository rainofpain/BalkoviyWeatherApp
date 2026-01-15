import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtWebEngineWidgets as web_engine

from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageFilter

import folium
import io

from .app import app_obj
from utils import *


class MainWindow(qt_widgets.QMainWindow):
    def __init__(self, w, h):
        super().__init__()
        
        
        #data_dict = api_request("Dnipro")
        
        # write_json(data_dict, "static/json/city_data.json")
        data_dict = read_json("static/json/city_data.json")
        
        self.WINDOW_WIDTH = w
        self.WINDOW_HEIGHT = h
        
        
        screen = app_obj.primaryScreen()
        screen_size = screen.size()
        
        self.SCREEN_WIDTH = screen_size.width()
        self.SCREEN_HEIGHT = screen_size.height()
        
        self.MAIN_WINDOW_SIZE = core.QSize(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)
        
        self.CENTER_X = (self.SCREEN_WIDTH // 2) - (self.WINDOW_WIDTH // 2)
        self.CENTER_Y = (self.SCREEN_HEIGHT // 2) - (self.WINDOW_HEIGHT // 2)
        
        
        self.setGeometry(
            self.CENTER_X, 
            self.CENTER_Y, 
            self.WINDOW_WIDTH,
            self.WINDOW_HEIGHT
        )
        self.setWindowTitle("Weather forecast")
        self.setStyleSheet("background-color: transparent; ")
        
        
        self.CENTRAL_WIDGET = qt_widgets.QWidget(parent = self)
        self.CENTRAL_WIDGET.setStyleSheet('background-color: transparent; ')
        self.CENTRAL_WIDGET.setFixedSize(self.MAIN_WINDOW_SIZE)
        
        self.CENTRAL_WIDGET_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignCenter
        )
        
        
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)
        
        
        cat_image = Image.open("media/cat.png")
        cat_image = cat_image.rotate(90)
        
        # Фільтри зображення
        cat_image = cat_image.filter(ImageFilter.BLUR)
        
        qt_image = ImageQt(cat_image)
        
        self.TEXT_LABEL = qt_widgets.QLabel(parent = self.CENTRAL_WIDGET, text = "HEllo world")
        
        image_widget = qt_gui.QImage(qt_image)
        pixmap = qt_gui.QPixmap(image_widget)
        
        pixmap = pixmap.scaled(200, 200)
        self.TEXT_LABEL.setPixmap(pixmap)
        
        self.TEXT_LABEL.setStyleSheet("""
            font-size: 36px;
            font-weight: 500;
            font-style: italic;
        """)
        
        
        self.PRINT_JSON_LABEL = qt_widgets.QLabel(parent = self.CENTRAL_WIDGET, text = f"{data_dict["weather"][0]["main"]}, {round(data_dict["main"]["temp"])}")
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.PRINT_JSON_LABEL)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.TEXT_LABEL)
        
        self.BUTTON = qt_widgets.QPushButton(parent = self.CENTRAL_WIDGET, text = "Push!")
        self.BUTTON.setStyleSheet("""
            border: 3px solid rgba(1, 2, 3, 0.5); 
            border-radius: 5px; 
        """)
        self.BUTTON.clicked.connect(self.button_click)
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.BUTTON)
        
        
        # self.INPUT1 = qt_widgets.QLineEdit(parent = self.CENTRAL_WIDGET)
        # self.INPUT1.setPlaceholderText("Placeholder")
        # self.CENTRAL_WIDGET_LAYOUT.addWidget(self.INPUT1)
        
        # self.INPUT1.textChanged.connect(self.input_text_changed)
        
        
        self.DROPDOWN_MENU = qt_widgets.QComboBox(parent = self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.DROPDOWN_MENU)
        
        self.DROPDOWN_MENU.addItem("OPtion1")
        self.DROPDOWN_MENU.addItem("OPtion2")
        self.DROPDOWN_MENU.addItem(qt_gui.QIcon("media/cat.png"), "12345")
        
        
        # Radio button
        self.BUTTON_GROUP = qt_widgets.QButtonGroup(parent = self.CENTRAL_WIDGET)
        
        radio_button1 = qt_widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "Another")
        radio_button2 = qt_widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "Hello")
        radio_button3 = qt_widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "123")
        
        self.BUTTON_GROUP.addButton(radio_button1)
        self.BUTTON_GROUP.addButton(radio_button2)
        self.BUTTON_GROUP.addButton(radio_button3)
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button1)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button2)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button3)
        
        
        # Checkbox
        self.CHECKBOX_BUTTON_GROUP = qt_widgets.QButtonGroup(parent = self.CENTRAL_WIDGET)
        self.CHECKBOX_BUTTON_GROUP.setExclusive(False)
        
        self.CHECKBOX1 = qt_widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Main")
        checkbox2 = qt_widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Additional1")
        checkbox3 = qt_widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Additional2")
        
        self.CHECKBOX_BUTTON_GROUP.addButton(checkbox2)
        self.CHECKBOX_BUTTON_GROUP.addButton(checkbox3)
        
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CHECKBOX1)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(checkbox2)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(checkbox3)
    
    
    def button_click(self):
        
        # Shadow modal
        self.SHADOW_MODAL = qt_widgets.QWidget(parent = self)
        self.SHADOW_MODAL.setGeometry(
            (self.WINDOW_WIDTH // 2) - 395, 
            (self.WINDOW_HEIGHT // 2) - 344, 
            790, 
            688
        )
        self.SHADOW_MODAL.setStyleSheet("background-color: #FFF; border-radius: 10px; ")
        
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
    
    
    def mousePressEvent(self, event: qt_gui.QMouseEvent):
        
        if event.button() == core.Qt.MouseButton.LeftButton:
            print("Left button clicked")
    
    
    def mouseMoveEvent(self, event: qt_gui.QMouseEvent):
        
        self.setMouseTracking(False)
        
        print(event.position().toPoint())
    
    
    def mouseReleaseEvent(self, event: qt_gui.QMouseEvent):
        
        if event.button() == core.Qt.MouseButton.LeftButton:
            print("Left button released")
    
    
    def keyPressEvent(self, event: qt_gui.QKeyEvent):
        key = event.key()
        text = event.text()
        print(text, key)
        
        if key == core.Qt.Key.Key_Return or key == core.Qt.Key.Key_Enter:
            print("Enter")

main_window = MainWindow(w = 1280, h = 800)

