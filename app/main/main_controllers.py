# Import flask dependencies
from flask import (
  Blueprint,
  request,
  render_template,
  flash,
  g,
  session as login_session,
  redirect,
  url_for
  )


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


@mainBase.route('/', methods=['GET', 'POST'])
def loadMain():

    """

        loadMain: Show all features

        Args:

        Returns:
            Returns rendered main.html
    """
    features = db.session.query(Feature).all()
    return jsonify(features=[r.serialize for r in features])

    # return render_template("main/main.html")
