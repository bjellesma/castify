from models.models import db
from routes.routing_functions import flask_abort


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        """
        set class variables
        """
        self.name = name

    def format(self):
        return {
            'name': self.name
        }

    def create_genre(name):
        """Create new genre

        Args:
            name (string): name of the genre

        Returns:
            int: the id of the genre inserted
        """
        genre = Genre(
            name=name
        )
        db.session.add(genre)
        db.session.commit()
        return genre.id

    def update_genre(insert_data):
        """update genre object in database

        Args:
            insert_data (dict): {
                id: id of genre to updata
                name: name of the genre to update to, if applicable
            }

        Returns:
            object: genre sqlalchemy object
        """
        genre_id = insert_data.get('id')
        genre = Genre.query.get(genre_id)
        if not genre:
            flask_abort(404, message=f"No genre was found for id {genre_id}")
        genre.name = insert_data.get(
            'name') if insert_data.get('name') else genre.name
        db.session.commit()
        return genre

    def delete_genre(genre_id):
        genre = Genre.query.get(genre_id)
        if not genre:
            flask_abort(
                status_code=404,
                message=f"No genre was found for id {genre_id}")
        db.session.delete(genre)
        db.session.commit()
        return genre.id
