from flask import Blueprint, request, jsonify, make_response, render_template
from codemao import login

login_creater = Blueprint('login', __name__)


@login_creater.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            username = request.json['username']
            password = request.json['password']
        except KeyError:
            return jsonify({'active':'failed','msg':'确保参数均为已填'})
        token = login(username,password)
        if token:
            response = make_response(jsonify({'active':'successful','msg':token}))
            response.set_cookie('token', token, max_age=60 * 60 * 24 * 3)
            return response
        else:
            return jsonify({'active':'failed','msg':'账号或密码错误'})
    if request.method == 'GET':
        return render_template('login.html')
