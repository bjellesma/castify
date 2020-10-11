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
