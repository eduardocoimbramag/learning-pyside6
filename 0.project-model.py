from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QFrame
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit & QLabel")

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()