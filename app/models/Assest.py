from app import db
from datetime import datetime


class Group(db.Model):
    __tablename__ = 'PGROUP'
    GID = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    ISDELETED = db.Column(db.Integer, default=0)
    NAME = db.Column(db.String(100), default=None)
    ICON = db.Column(db.String(100), default=None)
    UID = db.Column(db.String(36))

    # EMPLOYDATE = db.Column(db.DATETIME, default=datetime.now)

    # organizations = db.relationship('Organization',
    #                                 secondary=user_organization_table,
    #                                 backref=db.backref('users', lazy='dynamic'),)

    # roles = db.relationship('Role',
    #                         secondary=user_role_table,
    #                         backref=db.backref('users', lazy='dynamic'),
    #                         lazy="dynamic")
    def to_json(self):
        return {
            'id': self.GID,
            # 'createdatetime':
            # self.CREATEDATETIME.strftime('%Y-%m-%d %H:%M:%S'),
            # 'updatedatetime':
            # self.UPDATEDATETIME.strftime('%Y-%m-%d %H:%M:%S'),
            'name': self.NAME,
            'icon': self.ICON
        }


class Project(db.Model):
    __tablename__ = 'PROJECT'
    PID = db.Column(
        db.String(36),
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    NAME = db.Column(db.String(100), default=None)
    MODELS = db.Column(db.String(100), default=None)
    SETTINGTS = db.Column(db.String(100), default=None)
    ISDELETED = db.Column(db.Integer, default=0)
    UPDATEDATETIME = db.Column(db.DateTime,
                               default=datetime.now,
                               onupdate=datetime.now)
    CREATEDATETIME = db.Column(db.DateTime, default=datetime.now)
    GID = db.Column(db.String(36))