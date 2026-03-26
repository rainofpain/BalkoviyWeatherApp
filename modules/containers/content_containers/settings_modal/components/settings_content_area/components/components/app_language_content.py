import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from config import app_language

class AppLanguageContent(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.STYLE = self.window().CENTRAL_WIDGET.property("style")

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
        self.OPTIONS_FRAME.setMinimumSize(239, 161)

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

        self.CHOOSE_LANGUAGE_FRAME = qt_widgets.QFrame(parent = self.OPTIONS_FRAME)
        self.OPTIONS_FRAME_LAYOUT.addWidget(self.CHOOSE_LANGUAGE_FRAME)
        self.CHOOSE_LANGUAGE_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop| core.Qt.AlignmentFlag.AlignLeft
            )
        self.CHOOSE_LANGUAGE_FRAME.setLayout(self.CHOOSE_LANGUAGE_FRAME_LAYOUT)
        self.CHOOSE_LANGUAGE_FRAME.setMinimumSize(239, 54)

        self.CHOOSE_LANGUAGE_FRAME.setStyleSheet(
            """
            QComboBox{
            background-color: rgba(236, 236, 236, 1);
            border-radius: 4px;
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            padding: 8 5 8 8;
            }

            QComboBox::placeholder{
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            }

            QComboBox::drop-down {
                width: 16px;
                margin-right: 8px;
                background: transparent;      
            }

            QComboBox::down-arrow {
                image: url(media/chevrones/chevron_down.svg);        
                width: 16px;
                height: 16px;
            }
            
            QComboBox QAbstractItemView::item {
                min-height: 30px;
                padding-left: 10px;
                border: none;
                border-radius: 10px;
            }
            QComboBox QAbstractItemView::item::hover {
                background-color: rgba(0, 0, 0, 0.2);
                min-height: 30px;
                padding-left: 10px;
                border: none;
                border-radius: 10px;
            }
            """
            )
        
        self.CHOOSE_LANGUAGE_FRAME.setObjectName("ChooseLanguageFrame")
        self.CHOOSE_LANGUAGE_FRAME.setProperty("style", self.STYLE)

        set_property.message.connect(self.set_property)

        self.CHOOSE_LANGUAGE_LABEL = qt_widgets.QLabel(parent = self.CHOOSE_LANGUAGE_FRAME)
        self.CHOOSE_LANGUAGE_FRAME_LAYOUT.addWidget(self.CHOOSE_LANGUAGE_LABEL)
        self.CHOOSE_LANGUAGE_LABEL.setStyleSheet("color: rgba(255, 255, 255, 1); font-size: 14px; font-weight: 500;")

        self.LANGUAGE_DROPDOWN = qt_widgets.QComboBox(parent = self.CHOOSE_LANGUAGE_FRAME)
        self.CHOOSE_LANGUAGE_FRAME_LAYOUT.addWidget(self.LANGUAGE_DROPDOWN)
        self.LANGUAGE_DROPDOWN.setFixedSize(240, 32)
        
        self.LANGUAGE_DROPDOWN.setContentsMargins(10, 8, 0,8)
        self.LANGUAGE_DROPDOWN.view().setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.LANGUAGE_DROPDOWN.view().window().setWindowFlags(core.Qt.WindowType.Popup | core.Qt.WindowType.FramelessWindowHint | core.Qt.WindowType.NoDropShadowWindowHint)
        self.LANGUAGE_DROPDOWN.view().window().setAttribute(core.Qt.WidgetAttribute.WA_TranslucentBackground)

        
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
        self.SAVE_BUTTON.clicked.connect(self.save_app_language)
        self.change_language()

    def save_app_language(self):
        if self.LANGUAGE_DROPDOWN.currentText() == "Українська" or self.LANGUAGE_DROPDOWN.currentText() == "Ukrainian":
            app_language[0] = "uk"
        elif self.LANGUAGE_DROPDOWN.currentText() == "Англійська" or self.LANGUAGE_DROPDOWN.currentText() == "English":
            app_language[0] = "en"
        language_change.message.emit(app_language[0])
        self.change_language()
    
    def change_language(self):
        if app_language[0] == "uk":
            self.TITLE_LABEL.setText("Оберіть мову додатку")
            self.CHOOSE_LANGUAGE_LABEL.setText("Мова додатку")
            self.LANGUAGE_DROPDOWN.clear()
            self.LANGUAGE_DROPDOWN.addItems(["Українська", "Англійська"])
            self.LANGUAGE_DROPDOWN.setCurrentIndex(0)
            self.SAVE_BUTTON.setText("Зберегти")
        elif app_language[0] == "en":
                self.TITLE_LABEL.setText("Choose app language")
                self.CHOOSE_LANGUAGE_LABEL.setText("App language")
                self.LANGUAGE_DROPDOWN.clear()
                self.LANGUAGE_DROPDOWN.addItems(["Ukrainian", "English"])
                self.LANGUAGE_DROPDOWN.setCurrentIndex(1)
                self.SAVE_BUTTON.setText("Apply")

    def set_property(self, property):
        self.CHOOSE_LANGUAGE_FRAME.setProperty("style", property)
        self.CHOOSE_LANGUAGE_FRAME.style().unpolish(self.CHOOSE_LANGUAGE_FRAME)
        self.CHOOSE_LANGUAGE_FRAME.style().polish(self.CHOOSE_LANGUAGE_FRAME)

        self.LANGUAGE_DROPDOWN.view().style().unpolish(self.LANGUAGE_DROPDOWN.view())
        self.LANGUAGE_DROPDOWN.view().style().polish(self.LANGUAGE_DROPDOWN.view())

        self.LANGUAGE_DROPDOWN.view().style().unpolish(self.LANGUAGE_DROPDOWN.view())
        self.LANGUAGE_DROPDOWN.view().style().polish(self.LANGUAGE_DROPDOWN.view())
