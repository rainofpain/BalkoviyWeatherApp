import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from ....containers_utils import api_link_message, city_name_message
from config import API_KEY
from utils import *

class SearchDropdownMenu(qt_widgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setObjectName("SearchDropdownMenu")
        self.setAttribute(core.Qt.WidgetAttribute.WA_StyledBackground)
        self.move(923, 96)
        self.setFixedWidth(261)
        self.setFixedHeight(200)
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 8, 0, 8), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)

        self.LABEL = qt_widgets.QLabel("Результати пошуку", parent = self)
        self.LAYOUT.addWidget(self.LABEL)
        self.LABEL.setFixedSize(261, 14)
        self.LABEL.setStyleSheet(
            """
            padding-left: 8px;
            font-size: 12px; 
            background-color: transparent;
            color: rgba(255, 255, 255, 0.8);
            """
            )
       
        self.LIST_WIDGET = qt_widgets.QListWidget(parent = self)
        self.LAYOUT.addWidget(self.LIST_WIDGET)
        self.LIST_WIDGET.setStyleSheet(
            """
            QListWidget{
            border: none;
            outline: none;
            background-color: transparent;
            }

            QListWidget::item{
            padding-left: 8px;
            width: 261px;
            height: 32px;
            color: rgba(255, 255, 255, 1);
            font-size: 14px;
            border: none;
            }

            QListWidget::item::hover{
            background-color: rgba(0, 0, 0, 0.2);
            color: rgba(255, 255, 255, 1);
            font-size: 14px;
            border-radius: 8px;
            border: none;
            }
            """
            )
        self.LIST_WIDGET.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.LIST_WIDGET.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.LIST_WIDGET.itemClicked.connect(self.item_clicked)
    
    def item_clicked(self, item):
        search_frame = self.window().findChild(qt_widgets.QFrame, "SearchFrame")
        city_name = item.text()
        search_frame.SEARCH_FIELD.setText(city_name)
        api_link_message.message.emit(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={city_name}&appid={API_KEY}&lang=ua")
        city_name_message.message.emit(city_name)
        self.hide()
        self.LIST_WIDGET.clear()