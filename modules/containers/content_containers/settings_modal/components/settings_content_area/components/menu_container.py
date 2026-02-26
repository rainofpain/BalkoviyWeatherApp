import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from .components import MenuButton, SearchCityContent, AppSizeContent, AppLanguageContent, ImageListsContent

class SettingsMenuContainer(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        self.CONTENT_CONTAINER = self.parent().CONTENT_CONTAINER
        self.setFixedSize(174, 578)
        self.setStyleSheet(
            """
            SettingsMenuContainer{
                border-right: 1px solid rgba(255, 255, 255, 0.2);
                }
            """
            )
        self.LAYOUT = create_layout(
            orientation = "h", 
            spacing = 0, 
            content_margins = (0, 0, 16, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )
        self.setLayout(self.LAYOUT)

        self.BUTTON_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.BUTTON_FRAME)

        self.BUTTON_FRAME_LAYOUT = create_layout(
            orientation = "v", 
            spacing = 0, 
            content_margins = (0, 0, 0, 0), 
            alignment = core.Qt.AlignmentFlag.AlignTop
        )

        self.BUTTON_FRAME.setLayout(self.BUTTON_FRAME_LAYOUT)
        self.BUTTON_FRAME.setFixedSize(158, 140)

        self.CITY_SEARCH_BUTTON = MenuButton(
            parent = self.BUTTON_FRAME, 
            clicked_callback = self.show_city_search
            )
        self.BUTTON_FRAME_LAYOUT.addWidget(self.CITY_SEARCH_BUTTON)
        self.CITY_SEARCH_BUTTON.LABEL.setText("Пошук міста")

        self.APP_SIZE_BUTTON = MenuButton(
            parent = self.BUTTON_FRAME, 
            clicked_callback = self.show_app_size
            )
        self.BUTTON_FRAME_LAYOUT.addWidget(self.APP_SIZE_BUTTON)
        self.APP_SIZE_BUTTON.LABEL.setText("Розмір додатку")

        self.APP_LANGUAGE_BUTTON = MenuButton(
            parent = self.BUTTON_FRAME, 
            clicked_callback = self.show_app_language
            )
        self.BUTTON_FRAME_LAYOUT.addWidget(self.APP_LANGUAGE_BUTTON)
        self.APP_LANGUAGE_BUTTON.LABEL.setText("Мова додатку")

        self.IMAGE_LISTS_BUTTON = MenuButton(
            parent = self.BUTTON_FRAME, 
            clicked_callback = self.show_images_lists
            )   
        self.BUTTON_FRAME_LAYOUT.addWidget(self.IMAGE_LISTS_BUTTON) 
        self.IMAGE_LISTS_BUTTON.LABEL.setText("Списки зображень")         

    def show_city_search(self):
        if self.CONTENT_CONTAINER.LAYOUT.count() > 0:
            clear_layout(self.CONTENT_CONTAINER.LAYOUT)
        self.CONTENT = SearchCityContent(parent = self.CONTENT_CONTAINER)
        self.CONTENT_CONTAINER.LAYOUT.addWidget(self.CONTENT)

    def show_app_size(self):
        if self.CONTENT_CONTAINER.LAYOUT.count() > 0:
            clear_layout(self.CONTENT_CONTAINER.LAYOUT)
        self.CONTENT = AppSizeContent(parent = self.CONTENT_CONTAINER)
        self.CONTENT_CONTAINER.LAYOUT.addWidget(self.CONTENT)

    def show_app_language(self):
        if self.CONTENT_CONTAINER.LAYOUT.count() > 0:
            clear_layout(self.CONTENT_CONTAINER.LAYOUT)
        self.CONTENT = AppLanguageContent(parent = self.CONTENT_CONTAINER)
        self.CONTENT_CONTAINER.LAYOUT.addWidget(self.CONTENT)

    def show_images_lists(self):
        if self.CONTENT_CONTAINER.LAYOUT.count() > 0:
            clear_layout(self.CONTENT_CONTAINER.LAYOUT)
        self.CONTENT = ImageListsContent(parent = self.CONTENT_CONTAINER)
        self.CONTENT_CONTAINER.LAYOUT.addWidget(self.CONTENT)
        
    def reset_card_click(self):
        for index in range(self.BUTTON_FRAME_LAYOUT.count()):
            item = self.BUTTON_FRAME_LAYOUT.itemAt(index)
            widget = item.widget()
            widget.CLICKED = False
            widget.setStyleSheet("font-size: 16px; color: rgba(255, 255, 255, 0.2); border: none;")
