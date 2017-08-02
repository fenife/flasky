"""
hello.py

重定向和用户会话
"""

from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# 初始化
app = Flask(__name__)
# 设置Flask-WTF
app.config['SECRET_KEY'] = 'hard to guess string'

# 使用扩展模块Flask-Script支持命令行选项
manager = Manager(app)

# 初始化Flask-Script
bootstrap = Bootstrap(app)

# 初始化Flask-Moment
moment = Moment(app)


# 定义表单类
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# URL和视图函数的映射关系（路由）
@app.route('/', methods=['GET', 'POST'])
def index():
    """ 程序URL根地址'/'的响应函数 """

    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))   # 重定向URL
    return render_template('index.html', form=form, name=session.get('name'))


# 启动服务器
if __name__ == '__main__':
    manager.run()
