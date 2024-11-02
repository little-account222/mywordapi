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
    if confirm_account(request.cookies.get('token')) == 'succ':
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
                # 上传文件到指定的位置
                if isinstance(content, str):
                    # 如果内容是字符串，则需要将其转换为字节
                    content = content.encode('utf-8')
                response = requests.post('https://upload.qiniup.com/',
                                        data={'token': info['data'][0]['token'], 'key': info['data'][0]['filename']},
                                        files={'file': (info['data'][0]['filename'], content)})
                info = loads(response.text)
                return jsonify({'active': 'successful', 'msg': f'https://dianmao.fantasywork.us.kg/person/page/{re.match(r".*/(.*)", info["key"]).group(1)}'})
            except KeyError:
                return jsonify({'active': 'failed', 'msg': '未知错误'})
        else:
            return jsonify({'active': 'failed', 'msg': '不支持此格式的文件'})
    else:
        return jsonify({'active': 'failed', 'msg': confirm_account(request.cookies.get('token'))})
@person_creater.route('/page/<pageid>', methods=['GET'])
def return_page(pageid):
    _, file_extension = os.path.splitext(pageid)
    file_extension = file_extension.lower()

    print(type(pageid.split('.')[1]), pageid.split('.')[1])

    _content = requests.get('https://static.codemao.cn/Fantasy/Static/' + pageid)

    response = make_response(_content.text)

    # 根据 pageid 的扩展名设置 Content-Type 头
    if file_extension in ['.html', '.htm', '.js', '.jsx', '.css']:
        _content.encoding = 'utf-8'  # 对于 HTML, CSS, JS 文件设置编码为 utf-8
        if file_extension in ['.html', '.htm']:
            response.headers["Content-Type"] = "text/html"
        elif file_extension in ['.js', '.jsx']:
            response.headers["Content-Type"] = "application/javascript"
        elif file_extension in ['.css']:
            response.headers["Content-Type"] = "text/css"
    else:
        response.headers["Content-Type"] = "application/octet-stream"  # 对于其他类型的文件使用二进制流类型
    return response
@person_creater.route('/',methods=['GET'])
def main_page():
    return render_template('upload.html')
