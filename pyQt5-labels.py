#pyQt labels

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eren")
        self.setGeometry(250,250,500,450)

        label = QLabel("fuck you", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(100, 50, 250, 250)
        label.setStyleSheet("color: yellow;"
                            "background-color: black;")
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()