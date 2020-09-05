from flask import Blueprint, request, abort, jsonify    
from flask_cors import CORS, cross_origin
from models.movies import Movie
from voluptuous import Schema, Required

movie_routes = Blueprint('movie_routes', __name__)

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
    # define schema
    movie_schema = Schema({
        Required('title'):str
    })
    # Validate json sent
    try:
        data = movie_schema(data)
    except Exception as errors:
        for err in errors.errors:
            if err.msg == "required key not provided":
                api_errors.append(f'{err.path[0]} was required and not provided for call to {request.path} as {request.method}. Please consult the documentation.')
            elif 'expected' in err.msg:
                api_errors.append(f'{err.path[0]} was in the incorrect format for call to {request.path} as {request.method}. Please consult the documentation.')
    
    if api_errors:
        abort(400, description=api_errors)
    title = data["title"]
    mid = Movie.create_movie(
        title = title
    )
    return jsonify({
        "success": True,
        "movie_id": mid
    })

@movie_routes.route('/api/movies/<int:movie_id>', methods=['PATCH'])
@cross_origin()
def update_movie(movie_id):
    """Update a movie in a database

    Args:
        movie_id (int): id of the movie to be updated
    """
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404, description=f"No movie was found for id {movie_id}")
    movie.title = title