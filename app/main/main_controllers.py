# Import flask dependencies
from flask import (
  Blueprint,
  request,
  render_template,
  flash,
  g,
  session as login_session,
  redirect,
  url_for,
  jsonify
  )

import json

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import the database object from the main app module
from app import db

# Import module models
from app.main.main_model import Client, ProductArea, User, Feature

# Define the blueprint: 'main', set its url prefix: app.url/
mainBase = Blueprint('main', __name__, url_prefix='')

'''
    Set the route and accepted methods Main
'''
@mainBase.route('/', methods=['GET'])
def loadMain():

    """

        loadMain: Frontend app for data

        Args:

        Returns:
            Returns rendered main.html
    """
    return render_template("main/main.html")

@mainBase.route('/features', methods=['GET'])
def loadFeatures():

    """

        loadMain: Show all features

        Args:

        Returns:
            Returns json
    """
    features = db.session.query(Feature).all()
    return jsonify(features=[r.serialize for r in features])

@mainBase.route('/clients', methods=['GET'])
def loadClients():

    """

        loadMain: Show all clients

        Args:

        Returns:
            Returns json
    """
    clients = db.session.query(Client).all()
    return jsonify(clients=[r.serialize for r in clients])

@mainBase.route('/users', methods=['GET'])
def loadUsers():

    """

        loadMain: Show all users

        Args:

        Returns:
            Returns json
    """
    users = db.session.query(User).all()
    return jsonify(users=[r.serialize for r in users])
  
@mainBase.route('/product_areas', methods=['GET'])
def loadProductAreas():

    """

        loadMain: Show all product_areas

        Args:

        Returns:
            Returns json
    """
    product_areas = db.session.query(ProductArea).all()
    return jsonify(product_areas=[r.serialize for r in product_areas])