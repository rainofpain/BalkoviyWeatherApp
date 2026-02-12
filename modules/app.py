import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

import sys

widgets.QApplication.setAttribute(core.Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

app_obj = widgets.QApplication(sys.argv)

app_obj.setStyleSheet(
    """
    #ContentFrame{
            background: qlineargradient(
                x1: 0 y1: 0,
                x2: 0 y2: 1,
                stop:0 rgba(255, 223, 86, 1), stop:1 rgba(135, 206, 250, 1)
            ); 
    }

    #LeftContainer{
    background: rgba(0, 0, 0, 0.4);
    }

    #Arrow{
    background-image: url('media/navigation/navigation_light.svg');
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
