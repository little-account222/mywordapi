class PROJECT:
    NAME = "源码反编译器4"
    VERSIONS = "1.0.3"
    class AUTHOR:
        NAME = "SLIGHTNING"

def printMetaData():
    print(PROJECT.NAME)
    print(f"欢迎使用 \033[4;94m{PROJECT.NAME}\033[0m {PROJECT.VERSIONS} 版本。")
    print(f"该软件由 \033[4;94m{PROJECT.AUTHOR.NAME}\033[0m 开发。")

