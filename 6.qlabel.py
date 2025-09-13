from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QFrame, QLabel
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label")
        self.setFixedSize(QSize(600,400))

        self.input = QLineEdit()
        self.lbl = QLabel() #Adiciona o Label

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input.textChanged.connect(self.lbl.setText) #Conectar o Input com o Label

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()