from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel
)

from PyQt6.QtCore import Qt


class WeatherUI(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Weather App")
        self.setMinimumSize(400, 500)

        main_layout = QVBoxLayout()
        search_layout = QHBoxLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city...")

        self.search_btn = QPushButton("Search")

        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.search_btn)

        self.condition_label = QLabel("Condition: --")
        self.condition_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.condition_label.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )

        self.icon_label = QLabel()
        self.icon_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.wind_label = QLabel("Wind: -- kph")
        self.wind_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.humidity_label = QLabel("Humidity: -- %")
        self.humidity_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(search_layout)

        main_layout.addWidget(self.condition_label)
        main_layout.addWidget(self.icon_label)
        main_layout.addWidget(self.wind_label)
        main_layout.addWidget(self.humidity_label)

        self.setLayout(main_layout)

    def update_weather(
        self,
        condition,
        wind_kph,
        humidity,
        icon_pixmap
    ):

        self.condition_label.setText(
            f"Condition: {condition}"
        )

        self.wind_label.setText(
            f"Wind: {wind_kph} kph"
        )

        self.humidity_label.setText(
            f"Humidity: {humidity}%"
        )

        if icon_pixmap:
            self.icon_label.setPixmap(icon_pixmap)