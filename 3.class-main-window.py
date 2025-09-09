from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first program")

        button = QPushButton("Click here")
        self.setCentralWidget(button)
        button.clicked.connect(self.imprimir)

    def imprimir(self):
        print("button-test")

main = MainWindow()
main.show()

app.exec()