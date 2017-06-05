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
mainModBase = Blueprint('mainMod', __name__, url_prefix='')

@mainModBase.route('/add_feature', methods=['POST'])
def addFeature():
  featureRequested = request.json
  client_id = db.session.query(Client.id).filter_by(featureRequested['clientName']).one()
  productArea_id = db.session.query(ProductArea.id).filter_by(featureRequested['productAreaName']).one()
  submitter_id = db.session.query(User.id).filter_by(featureRequested['submitter_id']).one()
  
  newFeature = Feature(title=featureRequested['title'], description=featureRequested['description'],
                       client_id=client_id, priority=featureRequested['priority'],
                       productArea_id=productArea_id, submitter_id=submitter_id)
  db.session.add(newFeature)
  db.session.commit()
  return redirect('/')

@mainModBase.route('/add_client', methods=['POST'])
def addclient():
  clientRequested = request.json
  newclient = Client(name=clientRequested['name'])
  db.session.add(newclient)
  db.session.commit()
  return redirect('/')
  