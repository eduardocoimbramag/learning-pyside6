from PySide6.QtWidgets import QApplication, QWidget
import sys

# Cria a aplicação
app = QApplication(sys.argv)

# Cria a janela
janela = QWidget()
janela.show()

# Executa o loop da aplicação
app.exec()