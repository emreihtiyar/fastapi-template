"""MongoDB Helper"""

import asyncio
from asyncio import Task
from typing import Dict
from motor.motor_asyncio import AsyncIOMotorClient
from src.configs import MongoDBConfigs


class MongoHelper:
    """CRUD Helper for MongoDB"""
    def __init__(self, collection_name):
        self.client = AsyncIOMotorClient(MongoDBConfigs.db_url)
        self.db = self.client[MongoDBConfigs.db_name]
        self.collection = self.db[collection_name]
        self.event_loop = asyncio.get_event_loop()
    async def create(self, data: Dict) -> str | None:
        """Create data to MongoDB"""
        result = await self.collection.insert_one(data)
        if result.acknowledged:
            return str(result.inserted_id)
        return None
    async def read(self, query: Dict):
        """Read data from MongoDB"""
        return self.collection.find(query)
    async def update(self, query, data):
        """Update data to MongoDB"""
        pass
    async def delete(self, query):
        """Delete data from MongoDB"""
        pass
