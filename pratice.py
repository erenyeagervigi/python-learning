import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 500, 450)
        self.checkbox = QCheckBox("hii", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry( 100, 50, 250, 250)
        self.checkbox.setStyleSheet("font: 50px;")
        self.checkbox.stateChanged.connect(self.on_click)

    def on_click(self,state):
        if state == Qt.Checked:
            print("yoo")
        else:
            print("hey..")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())