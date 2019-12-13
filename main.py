from qtpy import QtWidgets

from User import User
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from ui.mainWindow import Ui_MainWindow
from ui.newUserDialog import Ui_Dialog

global MainWindow
global mainWindowUI


def openConfig():
    config = open("config.json", 'w', encoding='utf-8')
    config.write("test")
    config.close()


# def addUserClick():


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    mainWindowUI = Ui_MainWindow()
    mainWindowUI.setupUi(MainWindow)
    MainWindow.show()
    newUserDialogUI = Ui_Dialog()
    dialog = QtWidgets.QDialog()
    newUserDialogUI.setupUi(dialog)
    button = mainWindowUI.add_user_button
    button.clicked.connect(dialog.show)

    # addUserClick()
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
