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

#JSON Error Response Missing ID
idError = {}
idError['Error'] = 'ID Required'
idErrorJson = json.dumps(idError)

noResultError = {}
noResultError['Error'] = 'No Result Found'
noResultErrorJson = json.dumps(noResultError)
'''
  Add objects
'''
@mainModBase.route('/add_feature', methods=['POST'])
def addFeature():
  featureRequested = request.json
  client_id = db.session.query(Client.id).filter_by(
    client_name=featureRequested['client_name']).first()
  productArea_id = db.session.query(ProductArea.id).filter_by(
    productArea_name=featureRequested['productArea_name']).first()
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

'''
  Edit objects
'''
@mainModBase.route('/edit_feature', methods=['POST'])
def editFeature():
  featureRequested = request.json
  if('id' not in featureRequested or featureRequested['id']==''):
    return idErrorJson
  editFeature = db.session.query(Feature).filter_by(id=featureRequested['id']).first()
  if(editFeature):
    for field in featureRequested:
      if field == 'title':
        editFeature.title=featureRequested['title']
      elif field == 'description':
        editFeature.description=featureRequested['description']
      elif field == 'client_id':
        editFeature.client_id=featureRequested['client_id']
      elif field == 'priority':
        editFeature.priority=featureRequested['priority']
      elif field == 'target_date':
        editFeature.targetDate=datetime.datetime.strptime(
          featureRequested['targetDate'], '%m/%d/%Y')
      elif field == 'productArea_id':
        editFeature.productArea_id=featureRequested['productArea_id']
      elif field == 'submitter_id':
        editFeature.submitter_id=featureRequested['submitter_id']
    db.session.add(editFeature)
    db.session.commit()
    return redirect('/features')

  else:
    return noResultErrorJson

@mainModBase.route('/edit_client', methods=['POST'])
def editClient():
  clientRequested = request.json
  if('id' not in clientRequested or clientRequested['id']==''):
    return idErrorJson
  editClient = db.session.query(Client).filter_by(id=clientRequested['id']).first()
  if(editClient):
    editClient.client_name = clientRequested['client_name']
    db.session.add(editClient)
    db.session.commit()
    return redirect('/clients')
  else:
    return noResultErrorJson

@mainModBase.route('/edit_product_area', methods=['POST'])
def editProductArea():
  productAreaRequested = request.json
  if('id' not in productAreaRequested or productAreaRequested['id']==''):
    return idErrorJson
  editProductArea = db.session.query(ProductArea).filter_by(id=productAreaRequested['id']).first()
  if(editProductArea):
    editProductArea.productArea_name = productAreaRequested['productArea_name']
    db.session.add(editProductArea)
    db.session.commit()
    return redirect('/product_areas')
  else:
    return noResultErrorJson
  
@mainModBase.route('/edit_user', methods=['POST'])
def editUser():
  userRequested = request.json
  if('id' not in userRequested or userRequested['id']==''):
    return idErrorJson
  editUser = db.session.query(User).filter_by(id=userRequested['id']).first()
  if(editUser):
    editUser.user_name = userRequested['user_name']
    db.session.add(editUser)
    db.session.commit()
    return redirect('/users')
  else:
    return noResultErrorJson

'''
  Delete objects
'''
@mainModBase.route('/delete_feature', methods=['POST'])
def deleteFeature():
  featureRequested = request.json
  if('id' not in featureRequested or featureRequested['id']==''):
    return idErrorJson
  deleteFeature = db.session.query(Feature).filter_by(
    id=featureRequested['id']).first()
  if(deleteFeature):
    db.session.delete(deleteFeature)
    db.session.commit()
    return redirect('/features')
  else:
    return noResultErrorJson

@mainModBase.route('/delete_client', methods=['POST'])
def deleteClient():
  clientRequested = request.json
  if('id' not in clientRequested or clientRequested['id']==''):
    return idErrorJson
  deleteClient = db.session.query(Client).filter_by(
    id=clientRequested['id']).first()
  if(deleteClient):
    relatedFeatures = db.session.query(Feature).filter_by(
      client_id=clientRequested['id']).all()
    for feature in relatedFeatures:
      feature.client_id = None
      db.session.add(feature)
    db.session.delete(deleteClient)
    db.session.commit()
    return redirect('/clients')
  else:
    return noResultErrorJson

@mainModBase.route('/delete_product_area', methods=['POST'])
def deleteProductArea():
  productAreaRequested = request.json
  if('id' not in productAreaRequested or productAreaRequested['id']==''):
    return idErrorJson
  deleteProductArea = db.session.query(ProductArea).filter_by(
    id=productAreaRequested['id']).first()
  if(deleteProductArea):
    relatedFeatures = db.session.query(Feature).filter_by(
      productArea_id=productAreaRequested['id']).all()
    for feature in relatedFeatures:
      feature.productArea_id = None
      db.session.add(feature)
    db.session.delete(deleteProductArea)
    db.session.commit()
    return redirect('/product_areas')
  else:
    return noResultErrorJson
  
@mainModBase.route('/delete_user', methods=['POST'])
def deleteUser():
  userRequested = request.json
  if('id' not in userRequested or userRequested['id']==''):
    return idErrorJson
  deleteUser = db.session.query(User).filter_by(
    id=userRequested['id']).first()
  if(deleteUser):
    relatedFeatures = db.session.query(Feature).filter_by(
      submitter_id=userRequested['id']).all()
    for feature in relatedFeatures:
      feature.submitter_id = None
      db.session.add(feature)
    db.session.delete(deleteUser)
    db.session.commit()
    return redirect('/users')
  else:
    return noResultErrorJson