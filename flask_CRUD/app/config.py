import os
class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/flask_monog_crud")