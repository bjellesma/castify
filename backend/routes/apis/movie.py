from flask import Blueprint, request, abort, jsonify    
from flask_cors import CORS, cross_origin
from routes.routing_functions import validate_against_api
from models.movies import Movie
from voluptuous import Schema, Required

movie_routes = Blueprint('movie_routes', __name__)

# define schema as global so that it can be used by the whole route
# TODO validating as str for now
movie_schema = Schema({
    Required('title'):str,
    Required('release_date'):str
})

@movie_routes.route('/api/movies', methods=['GET'])
@cross_origin()
def read_all_movies():
    """Read all movies in database

    Returns:
        JSON: {
            "success": boolean describing if the database read was successful
            "movies": A list of all dictionary representations of movies in the database
        }
    """
    try:
        movies = Movie.query.all()
        
    except Exception as err:
        abort(422, description=err)
    # if there are no movies, then 404
    if not movies:
        abort(404, description="No movies have been found!")
    return jsonify({
        "success": True,
        "movies": [movie.format() for movie in movies]
    })


@movie_routes.route('/api/movies/<int:movie_id>', methods=['GET'])
@cross_origin()
def read_single_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404, description=f"No movie was found for id {movie_id}")
    return jsonify({
        "success": True,
        "movie": movie.format()
    })

@movie_routes.route('/api/movies', methods=['POST'])
@cross_origin()
def create_movie():
    """Insert Movie into database if validation is passed

    Returns:
        JSON: {
            "success": boolean describing if the insert was successful
            "movie_id": int id of newly created movie
        }
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(data=data, schema=movie_schema, request=request)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    title = data["title"]
    release_data = data["release_date"]
    movie_id = Movie.create_movie(
        title = title,
        release_date = release_data
    )
    return jsonify({
        "success": True,
        "movie_id": movie_id
    })

@movie_routes.route('/api/movies/<int:movie_id>', methods=['PATCH'])
@cross_origin()
def update_movie(movie_id):
    """Update a movie in a database
    
    Args:
        movie_id (int): id of the movie to be updated
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(data=data, schema=movie_schema, request=request, optional=True)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    movie = Movie.update_movie({
        "id": movie_id,
        "title": data.get("title"),
        "release_date": data.get("release_date")
    })
    return jsonify({
        "success": True,
        "movie": movie.format()
    })

@movie_routes.route('/api/movies/<int:movie_id>', methods=['Delete'])
@cross_origin()
def delete_single_movie(movie_id):
    """delete single movie from the database

    Args:
        movie_id (int): id of movie to delete

    Returns:
        json: {
            success: true if delete was successful,
            movie_id: id of deleted movie
        }
    """
    movie_id = Movie.delete_movie(movie_id)
    return jsonify({
        "success": True,
        "movie_id": movie_id
    })