from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
from enum import Enum

class User(BaseModel):
    id: str
    hashed_password: str
    username: str
    firstname: str
    lastname: str
    role: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    active: Optional[bool]
    profile_image: Optional[str]
    profile_image_url: Optional[str]
    created_date: Optional[datetime|str|date]
    updated_date: Optional[datetime|str|date]
    last_login_date: Optional[datetime|str|date]

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id') or uuid.uuid4().hex,
            hashed_password=data.get('hashed_password'),
            username=data.get('username'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            role=cls.UserRoles(data.get('role')),
            phone=data.get('phone'),
            email=data.get('email'),
            active=data.get('active'),
            profile_image=data.get('profile_image'),
            profile_image_url=data.get('profile_image_url'),
            created_date=data.get('created_date'),
            updated_date=data.get('updated_date'),
            last_login_date=data.get('last_login_date'),
    )


class UserCreate(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    email: Optional[EmailStr]
    phone: Optional[str]

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "email": self.email,
        }