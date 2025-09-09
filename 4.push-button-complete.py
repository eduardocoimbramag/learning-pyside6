from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first program")

        self.button = QPushButton("Click here")
        self.setCentralWidget(self.button)
        
        self.button.setCheckable(True)
        self.button.clicked.connect(self.imprimir)
        self.button.clicked.connect(self.clicado)

    def imprimir(self):
        print("button-test")

    def clicado(self, s):
        print("clicado", s)
        if s:
            self.button.setStyleSheet(u"background-color:green")
            self.button.setText("Ligado!")
        else:
            self.button.setStyleSheet(u"background-color:red")
            self.button.setText("Desligado!")

main = MainWindow()
main.show()

app.exec()