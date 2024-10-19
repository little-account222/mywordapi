
from flask import Flask
from .login import login_creater
# 在 ./api/index.py 文件中

import sys
import os

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)

# 获取当前文件所在目录的路径
current_dir_path = os.path.dirname(current_file_path)

# 计算到 Main.py 文件的相对路径
main_module_path = os.path.join(current_dir_path, '..', 'Kitten-4-Decompiler-main', 'Kitten-4-Decompiler-main')

# 确保该路径不在 sys.path 中
if main_module_path not in sys.path:
    sys.path.append(main_module_path)

# 现在可以导入 Main 模块
import Main

# 你现在可以使用 Main 模块中的任何函数或类 
# 例如：Main.some_function()


app = Flask(__name__)
@app.route("/")
def main():
  return Main.main(240362475)


@app.route("/z")
def main():
  return "6666"
app.register_blueprint(login_creater, url_prefix='/login')
app.json.ensure_ascii = False
