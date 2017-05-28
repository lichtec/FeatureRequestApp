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
from app.records.record_model import Genre, Artist, Record

# Define the blueprint: 'main', set its url prefix: app.url/
mainBase = Blueprint('main', __name__, url_prefix='')

'''
    Set the route and accepted methods Main
'''


@recordBase.route('/', methods=['GET', 'POST'])
def loadMain():
    """

        loadMain: Show all records

        Args:

        Returns:
            Returns rendered main.html
    """
    return render_template("main/main.html")
