from flask import Blueprint, request, jsonify
from app.services import service

user_bp = Blueprint('user_bp', __name__)

#get - list all the users (/users)
@user_bp.route('/', methods=["GET"])
def get_users():
    users = service.get_all_usrs()
    return jsonify(users), 200

#get - get single user (/users/<id>)
@user_bp.route("/<string:user_id>", methods=['GET'])
def get_user(user_id):
    user = service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not Found'}), 404

#POST /users - Create a new user
@user_bp.route('/', methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in ['name', 'email', 'password']):
        return jsonify({'error': 'Missing required fields'}), 400
    user_id = service.create_user(data)
    return jsonify({'message': "User created", "id": user_id}), 201

#PUT /users/<id/ - update
@user_bp.route("/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': "No data given"}), 400
    updated = service.update_user(user_id, data)
    if updated:
        return jsonify({"message": "User updated"}), 200
    return jsonify({'error': "User not found"}), 404

#DELETE (/user/<id/)
@user_bp.route('/<string:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    deleted = service.delete_user(user_id)
    if deleted:
        return jsonify({"message": "user deleted"}), 200
    return jsonify({"error": "User not found"}), 404