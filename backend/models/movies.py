from models.models import db
from models.relations import movie_actor, movie_genre
from models.actors import Actor
from models.genres import Genre



class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String, nullable=False)
    # release_date = db.Column(db.Datetime, nullable=False)
    actors = db.relationship('Actor', secondary=movie_actor, backref='movie', lazy=True)
    genres = db.relationship('Genre', secondary=movie_genre, backref='movie', lazy=True)

    def __init__(self, title):
        """
        set class variables
        """
        self.title = title

    def format(self):
        return {
            'id': self.id,
            'title': self.title
        }

    def create_movie(title):
        """Create new movie

        Args:
            title (string): title of the movie

        Returns:
            int: the id of the movie inserted
        """
        movie = Movie(
            title=title
        )
        db.session.add(movie)
        db.session.commit()
        return movie.id 