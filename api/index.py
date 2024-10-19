import sys
import os
from flask import Flask
from .login import login_creater
from .kittenserver import kitten_creater

app = Flask(__name__)
app.register_blueprint(login_creater, url_prefix='/login')
app.register_blueprint(kitten_creater, url_prefix='/kitten') 
app.json.ensure_ascii = False
  
@app.route("/") 
def main():   
    return '服务器正常运行中'   
  
   
