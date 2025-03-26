import os
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_URI'])
db = client[os.environ['DB_NAME']]
tasks_collection = db.tasks
