from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS, cross_origin
from auth import requires_auth
from routes.routing_functions import validate_against_api
from models.actors import Actor
from voluptuous import Schema, Required, Optional

actor_routes = Blueprint('actor_routes', __name__)

# define schema as global so that it can be used by the whole route
# TODO validating as str for now
actor_schema = Schema({
    Required('name'): str,
    Required('age'): int,
    Optional('gender'): str
})


@actor_routes.route('/api/actors', methods=['GET'])
@cross_origin()
def read_all_actors():
    """Read all actors in database

    Returns:
        JSON: {
            "success": boolean describing if the database read was successful
            "actors": A list of all dictionary representations of actors
                in the database
        }
    """
    try:
        actors = Actor.query.all()
    except Exception as err:
        abort(422, description=err)
    return jsonify({
        "success": True,
        "actors": [actor.format() for actor in actors]
    })


@actor_routes.route('/api/actors/<int:actor_id>', methods=['GET'])
# @requires_auth('read:actors')
@cross_origin()
def read_single_actor(actor_id):
    """Read Single Actor from database

    Args:
        actor_id (int): id of actor

    Returns:
        JSON: {
            success: true if call succeeded
            actor: {
                id: id of actor
                name: name of actor
                age: age of actor
                gender: gender of actor
            }
        }
    """
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404, description=f"No actor was found for id {actor_id}")
    return jsonify({
        "success": True,
        "actor": actor.format()
    })


@actor_routes.route('/api/actors', methods=['POST'])
# @requires_auth('create:actors')
@cross_origin()
def create_actor():
    """Insert Actor into database if validation is passed

    Returns:
        JSON: {
            "success": boolean describing if the insert was successful
            "actor_id": int id of newly created actor
        }
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(
        data=data, schema=actor_schema, request=request)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)
    name = data["name"]
    age = data["age"]
    # gender is optional
    gender = data["gender"] if "gender" in data else None
    actor_id = Actor.create_actor(
        name=name,
        age=age,
        gender=gender
    )
    return jsonify({
        "success": True,
        "actor_id": actor_id
    })


@actor_routes.route('/api/actors/<int:actor_id>', methods=['PATCH'])
# @requires_auth('update:actors')
@cross_origin()
def update_actor(actor_id):
    """Update a actor in a database

    Args:
        actor_id (int): id of the actor to be updated
    """
    data = request.get_json()
    api_errors = []
    # Validate json sent
    api_errors = validate_against_api(
        data=data,
        schema=actor_schema,
        request=request,
        optional=True)
    # if there are errors, abort with a 400
    if api_errors:
        abort(400, description=api_errors)

    actor = Actor.update_actor({
        "id": actor_id,
        "name": data.get("name"),
        "age": data.get("age"),
        "gender": data.get("gender")
    })
    return jsonify({
        "success": True,
        "actor": actor.format()
    })


@actor_routes.route('/api/actors/<int:actor_id>', methods=['Delete'])
# @requires_auth('delete:actors')
@cross_origin()
def delete_single_actor(actor_id):
    """delete single actor from the database

    Args:
        actor_id (int): id of actor to delete

    Returns:
        json: {
            success: true if delete was successful,
            actor_id: id of deleted actor
        }
    """
    actor_id = Actor.delete_actor(actor_id)
    return jsonify({
        "success": True,
        "actor_id": actor_id
    })
