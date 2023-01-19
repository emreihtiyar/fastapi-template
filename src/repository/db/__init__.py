"""DB module"""

from typing import Dict
from src.repository.db.mongo import MongoHelper


class DBHelper:
    """Helper class for DB operations"""
    def __init__(self, collection_name):
        self.__helper = MongoHelper(collection_name)
    async def create(self, data: Dict):
        """Create data to MongoDB"""
        return await self.__helper.create(data)
    async def read(self, query: Dict):
        """Read data from MongoDB"""
        return await self.__helper.read(query)
    async def update(self, query, data):
        """Update data to MongoDB"""
        return await self.__helper.update(query, data)
    async def delete(self, query):
        """Delete data from MongoDB"""
        return await self.__helper.delete(query)