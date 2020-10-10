from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS, cross_origin
from auth import requires_auth
from routes.routing_functions import validate_against_api
from models.genres import Genre
from voluptuous import Schema, Required

genre_routes = Blueprint('genre_routes', __name__)

# define schema as global so that it can be used by the whole route
# TODO validating as str for now
genre_schema = Schema({
    Required('name'): str
})


@genre_routes.route('/api/genres', methods=['GET'])
@requires_auth('read:genres')
# @cross_origin()
def read_all_genres():
    """Read all genres in database

    Returns:
        JSON: {
            "success": boolean describing if the database read was successful
            "genres": A list of all dictionary representations of genres
            in the database
        }
    """
    try:
        genres = Genre.query.all()

    except Exception as err:
        abort(422, description=err)
    return jsonify({
        "success": True,
        "genres": [genre.format() for genre in genres]
    })

# TODO need docstring


@genre_routes.route('/api/genres/<int:genre_id>', methods=['GET'])
@requires_auth('read:genres')
# @cross_origin()
def read_single_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        abort(404, description=f"No genre was found for id {genre_id}")
    return jsonify({
        "success": True,
        "genre": genre.format()
    })


@genre_routes.route('/api/genres', methods=['POST'])
@requires_auth('create:genres')
@cross_origin()
def create_genre():
    """Insert Genre into database if validation is passed

    Returns:
        JSON: {
            "success": boolean describing if the insert was successful
            "genre_id": int id of newly created genre
        }
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(
        data=data, schema=genre_schema, request=request)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    name = data["name"]
    genre_id = Genre.create_genre(
        name=name
    )
    return jsonify({
        "success": True,
        "genre_id": genre_id
    })


@genre_routes.route('/api/genres/<int:genre_id>', methods=['PATCH'])
@requires_auth('update:genres')
@cross_origin()
def update_genre(genre_id):
    """Update a genre in a database

    Args:
        genre_id (int): id of the genre to be updated
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(
        data=data,
        schema=genre_schema,
        request=request,
        optional=True)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    genre = Genre.update_genre({
        "id": genre_id,
        "name": data.get("name")
    })
    return jsonify({
        "success": True,
        "genre": genre.format()
    })


@genre_routes.route('/api/genres/<int:genre_id>', methods=['Delete'])
@requires_auth('delete:genres')
@cross_origin()
def delete_single_genre(genre_id):
    """delete single genre from the database

    Args:
        genre_id (int): id of genre to delete

    Returns:
        json: {
            success: true if delete was successful,
            genre_id: id of deleted genre
        }
    """
    genre_id = Genre.delete_genre(genre_id)
    return jsonify({
        "success": True,
        "genre_id": genre_id
    })
