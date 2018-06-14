#!/usr/bin/env python3
# coding=utf-8

from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from run import login_manger
from run import db

class Users(UserMixin, db.Model):
    __tablename__ = 'user' # 对应 MySql 数据表
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False