import json
import traceback

from CommunityAPI import *
from KittenDecompiler import KittenWorkDecompiler
from CoCoDecompiler import CoCoWorkDecompiler
from MetaData import *
from Tool import showError
from UI import *
from HTTP import HTTP

def main():
    printMetaData()

    workID = UI.askInteger("请输入要反编译的作品 ID")

    workInfo = getWorkInfo(workID)
    log(INFO, f"成功获取作品 \033[4;32m{workInfo['name']}\033[0m 的信息。")
    log(INFO, f"该作品由 \033[4;94m{workInfo['type']}\033[0m {workInfo['version']} 版本制作")

    compiledWorkURL = getCompiledWorkURL(workInfo)
    log(INFO, f"成功获取作品 \033[4;32m{workInfo['name']}\033[0m 的编译文件 URL。")

    compiledWork = HTTP.getJSON(compiledWorkURL)
    log(INFO, f"成功获取作品 \033[4;32m{workInfo['name']}\033[0m 的编译文件。")

    try:
        decompiler = {
            "KITTEN4": KittenWorkDecompiler,
            "KITTEN3": KittenWorkDecompiler,
            "KITTEN2": KittenWorkDecompiler,
            "COCO": CoCoWorkDecompiler,
        }[workInfo["type"]](workInfo, compiledWork)
        decompiler.onStart = lambda: log(INFO, f"开始反编译，作品名称：\033[4;32m{workInfo['name']}\033[0m。")
        def setActorLog(actor):
            actor.onPrepare = lambda: log(VERBOSE, f"正在准备角色 \033[4;32m{actor.actor['name']}\033[0m……")
            actor.onPrepareFunction = lambda name: log(VERBOSE, f"正在准备函数 \033[4;32m{name}\033[0m ……")
            actor.onStart = lambda: log(VERBOSE, f"正在反编译角色 \033[4;32m{actor.actor['name']}\033[0m……")
            actor.onStartFunction = lambda name: log(VERBOSE, f"正在反编译函数 \033[4;32m{name}\033[0m……")
        decompiler.onCreateActor = setActorLog
        decompiler.onPrepareActors = lambda: log(INFO, "正在准备角色……")
        decompiler.onStartActors = lambda: log(INFO, "正在反编译角色……")
        decompiler.onWriteWorkInfo = lambda: log(INFO, "正在清理……")
        decompiler.onClean = lambda: log(INFO, "正在写入作品信息……")
        decompiler.onFinish = lambda: log(INFO, "反编译完成。")
        decompiler.start()
    except:
        showError("反编译失败。", traceback.format_exc())
    return compiledWork

