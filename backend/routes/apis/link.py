"""Links are meant to be used after other objects are created and can associate relationships between objects
For example, a movie can have more than one actor and an actor can be associated with more than one movie
Because a movie or actor can be created without having an association, the link routes can be used to associate
    those already existing objects to one another
"""

from flask import Blueprint, request, abort, jsonify    
from flask_cors import CORS, cross_origin
from routes.routing_functions import validate_against_api
from models.links import create_movie_actor_link
from voluptuous import Schema, Required

link_routes = Blueprint('link_routes', __name__)

# This will be a POST route because we are creating a link
# TODO This naming convention may not be best practice
@link_routes.route('/api/links/movie_actor', methods=['Post'])
@cross_origin()
def post_movie_actor_link():
    movie_actor_schema = Schema({
        Required('movie_id'):int,
        Required('actor_id'):int
    })
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(data=data, schema=movie_actor_schema, request=request)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    movie_id=data['movie_id']
    actor_id=data['actor_id']
    movie, actor = create_movie_actor_link(
        movie_id=movie_id,
        actor_id=actor_id
    )
    return jsonify({
        'success':True,
        'movie':movie.format(),
        'actor':actor.format()
    })