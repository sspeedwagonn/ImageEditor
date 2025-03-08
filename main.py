import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QLabel, QGraphicsColorizeEffect, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.photo_label = QLabel()
        self.photo_label.setScaledContents(True)
        self.photo = QPixmap("resources/placeholder.png")

        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        self.bw_button = QPushButton("B/W")
        self.red_button = QPushButton("Red")
        self.orange_button = QPushButton("Orange")
        self.yellow_button = QPushButton("Yellow")
        self.green_button = QPushButton("Green")
        self.blue_button = QPushButton("Blue")
        self.purple_button = QPushButton("Purple")

        self.setFixedSize(500, 500)
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        self.setWindowTitle("Image Editor")
        self.setWindowIcon(QIcon("resources/icon.png"))

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.open_button)
        controls_layout.addWidget(self.save_button)
        main_layout.addLayout(controls_layout)

        self.photo_label.setPixmap(self.photo)
        main_layout.addWidget(self.photo_label)



        edits_layout = QHBoxLayout()
        edits_layout.addWidget(self.bw_button)
        edits_layout.addWidget(self.red_button)
        edits_layout.addWidget(self.orange_button)
        edits_layout.addWidget(self.yellow_button)
        edits_layout.addWidget(self.green_button)
        edits_layout.addWidget(self.blue_button)
        edits_layout.addWidget(self.purple_button)
        main_layout.addLayout(edits_layout)

        self.bw_button.clicked.connect(lambda: self.apply_color_filter(QColor(128, 128, 128)))
        self.red_button.clicked.connect(lambda: self.apply_color_filter(QColor(235, 30, 30)))
        self.yellow_button.clicked.connect(lambda: self.apply_color_filter(QColor(204, 153, 0)))
        self.orange_button.clicked.connect(lambda: self.apply_color_filter(QColor(201, 113, 18)))
        self.green_button.clicked.connect(lambda: self.apply_color_filter(QColor(33, 242, 22)))
        self.blue_button.clicked.connect(lambda: self.apply_color_filter(QColor(22, 44, 242)))
        self.purple_button.clicked.connect(lambda: self.apply_color_filter(QColor(146, 14, 207)))

        self.open_button.clicked.connect(self.open_image)
        self.save_button.clicked.connect(self.save_image)

        central_widget.setLayout(main_layout)

    def apply_color_filter(self, color):
        colorize = QGraphicsColorizeEffect()
        colorize.setColor(color)

        self.photo_label.setGraphicsEffect(colorize)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.jpg *.png *.jpeg)")

        if file_path:
            self.photo = QPixmap(file_path)
            self.photo_label.setPixmap(self.photo)

    def save_image(self):
        if self.photo_label.pixmap().isNull():
            return

        rendered_pixmap = QPixmap(self.photo_label.size())
        rendered_pixmap.fill(Qt.transparent)

        painter = QPainter(rendered_pixmap)
        self.photo_label.render(painter)
        painter.end()

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.jpg *.png *.jpeg)")

        if file_path:
            rendered_pixmap.save(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())