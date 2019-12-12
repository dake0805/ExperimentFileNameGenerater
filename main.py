from User import User

if __name__ == '__main__':
    studentId = input("学号：")
    name = input("姓名：")
    classId = input("班号：")

    user = User(studentId, name, classId)

    delimiter = input("分隔符：")

    array = []

    array.append(user.studentId)
    array.append(user.name)

    result = ""

    for index in range(len(array)):
        result += array[index] + delimiter

    print(result)