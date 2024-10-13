from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# 定义全局变量
a = 0

@app.route("/")
def main():
    global a  # 声明a为全局变量
    a += 1
    return f"Counter: {a}"

@app.route("/z")
def add():
    # 返回a的当前值，并确保它是字符串
    return str(a)
