from __future__ import print_function
import sqlalchemy as sa

from database import BaseModel


class UserTg(BaseModel):
    __tablename__ = 'usertg'
    __repr_attrs__ = ['name']

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.String(30), sa.UniqueConstraint)

    branch = sa.Column(sa.String(30))
    status = sa.Column(sa.Integer)


class Message(BaseModel):
    __tablename__ = 'message'
    __repr_attrs__ = ['body', 'usertg']

    id = sa.Column(sa.Integer, primary_key=True)
    body = sa.Column(sa.String(500))
    usertg_id = sa.Column(sa.Integer, sa.ForeignKey('usertg.id'))

    usertg = sa.orm.relationship('UserTg', backref='messages')
