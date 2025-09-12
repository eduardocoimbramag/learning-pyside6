from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Model")
        self.setFixedSize(QSize(600,400))

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()