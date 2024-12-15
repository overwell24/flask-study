from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from .domains.users.models import User
from .domains.users.schemas import UserSchema
from .config.extensions import db

main = Blueprint('main', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@main.route('/users', methods=['POST'])
def create_user():
    try:
        user = user_schema.load(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify(user_schema.dump(user)), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_schema.dump(user))