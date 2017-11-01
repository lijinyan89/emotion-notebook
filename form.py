#!/usr/bin/env python3
# coding=utf-8


from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import  Required
from flask_wtf import FlaskForm

#登录表单
class Login_Form(FlaskForm):
    name=StringField(u'用户名', validators=[Required()])
    pwd=PasswordField(u'密码', validators=[Required()])
    submit=SubmitField(u'登录')


#注册表单
class Register_Form(FlaskForm):
    name=StringField(u'用户名', validators=[Required()])
    pwd=PasswordField(u'密码', validators=[Required()])
    submit=SubmitField(u'注册')