
import os
import sys
from flask import Blueprint, request, jsonify, make_response, render_template, Response
from api.codemao import login, get_user_detail
import json
current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)
main_module_path = os.path.join(current_dir_path, '..', 'Kitten-4-Decompiler-main', 'Kitten-4-Decompiler-main')
if main_module_path not in sys.path:
    sys.path.append(main_module_path)

import Main

kitten_creater = Blueprint('kitten', __name__)
@kitten_creater.route('/get_work',methods=['GET'])
def get_work_code():
    file_content = Main.main(request.args.get('workid'))
    json_string = json.dumps(file_content)

    def generate():
        yield json_string.encode('utf-8')

    return Response(generate(), mimetype='application/octet-stream', headers={
        'Content-Disposition': 'attachment; filename=data.bcmc'
    })
