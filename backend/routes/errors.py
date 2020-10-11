from flask import Blueprint, jsonify
from auth import AuthError
error_routes = Blueprint('error_handlers', __name__)


@error_routes.app_errorhandler(400)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request",
        "additional_information": error.description
    }), 400


@error_routes.app_errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found",
        "additional_information": error.description
    }), 404


@error_routes.app_errorhandler(405)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method not allowed",
        "additional_information": error.description
    }), 405


@error_routes.app_errorhandler(422)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unable to process",
        "additional_information": error.description
    }), 422


@error_routes.app_errorhandler(500)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error",
        "additional_information": error.description
    }), 500


@error_routes.app_errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
