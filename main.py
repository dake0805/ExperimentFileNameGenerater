from random import random

from PyQt5.QtCore import Qt
from qtpy import QtWidgets
from PyQt5.QtWidgets import *
import sys

import utils
from ui.mainWindow import Ui_MainWindow
from ui.newUserDialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 添加用户 按钮
        button = self.add_user_button
        button.clicked.connect(self.showDialog)

        # 已有用户列表
        self.loadUserTable()

    def showDialog(self):
        # self.setWindowModality(Qt.ApplicationModal)
        self.addUserDialog = AddUserDialog()
        self.addUserDialog.setWindowTitle('对话框')
        self.addUserDialog.setWindowModality(Qt.ApplicationModal)
        self.addUserDialog.show()

    def loadUserTable(self):
        # 设置表格属性
        table = self.tableWidget
        table.setFrameShape(QFrame.NoFrame)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可更改
        table.setSelectionMode(QAbstractItemView.NoSelection)
        # 加载用户
        self.loadUser()

    def tableAddLine(self, user):
        table = self.tableWidget
        row = table.rowCount()
        table.setRowCount(row + 1)
        id = str(1)
        ##下面六行用于生成居中的checkbox，不知道有没有别的好方法
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        name = "testName"
        table.setItem(row, 0, QTableWidgetItem(id))
        table.setCellWidget(row, 1, w)
        table.setItem(row, 2, QTableWidgetItem(name))

    def loadUser(self):
        users = utils.loadUsers()
        for user in users:
            self.tableAddLine(user)


class AddUserDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

    # openConfig()
    #
    # studentId = input("学号：")
    # name = input("姓名：")
    # classId = input("班号：")
    #
    # user = User(studentId, name, classId)
    #
    # delimiter = input("分隔符：")
    #
    # array = []
    #
    # array.append(user.studentId)
    # array.append(user.name)
    #
    # result = delimiter.join(array)
    # print(result)
