
from flask import Flask
from .login import login_creater
from ...Kitten_4 Decompiler_main.Kitten_4 Decompiler_main import Main

app = Flask(__name__)
@app.route("/")
def main():
  return "888"
app.register_blueprint(login_creater, url_prefix='/login')
app.json.ensure_ascii = False
