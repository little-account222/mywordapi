import random

def askYesNot(text):
    return input(f"{text}(y/n)：").lower() in {"y", "yes"}

def showError(message, info):
    print(f"\033[1;7;91m错误\033[0;1;91m：{message}\033[0m")

    print(info)
    raise

def randomBlockID():
    return ''.join([random.choice('0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ') for i in range(20)])
