import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtGui as qt_gui


from modules import app_obj

from utils import *

class LeftContainerHeader(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.SWITCH = False

        self.setFixedSize(330, 44)
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 10, 0, 10), 
            alignment = core.Qt.AlignmentFlag.AlignRight
        )

        self.setLayout(self.LAYOUT)

        self.SWITCH_BUTTON = qt_widgets.QToolButton(parent = self)

        self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_dark.svg")
        
        self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
        self.SWITCH_BUTTON.setStyleSheet("border: none")

        icon_size = core.QSize(52,24)
        self.SWITCH_BUTTON.setIconSize(icon_size)

        self.SWITCH_BUTTON.clicked.connect(self.switch)

        self.LAYOUT.addWidget(self.SWITCH_BUTTON)

    def switch(self):
        if self.SWITCH == False:
            self.SWITCH = True
            self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_light.svg")
            self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
            app_obj.setStyleSheet(
                """
                #CentralWidget{
                background: qlineargradient(
                    x1: 0 y1: 0,
                    x2: 0 y2: 1,
                    stop:0 rgba(255, 223, 86, 1), stop:1 rgba(135, 206, 250, 1)
                ); 
                border-radius: 16px;
                }

                #TitleBar{
                background-color: rgba(0, 0, 0, 0.6); 
                border-top-left-radius: 16px;
                border-top-right-radius: 16px;
                }

                #LeftContainer{
                background: rgba(0, 0, 0, 0.4);
                border-bottom-left-radius: 16px;
                }

                #ContentContainer #Main{
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 10px;
                }
                #ContentContainer #Footer{
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 10px;
                }

                *{
                color: rgba(255, 255, 255, 1);
                font-weight: 500;
                background-color:transparent;                      
                }
                """
                )

        elif self.SWITCH == True:
            self.SWITCH = False
            self.SWITCH_ICON = qt_gui.QIcon("media/switch/switch_dark.svg")
            self.SWITCH_BUTTON.setIcon(self.SWITCH_ICON)
            app_obj.setStyleSheet(
                """
                #CentralWidget{
                background: qlineargradient(
                            x1: 0 y1: 0,
                            x2: 0 y2: 1,
                            stop:0 rgba(128, 128, 128, 1), stop:1 rgba(93, 173, 226, 1)
                            ); 
                border-radius: 16px;
                }

                #TitleBar{
                background-color: rgba(0, 0, 0, 0.6); 
                border-top-left-radius: 16px;
                border-top-right-radius: 16px;
                }

                #LeftContainer{
                background: rgba(0, 0, 0, 0.4);
                border-bottom-left-radius: 16px;
                }

                #ContentContainer #Main{
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 10px;
                }
                #ContentContainer #Footer{
                    background: rgba(0, 0, 0, 0.2);
                    border-radius: 10px;
                }

                *{
                color: rgba(255, 255, 255, 1);
                font-weight: 500;
                background-color:transparent;                      
                }
                """
                )

          


