from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime


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
    def from_dict(cls, data: dict):
        return cls(
            id=data.get('id'),
            hashed_password=data.get('hashed_password'),
            username=data.get('username'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            role=data.get('role'),
            phone=data.get('phone'),
            email=data.get('email'),
            active=data.get('active'),
            profile_image=data.get('profile_image'),
            profile_image_url=data.get('profile_image_url'),
            created_date=data.get('created_date'),
            updated_date=data.get('updated_date'),
            last_login_date=data.get('last_login_date'),
    )

    @classmethod
    def from_models(cls, data: 'UserDB'):
        return cls(
            id=data.id,
            hashed_password="this is a secret",
            username=data.username,
            firstname=data.firstname,
            lastname=data.lastname,
            role=data.role,
            phone=data.phone,
            email=data.email,
            active=data.active,
            profile_image=data.profile_image,
            profile_image_url=data.profile_image_url,
            created_date=data.created_date,
            updated_date=data.updated_date,
            last_login_date=data.last_login_date,
    )


class UserCreate(BaseModel):
    username: str
    firstname: str
    lastname: str
    password: str
    confirm_password: str
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