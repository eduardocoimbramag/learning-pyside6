from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")
        self.sp = QSpinBox()
        self.sp.setMinimum(10) #determina o minimo
        self.sp.setMaximum(100) #determina o maximo
        self.sp.setPrefix("R$") #determina o prefixo
        self.sp.setSingleStep(2) #pula de X em X numeros

        self.setCentralWidget(self.sp)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()