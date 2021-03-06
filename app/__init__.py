# Import flask and template operators
from flask import Flask, render_template
from sqlalchemy import create_engine, text

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

# Define the WSGI application object
app = Flask(__name__)

# Configuration
app.config.from_pyfile('config.py')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app.db = session

# Simple HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.main.main_controllers import mainBase as main
from app.main_mod.main_mod_controllers import mainModBase as mainMod

# Register blueprint(s)
app.register_blueprint(main)
app.register_blueprint(mainMod)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
