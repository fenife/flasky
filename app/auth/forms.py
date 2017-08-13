from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('再次确认密码', validators=[Required()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('此邮箱已经注册！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('此用户名已经被使用！')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[Required()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('再次确认密码', validators=[Required()])
    submit = SubmitField('修改密码')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField('密码重置')


class PasswordResetForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField('新密码', validators=[
        Required(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('再次确认密码', validators=[Required()])
    submit = SubmitField('修改密码')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不可用')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[Required(), Length(1, 64),
                                                 Email()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('更改邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('此邮箱已经被注册。')
