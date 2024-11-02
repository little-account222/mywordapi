from flask import Blueprint, request, jsonify, make_response, render_template
from .codemao import login, comfirm_account
import re, requests, os
from json import loads
person_creater = Blueprint('person', __name__)

pattern = r'^Fantasy/Static/(.+)$'
ALLOWED_EXTENSIONS = {'js', 'css', 'html', 'bcm4', 'exe', 'png', 'jpeg', 'xls', 'xlsx', 'txt', 'jsx', 'htm'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@person_creater.route('/upload', methods=['POST'])
def upload_file():
    if comfirm_account(request.cookies.get('token')) == 'succ':
        if 'file' not in request.files:
            return jsonify({'active': 'failed', 'msg': '请上传有效文件'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'active': 'failed', 'msg': '请上传有效文件'})
        
        # 检查文件扩展名是否在允许的范围内
        if file and allowed_file(file.filename):
            # 定义允许以 utf-8 读取的文件类型
            TEXT_FILE_TYPES = {'htm', 'html', 'css', 'js', 'jsx'}
            extension = file.filename.rsplit('.', 1)[1].lower()
            
            if extension in TEXT_FILE_TYPES:
                # 对于特定的文本文件类型，使用 utf-8 解码
                content = file.read().decode('utf-8')
            else:
                # 对于其他类型的文件，不需要解码，直接获取原始数据
                content = file.read()

            # 获取上传所需的 token 和其他信息
            info = loads(requests.get(f'https://oversea-api.code.game/tiger/kitten/cdn/token/1?type={extension}&prefix=Fantasy/Static&bucket=static').text)
            try:

                response = requests.post('https://upload.qiniup.com/',
                                        data={'token': info['data'][0]['token'], 'key': info['data'][0]['filename']},
                                        files={'file': (info['data'][0]['filename'], content)})
                info = loads(response.text)
                return jsonify({'active': 'successful', 'msg': f'https://dianmao.fantasywork.us.kg/person/page/{re.match(pattern, info["key"]).group(1)}'})
            except KeyError:
                return jsonify({'active': 'failed', 'msg': '未知错误'})
        else:
            return jsonify({'active': 'failed', 'msg': '不支持此格式的文件'})
    else:
        return jsonify({'active': 'failed', 'msg': comfirm_account(request.cookies.get('token'))})
@person_creater.route('/page/<pageid>', methods=['GET'])
def return_page(pageid):
    _, file_extension = os.path.splitext(pageid)
    file_extension = file_extension.lower()

    # 打印调试信息
    print(type(pageid.split('.')[1]), pageid.split('.')[1])

    url = 'https://static.codemao.cn/Fantasy/Static/' + pageid
    _response = requests.get(url)

    # 检查是否需要解码为 UTF-8
    if file_extension in ['.html', '.htm', '.js', '.jsx', '.css']:
        _response.encoding = 'utf-8'  # 设置编码为 utf-8
        content = _response.text  # 使用文本形式的内容
    else:
        content = _response.content  # 使用原始的二进制内容

    # 创建响应对象
    response = make_response(content)

    # 根据 file_extension 设置 Content-Type 头
    if file_extension in ['.html', '.htm']:
        response.headers["Content-Type"] = "text/html; charset=utf-8"
    elif file_extension in ['.js', '.jsx']:
        response.headers["Content-Type"] = "application/javascript; charset=utf-8"
    elif file_extension in ['.css']:
        response.headers["Content-Type"] = "text/css; charset=utf-8"
    else:
        response.headers["Content-Type"] = "application/octet-stream"

    return response
@person_creater.route('/',methods=['GET'])
def main_page():
    return render_template('upload.html')
