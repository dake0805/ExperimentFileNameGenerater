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
    # TODO 新创建文件
    # if(config.readline().)
    configJson = config.read()
    data = json.loads(configJson)
    list(data['users']).append(user.to_dict())
    data = json.dumps(configJson)
    config.write(data)
