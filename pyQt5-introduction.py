#pyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #setwindowtitile is used to set the title of the window
        self.setWindowTitle("Eren")
        #setgeometry is used to set the screen where you want it to be
        self.setGeometry(250, 250, 500, 450)
        #setwindowicon is used to give it a icon
        self.setWindowIcon(QIcon("ereen.jpg"))

def main():
    #in my pov Qapplication is used to set the parameters of the application
    app = QApplication(sys.argv)
    #mainwindow is used to open the window
    window = MainWindow()
    #this is used to make the window to be in the opened state
    window.show()
    #sys.exit is used to close the window when u need it
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()