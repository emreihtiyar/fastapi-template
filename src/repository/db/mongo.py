"""MongoDB Helper"""

from typing import Dict, List
from motor.motor_asyncio import AsyncIOMotorClient
from src.configs import MongoDBConfigs

class MongoHelper():
    """CRUD Helper for MongoDB"""
    def __init__(self, collection_name):
        """
        It creates a connection to the MongoDB database, and then creates a collection object that we
        can use to interact with the database
        
        :param collection_name: The name of the collection to be used
        """
        print(MongoDBConfigs.db_url)
        self.client = AsyncIOMotorClient(MongoDBConfigs.db_url)
        self.db = self.client[MongoDBConfigs.db_name]
        self.collection = self.db[collection_name]
    async def create(self, data: Dict | List[Dict]) -> List | None:
        """
        It takes a dictionary or a list of dictionaries as an argument, and returns a list of ObjectIds
        or None
        
        :param data: The data to be inserted
        :type data: Dict | List[Dict]
        :return: A list of strings.
        """
        if isinstance(data, (Dict, dict)):
            data = [data]
        result = await self.collection.insert_many(data)
        if result.acknowledged:
            return [str(_id) for _id in result.inserted_ids]
        return None
    async def read(self, data: Dict) -> List[Dict] | None:
        """Read data from MongoDB"""
        ret = []
        async for res in self.collection.find(data):
            ret.append(res)
        if len(ret) > 0:
            return ret
        return None
    async def update(self, data: Dict) -> List[Dict] | None:
        """Update data to MongoDB"""
        pass
    async def delete(self, data):
        """Delete data from MongoDB"""
        return await self.collection.delete_one(data)
