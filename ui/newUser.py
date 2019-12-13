# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 643)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.studentId = QtWidgets.QLineEdit(Dialog)
        self.studentId.setGeometry(QtCore.QRect(110, 110, 113, 21))
        self.studentId.setObjectName("studentId")
        self.classId = QtWidgets.QLineEdit(Dialog)
        self.classId.setGeometry(QtCore.QRect(100, 190, 113, 21))
        self.classId.setObjectName("classId")
        self.studentName = QtWidgets.QLineEdit(Dialog)
        self.studentName.setGeometry(QtCore.QRect(110, 150, 113, 21))
        self.studentName.setObjectName("studentName")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
