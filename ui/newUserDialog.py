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
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 230, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_user = QtWidgets.QPushButton(self.layoutWidget)
        self.add_user.setObjectName("add_user")
        self.horizontalLayout.addWidget(self.add_user)
        self.cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 160, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.student_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.student_id.setObjectName("student_id")
        self.verticalLayout.addWidget(self.student_id)
        self.class_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.class_id.setObjectName("class_id")
        self.verticalLayout.addWidget(self.class_id)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add_user.setText(_translate("Dialog", "ADD"))
        self.cancel.setText(_translate("Dialog", "CANCEL"))
