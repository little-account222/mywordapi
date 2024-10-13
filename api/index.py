from flask import Flask
import threading
import time

app = Flask(__name__)

# 定义全局变量
a = 0

def increment_a():
    global a
    while True:
        a += 1
        time.sleep(1)  # 等待1秒钟

@app.route("/")
def main():
    return f"Counter: {a}666"
thread = threading.Thread(target=increment_a)
thread.start()

