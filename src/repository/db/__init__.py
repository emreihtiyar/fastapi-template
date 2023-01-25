"""DB module"""
import abc
from typing import List, Dict, AnyStr
from src.models.db.user import User
from src.repository.db.mongo import MongoHelper


class UserOp:
    """User operations"""
    db = MongoHelper("users")
    @classmethod
    async def create(cls, user: User|List[User]) -> AnyStr | None:
        """Create user"""
        users = await cls.db.create(user.to_dict())
        if users:
            return users[0]
        return None
    @classmethod
    async def get(cls, user_id: str) -> List[User] | None:
        """Read user"""
        user = await cls.db.read({"id": user_id})
        if user is not None:
            return User.from_dict(user[0])
        return None
    @classmethod
    async def update(cls, user: User) -> List[User] | None:
        """Update user"""
        return await cls.db.update(user.to_json(filter_none=True))
    @classmethod
    async def delete(cls, user_id: str) -> List[User] | None:
        """Delete user"""
        return await cls.db.delete({"id": user_id})
    @classmethod
    async def get_all(cls) -> List[User] | None:
        """Get all users"""
        users = await cls.db.read({})
        if users is not None:
            return [User.from_dict(user) for user in users]
        return None
        