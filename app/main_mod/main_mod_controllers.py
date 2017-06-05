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
import datetime
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

# Import the database object from the main app module
from app import db

# Import module models
from app.main.main_model import Client, ProductArea, User, Feature

# Define the blueprint: 'main', set its url prefix: app.url/
mainModBase = Blueprint('mainMod', __name__, url_prefix='')

@mainModBase.route('/add_feature', methods=['POST'])
def addFeature():
  featureRequested = request.json
  client_id = db.session.query(Client.id).filter_by(
    client_name=featureRequested['client_name']).one()
  productArea_id = db.session.query(ProductArea.id).filter_by(
    productArea_name=featureRequested['productArea_name']).one()
  submitter_id = db.session.query(User.id).filter_by(
    user_name=featureRequested['submitter_name']).one()
  
  newFeature = Feature(title=featureRequested['title'],
                       description=featureRequested['description'],
                       client_id=client_id[0],
                       priority=featureRequested['priority'],
                       targetDate=datetime.datetime.strptime(
                         featureRequested['targetDate'], '%m/%d/%Y'),
                       productArea_id=productArea_id[0],
                       submitter_id=submitter_id[0])
  db.session.add(newFeature)
  db.session.commit()
  return redirect('/features')

@mainModBase.route('/add_client', methods=['POST'])
def addclient():
  clientRequested = request.json
  newClient = Client(client_name=clientRequested['client_name'])
  db.session.add(newClient)
  db.session.commit()
  return redirect('/clients')

@mainModBase.route('/add_product_area', methods=['POST'])
def addProductArea():
  productAreaRequested = request.json
  newProductArea = ProductArea(productArea_name=productAreaRequested['productArea_name'])
  db.session.add(newProductArea)
  db.session.commit()
  return redirect('/product_areas')
  
@mainModBase.route('/add_user', methods=['POST'])
def addUser():
  userRequested = request.json
  newUser = User(user_name=userRequested['user_name'])
  db.session.add(newUser)
  db.session.commit()
  return redirect('/users')