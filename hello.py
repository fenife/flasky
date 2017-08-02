"""
hello.py
了解Flask框架程度的基本结构
"""

from flask import Flask
from flask_script import Manager

# 初始化
app = Flask(__name__)

# 使用扩展模块Flask-Script支持命令行选项
manager = Manager(app)

# URL和视图函数的映射关系（路由）
@app.route('/')
def index():
    """ 程序URL根地址'/'的响应函数 """
    return '<h1>Hello World!</h1>'

# 支持URL的动态参数
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1> ' % name

# 启动服务器
if __name__ == '__main__':
    manager.run()
