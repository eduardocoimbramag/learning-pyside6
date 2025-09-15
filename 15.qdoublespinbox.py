from PySide6.QtWidgets import QApplication, QMainWindow, QDoubleSpinBox
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QSpinBox")
        self.sp = QDoubleSpinBox() #trabalha com decimais
        self.sp.setMinimum(10) 
        self.sp.setMaximum(100) 
        self.sp.setPrefix("R$") 

        self.setCentralWidget(self.sp)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()