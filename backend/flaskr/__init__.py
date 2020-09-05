#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask # main import for running server
from flask_sqlalchemy import SQLAlchemy # database connection
from flask_migrate import Migrate #database migrations
from flask_cors import CORS # CRSF protection
from models.models import setup_db
# The following imports are necessary to get the database structure properly set
from models.movies import *
from models.actors import *
from models.genres import *
import logging # app logging


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

def create_app(test_config=None):

    app = Flask(__name__)
    
    setup_db(app)
    app.config.from_object('config')
    # TODO will it
    # Necessary because our frontend connects with a different port
    CORS(app, resources={r"/api/*": {"origins": "*"}}) 
    from routes.api import api_routes
    from routes.apis.movie import movie_routes
    from routes.errors import error_routes
    app.register_blueprint(api_routes)
    app.register_blueprint(movie_routes)
    app.register_blueprint(error_routes)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    return app
