from flask import Blueprint, request, jsonify, make_response, render_template
from codemao import login, get_user_detail, comfirm_account, post_comment

attack_creater = Blueprint('login', __name__)


@attack_creater.route('/dom/post/<int:pid>',methods=['GET'])
def attack_dom_post(pid):
    active = comfirm_account(request.cookies.get('token'))
    if active == 'succ':
        post_comment(pid,token)
        return jsonify({'active':'successful'})
    else:
      return jsonify({'active':'failed','msg':active})
