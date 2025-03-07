import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(250, 250, 500, 450)
        self.button = QPushButton("smash me!", self)
        self.label = QLabel("fuck me", self)
        self.initUI()


    def initUI(self):

        self.button.setGeometry( 100, 100, 200, 100)
        self.button.setStyleSheet("color: red;"
                             "font-size: 35px")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(100,200,200,100)
        self.label.setStyleSheet("font-size: 50px")

    def on_click(self):
        print("button is smashed ^-^")
        self.button.setText("smashed!!!")

        self.label.setText("ahhh")

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()