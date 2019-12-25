import json


def loadUsers():
    config = open("config.json", 'r', encoding='utf-8')
    configJson = config.read()
    # print(configJson)
    config.close()
    data = json.loads(configJson)
    users = list(data['users'])
    return users
