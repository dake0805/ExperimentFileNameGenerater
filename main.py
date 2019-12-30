from random import random

from PyQt5.QtCore import Qt
from qtconsole.qt import QtCore
from qtpy import QtWidgets
from PyQt5.QtWidgets import *
import sys

import utils
from User import User
from ui.mainWindow import Ui_MainWindow
from ui.newUserDialog import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 添加用户 按钮
        button = self.add_user_button
        button.clicked.connect(self.showDialog)

        # 已选择的用户
        self.checkUserList = []

        # 已有用户列表
        self.initUserTable()
        # 选择列表click
        self.toChooseListInit()

    def showDialog(self):
        self.addUserDialog = AddUserDialog(self)
        self.addUserDialog.setWindowTitle('对话框')
        self.addUserDialog.setWindowModality(Qt.ApplicationModal)
        self.addUserDialog.show()

    def initUserTable(self):
        # 设置表格属性
        table = self.tableWidget
        table.setFrameShape(QFrame.NoFrame)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可更改
        table.setSelectionMode(QAbstractItemView.NoSelection)
        # 加载用户
        self.loadUser()

    def tableAddLine(self, newUser):
        user = User(newUser["studentId"], newUser["name"], newUser["classId"])
        table = self.tableWidget
        row = table.rowCount()
        table.setRowCount(row + 1)
        studentId = user.studentId
        name = user.name
        classId = user.classId
        ##下面六行用于生成居中的checkbox，不知道有没有别的好方法
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        table.setItem(row, 0, QTableWidgetItem(name))
        table.setItem(row, 1, QTableWidgetItem(studentId))
        table.setItem(row, 2, QTableWidgetItem(classId))
        table.setCellWidget(row, 3, w)
        self.checkUserList.append([name, studentId, classId, ck])

    def loadUser(self):
        users = utils.loadUsers()
        # 清空准备重新更新
        self.checkUserList = []
        self.tableWidget.setRowCount(0)
        for user in users:
            self.tableAddLine(user)

    # click绑定可选择按钮
    # TODO 自定义，弹出Dialog完成自定义输入
    def toChooseListInit(self):
        studentIdButton = self.choose_studentId
        classIdButton = self.choose_classId
        nameButton = self.choose_name
        customButton = self.choose_custom
        clearButton = self.clear_choose_button
        removeButton = self.remove_user_button
        studentIdButton.clicked.connect(self.clickChooseStudent)
        classIdButton.clicked.connect(self.clickChooseClassId)
        nameButton.clicked.connect(self.clickChooseName)
        customButton.clicked.connect(self.clickChooseCustom)
        clearButton.clicked.connect(self.clickClear)
        removeButton.clicked.connect(self.clickRemoveUser)
        self.generate_result_button.clicked.connect(self.generateResult)

    def clickChooseStudent(self):
        self.choose_form.addItem("studentId")

    def clickChooseClassId(self):
        self.choose_form.addItem("classId")

    def clickChooseName(self):
        self.choose_form.addItem("name")

    def clickChooseCustom(self):
        text, okPressed = QInputDialog.getText(self, "自定义", "Input:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.choose_form.addItem(text)

    def clickClear(self):
        chooseList = self.choose_form
        if chooseList.currentRow() == -1:
            chooseList.clear()
        else:
            chooseList.takeItem(chooseList.currentRow())

    def clickRemoveUser(self):
        saveUserList = []
        for userItem in self.checkUserList:
            if not userItem[3].isChecked():
                saveUserList.append(User(userItem[1], userItem[0], userItem[2]))
        utils.saveUserList(saveUserList)
        self.loadUser()

    # TODO 从choose_form得到已选，生成结果
    # TODO 读取已选的用户列表check box
    def generateResult(self):
        global result
        choosedKindList = []
        for i in range(self.choose_form.count()):
            choosedKindList.append(self.choose_form.item(i).text())
        for useritem in self.checkUserList:
            if useritem[3].isChecked():
                self.textbrowser.sethtml("")
                break
        for userItem in self.checkUserList:
            if userItem[3].isChecked():
                userInfoArray = []
                for choosedInfo in choosedKindList:
                    if choosedInfo == "name":
                        userInfoArray.append(userItem[0])
                    elif choosedInfo == "studentId":
                        userInfoArray.append(userItem[1])
                    elif choosedInfo == "classId":
                        userInfoArray.append(userItem[2])
                    else:
                        userInfoArray.append(choosedInfo)
                    result = self.choose_delimiter.currentText().join(userInfoArray)
                self.textBrowser.append(result)

        # def clickChooseCustom(self):
    #     # self.chooseList.append("studentId")
    #     # self.choosed_label.text() + "  "


class AddUserDialog(QDialog, Ui_Dialog):

    def __init__(self, mainWindow, parent=None, ):
        self.mainWindow = mainWindow
        super(AddUserDialog, self).__init__(parent)
        self.setupUi(self)
        add = self.add_user
        cancel = self.cancel
        add.clicked.connect(self.addUser)
        cancel.clicked.connect(self.close)

    def addUser(self):
        user = User(self.student_id.text(), self.name.text(), self.class_id.text())
        utils.saveUser(user)
        self.mainWindow.loadUser()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

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
