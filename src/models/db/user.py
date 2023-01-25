"""User model."""
import json
from dataclasses import dataclass
from typing import Dict, List
from src.models.db import BaseModel
from src.models.schemas.user import User as UserSchema

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

    def __to_dict(self) -> Dict:
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
    def to_dict(self, without_keys:List|None=None, filter_none=False) -> Dict:
        """Convert user to dict."""
        if without_keys is None:
            without_keys = []
        return {key: value for key, value in self.__to_dict().items() \
                    if key not in without_keys and (value is not None or not filter_none)}
    def to_json(self, without_keys:List|None=None, filter_none=False) -> str:
        """Convert user to json."""
        return json.dumps(self.to_dict(without_keys, filter_none))
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
        