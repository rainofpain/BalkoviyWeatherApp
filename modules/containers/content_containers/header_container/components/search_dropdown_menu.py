import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets


from utils import *

class SearchDropdownMenu(qt_widgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent = parent)

        self.setObjectName("SearchDropdownMenu")
        self.setAttribute(core.Qt.WidgetAttribute.WA_StyledBackground)

        self.setGeometry(
            923,
            105,
            261, 
            200
            )
        
        self.LAYOUT = create_layout(
            orientation = "v", 
            spacing = 10, 
            content_margins = (0, 8, 0, 8), 
            alignment = core.Qt.AlignmentFlag.AlignHCenter
        )
        self.setLayout(self.LAYOUT)

        self.LABEL = qt_widgets.QLabel("Результати пошуку", parent = self)
        self.LAYOUT.addWidget(self.LABEL)
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
        self.LIST_WIDGET.setFixedSize(261, 160)
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