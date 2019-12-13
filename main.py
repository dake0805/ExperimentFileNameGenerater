from qtpy import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from ui.mainWindow import Ui_MainWindow
from ui.newUserDialog import Ui_Dialog


# def openConfig():
#     config = open("config.json", 'w', encoding='utf-8')
#     config.write("test")
#     config.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        addUserButton = AddUserButton()
        button = self.add_user_button
        button.clicked.connect(addUserButton.show)


class AddUserButton(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(AddUserButton, self).__init__()
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
