# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask  # main import for running server
from flask_sqlalchemy import SQLAlchemy  # database connection

from flask_cors import CORS  # CRSF protection
from models.models import setup_db
# The following imports are necessary to get the database structure
# properly set
from models.movies import *
from models.actors import *
from models.genres import *
import logging  # app logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from routes.api import api_routes
from routes.apis.movie import movie_routes
from routes.apis.genre import genre_routes
from routes.apis.actor import actor_routes
from routes.apis.link import link_routes
from routes.server import server_routes
from routes.errors import error_routes

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    app.config.from_object('config')
    # Necessary because our frontend connects with a different port
    CORS(app)
    # logging
    file_handler = RotatingFileHandler('logs/castify.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    auth = None
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
    # mail
    mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject='Error from castify',
        credentials=auth, secure=secure)
    mail_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(mail_handler)
    app.logger.addHandler(file_handler)
    app.logger.info('test log')
    # enable logging for flask cors
    logging.getLogger('flask_cors').level = logging.DEBUG
    app.register_blueprint(api_routes)
    app.register_blueprint(movie_routes)
    app.register_blueprint(genre_routes)
    app.register_blueprint(actor_routes)
    app.register_blueprint(error_routes)
    app.register_blueprint(link_routes)
    app.register_blueprint(server_routes)
    
    return app
