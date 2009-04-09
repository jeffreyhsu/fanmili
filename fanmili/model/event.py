# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import Unicode, Integer, DateTime, Boolean

from fanmili.model import DeclarativeBase, metadata, DBSession
from fanmili.model.auth import User

__all__ = ['Event']

event_user_table = Table('event_user', metadata,
    Column('event_id', ForeignKey('event.id')),
    Column('user_id', ForeignKey('auth_user.user_id'))
)

class Event(DeclarativeBase):
    __tablename__ = 'event'

    #{ Columns
    id = Column(Integer, autoincrement=True, primary_key=True)

    title = Column(Unicode(255), nullable=False)

    type = Column(Unicode(255), nullable=False)

    creator_id = Column(Integer, ForeignKey('auth_user.user_id'))

    created = Column(DateTime, default=datetime.now)

    updated = Column(DateTime, onupdate=func.current_timestamp())

    when_start = Column(DateTime, nullable=False)

    when_end = Column(DateTime)

    where = Column(Unicode(255), nullable=False)

    description = Column(UnicodeText)

    join_level = Column(Unicode)

    allow_invite = Column(Boolean)

    #{ Relations
    creator = relation(User, backref='lunched_events')

    users = relation(User, secondary=event_user_table, backref='joined_events')

    #{ Special methods

    def __repr__(self):
        return '<Event: title=%s>' % self.title

    def __unicode__(self):
        return self.title
    #}