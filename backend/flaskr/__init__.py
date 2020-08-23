#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask # main import for running server
from flask_sqlalchemy import SQLAlchemy # database connection
from flask_migrate import Migrate #database migrations
from flask_cors import CORS # CRSF protection
import logging # app logging
from models.actors import *
from models.movies import *
from routes.api import api_routes

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

def create_app(test_config=None):

    app = Flask(__name__)
    # TODO will it
    # Necessary because our frontend connects with a different port
    CORS(app, resources={r"/api/*": {"origins": "*"}}) 
    app.register_blueprint(api_routes)
    # Setup Database
    app.config.from_object('config')
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad Request",
        "additional_information": error.description
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not Found",
        "additional_information": error.description
        }), 404

    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 405,
        "message": "Method not allowed",
        "additional_information": error.description
        }), 405

    @app.errorhandler(422)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 422,
        "message": "Unable to process",
        "additional_information": error.description
        }), 422

    @app.errorhandler(500)
    def not_found(error):
        return jsonify({
        "success": False, 
        "error": 500,
        "message": "Internal Server Error",
        "additional_information": error.description
        }), 500
    
    @app.route('/', methods=['GET'])
    def get_index():
        """Returns a message to tell the user that they've successfully connected"""
        return 'Hello Server'

    return app

