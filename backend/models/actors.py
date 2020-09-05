from models.models import db
import enum
from models.relations import movie_actor

class Gender(enum.Enum):
    male = "Male",
    female = "Female"

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age=db.Column(db.Integer, nullable=False)
    gender=db.Column(db.Enum(Gender))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    # actors = db.relationship('Actor', secondary=actor_movie, backref='actor', lazy=True)
    