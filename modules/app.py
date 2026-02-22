import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

import sys

widgets.QApplication.setAttribute(core.Qt.ApplicationAttribute.AA_ShareOpenGLContexts)

app_obj = widgets.QApplication(sys.argv)

app_obj.setStyleSheet(
    """
   
    #CentralWidget[style = "dark"]{
        background: qlineargradient(
            x1: 0 y1: 0,
            x2: 0 y2: 1,
            stop:0 rgba(128, 128, 128, 1), stop:1 rgba(93, 173, 226, 1)
            ); 
        border-radius: 16px;
    }

    #SearchDropdownMenu[style = "dark"]{
        background-color: rgb(76, 82, 88); 
        border-radius: 10px;
    }

    #CentralWidget[style="light"]{
            background: qlineargradient(
                x1: 0 y1: 1,
                x2: 1 y2: 0,
                stop:0 rgba(135, 206, 250, 1), stop:1 rgba(255, 223, 86, 1)
            ); 
            border-radius: 16px;
        }

    #SearchDropdownMenu[style="light"]{
        background-color: rgb(146, 137, 72); 
        border-radius: 10px;
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

    #ContentContainer #Main #WeatherWidget{
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }

    #ContentContainer #Main #ClockWidget{
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    
    #ContentContainer #Footer #TopFrame,#BottomFrame{
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
