import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton , QButtonGroup

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 500, 450)
        self.radio1 = QRadioButton("visa", self)
        self.radio2 = QRadioButton("master card", self)
        self.radio3 = QRadioButton("gift card", self)
        self.radio4 = QRadioButton("IN- store", self)
        self.radio5 = QRadioButton("online", self)

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.setStyleSheet("QRadioButton{"
                           "font-size : 30px};"
                           "font: Bookman;"
                           "padding: 10px")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)


    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())