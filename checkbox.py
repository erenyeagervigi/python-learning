import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 500, 450)
        self.checkbox = QCheckBox("do u like to fuck?",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(40, 0, 250, 250)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
       if state == Qt.Checked:
           print("ay ay")
       else:
           print("your gay")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()