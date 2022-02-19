import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config
from flask_login import LoginManager  # Flask-Login 为 Flask 提供对用户 session 的管理。它能够处理登录，注销和长时间记住用户 session 等常用任务。

db = SQLAlchemy()
redis_store = None
loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'base.login'


def create_app(config_tpye: str):
    from .base import base
    # from app import db

    app = Flask(__name__)
    '''
        配置文件
    '''
    app.config.from_object(config[config_tpye])
    loginmanager.init_app(app)
    db.init_app(app)

    redis_store = redis.StrictRedis(config[config_tpye].REDIS_HOST,
                                    config[config_tpye].REDIS_PORT)
    Session(app)

    app.register_blueprint(base)

    return app


if __name__ == '__main__':
    app = create_app()
    print(CSRFProtect)
    print(Session)