# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import Unicode, Integer, DateTime, Boolean

from fanmili.model import DeclarativeBase, metadata, DBSession
from fanmili.model.auth import User

__all__ = ['Category', 'Shop', 'Review']

class Category(DeclarativeBase):
    __tablename__ = 'shop_category'

    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(Unicode(100), unique=True)

    parent_id = Column(Integer, ForeignKey('shop_category.id'))

    children = relation('Category', backref=backref("parent", remote_side="Category.id"))

class Shop(DeclarativeBase):

    __tablename__ = 'shop_shop'

    #{ Columns
    id = Column(Integer, autoincrement=True, primary_key=True)

    from_url = Column(Unicode(255))

    name = Column(Unicode(255))

    alias

    pageviews = Column(Integer(10))

    province = Column(Unicode(30))

    city = Column(Unicode(30))

    section = Column(Unicode(30))

    geo = Column(Unicode(100))

    address = Column(Unicode(255))

    landmark = Column(Unicode(255))

    tel = Column(Unicode(20))

    mobile = Column(Unicode(20))

    category_id = Column(Integer, ForeignKey('shop_category.id'))

    tags = Column(UnicodeText)

    intro = Column(UnicodeText)

    recommendations = Column(UnicodeText)

    rating = Column(Float)

    reviews = Column(UnicodeText)

    spend_per = Column(Integer)

    extensions = Column(UnicodeText)

    creator_id = Column(User, ForeignKey('auth_user.user_id'))

    created = Column(DateTime, default=datetime.now)

    updated = Column(DateTime, onupdate=func.current_timestamp())

    #{ Relations
    category = relation(Category, backref='shops')

    creator = relation(User, backref='shops')

class Review(DeclarativeBase):

    __tablename__ = 'shop_review'

    #{ Columns
    id = Column(Integer, primary_key=True)

    creator_id = Column(User, ForeignKey('auth_user.user_id'))

    shop_id = Column(Shop, ForeignKey('shop_shop.id'))

    created = Column(DateTime, default=datetime.now)

    updated = Column(DateTime, onupdate=func.current_timestamp())

    #{ Relations
    creator = relation(User)

    shop = relation(Shop, backref='reviews')