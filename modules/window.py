import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets
import PyQt6.QtGui as qt_gui

from PIL import Image
from PIL.ImageQt import ImageQt
from PIL import ImageFilter

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
        self.CENTRAL_WIDGET_LAYOUT.setAlignment(core.Qt.AlignmentFlag.AlignCenter)
        
        self.CENTRAL_WIDGET.setLayout(self.CENTRAL_WIDGET_LAYOUT)
        
        
        cat_image = Image.open("media/cat.png")
        cat_image = cat_image.rotate(90)
        
        # Фільтри зображення
        cat_image = cat_image.filter(ImageFilter.BLUR)
        
        qt_image = ImageQt(cat_image)
        
        self.TEXT_LABEL = widgets.QLabel(parent = self.CENTRAL_WIDGET, text = "HEllo world")
        
        image_widget = qt_gui.QImage(qt_image)
        pixmap = qt_gui.QPixmap(image_widget)
        
        pixmap = pixmap.scaled(200, 200)
        self.TEXT_LABEL.setPixmap(pixmap)
        
        self.TEXT_LABEL.setStyleSheet("""
            font-size: 36px;
            font-weight: 500;
            font-style: italic;
        """)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.TEXT_LABEL)
        
        button = widgets.QPushButton(parent = self.CENTRAL_WIDGET, text = "Push!")
        button.setStyleSheet("""
            border: 3px solid rgba(1, 2, 3, 0.5); 
            border-radius: 5px; 
        """)
        button.clicked.connect(self.button_clicked)
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(button)
        
        
        # self.INPUT1 = widgets.QLineEdit(parent = self.CENTRAL_WIDGET)
        # self.INPUT1.setPlaceholderText("Placeholder")
        # self.CENTRAL_WIDGET_LAYOUT.addWidget(self.INPUT1)
        
        # self.INPUT1.textChanged.connect(self.input_text_changed)
        
        
        self.DROPDOWN_MENU = widgets.QComboBox(parent = self.CENTRAL_WIDGET)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.DROPDOWN_MENU)
        
        self.DROPDOWN_MENU.addItem("OPtion1")
        self.DROPDOWN_MENU.addItem("OPtion2")
        self.DROPDOWN_MENU.addItem(qt_gui.QIcon("media/cat.png"), "12345")
        
        self.DROPDOWN_MENU.currentTextChanged.connect(self.button_clicked)
        
        
        # Radio button
        self.BUTTON_GROUP = widgets.QButtonGroup(parent = self.CENTRAL_WIDGET)
        
        radio_button1 = widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "Another")
        radio_button2 = widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "Hello")
        radio_button3 = widgets.QRadioButton(parent = self.CENTRAL_WIDGET, text = "123")
        
        self.BUTTON_GROUP.addButton(radio_button1)
        self.BUTTON_GROUP.addButton(radio_button2)
        self.BUTTON_GROUP.addButton(radio_button3)
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button1)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button2)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(radio_button3)
        
        
        # Checkbox
        self.CHECKBOX_BUTTON_GROUP = widgets.QButtonGroup(parent = self.CENTRAL_WIDGET)
        self.CHECKBOX_BUTTON_GROUP.setExclusive(False)

        self.CHECKBOX1 = widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Main")
        checkbox2 = widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Additional1")
        checkbox3 = widgets.QCheckBox(parent = self.CENTRAL_WIDGET, text = "Additional2")
        
        print(self.CHECKBOX1.checkState())
        
        self.CHECKBOX_BUTTON_GROUP.addButton(checkbox2)
        self.CHECKBOX_BUTTON_GROUP.addButton(checkbox3)
        
        
        self.CENTRAL_WIDGET_LAYOUT.addWidget(self.CHECKBOX1)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(checkbox2)
        self.CENTRAL_WIDGET_LAYOUT.addWidget(checkbox3)
        
        self.CHECKBOX1.toggled.connect(self.checkbox_toggled)
    
    
    def checkbox_toggled(self, state: bool):
        
        button_list = self.CHECKBOX_BUTTON_GROUP.buttons()
        
        for button in button_list:
            button: widgets.QCheckBox
            
            print(button.checkState())
            button.setChecked(state)
    
    
    def button_clicked(self):
        print(self.DROPDOWN_MENU.currentText())
    
    
    def input_text_changed(self):
        print(123)
        


main_window = MainWindow()

