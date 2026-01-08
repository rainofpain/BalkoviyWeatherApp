import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets


def create_layout(orientation: str, spacing: int, content_margins: tuple, alignment: core.Qt.AlignmentFlag):
    """
    v - vertical
    h - horizontal
    g - grid
    """
    
    
    if orientation == "v":
        layout = widgets.QVBoxLayout()
    elif orientation == "h":
        layout = widgets.QHBoxLayout()
    elif orientation == "g":
        layout = widgets.QGridLayout()
    
    
    layout.setSpacing(spacing)
    left, top, right, bottom = content_margins
    layout.setContentsMargins(left, top, right, bottom)
    layout.setAlignment(alignment)
    
    return layout
