# src/db.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Read URI from .env
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# Database and collections
db = client["customer_segmentation"]
predictions_collection = db["predictions"]
logs_collection = db["logs"]
users_collection = db["users"]
