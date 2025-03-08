import sys

from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, \
    QLabel, QGraphicsColorizeEffect


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.photo_label = QLabel()
        self.photo = QPixmap("photo.png")

        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        self.bw_button = QPushButton("BW")
        self.red_button = QPushButton("Red")
        self.orange_button = QPushButton("Orange")
        self.yellow_button = QPushButton("Yellow")
        self.green_button = QPushButton("Green")
        self.blue_button = QPushButton("Blue")
        self.purple_button = QPushButton("Purple")


        self.setGeometry(700, 300, 500, 500)
        self.initUI()
        self.setWindowTitle("Image Editor")
        self.setWindowIcon(QIcon("photo.png"))

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
        self.yellow_button.clicked.connect(lambda: self.apply_color_filter(QColor(255, 255, 0)))
        self.orange_button.clicked.connect(lambda: self.apply_color_filter(QColor(201, 113, 18)))
        self.green_button.clicked.connect(lambda: self.apply_color_filter(QColor(33, 242, 22)))
        self.blue_button.clicked.connect(lambda: self.apply_color_filter(QColor(22, 44, 242)))
        self.purple_button.clicked.connect(lambda: self.apply_color_filter(QColor(146, 14, 207)))

        central_widget.setLayout(main_layout)

    def apply_color_filter(self, color):
        colorize = QGraphicsColorizeEffect()
        colorize.setColor(color)

        self.photo_label.setGraphicsEffect(colorize)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())