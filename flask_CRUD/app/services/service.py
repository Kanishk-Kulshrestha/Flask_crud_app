from bson import ObjectId
from app.extensions import mongo
from app.models.user import User


def create_user(data):
    collection = mongo.db.users
    user = User.from_dict(data)
    user_dict = user.to_dict()

    user_dict.pop("_id")
    result = collection.insert_one(user_dict)
    return str(result.inserted_id)

def get_all_users():
    collection = mongo.db.users
    users = collection.find()
    return [User.from_dict(u).__dict__ for u in users]

def get_user_by_id(id):
    collection = mongo.db.users
    user = collection.find_one({"_id": ObjectId(id)})
    return User.from_dict(user).__dict__ if user else None

def update_user(user_id, data):
    collection = mongo.db.users
    update_data = {k:v for k, v in data.items() if k in ["name", "email", "passowrd"]}
    result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    return result.modified_count > 0

def delete_user(user_id):
    collection = mongo.db.users
    result = collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0