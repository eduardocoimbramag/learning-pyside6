from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Model")

        self.cb = QComboBox()
        self.cb.addItem("Item 1")
        self.cb.addItem("Item 2")
        self.setCentralWidget(self.cb)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()