from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 定义模型
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
@app.route("/")
def main():
    db.create_all()

# 添加待办事项路由（使用GET方法）
@app.route('/add', methods=['GET'])
def add_todo():
    task = request.args.get('task', '')
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('todos'))

# 显示待办事项路由
@app.route('/todos')
def todos():
    todos = Todo.query.all()
    todo_list_html = '<h1>Todo List</h1><ul>'
    for todo in todos:
        todo_list_html += f'<li>{todo.task} <a href="{url_for("delete", todo_id=todo.id)}">Delete</a></li>'
    todo_list_html += '</ul>'
    return todo_list_html

# 删除待办事项路由
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todo.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('todos'))
