from motor.motor_asyncio import AsyncIOMotorClient
from src.configs import MongoDBConfigs

client = AsyncIOMotorClient(MongoDBConfigs.db_url)
db = client.test_database
db = client[MongoDBConfigs.db_name]