## Bibliotecas
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QPushButton, QLineEdit, QLabel
from FabioTurtle import FabioTurtle as ft

# Caso não gere o arquivo da interface a partir do form.ui
from ui_form import Ui_WidgetApp
# pyside6-uic form.ui -o ui_form.py

## Algoritmo
class WidgetApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetApp()
        self.ui.setupUi(self)

        # Configuração do botão e seu listener
        self.botao = self.findChild(QPushButton, "checkar")
        self.botao.clicked.connect(self.on_button_clicked)

        # Entrada de texto
        self.input = self.findChild(QLineEdit, "input")

        # Foto do Fábio + Tuple
        self.fabio = self.findChild(QLabel, "fabio")


    def on_button_clicked(self): # Callback do botão

        ## Declarações
        texto: str

        ## Algoritmo
        input:str = self.input.text()
        if (input == ""): return

        # Ajustar o input para ser reconhecido na tuple
        input = input.lower().capitalize()

        texto = (f"O nome {input} contém na lista" if ft(input).checkar()
                else f"O nome {input} NÃO contém na lista")

        QMessageBox.information(self, "Fábio Tuple", texto)

# Simulação de um main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WidgetApp()
    widget.show()
    sys.exit(app.exec())
