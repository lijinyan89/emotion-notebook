#!/ usr/bin/env python3
# coding=utf-8

from flask import Flask,render_template,flash,url_for,redirect,Blueprint
from flask_bootstrap import Bootstrap

from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from flask_sqlalchemy import SQLAlchemy

from note_db import insert_data, obtain_data, get_history, update

# 解决 python3.x 不适用 mysqldb Model 的bug
import pymysql
pymysql.install_as_MySQLdb()

import sys

#解决flash的一个bug
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


app = Flask(__name__)

#各项插件的配置
app.config['SECRET_KEY']='hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/eNote'#配置数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)
moment=Moment(app)
login_manger=LoginManager()
login_manger.session_protection='strong'
login_manger.login_view='eNote.login'
login_manger.init_app(app)

@login_manger.user_loader
def load_user(user_id):
    from model import Users
    return Users.query.get(int(user_id))

"""
蓝图注册
"""
def init():
    from views import eNote
    app.register_blueprint(blueprint=eNote, url_prefix='/eNote') # 调用视图函数蓝图


if __name__ == '__main__':
    init()
    app.run(port=6868, debug=True)
