#pyQt5-images

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 500, 450)
        self.setWindowTitle("smtg")

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("ereen.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height()- label.height()) //2,
                          label.width(),label.height())

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()