import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class AppSizeContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.MAIN_WINDOW = self.window()
        self.NEW_WINDOW_WIDTH = 0
        self.NEW_WINDOW_HEIGHT = 0
        self.setFixedSize(544, 578)
        self.LAYOUT = create_layout(
            orientation  = "v",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop| core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)

        self.OPTIONS_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.OPTIONS_FRAME)
        self.OPTIONS_FRAME.setFixedSize(239, 219)

        self.OPTIONS_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 24,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop| core.Qt.AlignmentFlag.AlignLeft
        )
        self.OPTIONS_FRAME.setLayout(self.OPTIONS_FRAME_LAYOUT)

        self.TITLE_LABEL = qt_widgets.QLabel("Оберіть розмір додатку", parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.TITLE_LABEL)
        self.TITLE_LABEL.setFixedWidth(239)
        self.TITLE_LABEL.setStyleSheet("font-size: 18px; border: none;")
        self.TITLE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignLeft)

        self.SIZE_OPTIONS_BOX = qt_widgets.QFrame(parent = self.OPTIONS_FRAME)
        self.SIZE_OPTIONS_BOX.setFixedSize(239, 112)
        self.SIZE_OPTIONS_BOX_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop| core.Qt.AlignmentFlag.AlignLeft
        )
        self.SIZE_OPTIONS_BOX.setLayout(self.SIZE_OPTIONS_BOX_LAYOUT)

        self.SIZE_OPTIONS_BOX.setStyleSheet(
            """
                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                }
                QRadioButton::indicator:unchecked {
                    image: url(media/radio_button/unchecked.svg);
                }
                QRadioButton::indicator:checked {
                    image: url(media/radio_button/checked.svg);
                }
            """
            )

        self.SIZE_1200X800 = qt_widgets.QRadioButton("1200x800")
        self.SIZE_OPTIONS_BOX_LAYOUT.addWidget(self.SIZE_1200X800)
        self.SIZE_1200X800.clicked.connect(self.resize_window_1200x800)

        self.SIZE_1440x1024 = qt_widgets.QRadioButton("1440x1024")
        self.SIZE_OPTIONS_BOX_LAYOUT.addWidget(self.SIZE_1440x1024)
        self.SIZE_1440x1024.clicked.connect(self.resize_window_1440x1024)

        self.SIZE_1512x982 = qt_widgets.QRadioButton("1512x982")
        self.SIZE_OPTIONS_BOX_LAYOUT.addWidget(self.SIZE_1512x982)
        self.SIZE_1512x982.clicked.connect(self.resize_window_1512x982)

        self.SIZE_1728x1117 = qt_widgets.QRadioButton("1728x1117")
        self.SIZE_OPTIONS_BOX_LAYOUT.addWidget(self.SIZE_1728x1117)
        self.SIZE_1728x1117.clicked.connect(self.resize_window_1728x1117)

        self.OPTIONS_FRAME_LAYOUT.addWidget(self.SIZE_OPTIONS_BOX)

        if self.MAIN_WINDOW.WINDOW_WIDTH == 1200:
            self.SIZE_1200X800.setChecked(True)
        elif self.MAIN_WINDOW.WINDOW_WIDTH == 1440:
            self.SIZE_1440x1024.setChecked(True)
        elif self.MAIN_WINDOW.WINDOW_WIDTH == 1512:
            self.SIZE_1512x982.setChecked(True)
        elif self.MAIN_WINDOW.WINDOW_WIDTH == 1728:
            self.SIZE_1728x1117.setChecked(True)

        self.SAVE_BUTTON = qt_widgets.QPushButton("Зберегти", parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.SAVE_BUTTON)
        self.SAVE_BUTTON.setFixedSize(105, 38)
        self.SAVE_BUTTON.setStyleSheet(
            """
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px;
                color: rgba(255, 255, 255, 1);
                font-size: 14px;
            """
            )
        self.SAVE_BUTTON.clicked.connect(self.save_resize)
    
    def save_resize(self):
        self.MAIN_WINDOW.resize(self.NEW_WINDOW_WIDTH, self.NEW_WINDOW_HEIGHT + 40)
        self.MAIN_WINDOW.CENTRAL_WIDGET.resize(self.NEW_WINDOW_WIDTH, self.NEW_WINDOW_HEIGHT + 40)
        self.MAIN_WINDOW.SEARCH_DROPDOWN_MENU.move(self.NEW_WINDOW_WIDTH - 280, 96)
        self.MAIN_WINDOW.WINDOW_WIDTH = self.NEW_WINDOW_WIDTH
        self.MAIN_WINDOW.WINDOW_HEIGHT = self.NEW_WINDOW_HEIGHT

    def resize_window_1200x800(self):
        self.NEW_WINDOW_WIDTH = 1200
        self.NEW_WINDOW_HEIGHT = 800

    def resize_window_1440x1024(self):
        self.NEW_WINDOW_WIDTH = 1440
        self.NEW_WINDOW_HEIGHT = 1024
    
    def resize_window_1512x982(self):
        self.NEW_WINDOW_WIDTH = 1512
        self.NEW_WINDOW_HEIGHT = 982
    
    def resize_window_1728x1117(self):
        self.NEW_WINDOW_WIDTH = 1728
        self.NEW_WINDOW_HEIGHT = 1117