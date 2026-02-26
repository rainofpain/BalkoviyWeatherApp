import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui

from utils import *

class MenuButton(qt_widgets.QFrame):
    def __init__(self, parent, clicked_callback = None):
        super().__init__(parent = parent)

        self.CLICKED_CALLBACK = clicked_callback
        self.MENU_CONTAINER = self.parent().parent()
        self.setObjectName("MenuButton")
        self.setStyleSheet("font-size: 16px; color: rgba(255, 255, 255, 0.2); border: none; ")
        self.CLICKED = False

        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (8, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)

        self.setFixedSize(158, 35)

        self.LABEL = qt_widgets.QLabel(parent = self)
        
        self.LAYOUT.addWidget(self.LABEL)
    
    def mousePressEvent(self, event: qt_gui.QMouseEvent):

        button = event.button()
    
        if button == core.Qt.MouseButton.LeftButton:

            if self.CLICKED == False:

                self.MENU_CONTAINER.reset_card_click()
                self.CLICKED = True
                self.setStyleSheet(
                    """
                    *{
                    background-color: transparent;
                    font-size: 16px; 
                    color: rgba(255, 255, 255, 1); 
                    border: none;
                    }

                    #MenuButton {
                        background-color: rgba(0, 0, 0, 0.2); 
                        border-radius: 4px;
                    }
                    """
                    )
                
            if self.CLICKED_CALLBACK:
                self.CLICKED_CALLBACK()
            