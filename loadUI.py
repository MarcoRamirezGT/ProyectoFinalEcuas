from select import select
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QRadioButton, QTextEdit
from PyQt5 import uic
from edo_F import ed_f
from laplace_simple import laplace_simple
from laplace_inv import laplace_inv
from sympy import *
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load de ui file
        uic.loadUi("main.ui", self)

        # Definir los componentes
        self.ingresa = self.findChild(QTextEdit, "ecua")
        self.edo = self.findChild(QRadioButton, "ed")
        self.laplace = self.findChild(QRadioButton, "tdl")
        self.laplaceI = self.findChild(QRadioButton, "tidl")
        self.label = self.findChild(QLabel, "resul")
        self.calcular = self.findChild(QPushButton, "CALCULAR")
        self.clear = self.findChild(QPushButton, "LIMPIAR")
        self.instruc = self.findChild(QPushButton, "INSTU")

        # Instrucciones
        self.clear.clicked.connect(self.limpiar)
        self.instruc.clicked.connect(self.mos_ins)
      #  self.calcular.clicked.connect(ed_f(str(self.ingresa)))

        # Show de UI
        self.show()

# AQUI EMPIEZA LO BUENO, VAMOS A METER TODAS LAS INSTRUCCIONES
    def limpiar(self):
        self.ingresa.setPlainText("")

    def mos_ins(self):
        uic.loadUi("instruc.ui", self)
        self.vuelta = self.findChild(QPushButton, "regre")

        self.vuelta.clicked.connect(UI)


# Empezar la app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
