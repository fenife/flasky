"""
hello.py

使用Flask-Moment本地化日期和时间
"""

from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# 初始化
app = Flask(__name__)

# 使用扩展模块Flask-Script支持命令行选项
manager = Manager(app)

# 初始化Flask-Script
bootstrap = Bootstrap(app)

# 初始化Flask-Moment
moment = Moment(app)

# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# URL和视图函数的映射关系（路由）
@app.route('/')
def index():
    """ 程序URL根地址'/'的响应函数 """
    return render_template('index.html',
            current_time=datetime.utcnow())

# 支持URL的动态参数
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# 启动服务器
if __name__ == '__main__':
    manager.run()
