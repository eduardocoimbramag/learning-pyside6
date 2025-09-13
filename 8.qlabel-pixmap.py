from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PixMap")

        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("mypresident.jpg")) #setando o label como imagem
        self.lbl.setScaledContents(True) #acompanha a largura e altura da janela

        self.setCentralWidget(self.lbl)



app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()