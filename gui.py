import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(75, 100, 800, 500)


        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)

        pixmap = QPixmap("ereen.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry(200, 100, label.width(), label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()