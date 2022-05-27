from select import select
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QPlainTextEdit
from PyQt5 import uic
from sympy import *
import sys


class VerUI(QMainWindow):
    def __init__(self):
        super(VerUI, self).__init__()

        # load de ui file
        uic.loadUi("main.ui", self)

        # Definir los componentes
        self.calcular = self.findChild(QPushButton, "cargar")
        self.txt = self.findChild(QPlainTextEdit, "texty")

        # Instrucciones
        self.calcular.clicked.connect(self.limpiar)

        self.show()

# AQUI EMPIEZA LO BUENO, VAMOS A METER TODAS LAS INSTRUCCIONES
    def limpiar(self):
        fname = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "")
        if fname: 
            self.txt.setPlainText(str(fname))


"""
# Empezar la app
app = QApplication(sys.argv)
UIWindow = VerUI()
app.exec_()
"""