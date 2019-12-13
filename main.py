from User import User
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui import mainUI


def openConfig():
    config = open("config.json", 'w', encoding='utf-8')
    config.write("test")
    config.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    openConfig()

    studentId = input("学号：")
    name = input("姓名：")
    classId = input("班号：")

    user = User(studentId, name, classId)

    delimiter = input("分隔符：")

    array = []

    array.append(user.studentId)
    array.append(user.name)

    result = delimiter.join(array)
    print(result)


