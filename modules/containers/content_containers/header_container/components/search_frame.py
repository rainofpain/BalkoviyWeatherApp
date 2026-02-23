import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui
import PyQt6.QtSvgWidgets as qt_svg

from utils import *
from config import cities_dict
from ....containers_utils import search_field_text

class SearchFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setFixedSize(261, 36)
        self.setObjectName("SearchFrame")
        self.LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (8, 6, 8, 7),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)
        self.setStyleSheet(
            """
            #SearchFrame {
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
            }
            """
        )
        self.ICON_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.ICON_FRAME)
        self.ICON_FRAME_LAYOUT = create_layout(
            orientation = "h",
            spacing = 0,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.ICON_FRAME.setLayout(self.ICON_FRAME_LAYOUT)
        self.ICON_FRAME.setFixedSize(25, 22)
        self.ICON_FRAME.setStyleSheet("padding-left: 3px; padding-top: 1px; margin-top: 1px;")
        self.ICON = qt_svg.QSvgWidget("media/search_icon.svg", parent = self.ICON_FRAME)
        self.ICON_FRAME_LAYOUT.addWidget(self.ICON)
        self.ICON.renderer().setAspectRatioMode(core.Qt.AspectRatioMode.KeepAspectRatio)

        self.SEARCH_FIELD = qt_widgets.QLineEdit(parent = self)
        self.SEARCH_FIELD.setStyleSheet("border:none; font-size: 16px; color: rgba(255, 255, 255, 1);")
        self.LAYOUT.addWidget(self.SEARCH_FIELD)
        self.SEARCH_FIELD.setFixedSize(220, 22)
        self.SEARCH_FIELD.setPlaceholderText("Пошук")
        self.SEARCH_FIELD.textChanged.connect(self.text_changed)

        self.CLEAR_BUTTON = qt_widgets.QPushButton(parent = self)
        self.LAYOUT.addWidget(
            self.CLEAR_BUTTON, 
            alignment = core.Qt.AlignmentFlag.AlignAbsolute| core.Qt.AlignmentFlag.AlignRight
            )
        self.CLEAR_BUTTON.hide()
        self.CLEAR_BUTTON.setIcon(qt_gui.QIcon("media/clear.svg"))
        self.CLEAR_BUTTON.setFixedSize(20, 22)
        self.CLEAR_BUTTON.setStyleSheet("margin-top: 2px; border: none;")
        
        self.CLEAR_BUTTON.clicked.connect(self.clear_search)
        self.ADD_CITY_BUTTON = self.parent().parent().ADD_CITY_BUTTON
        

    def text_changed(self):
        
        if self.SEARCH_FIELD.text() != "":
            self.CLEAR_BUTTON.show()
            self.window().SEARCH_DROPDOWN_MENU.LIST_WIDGET.clear()
            for letter in cities_dict:
                if letter.lower() == self.SEARCH_FIELD.text()[0].lower():
                    for city in cities_dict[letter]:

                        
                        if self.SEARCH_FIELD.text().lower() in city.lower():
                            if self.window().SEARCH_DROPDOWN_MENU.LIST_WIDGET.count() < 30:
                                self.window().SEARCH_DROPDOWN_MENU.LIST_WIDGET.addItem(city)
                                if len(self.SEARCH_FIELD.text()) == len(city):
                                    self.ADD_CITY_BUTTON.show()
                                    break
                                else:
                                    self.ADD_CITY_BUTTON.hide()
                            else:
                                break
                        if len(self.SEARCH_FIELD.text()) > len(city): 
                            self.ADD_CITY_BUTTON.hide()
                            
            self.window().SEARCH_DROPDOWN_MENU.show()
            self.CLEAR_BUTTON.clicked.connect(self.clear_search)
        else:
            self.CLEAR_BUTTON.hide()
            self.ADD_CITY_BUTTON.hide()
            self.window().SEARCH_DROPDOWN_MENU.hide()
            self.window().SEARCH_DROPDOWN_MENU.LIST_WIDGET.clear()
    
    def clear_search(self):
        self.SEARCH_FIELD.setText("")
       