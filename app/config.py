# Statement for enabling the development environment
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = "postgresql://featurerequser:e038VyOXCE1d@localhost/featurerequest"
DATABASE_CONNECT_OPTIONS = {}

# Application threads. Sticking with standard 2
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secretTopherPotato1982"

# Secret key for signing cookies
SECRET_KEY = "secret"
