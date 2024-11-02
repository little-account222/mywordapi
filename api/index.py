import sys
import os
from flask import Flask, request, render_template, jsonify
from .login import login_creater 
from .kittenserver import kitten_creater
from .attack import attack_creater    
from .personal import person_creater   
from .codemao import comfirm_account   
from json import loads   
import requests      
   
    
app = Flask(__name__)   
app.register_blueprint(login_creater, url_prefix='/login') 
app.register_blueprint(kitten_creater, url_prefix='/kitten')
app.register_blueprint(attack_creater, url_prefix='/attack')
app.register_blueprint(person_creater, url_prefix='/person')
app.json.ensure_ascii = False 


@app.route("/")
def main():
    token = request.cookies.get('token')
    if comfirm_account(token) == 'succ':
        info = loads(requests.get('https://api.codemao.cn/creation-tools/v1/user/center/honor',headers={'cookie':'authorization='+token}).text)
        return render_template('home.html',info=info)
    else:
        return render_template('unlogin.html')
