from bson import ObjectId

class User:
    def __init__(self, name, email, password, _id=None):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password"),
            _id=str(data.get("_id")) if data.get("_id") else None
        )
