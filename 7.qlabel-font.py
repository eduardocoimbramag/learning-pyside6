from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Model")
        self.setFixedSize(QSize(600,400))

        self.lbl = QLabel("Hello, World")
        h1 = self.lbl.font()
        h1.setPointSize(48)
        self.lbl.setFont(h1)


        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()