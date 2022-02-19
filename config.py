import os
import redis

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOU-WILL-NEVER-GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''
        开发模式配置
    '''
    DEBUG = True
    # MAIL_SERVER = 'smtp.qq.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'mysql+pymysql://root:77889911@192.168.3.205/DVIS'
    # redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    SESSION_TYPE = 'redis'

    # 加密
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


# class TestingConfig(Config):
#     TESTING = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
#                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
#                               'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {'development': DevelopmentConfig, 'test': '', 'production': ''}
