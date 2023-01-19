""" Database connection """

import abc
from dataclasses import dataclass
from typing import Dict, List
from motor.motor_asyncio import AsyncIOMotorClient

from src.configs import MongoDBConfigs
from src.utils.exceptions.mongo import DbNotFoundError
from src.models.schemas import BaseSchema


async_client = AsyncIOMotorClient(MongoDBConfigs.db_url)
if MongoDBConfigs.db_name:
    async_db = async_client[MongoDBConfigs.db_name]
else:
    raise DbNotFoundError(
        f"Database name not found in MongoDBConfigs: {MongoDBConfigs.db_name}"
    )

if MongoDBConfigs.db_name:
    users_collection = async_db["users"]

class BaseModel(abc.ABC):
    """ Base model class """
    @abc.abstractmethod
    def to_dict(self) -> Dict:
        """ Convert model to dict """
        return self.__dict__
    @abc.abstractmethod
    def to_schema(self) -> BaseSchema:
        """ Convert model to schema """
        return BaseSchema(**self.__dict__)
    @classmethod
    @abc.abstractmethod
    def from_dict(cls, data: Dict) -> 'BaseModel':
        """ Convert dict to model """
        return cls(**data)
    @classmethod
    def from_schema(cls, data: BaseSchema) -> 'BaseModel':
        """ Convert schema to model """
        return cls(**data.to_dict())
    @classmethod
    @abc.abstractmethod
    async def create(cls, data: Dict|BaseSchema) -> 'BaseModel':
        """ Create model from dict """
        raise NotImplementedError
    @classmethod
    @abc.abstractmethod
    async def get(cls, _id: str) -> 'BaseModel':
        """ Get model by id """
        raise NotImplementedError
    @classmethod
    @abc.abstractmethod
    async def update(cls, _id: str, data: Dict|BaseSchema) -> 'BaseModel':
        """ Update model by id """
        raise NotImplementedError
    @classmethod
    @abc.abstractmethod
    async def delete(cls, _id: str) -> 'BaseModel':
        """ Delete model by id """
        raise NotImplementedError
    @classmethod
    @abc.abstractmethod
    async def get_all(cls) -> List['BaseModel']:
        """ Get all models """
        raise NotImplementedError
        