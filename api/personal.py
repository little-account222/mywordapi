from flask import Blueprint, request, jsonify, make_response, render_template
from .codemao import login, comfirm_account
import re, requests
from json import loads
person_creater = Blueprint('person', __name__)

pattern = r'^Fantasy/Static/(.+)$'
ALLOWED_EXTENSIONS = {'js', 'css', 'html'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@person_creater.route('/upload',methods=['POST','GET'])
def upload_file():
    if comfirm_account(request.cookies.get('token')) == 'succ':
        if 'file' not in request.files:
            return jsonify({'active': 'failed','msg':'请上传有效文件'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'active': 'failed','msg':'请上传有效文件'})
        if file and allowed_file(file.filename):
            content = file.read().decode('utf-8')
            info = loads(requests.get(f'https://oversea-api.code.game/tiger/kitten/cdn/token/1?type={file.filename.rsplit(".", 1)[1].lower()}&prefix=Fantasy/Static&bucket=static').text)
            try:
                info = loads(requests.post('https://upload.qiniup.com/',data={'token': info['data'][0]['token'], 'key': info['data'][0]['filename']}, files={'file': content}).text)
                return jsonify({'active': 'successful', 'msg': 'https://dianmao.fantasywork.us.kg/page/'+re.match(pattern, info['filename']).group(1)})
            except KeyError:
                return jsonify({'active': 'failed', 'msg': '未知错误'+str(info)})

    else:
        return jsonify({'active': 'failed','msg':comfirm_account(request.cookies.get('token'))})

