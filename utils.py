import json


def loadUsers():
    config = open("config.json", 'r', encoding='utf-8')
    configJson = config.read()
    # print(configJson)
    config.close()
    data = json.loads(configJson)
    users = list(data['users'])
    return users


# TODO
def saveUser(user):
    config = open("config.json", 'r+', encoding='utf-8')
    # if(config.readline().)
    configJson = config.read()
    data = json.loads(configJson)
    config.seek(0)
    config.truncate()  # 清空文件
    a = list(data['users'])
    a.append(user.to_dict())
    data['users'] = a
    json.dump(data, config)
    config.close()


def saveUserList(userList):
    userDicList = []
    for userItem in userList:
        userDicList.append(userItem.to_dict())
    config = open("config.json", 'r+', encoding='utf-8')
    configJson = config.read()
    data = json.loads(configJson)
    config.seek(0)
    config.truncate()  # 清空文件
    data['users'] = userDicList
    json.dump(data, config)
    config.close()
