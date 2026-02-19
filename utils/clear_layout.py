import PyQt6.QtWidgets as qt_widgets

def clear_layout(layout: qt_widgets.QLayout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
        elif child.layout():
            clear_layout(child.layout())