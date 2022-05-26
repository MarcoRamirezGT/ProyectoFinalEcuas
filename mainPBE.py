from unittest import result
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from edo_F import ed_f
from laplace_simple import laplace_simple
from laplace_inv import laplace_inv
from edo_CI2 import edo_CI2
from sympy import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Ecuaciones diferenciales ")

        # setting geometry
        self.setGeometry(500, 500, 500, 500)
        self.setFixedSize(500, 500)
        self.move(200, 200)
        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components

    def UiComponents(self):
        # creating a QLineEdit object
        def checkBoxChangedActionEdo(state):
            if (QtCore.Qt.Checked == state):

                edoCi.setDisabled(True)
                laplace.setDisabled(True)
                laplaceInv.setDisabled(True)
                calcular.setDisabled(False)
                line_edit.setDisabled(False)
                ej.setText("Ejemplo: 3*x*y(x).diff(x)-(x**2-9)*y(x)+1/x")

            else:

                edoCi.setDisabled(False)
                laplace.setDisabled(False)
                laplaceInv.setDisabled(False)
                calcular.setDisabled(True)
                resultado.setText('El resultado es: ')
                line_edit.setDisabled(True)
                line_edit.setText(' ')
                ej.setText(' ')

        def checkBoxChangedActionEdoCi(state):
            if (QtCore.Qt.Checked == state):

                edo.setDisabled(True)
                laplace.setDisabled(True)
                laplaceInv.setDisabled(True)
                y1.setEnabled(True)
                y1Name.setEnabled(True)
                y1Name2.setEnabled(True)
                x1.setEnabled(True)
                y2.setEnabled(True)
                y2Name.setEnabled(True)
                y2Name2.setEnabled(True)
                x2.setEnabled(True)
                ej.setText("Ejemplo : y(x).diff(x, x)-y(x).diff(x)-2*y(x)")
                y1.setText('0')
                x1.setText('2')
                y2.setText('0')
                x2.setText('1')
                calcular.setDisabled(False)
                line_edit.setDisabled(False)
            else:

                edo.setDisabled(False)
                laplace.setDisabled(False)
                laplaceInv.setDisabled(False)
                y1.setEnabled(False)
                y1Name.setEnabled(False)
                y1Name2.setEnabled(False)
                x1.setEnabled(False)
                y2.setEnabled(False)
                y2Name.setEnabled(False)
                y2Name2.setEnabled(False)
                x2.setEnabled(False)
                y1.setText(' ')
                x1.setText(' ')
                y2.setText(' ')
                x2.setText(' ')
                ej.setText('Ejemplo: ')
                calcular.setDisabled(True)
                resultado.setText('El resultado es: ')
                line_edit.setDisabled(True)
                line_edit.setText(' ')

        def checkBoxChangedActionLaplace(state):
            if (QtCore.Qt.Checked == state):

                edo.setDisabled(True)
                edoCi.setDisabled(True)
                laplaceInv.setDisabled(True)
                calcular.setDisabled(False)
                line_edit.setDisabled(False)
                ej.setText("Ejemplo: exp(-t)*sin(t)")
            else:

                edo.setDisabled(False)
                edoCi.setDisabled(False)
                laplaceInv.setDisabled(False)
                calcular.setDisabled(True)
                resultado.setText('El resultado es: ')
                line_edit.setDisabled(True)
                line_edit.setText(' ')
                ej.setText(' ')

        def checkBoxChangedActionLaplaceInv(state):
            if (QtCore.Qt.Checked == state):

                edo.setDisabled(True)
                laplace.setDisabled(True)
                edoCi.setDisabled(True)
                calcular.setDisabled(False)
                line_edit.setDisabled(False)
                ej.setText("Ejemplo: ((s+1)**3)/(s**4)")
            else:

                edo.setDisabled(False)
                laplace.setDisabled(False)
                edoCi.setDisabled(False)
                calcular.setDisabled(True)
                resultado.setText('El resultado es: ')
                line_edit.setDisabled(True)
                line_edit.setText(' ')
                ej.setText(' ')

        def on_click(self):
            if(laplace.isEnabled()):

                ec = line_edit.text()
                res = laplace_simple(ec)
                resultado.setText(str(res))

            if(laplaceInv.isEnabled()):
                ec = line_edit.text()
                res = laplace_inv(ec)
                resultado.setText(str(res))

            if(edo.isEnabled()):
                ec = line_edit.text()
                res = ed_f(ec)
                resultado.setText(str(res))

            if(edoCi.isEnabled()):

                ec = line_edit.text()
                x1_ec = int(x1.text())
                y1_ec = int(y1.text())
                x2_ec = int(x1.text())
                y2_ec = int(y1.text())

                res = edo_CI2(ec, x1_ec, y1_ec, x2_ec, y2_ec)
                resultado.setText(str(res))
        # creating a label
        title = QLabel('Calculadora', self)
        title.setGeometry(150, 15, 120, 60)
        title.move(215, 15)

        laplace = QCheckBox("Transformada de laplace ", self)
        laplace.setGeometry(100, 100, 500, 40)
        laplace.move(30, 50)
        laplace.stateChanged.connect(checkBoxChangedActionLaplace)

        laplaceInv = QCheckBox("Transformada de laplace inversa ", self)
        laplaceInv.setGeometry(100, 100, 500, 40)
        laplaceInv.move(30, 70)
        laplaceInv.stateChanged.connect(checkBoxChangedActionLaplaceInv)

        edo = QCheckBox("Ecuacion diferencial ", self)
        edo.setGeometry(100, 100, 500, 40)
        edo.move(30, 90)
        edo.stateChanged.connect(checkBoxChangedActionEdo)
        # Checkbox Edo
        edoCi = QCheckBox(
            "Ecuacion diferencial con condiciones iniciales", self)
        edoCi.setGeometry(100, 100, 500, 40)
        edoCi.move(30, 110)
        edoCi.stateChanged.connect(checkBoxChangedActionEdoCi)

        y1 = QLineEdit(" ", self)
        y1.setGeometry(25, 25, 25, 25)
        y1.move(130, 150)
        y1.setEnabled(False)

        y1Name = QLabel("y (", self)
        y1Name.setGeometry(25, 25, 25, 25)
        y1Name.move(110, 150)
        y1Name.setEnabled(False)

        y1Name2 = QLabel(") = ", self)
        y1Name2.setGeometry(25, 25, 25, 25)
        y1Name2.move(160, 150)
        y1Name2.setEnabled(False)

        x1 = QLineEdit(" ", self)
        x1.setGeometry(25, 25, 25, 25)
        x1.move(180, 150)
        x1.setEnabled(False)

        y2 = QLineEdit(" ", self)
        y2.setGeometry(25, 25, 25, 25)
        y2.move(310, 150)
        y2.setEnabled(False)

        y2Name = QLabel("y' (", self)
        y2Name.setGeometry(25, 25, 25, 25)
        y2Name.move(290, 150)
        y2Name.setEnabled(False)

        y2Name2 = QLabel(") = ", self)
        y2Name2.setGeometry(25, 25, 25, 25)
        y2Name2.move(340, 150)
        y2Name2.setEnabled(False)

        x2 = QLineEdit(" ", self)
        x2.setGeometry(25, 25, 25, 25)
        x2.move(360, 150)
        x2.setEnabled(False)

        # y1Name.setEnabled(False)

        ej = QLabel("Ejemplo: ", self)
        ej.setGeometry(100, 100, 500, 40)
        ej.move(150, 200)

        line_edit = QLineEdit("", self)
        line_edit.setGeometry(100, 100, 300, 40)
        line_edit.move(100, 230)

        calcular = QPushButton('Calcular ', self)
        calcular.setGeometry(100, 100, 100, 40)
        calcular.move(200, 290)
        calcular.clicked.connect(on_click)
        calcular.setEnabled(False)

        resultado = QLabel("El resultado es: ", self)
        resultado.setGeometry(50, 50, 500, 50)
        resultado.move(100, 330)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
