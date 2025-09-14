from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Model")
        
        self.lw = QListWidget()
        self.lw.addItems(["ITEM 1", "ITEM 2", "ITEM 3"])
                         
        self.setCentralWidget(self.lw)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()