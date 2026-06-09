import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from ui.food_ui import FoodUI
from service.food_service import get_random_food


class FoodApp(FoodUI):

    def __init__(self):
        super().__init__()

        self.random_btn.clicked.connect(
            self.load_food
        )

    def load_food(self):

        data = get_random_food()

        pixmap = None

        if data["image_bytes"]:

            pixmap = QPixmap()

            pixmap.loadFromData(
                data["image_bytes"]
            )

            pixmap = pixmap.scaled(
                400,
                400,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )

        self.update_food(
            food_name=data["food_name"],
            pixmap=pixmap
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = FoodApp()

    window.show()

    sys.exit(app.exec())