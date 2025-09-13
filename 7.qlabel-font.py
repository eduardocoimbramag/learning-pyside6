from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Model")
        self.setFixedSize(QSize(600,400))

        self.lbl = QLabel("Hello, World")
        h1 = self.lbl.font() #indicar que o H1 é a fonte do label
        h1.setPointSize(48) #indicar tamanho o font-size de H1
        self.lbl.setFont(h1) #setar o tamanho da fonte H1
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #alinhamento horizontal e vertical, respectivamente



        self.setCentralWidget(self.lbl)


app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()