# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newUserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.student_id = QtWidgets.QLineEdit(Dialog)
        self.student_id.setGeometry(QtCore.QRect(40, 40, 113, 21))
        self.student_id.setObjectName("student_id")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(90, 100, 195, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_user = QtWidgets.QPushButton(self.widget)
        self.add_user.setObjectName("add_user")
        self.horizontalLayout.addWidget(self.add_user)
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_user.setText(_translate("Dialog", "ADD"))
        self.cancel.setText(_translate("Dialog", "CANCEL"))
