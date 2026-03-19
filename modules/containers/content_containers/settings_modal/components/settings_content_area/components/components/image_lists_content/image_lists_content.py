import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *
from config import path_to_image_list
from .image_set import ImageSet

class ImageListsContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        language_change.message.connect(self.change_language)

        self.CHOICE_BUFFER = ""
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
        self.OPTIONS_FRAME.setFixedSize(490, 451)

        self.OPTIONS_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 24,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop| core.Qt.AlignmentFlag.AlignLeft
        )
        self.OPTIONS_FRAME.setLayout(self.OPTIONS_FRAME_LAYOUT)

        self.TITLE_LABEL = qt_widgets.QLabel(parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.TITLE_LABEL)
        self.TITLE_LABEL.setFixedWidth(239)
        self.TITLE_LABEL.setStyleSheet("font-size: 18px; border: none;")
        self.TITLE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignLeft)

        self.ADD_BUTTON = qt_widgets.QPushButton(parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.ADD_BUTTON)
        self.ADD_BUTTON.setFixedSize(96, 36)
        self.ADD_BUTTON.setIcon(qt_gui.QIcon("media/add_btn.svg"))
        self.ADD_BUTTON.setStyleSheet(
            """
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px;
                color: rgba(255, 255, 255, 1);
                font-size: 17px;
            """
            )

        self.IMAGE_SELECTION_FRAME = qt_widgets.QFrame(parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.IMAGE_SELECTION_FRAME)
        self.IMAGE_SELECTION_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 10,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop
        )

        self.IMAGE_SET_1 = ImageSet(parent = self.IMAGE_SELECTION_FRAME, path_to_images = "media/weather_icons/set_1")
        self.IMAGE_SELECTION_FRAME_LAYOUT.addWidget(self.IMAGE_SET_1)

        self.IMAGE_SET_2 = ImageSet(parent = self.IMAGE_SELECTION_FRAME, path_to_images = "media/weather_icons/set_2")
        self.IMAGE_SELECTION_FRAME_LAYOUT.addWidget(self.IMAGE_SET_2)
        

        self.IMAGE_SELECTION_FRAME.setLayout(self.IMAGE_SELECTION_FRAME_LAYOUT)
        

        self.SAVE_BUTTON = qt_widgets.QPushButton(parent = self.OPTIONS_FRAME)
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
        self.SAVE_BUTTON.clicked.connect(self.save_image_list)
        self.change_language(language = self.window().APP_LANGUAGE)
    
    def reset_card_click(self):
        for index in range(self.IMAGE_SELECTION_FRAME_LAYOUT.count()):
            item = self.IMAGE_SELECTION_FRAME_LAYOUT.itemAt(index)
            widget = item.widget()
            widget.CLICKED = False
            widget.setStyleSheet(
                    """
                    ImageSet::hover{
                        background-color: rgba(0, 0, 0, 0.2);
                        border-radius: 4px;
                    }

                    QSvgWidget{
                        background-color: rgba(255, 255, 255, 0.2); 
                        border-radius: 10px;
                    }
                    ImageSet{
                        background-color: transparent;
                    }
                    
                    """
                    )

    def save_image_list(self):
        path_to_image_list[0] = self.CHOICE_BUFFER
        image_list.message.emit(path_to_image_list[0])

    def change_language(self, language):
        if language == "uk":
            self.IMAGE_SET_1.LABEL.setText("Список зображень №1")
            self.IMAGE_SET_2.LABEL.setText("Список зображень №2")
            self.TITLE_LABEL.setText("Списки зображень")
            self.ADD_BUTTON.setText("Додати")
            self.SAVE_BUTTON.setText("Зберегти")
        elif language == "en":
            self.IMAGE_SET_1.LABEL.setText("Image list №1")
            self.IMAGE_SET_2.LABEL.setText("Image list №2")
            self.TITLE_LABEL.setText("Image lists")
            self.ADD_BUTTON.setText("Add")
            self.SAVE_BUTTON.setText("Apply")