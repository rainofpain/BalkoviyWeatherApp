import PyQt6.QtCore as core
import PyQt6.QtWidgets as qt_widgets

from utils import *
from config import countries_and_cities_dict, city_name_list, API_KEY
from .........left_container import InfoCard

class CityInputFrame(qt_widgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent = parent)

        language_change.message.connect(self.change_language)

        self.PARENT = self.parent().parent()
        self.CHECK_RESULT = {}
        self.LEFT_CONTAINER_SCROLL = self.window().findChild(qt_widgets.QFrame, "LeftContainerScroll")
        self.STYLE = self.window().CENTRAL_WIDGET.property("style")

        self.setFixedSize(239, 320)
        self.LAYOUT = create_layout(
            orientation  = "v",
            spacing = 24,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
        )
        self.setLayout(self.LAYOUT)

        self.TITLE_LABEL = qt_widgets.QLabel(parent = self)
        self.LAYOUT.addWidget(self.TITLE_LABEL)
        self.TITLE_LABEL.setFixedWidth(239)
        self.TITLE_LABEL.setStyleSheet("font-size: 18px; border: none;")
        self.TITLE_LABEL.setAlignment(core.Qt.AlignmentFlag.AlignLeft)

        self.INPUT_FIELDS_FRAME = qt_widgets.QFrame(parent = self)
        self.LAYOUT.addWidget(self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME.setFixedWidth(239)
        self.INPUT_FIELDS_FRAME.setObjectName("SettingsInputFields")
        self.INPUT_FIELDS_FRAME.setProperty("style", self.STYLE)
        
        set_property.message.connect(self.set_property)

        self.INPUT_FIELDS_FRAME.setStyleSheet(
            """
            QComboBox{
            background-color: rgba(236, 236, 236, 1);
            border-radius: 4px;
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            padding: 8 5 8 8;
            }

            QComboBox::placeholder{
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            }

            QComboBox::drop-down {
                width: 16px;
                margin-right: 8px;
                background: transparent;      
            }

            QComboBox::down-arrow {
                image: url(media/chevrones/chevron_down.svg);        
                width: 16px;
                height: 16px;
            }
            
            QComboBox QAbstractItemView::item {
                min-height: 30px;
                padding-left: 10px;
                border: none;
                border-radius: 10px;
            }
            QComboBox QAbstractItemView::item::hover {
                background-color: rgba(0, 0, 0, 0.2);
                min-height: 30px;
                padding-left: 10px;
                border: none;
                border-radius: 10px;
            }
            """
            )
        

        self.INPUT_FIELDS_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 16,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
            )
        
        self.INPUT_FIELDS_FRAME.setLayout(self.INPUT_FIELDS_FRAME_LAYOUT)

        # COUNTRY_FRAME

        self.COUNTRY_FRAME = qt_widgets.QFrame(parent = self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME_LAYOUT.addWidget(self.COUNTRY_FRAME)
        self.COUNTRY_FRAME.setFixedWidth(239)
        self.COUNTRY_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
            )
        self.COUNTRY_FRAME.setLayout(self.COUNTRY_FRAME_LAYOUT)
        self.COUNTRY_FRAME_LABEL = qt_widgets.QLabel(parent = self.COUNTRY_FRAME)
        self.COUNTRY_FRAME_LAYOUT.addWidget(self.COUNTRY_FRAME_LABEL)
        self.COUNTRY_FRAME_LABEL.setStyleSheet("font-size: 14px; font-weight: 500; border: none;")

        self.COUNTRY_FRAME_DROPDOWN = qt_widgets.QComboBox(parent = self.COUNTRY_FRAME)
        self.COUNTRY_FRAME_LAYOUT.addWidget(self.COUNTRY_FRAME_DROPDOWN)
        self.COUNTRY_FRAME_DROPDOWN.setFixedWidth(240)
        self.COUNTRY_FRAME_DROPDOWN.setContentsMargins(10, 8, 0,8)
        self.COUNTRY_FRAME_DROPDOWN.setMaxVisibleItems(9)
        self.COUNTRY_FRAME_DROPDOWN.view().setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.COUNTRY_FRAME_DROPDOWN.view().window().setWindowFlags(core.Qt.WindowType.Popup | core.Qt.WindowType.FramelessWindowHint | core.Qt.WindowType.NoDropShadowWindowHint)
        self.COUNTRY_FRAME_DROPDOWN.view().window().setAttribute(core.Qt.WidgetAttribute.WA_TranslucentBackground)

        if self.window().APP_LANGUAGE == "uk":
            self.COUNTRY_FRAME_DROPDOWN.setPlaceholderText("Виберіть країну")
        elif self.window().APP_LANGUAGE == "en":
            self.COUNTRY_FRAME_DROPDOWN.setPlaceholderText("Select country")
         
    
        for country_dict in countries_and_cities_dict["data"]:
            self.COUNTRY_FRAME_DROPDOWN.addItem(country_dict["country"])
        
        self.COUNTRY_FRAME_DROPDOWN.currentTextChanged.connect(self.fill_city_dropdown)

        #CITY_FRAME

        self.CITY_FRAME = qt_widgets.QFrame(parent = self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME_LAYOUT.addWidget(self.CITY_FRAME)
        self.CITY_FRAME.setFixedWidth(239)
        self.CITY_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
            )
        self.CITY_FRAME.setLayout(self.CITY_FRAME_LAYOUT)
        self.CITY_FRAME_LABEL = qt_widgets.QLabel(parent = self.COUNTRY_FRAME)
        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_FRAME_LABEL)
        self.CITY_FRAME_LABEL.setStyleSheet("font-size: 14px; font-weight: 500; border: none;")

        self.CITY_FRAME_DROPDOWN = qt_widgets.QComboBox(parent = self.COUNTRY_FRAME)
        self.CITY_FRAME_LAYOUT.addWidget(self.CITY_FRAME_DROPDOWN)
        self.CITY_FRAME_DROPDOWN.setFixedWidth(240)
        self.CITY_FRAME_DROPDOWN.setContentsMargins(10, 8, 0,8)
        self.CITY_FRAME_DROPDOWN.setMaxVisibleItems(5)
        self.CITY_FRAME_DROPDOWN.view().setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CITY_FRAME_DROPDOWN.view().window().setWindowFlags(core.Qt.WindowType.Popup | core.Qt.WindowType.FramelessWindowHint | core.Qt.WindowType.NoDropShadowWindowHint)
        self.CITY_FRAME_DROPDOWN.view().window().setAttribute(core.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.CITY_FRAME_DROPDOWN.currentTextChanged.connect(self.city_choosed)

        # COORDINATES_FRAME

        self.COORDINATES_FRAME = qt_widgets.QFrame(parent = self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME_LAYOUT.addWidget(self.COORDINATES_FRAME)
        self.COORDINATES_FRAME.setFixedWidth(239)
        self.COORDINATES_FRAME_LAYOUT = create_layout(
            orientation  = "v",
            spacing = 8,
            content_margins = (0, 0, 0, 0),
            alignment = core.Qt.AlignmentFlag.AlignTop | core.Qt.AlignmentFlag.AlignLeft
            )
        self.COORDINATES_FRAME.setLayout(self.COORDINATES_FRAME_LAYOUT)
        self.COORDINATES_FRAME_LABEL = qt_widgets.QLabel(parent = self.COUNTRY_FRAME)
        self.COORDINATES_FRAME_LAYOUT.addWidget(self.COORDINATES_FRAME_LABEL)
        self.COORDINATES_FRAME_LABEL.setStyleSheet("font-size: 14px; font-weight: 500; border: none;")

        self.COORDINATES_FRAME_INPUT = qt_widgets.QLineEdit(parent = self.COORDINATES_FRAME)
        self.COORDINATES_FRAME_LAYOUT.addWidget(self.COORDINATES_FRAME_INPUT)
        self.COORDINATES_FRAME_INPUT.setFixedSize(239, 32)
        self.COORDINATES_FRAME_INPUT.setStyleSheet(
            """
            QLineEdit{
            background-color: rgba(236, 236, 236, 1);
            border-radius: 4px;
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            padding: 8 10 8 10;
            }
            
            QLineEdit::placeholder{
            color: rgba(113, 113, 122, 1);
            font-size: 12px;
            }
            """
            )

        self.SAVE_BUTTON = qt_widgets.QPushButton(parent = self)
        self.LAYOUT.addWidget(self.SAVE_BUTTON)
        self.SAVE_BUTTON.setFixedSize(105, 38)
        self.SAVE_BUTTON.setStyleSheet(
            """
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px;
                color: rgba(255, 255, 255, 1);
                font-size: 14px;
            """
            )
        self.SAVE_BUTTON.clicked.connect(self.save_city)

        self.change_language(language = self.window().APP_LANGUAGE)
    
    def set_property(self, property):
        self.INPUT_FIELDS_FRAME.setProperty("style", property)
        self.INPUT_FIELDS_FRAME.style().unpolish(self.INPUT_FIELDS_FRAME)
        self.INPUT_FIELDS_FRAME.style().polish(self.INPUT_FIELDS_FRAME)

        self.CITY_FRAME_DROPDOWN.view().style().unpolish(self.CITY_FRAME_DROPDOWN.view())
        self.CITY_FRAME_DROPDOWN.view().style().polish(self.CITY_FRAME_DROPDOWN.view())

        self.COUNTRY_FRAME_DROPDOWN.view().style().unpolish(self.COUNTRY_FRAME_DROPDOWN.view())
        self.COUNTRY_FRAME_DROPDOWN.view().style().polish(self.COUNTRY_FRAME_DROPDOWN.view())
    
    def fill_city_dropdown(self, text):
        self.COORDINATES_FRAME_INPUT.setText("")
        self.CITY_FRAME_DROPDOWN.clear()
        for country_dict in countries_and_cities_dict["data"]:
            
            if text == country_dict["country"]:
                for city in country_dict["cities"]:
                    self.CITY_FRAME_DROPDOWN.addItem(city)
    
    def city_choosed(self, text):
        if text:
            self.CITY_NAME = text

            self.WEATHER_LOADER = WeatherLoader(
                api_request_link = f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={self.CITY_NAME}&appid={API_KEY}&lang={self.window().APP_LANGUAGE}",
                language = self.window().APP_LANGUAGE
                )
            self.WEATHER_LOADER.received_dict.connect(self.set_coords)
            self.WEATHER_LOADER.start()
    
    def set_coords(self, data):
        try:
            coord_tuple = (data["coord"]["lat"], data["coord"]["lon"])
            update_content.coord.emit(coord_tuple)
            self.COORDINATES_FRAME_INPUT.setText(f"{coord_tuple}")
            self.PARENT.MAP_FRAME.show()
        except:
            print("failed to load data")
        

    def save_city(self):
        city_name = self.CITY_NAME
    
        self.CARD = InfoCard(
                parent = self.LEFT_CONTAINER_SCROLL,
                search_city_name = city_name
                )
        self.CARD.load_weather()
        self.CARD.WEATHER_LOADER.filtered_dict.connect(self.check_data)  
    
    def check_data(self, data):
        try:
            self.CHECK_RESULT = data
            if len(self.CHECK_RESULT) > 0 and data["search_name"] not in city_name_list: 
                city_name_list.append(data["search_name"])
                self.CARD.LEFT_CONTAINER.reset_card_click()
                self.CARD.CLICKED = True
                self.CARD.ARROW.show()
                self.CARD.setStyleSheet(
                    """
                    *{
                    background-color: transparent;
                    }

                    #Card {
                    background-color: rgba(0, 0, 0, 0.2); 
                    border-radius: 8px;
                    }
                    """
                    )
                self.LEFT_CONTAINER_SCROLL.layout().addWidget(self.CARD, alignment = core.Qt.AlignmentFlag.AlignRight)
                api_link_message.message.emit(f"https://api.openweathermap.org/data/2.5/weather?units=metric&q={data["search_name"]}&appid={API_KEY}&lang={self.window().APP_LANGUAGE}")
                city_name_message.message.emit(data["search_name"])
                update_content.update_settings_container.emit(True)
        except Exception as error:
            print(error)

    def change_language(self, language):
       
        if language == "uk":
            self.TITLE_LABEL.setText("Пошук міста")
            self.COUNTRY_FRAME_LABEL.setText("Країна")
            self.CITY_FRAME_LABEL.setText("Місто")
            self.COORDINATES_FRAME_LABEL.setText("Координати")
            self.COUNTRY_FRAME_DROPDOWN.setPlaceholderText("Виберіть країну")
            self.CITY_FRAME_DROPDOWN.setPlaceholderText("Виберіть місто")
            self.COORDINATES_FRAME_INPUT.setPlaceholderText("(WGS 84,UTM,MGRS)")
            self.SAVE_BUTTON.setText("Зберегти")

        elif language == "en":
            self.TITLE_LABEL.setText("Search city")
            self.COUNTRY_FRAME_LABEL.setText("Country")
            self.CITY_FRAME_LABEL.setText("City")
            self.COORDINATES_FRAME_LABEL.setText("Coordinates")
            self.COUNTRY_FRAME_DROPDOWN.setPlaceholderText("Select country")
            self.CITY_FRAME_DROPDOWN.setPlaceholderText("Select city")
            self.COORDINATES_FRAME_INPUT.setPlaceholderText("(WGS 84,UTM,MGRS)")
            self.SAVE_BUTTON.setText("Apply")


