import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config
from flask_login import LoginManager  # Flask-Login 为 Flask 提供对用户 session 的管理。它能够处理登录，注销和长时间记住用户 session 等常用任务。
from app.utils.index import JSONEncoder

db = SQLAlchemy()
redis_store = None
loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
# loginmanager.login_view = 'base.login'


def create_app(config_tpye: str):
    '''
        TODO 做请求前拦截，发布JWT
        参考 https://cloud.tencent.com/developer/article/1604025#:~:text=flask%20%E4%B8%AD%E6%80%8E%E4%B9%88%E5%AE%9E%E7%8E%B0%E5%AF%B9%20url%20%E8%AF%B7%E6%B1%82%E7%9A%84%E6%8B%A6%E6%88%AA%20%EF%BC%9F%201%E3%80%81%E6%8B%A6%E6%88%AA%E5%99%A8%EF%BC%9A%E5%8F%AF%E4%BB%A5%E6%8B%A6%E6%88%AA%E6%89%80%E6%9C%89URL%E8%AF%B7%E6%B1%82%EF%BC%8C%E5%8D%B3%E5%8F%AA%E8%A6%81%E6%9C%89%20url%20%E8%AF%B7%E6%B1%82,%E6%9D%A5%E5%AE%8C%E6%88%90%20%EF%BC%8C%20%E5%AF%B9%E6%89%80%E6%9C%89%20url%20%E8%AF%B7%E6%B1%82%E8%BF%9B%E8%A1%8C%E6%8B%A6%E6%88%AA%20%EF%BC%8C%20%E6%88%91%E4%BB%AC%E9%9C%80%E8%A6%81%E5%9C%A8%E5%90%AF%E5%8A%A8%E7%A8%8B%E5%BA%8F%EF%BC%88app.py%EF%BC%89%E4%B8%AD%E8%BF%9B%E8%A1%8C%E6%8B%A6%E6%88%AA%20%E3%80%82
    '''
    from .base import base
    # from app import db

    app = Flask(__name__)
    app.json_encoder = JSONEncoder
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