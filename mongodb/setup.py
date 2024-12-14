import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, server_api=ServerApi("1"))
db = client["tpo_db"]
tpo_collection = db["tpo"]

tpo_collection.create_index([("expiresAt", 1)], expireAfterSeconds=0)


def setup_mongodb():
    try:
        client.admin.command("ping")
        return {
            "ok": True,
            "db": db,
            "collection": tpo_collection,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}
