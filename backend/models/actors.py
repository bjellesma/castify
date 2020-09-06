from models.models import db
import enum
from routes.routing_functions import flask_abort

class Gender(enum.Enum):
    male = "male",
    female = "female"

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age=db.Column(db.Integer, nullable=False)
    gender=db.Column(db.Enum(Gender))
    
    def __init__(self, name, age, gender):
        """
        set class variables
        """
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': str(self.gender)
        }

    def create_actor(name, age, gender):
        """Create new actor

        Args:
            title (string): title of the actor

        Returns:
            int: the id of the actor inserted
        """
        actor = Actor(
            name=name,
            age=age,
            gender=gender
        )
        db.session.add(actor)
        db.session.commit()
        return actor.id 

    # The update method for the other models need to be fixed as well
    def update_actor(insert_data):
        """update actor object in database

        Args:
            insert_data (dict): {
                id: id of actor to updata
                name: name to update, if applicable
                age: age to update if applicable
                gender: gender to update if applicable
            }

        Returns:
            object: actor sqlalchemy object
        """
        actor_id = insert_data.get('id')
        actor = Actor.query.get(actor_id)
        if not actor:
            flask_abort(404, message=f"No actor was found for id {actor_id}")
        actor.name = insert_data.get('name') if insert_data.get('name') else actor.name
        actor.age = insert_data.get('age') if insert_data.get('age') else actor.age
        actor.gender = insert_data.get('gender') if insert_data.get('gender') else actor.gender
        db.session.commit()
        return actor

    def delete_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            flask_abort(status_code=404, message=f"No actor was found for id {actor_id}")
        db.session.delete(actor)
        db.session.commit()
        return actor.id