from flask import Blueprint, jsonify
from flask_cors import CORS, cross_origin

api_routes = Blueprint('api_routes', __name__)


@api_routes.route('/api', methods=['GET'])
@cross_origin()
def get_index():
    return jsonify({
        'success': True,
        'message': 'Woohoo, the api is working!'
    })


# This decorator is needed for angular
@api_routes.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers',
        'Content-Type,Authorization,true')
    response.headers.add(
        'Access-Control-Allow-Methods',
        'GET,PATCH,POST,DELETE,OPTIONS')
    return response