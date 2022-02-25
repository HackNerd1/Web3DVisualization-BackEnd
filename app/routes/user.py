from flask_login import login_user
from flask import request, jsonify
from app.models import User
from ..base import base
from app import db
import hashlib
import uuid


@base.route('/login', methods=['POST'])
def login():
    '''
    检查用户名是否存在
    '''
    user = User.query.filter_by(USERNAME=request.form['username']).first()

    if user is not None:
        md = hashlib.md5()  #提交的密码MD5加密
        md.update(
            request.form.get('password').encode('utf-8'))  #MD5加密后的内容同数据库密码比较
        if md.hexdigest() == user.PASSWORD:
            login_user(user)
            return jsonify({'code': 201, 'msg': 'Secessfully login'})

    return jsonify({'code': 400, 'msg': 'Invalid username or password'})


@base.route('/register', methods=['POST'])
def register():
    if User.query.filter_by(USERNAME=request.form.get('username')).first():
        return jsonify({'code': 403, 'msg': '用户名已存在!'})

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

    return jsonify({'code': 200, 'msg': '新建用户成功!'})