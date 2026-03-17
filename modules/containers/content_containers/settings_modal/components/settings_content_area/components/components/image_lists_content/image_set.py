import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets
import PyQt6.QtSvgWidgets as qt_svg
import PyQt6.QtGui as qt_gui

from utils import *
from ........containers_utils import language_change
from config import path_to_image_list

class ImageSet(qt_widgets.QFrame):
    def __init__(self, parent, path_to_images):
        super().__init__(parent = parent)

        self.PATH_TO_IMAGES = path_to_images
        self.CLICKED = False

        self.LAYOUT = create_layout(
            orientation  = "v",
            spacing = 16,
            content_margins = (16, 16, 16, 16),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.setFixedSize(490, 136)

        if self.PATH_TO_IMAGES == path_to_image_list[0]:
            self.CLICKED = True
            self.setStyleSheet(
                """
                ImageSet{
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px;
                }
                QSvgWidget{
                    background-color: rgba(255, 255, 255, 0.2); 
                    border-radius: 10px;
                }
                """
                )
        else:
            self.setStyleSheet(
                """
                    ImageSet::hover{
                        background-color: rgba(0, 0, 0, 0.2);
                        border-radius: 4px;
                    }
                    QSvgWidget{
                        background-color: rgba(255, 255, 255, 0.2); 
                        border-radius: 10px;
                    }
                """
            )
        self.setLayout(self.LAYOUT)

        self.LABEL = qt_widgets.QLabel(parent = self)
        self.LABEL.setStyleSheet("font-size: 14px; font-weight: 500;")

        self.LAYOUT.addWidget(self.LABEL)

        self.ICONS_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.ICONS_FRAME)

        self.ICONS_FRAME_LAYOUT = create_layout(
            orientation  = "h",
            spacing = 22,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignLeft
        )
        self.ICONS_FRAME.setLayout(self.ICONS_FRAME_LAYOUT)

        self.ICONS_FRAME.setFixedSize(458, 74)
   
        for index in range(2):
            image = qt_svg.QSvgWidget(f"{path_to_images}/0{index + 1}d.svg")
            image.setFixedSize(74, 74)
           
            self.ICONS_FRAME_LAYOUT.addWidget(image)
        
        image = qt_svg.QSvgWidget(f"{path_to_images}/04d.svg")
        image.setFixedSize(74, 74)
       
        self.ICONS_FRAME_LAYOUT.addWidget(image)

        for index in range(2):
            image = qt_svg.QSvgWidget(f"{path_to_images}/0{index + 2}n.svg")
            image.setFixedSize(74, 74)
            
            self.ICONS_FRAME_LAYOUT.addWidget(image)
        
    def mousePressEvent(self, event: qt_gui.QMouseEvent):

        button = event.button()

        if button == core.Qt.MouseButton.LeftButton:
            
            self.parent().parent().parent().CHOICE_BUFFER = self.PATH_TO_IMAGES

            if self.CLICKED == False:

                self.parent().parent().parent().reset_card_click()
                self.CLICKED = True
                self.setStyleSheet(
                    """
                    ImageSet{
                    background-color: rgba(0, 0, 0, 0.2);
                    border-radius: 4px;
                    }
                    QSvgWidget{
                        background-color: rgba(255, 255, 255, 0.2); 
                        border-radius: 10px;
                    }
                    """
                    )

            

        
