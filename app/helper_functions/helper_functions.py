
from app import db
from sqlalchemy.orm import sessionmaker
from app.main.main_model import Feature

def reorder_priority(new_record, delete=None):
  print new_record.id
  features = db.session.query(Feature).filter_by(client_id= new_record.client_id).filter(Feature.priority>=new_record.priority).filter(id!=new_record.id).all()
  for x in features:
    print x
  
  if(delete):
    for feature in features:
      feature.priority = int(feature.priority) - 1
      db.session.add(feature)
      db.session.commit()
    return
  else:
    for feature in features:
      print feature.id
      feature.priority = int(feature.priority) + 1
      db.session.add(feature)
      db.session.commit()