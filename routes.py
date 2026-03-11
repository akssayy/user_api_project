from flask import Blueprint, request

from models import db, User
from schemas import user_schema, users_schema

bp = Blueprint('users', __name__)


@bp.route('/users', methods=['POST'])
def create_user():

    data = request.get_json()

    user = User(
        name=data['name'],
        age=data['age'], 
        email=data['email']
    )
    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201

@bp.route('/users', methods=['GET'])
def get_users():

    users = User.query.all()
    
    return users_schema.dump(users), 200

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):

    user = User.query.get(id)

    if not user:
        return {'error': 'User not found'}, 404

    return user_schema.dump(user), 200

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):

    user = User.query.get(id)

    if not user:
        return {'error': 'User not found'}, 404

    data = user_schema.load(request.json)

    user.name = data['name']
    user.age = data['age']
    user.email = data['email']

    db.session.commit()

    return user_schema.dump(user), 200

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):

    user = User.query.get(id)

    if not user:
        return {'error': 'User not found'}, 404

    db.session.delete(user)
    db.session.commit()

    return {"message": "User deleted"}, 200