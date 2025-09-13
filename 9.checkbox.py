from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBox")
        self.setFixedSize(QSize(600,400))
        self.cb = QCheckBox("Click Here") #setando checkbox
        self.cb.setCheckedState(Qt.Checked) #deixando a checkbox ja marcada

        self.setCentralWidget(self.cb)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()