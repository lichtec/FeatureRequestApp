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

noResultError = {}
noResultError['Error'] = 'No Result Found'
noResultErrorJson = json.dumps(noResultError)

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
#     print features
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


@mainBase.route('/feature/<int:feature_id>', methods=['GET'])
def loadFeature(feature_id):

    """

        loadMain: Show a feature

        Args: feature_id

        Returns:
            Returns json
    """
    feature = db.session.query(Feature).filter_by(id=feature_id).first()
    if(feature):
      return jsonify(feature.serialize)
    else:
      return noResultErrorJson

@mainBase.route('/client/<int:client_id>', methods=['GET'])
def loadClient(client_id):

    """

        loadMain: Show a client

        Args:client_id

        Returns:
            Returns json
    """
    client = db.session.query(Client).filter_by(id=client_id).first()
    if(client):
      return jsonify(client.serialize)
    else:
      return noResultErrorJson

@mainBase.route('/user/<int:user_id>', methods=['GET'])
def loadUser(user_id):

    """

        loadMain: Show a user

        Args:user_id

        Returns:
            Returns json
    """
    user = db.session.query(User).filter_by(id=user_id).first()
    if(user):
      return jsonify(user.serialize)
    else:
      return noResultErrorJson
  
@mainBase.route('/product_area/<int:product_area_id>', methods=['GET'])
def loadProductArea(product_area_id):

    """

        loadMain: Show a product_area

        Args:product_area_id

        Returns:
            Returns json
    """
    product_area = db.session.query(ProductArea).filter_by(id=product_area_id).first()
    if(product_area):
      return jsonify(product_area.serialize)
    else:
      return noResultErrorJson