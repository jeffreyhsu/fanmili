# -*- coding: utf-8 -*-
import os
from datetime import datetime
import sys

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.types import Unicode, Integer, DateTime, Boolean

from fanmili.model import DeclarativeBase, metadata, DBSession
from fanmili.model.auth import User

__all__ = ['Category', 'Goods']

class Category(DeclarativeBase):
    __tablename__ = 'flee_category'

    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(Unicode(100), unique=True)

    parent_id = Column(Integer, ForeignKey('shop_category.id'))

    children = relation('Category', backref=backref("parent", remote_side="Category.id"))

class Item(DeclarativeBase):
    __tablename__ = 'flee_item'

    id = Column(Integer, autoincrement=True, primary_key=True)

    #{ Flee Columns
    name = Column(Unicode(255), nullable=False)

    category_id = Column(Integer, ForeignKey('flee_item.id'))

    owner_id = Column(Integer, ForeignKey('auth_user.id'))
    
    sku = Column(Unicode(255))

    condition = Column(Unicode(50))

    description = Column(UnicodeText)

    for_trade = Column(Boolean)

    trade_price_from = Column(Numeric)

    trade_price_to = Column(Numeric)

    #{ Product Columns
    price = Column(Numeric)

    rating = Column(Float)

    review = Column(UnicodeText)

class Want(DeclarativeBase):
    __tablename__ = 'flee_want'

    name = Column(Unicode(255))

    description = Column(UnicodeText)

    category_id = Column(Integer, ForeignKey('flee_category.id'))

    url = Column(UnicodeText)