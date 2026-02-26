import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *

class AppSizeContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

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

        self.INPUT_FIELDS_FRAME = qt_widgets.QFrame(parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME.setFixedSize(239, 112)

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