"""User model."""
from dataclasses import dataclass
from typing import Dict, List
from src.models.db import BaseModel
from src.models.schemas.user import User as UserSchema
from src.repository.db import DBHelper


@dataclass
class User(BaseModel):
    """
    User model.
    """
    id: str
    username: str
    firstname: str
    lastname: str
    password: str | None = None
    email: str | None = None
    phone: str | None = None
    role: str | None = None
    active: bool = True

    def to_dict(self) -> Dict:
        """Convert user to dict."""
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
            'active': self.active,
        }
    def to_schema(self) -> UserSchema:
        """Convert user to schema."""
        return UserSchema(
            id=self.id,
            username=self.username,
            firstname=self.firstname,
            lastname=self.lastname,
            email=self.email,
            phone=self.phone,
            role=self.role,
            active=self.active,
        )
    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        """Create user from dict."""
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            password=data.get('password'),
            email=data.get('email'),
            phone=data.get('phone'),
            role=data.get('role'),
            active=data.get('active'),
        )
    @classmethod
    def from_schema(cls, data: UserSchema) -> 'User':
        """Create user from schema."""
        return cls(
            id=data.id,
            username=data.username,
            firstname=data.firstname,
            lastname=data.lastname,
            email=data.email,
            phone=data.phone,
            role=data.role,
            active=data.active,
        )
    async def create(self) -> 'User':
        """Create user."""
        self.__db = DBHelper('users')
        user_id = await self.__db.create(self.to_dict())
        self.id = user_id
        return self
    @classmethod
    async def get(cls, _id: str) -> 'User':
        """Get user by id."""
        pass
    @classmethod
    async def update(cls, _id: str, data: Dict|UserSchema) -> 'User':
        """Update user by id."""
        pass
    @classmethod
    async def delete(cls, _id: str) -> 'User':
        """Delete user by id."""
        pass
    @classmethod
    async def get_all(cls) -> List['User']:
        """Get all users."""
        pass
