from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QFrame
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Line Edit")
        self.setFixedSize(QSize(600,400))

        self.input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.input)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()