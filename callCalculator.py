import sys

from PyQt6.QtWidgets import QApplication, QDialog
from demoCalculatormy import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonAdd.clicked.connect(self.doadd)
        self.ui.pushButtonSub.clicked.connect(self.dosub)
        self.ui.pushButtonMul.clicked.connect(self.domul)
        self.ui.pushButtonDiv.clicked.connect(self.dodiv)
        self.show()

    def doadd(self):
        if len(self.ui.lineEditFNum.text()) != 0:
            a = int(self.ui.lineEditFNum.text())
        else:
            a = 0

        if len(self.ui.lineEditSNum.text()) != 0:
            b = int(self.ui.lineEditSNum.text())
        else:
            b = 0

        sumit = a + b
        self.ui.labelShowResult.setText("Addition: " + str(sumit))

    def dosub(self):
        if len(self.ui.lineEditFNum.text()) != 0:
            a = int(self.ui.lineEditFNum.text())
        else:
            a = 0

        if len(self.ui.lineEditSNum.text()) != 0:
            b = int(self.ui.lineEditSNum.text())
        else:
            b = 0

        subit = a - b
        self.ui.labelShowResult.setText("Subtraction: " + str(subit))

    def domul(self):
        if len(self.ui.lineEditFNum.text()) != 0:
            a = int(self.ui.lineEditFNum.text())
        else:
            a = 0

        if len(self.ui.lineEditSNum.text()) != 0:
            b = int(self.ui.lineEditSNum.text())
        else:
            b = 0

        mulit = a * b
        self.ui.labelShowResult.setText("Multiplication: " + str(mulit))

    def dodiv(self):
        if len(self.ui.lineEditFNum.text()) != 0:
            a = int(self.ui.lineEditFNum.text())
        else:
            a = 0

        if len(self.ui.lineEditSNum.text()) != 0:
            b = int(self.ui.lineEditSNum.text())
        else:
            b = 0

        divit = a / b
        self.ui.labelShowResult.setText("Division: " + str(round(divit)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
