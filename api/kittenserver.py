
import os
import sys
from flask import Blueprint, request, jsonify, make_response, render_template, Response
from api.codemao import login, get_user_detail
from flask_limiter import Limiter
import json
current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
main_module_path = os.path.join(current_dir_path, '..', 'Kitten-4-Decompiler-main', 'Kitten-4-Decompiler-main')
if main_module_path not in sys.path:
    sys.path.append(main_module_path)

import Main

kitten_creater = Blueprint('kitten', __name__)


limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
@kitten_creater.route('/get_work',methods=['GET'])
@limiter.limit("1 per hour")
def get_work_code():
    token = request.cookies.get('token')
    if token is None:
        return jsonify({'active':'failed','msg':'请先登录'})
    try:
        if get_user_detail(token)['nickname'] != '':
            file_content = Main.main(request.args.get('workid'))
            json_string = json.dumps(file_content)

            def generate():
                yield json_string.encode('utf-8')

            return Response(generate(), mimetype='application/octet-stream', headers={
                'Content-Disposition': 'attachment; filename=data.bcm4'
            })
    except KeyError:
        return jsonify({'active':'failed','msg':'登录过期，重新登录'})

