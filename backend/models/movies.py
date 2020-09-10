from models.models import db
from models.relations import movie_actor, movie_genre
from routes.routing_functions import flask_abort


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    actors = db.relationship(
        'Actor',
        secondary=movie_actor,
        backref='movie',
        lazy=True)
    genres = db.relationship(
        'Genre',
        secondary=movie_genre,
        backref='movie',
        lazy=True)

    def __init__(self, title, release_date):
        """
        set class variables
        """
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title
        }

    def create_movie(title, release_date):
        """Create new movie

        Args:
            title (string): title of the movie

        Returns:
            int: the id of the movie inserted
        """
        movie = Movie(
            title=title,
            release_date=release_date
        )
        db.session.add(movie)
        db.session.commit()
        return movie.id

    def update_movie(insert_data):
        """update movie object in database

        Args:
            insert_data (dict): {
                id: id of movie to updata
                title: title to update, if applicable
                release_date: release date to update if applicable
            }

        Returns:
            object: movie sqlalchemy object
        """
        movie_id = insert_data.get('id')
        movie = Movie.query.get(movie_id)
        if not movie:
            flask_abort(404, message=f"No movie was found for id {movie_id}")
        movie.title = insert_data.get(
            'title') if insert_data.get('title') else movie.title
        movie.release_date = insert_data.get(
            'release_date') if insert_data.get(
            'release_date') else movie.release_date
        db.session.commit()
        return movie

    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            flask_abort(
                status_code=404,
                message=f"No movie was found for id {movie_id}")
        db.session.delete(movie)
        db.session.commit()
        return movie.id
