from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class FlowerUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Flower AI Explorer")
        self.resize(500, 600)
        
        # اصلی‌ترین Layout
        layout = QVBoxLayout()

        # 1. بخش ورودی
        self.label = QLabel("توضیح گل را وارد کنید:")
        layout.addWidget(self.label)

        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("مثال: A beautiful red rose in the garden")
        layout.addWidget(self.textbox)

        self.button = QPushButton("Generate & Identify")
        layout.addWidget(self.button)

        # 2. وضعیت پردازش
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        # 3. بخش نمایش تصویر
        self.image_label = QLabel("Image will appear here")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0;")
        self.image_label.setFixedSize(400, 400) # سایز ثابت برای نظم بیشتر
        layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # 4. نتایج علمی
        self.result_label = QLabel("Flower info will appear here")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def show_image(self, path):
        """تصویر را نمایش می‌دهد و به اندازه کادر در می‌آورد."""
        pixmap = QPixmap(path)
        if not pixmap.isNull():
            # مقیاس کردن تصویر به طوری که داخل کادر ۴۰۰x۴۰۰ جا بشه
            scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)
        else:
            self.image_label.setText("Failed to load image.")

    def set_status(self, text):
        """برای اینکه به کاربر خبر بدیم برنامه داره کار می‌کنه"""
        self.status_label.setText(text)
