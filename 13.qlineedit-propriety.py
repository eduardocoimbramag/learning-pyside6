from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QVBoxLayout
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QlineEdit")

        self.le1 = QLineEdit()
        self.le1.setMaxLength(10) #limita o numero de caracteres
        self.le1.setPlaceholderText("Write your nickname") #placeholder

        self.le2 = QLineEdit()
        self.le2.setInputMask("00/0000;_") #campo para preenchimento de data
        
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(self.le1)
        layout.addWidget(self.le2)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()