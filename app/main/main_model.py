from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import datetime

from app import db


class Base(db.Model):
    # Base model for subsequent models
    # Auth model also uses this base model

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())


class Client(Base):

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'client_name': self.client_name
        }

    # New instance instantiation procedure
        def __init__(self, client_name):
            self.client_name = client_name

    def __repr__(self):
        return '<client %r>' % (self.client_name)

class ProductArea(Base):

    __tablename__ = 'productArea'

    id = db.Column(db.Integer, primary_key=True)
    productArea_name = db.Column(db.String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'productArea_name': self.productArea_name
        }

    # New instance instantiation procedure
        def __init__(self, productArea_name):
            self.productArea_name = productArea_name

    def __repr__(self):
        return '<productArea %r>' % (self.productArea_name)

class User(Base):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'user_name': self.user_name
        }

    # New instance instantiation procedure
        def __init__(self, user_name):
            self.user_name = user_name

    def __repr__(self):
        return '<user %r>' % (self.user_name)

class Feature(Base):

    __tablename__ = 'feature'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(5000), nullable=False)
    client_id = db.Column(db.Integer, ForeignKey('client.id'))
    client = db.relationship(Client)
    priority = db.Column(db.Integer, nullable=False)
    targetDate = db.Column(db.DateTime, nullable=False)
    productArea_id = db.Column(db.Integer, ForeignKey('productArea.id'), nullable=True)
    productArea = db.relationship(ProductArea)
    submitter_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
    user = db.relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        if(self.user):
          submitter_name = self.user.serialize['user_name']
        else:
          submitter_name = ''
        if(self.productArea):
          productArea_name = self.productArea.serialize['productArea_name']
        else:
          productArea_name = ''
        if(self.client):
          client_name = self.client.serialize['client_name']
        else:
          client_name = ''
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'client_id': self.client_id,
            'client_name': client_name,
            'priority': self.priority,
            'targetDate':   self.targetDate.strftime('%m-%d-%Y'),
            'productArea_id': self.productArea_id,
            'productArea_name': productArea_name,
            'submitter_id': self.submitter_id,
            'submitter_name': submitter_name,
        }
    # New instance instantiation procedure

        def __init__(self, title, description, client_id, priority, targetDate,
                     productArea_id, submitter_id):
            self.id = id
            self.title = title
            self.description = description
            self.client_id = client_id
            self.priority = priority
            self.targetDate = targetDate
            self.productArea_id = productArea_id
            self.submitter_id = submitter_id

        def __repr__(self):
            return '<Feature %r>' % (self.title)
