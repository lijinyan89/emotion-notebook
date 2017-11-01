#！urs/bin/env python3
# coding=utf-8

from  flask import render_template, Blueprint, redirect, url_for, flash, request
from run import login_manger
from form import Login_Form, Register_Form
from model import  Users
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required
from run import db
import time

from note_db import insert_data, obtain_data, get_history, update
from rad import rand

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


eNote=Blueprint('eNote', __name__, template_folder='templates')  #蓝图

@eNote.route('/login', methods=['GET'])
def index():
    form=Login_Form()
    return render_template('login.html', form=form)


@eNote.route('/login',methods=['POST'])
def login():
        form=Login_Form()
        if form.validate_on_submit():
            user=Users.query.filter_by(username=form.name.data).first()
            if user is not  None and user.password==form.pwd.data:
                login_user(user)
                flash('登录成功')
                return  render_template('hello.html', name=form.name.data)
            else:
                flash('用户或密码错误')
                return render_template('login.html', form=form)

#用户登出
@eNote.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('eNote.index'))


@eNote.route('/register', methods=['GET','POST'])
def register():
    form=Register_Form()
    if form.validate_on_submit():
        user=Users(username=form.name.data, password=form.pwd.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('eNote.index'))
    return render_template('register.html', form=form)

#from graduation

@eNote.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('start.html')

@eNote.route('/start', methods = ['GET', 'POST'])
def start():
    return render_template('index.html', date = date)

@eNote.route('/write', methods = ['GET', 'POST'])
def record():
    name = request.args.get('name')
    event = request.args.get('event')

    scenes = request.args.get('scenes')
        # 把列表转换为字符串，字符串相加
    relationship = '/'.join(request.values.getlist("relationship"))
    mood = '/'.join(request.values.getlist("mood"))
    mood_t = '    '.join(request.values.getlist("mood"))
    feel = '/'.join(request.values.getlist("feel"))
    user_write = "在{}，{}，我感到{}，{},".format(scenes, event, mood, feel)

    ent = ' '.join(request.values.getlist('ent'))

    reason = request.args.get("reason")

    understanding = request.args.get("understanding")

    next_write = "{}，我做了（想做）{}，\n我的理解：{}".format(user_write, ent, understanding)

    encour = rand()
    if request.args.get('submit') == "完成":

        insert_data(name, date, next_write)
        return render_template('sex.html', encour = encour, mood_t = mood_t)


@eNote.route('/404', methods = ["GET", "POST"])
def back():
    if request.args.get('submit') == "返回":
        return render_template('index.html')

@eNote.route('/note', methods = ["GET", "POST"])
def note():
    if request.args.get('submit') == "返回":
        return render_template('index.html', date = date)

@eNote.route('/happy', methods = ["GET", "POST"])
def happy():
    return render_template("happy.html", date = date)

@eNote.route('/end', methods = ["GET", "POST"])
def next():
    if request.args.get('submit') == "完成":
        name = request.args.get('name')
        happy_thing = request.args.get("happy_thing")
        insert_data(name, date, happy_thing)
        return render_template('recording_happy.html')

@eNote.route('/recording', methods = ["GET", "POST"])
def recording():
    if request.args.get('submit') == "返回":
        return render_template('index.html', date = date)

@eNote.route('/one', methods = ["GET", "POST"])
def history():
    history = get_history()
    return render_template('oneself.html', history = history)

@eNote.route('/online', methods = ["GET", "POST"])
def online():
    if request.args.get('submit') == "返回":
        return render_template('index.html')
