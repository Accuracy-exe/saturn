import dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

dotenv.load_dotenv()

uri = str(os.getenv("MONGO_URI"))

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged cluster. Successfully connected to MongoDB!")
except Exception as e:
    print(e)


def initCollection(guild_id):
    db = client["Saturn"]
    collection_name = str(guild_id)
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db[collection_name]


def saveItem(json, guild_id):
    db = client["Saturn"]
    colName = str(guild_id)
    collection = db[colName]
    collection.insert_one(json)
    
