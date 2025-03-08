import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout, \
    QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.photo_label = QLabel()
        self.photo = QPixmap("photo.png")
        self.open_button = QPushButton("Open")
        self.save_button = QPushButton("Save")

        self.bw_button = QPushButton("BW")
        self.blue_button = QPushButton("Blue")
        self.rose_button = QPushButton("Rose")
        self.yellow_button = QPushButton("Yellow")

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
        edits_layout.addWidget(self.blue_button)
        edits_layout.addWidget(self.rose_button)
        edits_layout.addWidget(self.yellow_button)
        main_layout.addLayout(edits_layout)

        central_widget.setLayout(main_layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())