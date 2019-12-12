from User import User


def openConfig():
    config = open("config.json", 'w', encoding='utf-8')
    config.write("test")
    config.close()


if __name__ == '__main__':
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
