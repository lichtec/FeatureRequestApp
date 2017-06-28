from app import db
from sqlalchemy.orm import sessionmaker
from app.main.main_model import Client, ProductArea, User, Feature

def reorder_priority(new_record, delete=None):
  features = db.session.query(Feature).filter_by(client_id == new_record.client_id).filter_by(priority>=new_record.priority).filter_by(id != new_record.id).all()
  
  if(delete):
    for feature in features:
      feature.priority = feature.priority -= 1
      db.session.add(feature)
      db.session.commit()
    return
  else:
    for feature in features:
      feature.priority = feature.priority += 1
      db.session.add(feature)
      db.session.commit()
      
      
            