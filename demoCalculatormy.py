# Form implementation generated from reading ui file 'demoCalculatormy.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 480)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 70, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditFNum = QtWidgets.QLineEdit(Dialog)
        self.lineEditFNum.setGeometry(QtCore.QRect(310, 70, 113, 22))
        self.lineEditFNum.setObjectName("lineEditFNum")
        self.lineEditSNum = QtWidgets.QLineEdit(Dialog)
        self.lineEditSNum.setGeometry(QtCore.QRect(310, 110, 113, 22))
        self.lineEditSNum.setObjectName("lineEditSNum")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(50, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonSub = QtWidgets.QPushButton(Dialog)
        self.pushButtonSub.setGeometry(QtCore.QRect(180, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButtonSub.setFont(font)
        self.pushButtonSub.setObjectName("pushButtonSub")
        self.pushButtonMul = QtWidgets.QPushButton(Dialog)
        self.pushButtonMul.setGeometry(QtCore.QRect(310, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButtonMul.setFont(font)
        self.pushButtonMul.setObjectName("pushButtonMul")
        self.pushButtonDiv = QtWidgets.QPushButton(Dialog)
        self.pushButtonDiv.setGeometry(QtCore.QRect(440, 250, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButtonDiv.setFont(font)
        self.pushButtonDiv.setObjectName("pushButtonDiv")
        self.labelShowResult = QtWidgets.QLabel(Dialog)
        self.labelShowResult.setGeometry(QtCore.QRect(50, 360, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelShowResult.setFont(font)
        self.labelShowResult.setText("")
        self.labelShowResult.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelShowResult.setObjectName("labelShowResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.label.setText(_translate("Dialog", "Enter First Number"))
        self.label_2.setText(_translate("Dialog", "Enter Second Number"))
        self.pushButtonAdd.setText(_translate("Dialog", "+"))
        self.pushButtonSub.setText(_translate("Dialog", "-"))
        self.pushButtonMul.setText(_translate("Dialog", "*"))
        self.pushButtonDiv.setText(_translate("Dialog", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())