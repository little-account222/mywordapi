from flask import Blueprint, request, jsonify, make_response, render_template
from .codemao import login, get_user_detail, comfirm_account, post_comment, invite_user
from flask_cors import cross_origin  # 只需要导入cross_origin
attack_creater = Blueprint('attack', __name__)


@attack_creater.route('/dom/post/more/<int:pid>',methods=['GET'])
def attack_dom_post(pid):
    active = comfirm_account(request.cookies.get('token'))
    if active == 'succ':
        post_comment(pid,request.cookies.get('token'))
        return jsonify({'active':'successful'})
    else:
      return jsonify({'active':'failed','msg':active})

info_list = {'clsid':0,'token':''}
@attack_creater.route('/class/info')
def get_info():
    return jsonify(info_list)

@attack_creater.route('/class/info/edit/')
def edit_info():
    info_list = {'clsid':int(request.args.get('clsid')),'token':str(request.args.get('token'))}
    return jsonify(info_list)

@attack_creater.route('/invite')
@cross_origin(origins='https://coco.codemao.cn/')  # 在路由级别启用跨域支持
def invite():
    invite_user(request.args.get('username'))
    return 'ok'
