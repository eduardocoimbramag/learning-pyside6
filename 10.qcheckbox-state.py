from PySide6.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CheckBox")
        self.question = QLabel("Do you smoke?")
        self.cb1 = QCheckBox("Yes")
        self.cb2 = QCheckBox("No")
        self.anwser1 = QLabel("")
        self.anwser2 = QLabel("")

        section1 = QVBoxLayout()
        section1.addWidget(self.question)
        section1.addWidget(self.cb1)
        section1.addWidget(self.cb2)
        section1.addWidget(self.anwser1)
        section1.addWidget(self.anwser2)

        container = QWidget()
        container.setLayout(section1)

        self.setCentralWidget(container)

        self.cb1.toggled.connect(self.on_yes)
        self.cb2.toggled.connect(self.on_no)

    def on_yes(self, checked: bool):
        print(f"[YES] toggled -> {checked}")
        self.anwser1.setText("so bad :(" if checked else " ")

    def on_no(self, checked: bool):
        print(f"[NO ] toggled -> {checked}")
        self.anwser2.setText("VERY GOOD!!!" if checked else " ")

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()