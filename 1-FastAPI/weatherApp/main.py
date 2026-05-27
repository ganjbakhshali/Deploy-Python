import sys

from PyQt6.QtWidgets import QApplication

from ui.weather_ui import WeatherUI
from service.weather_service import get_weather


class WeatherApp(WeatherUI):

    def __init__(self):
        super().__init__()

        self.search_btn.clicked.connect(self.search_weather)
        self.city_input.returnPressed.connect(self.search_weather)

    def search_weather(self):

        city_name = self.city_input.text().strip()

        if not city_name:
            self.condition_label.setText("Please enter city")
            self.wind_label.setText("--")
            self.humidity_label.setText("--")
            return

        data = get_weather(city_name)

        self.update_weather(
            condition=data["condition"],
            wind_kph=data["wind_kph"],
            humidity=data["humidity"],
            icon_pixmap=None
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WeatherApp()

    window.show()

    sys.exit(app.exec())