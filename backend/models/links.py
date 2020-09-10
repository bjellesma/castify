from models.models import db
from models.movies import Movie
from models.actors import Actor
from routes.routing_functions import flask_abort


def create_movie_actor_link(movie_id, actor_id):
    """Create new movie

    Args:
        movie_id (int) - id of movie to associate with actor
        actor_id (int) - id of actor to associate with movie

    Returns:
        tuple of sqlalchemy object: movie and actor
    """

    movie = Movie.query.get(movie_id)
    actor = Actor.query.get(actor_id)
    if not actor or not movie:
        flask_abort(
            status_code=404,
            message='Either the actor or movie does not exist.'
        )
    # Movie is the primary object that holds the relation
    movie.actors.append(actor)
    db.session.commit()
    return movie, actor
