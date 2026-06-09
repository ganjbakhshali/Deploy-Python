from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PyQt6.QtCore import Qt


class FoodUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Random Food")
        self.resize(500, 600)

        layout = QVBoxLayout()

        self.random_btn = QPushButton(
            "Random Food"
        )

        self.food_name_label = QLabel(
            "Food Name"
        )

        self.food_name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.food_name_label.setStyleSheet(
            "font-size: 18px; font-weight: bold;"
        )

        self.image_label = QLabel()

        self.image_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(self.random_btn)
        layout.addWidget(self.food_name_label)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

    def update_food(
        self,
        food_name,
        pixmap
    ):

        self.food_name_label.setText(food_name)

        if pixmap:
            self.image_label.setPixmap(pixmap)