"""
User schemas
"""
from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """ User schema """
    id: Optional[str]
    username: str
    firstname: str
    lastname: str
    password: Optional[str]
    password2: Optional[str]
    role: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    active: Optional[bool]

    @classmethod
    def from_dict(cls, data: dict):
        """ Create a User object from a dict"""
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            password=data.get('password'),
            password2=data.get('password2'),
            role=data.get('role'),
            phone=data.get('phone'),
            email=data.get('email'),
            active=data.get('active'),
    )
    