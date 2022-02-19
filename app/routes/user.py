import hashlib
from ..base import base
from flask import request, jsonify
from app.models import User
from app import db
from flask_login import login_user
import uuid


@base.route('/login', methods=['POST'])
def login():
    #检查用户名是否存在
    user = User.query.filter_by(USERNAME=request.form['username']).first()

    if user is not None:
        md = hashlib.md5()
        #提交的密码MD5加密
        md.update(request.form.get('password').encode('utf-8'))
        #MD5加密后的内容同数据库密码比较

        print(user.PASSWORD, md.hexdigest())
        if md.hexdigest() == user.PASSWORD:
            login_user(user)
            return jsonify({'success': True, 'msg': 'Secessfully login'})
    return jsonify({'success': False, 'msg': 'password error', 'status': 200})


@base.route('/register', methods=['POST'])
def register():
    # print(request.form.get('username'))
    if User.query.filter_by(USERNAME=request.form.get('username')).first():
        return jsonify({'success': False, 'msg': '用户名已存在!'})

    # TODO 用户名密码校验

    user = User()

    user.UID = str(uuid.uuid4())

    md = hashlib.md5()
    md.update(request.form.get('password').encode('utf-8'))
    user.PASSWORD = md.hexdigest()

    # user.NAME = request.form.get('name')
    user.USERNAME = request.form.get('username')
    # user.SEX = request.form.get('sex')
    # user.PHOTO = request.form.get('photo')

    # add current use to new user
    #current_user.roles.append(user)

    db.session.add(user)

    return jsonify({'success': True, 'msg': '新建用户成功!', 'status': 200})