from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first program")

        button = QPushButton("Click here")
        self.setCentralWidget(button)
        button.setCheckable(True)
        button.clicked.connect(self.imprimir)
        button.clicked.connect(self.clicado)

    def imprimir(self):
        print("button-test")

    def clicado(self, s):
        print("clicado", s)

main = MainWindow()
main.show()

app.exec()