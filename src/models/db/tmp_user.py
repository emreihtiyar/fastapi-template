import uuid

from mongoengine.document import Document
from mongoengine.fields import (
    BooleanField, 
    DateTimeField, 
    EmailField,
    StringField
)

from src.models.schemas.user import User as UserSchema
from src.models.schemas.user import UserCreate as UserCreateSchema


class User(Document):
    """ User model """
    id = StringField(required=True, primary_key=True, unique=True)
    username = StringField(required=True, unique=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    password = StringField(required=True)
    email = EmailField(unique=True)
    phone = StringField(unique=True)
    role = StringField()
    active = BooleanField()
    profile_image = StringField()
    profile_image_url = StringField()
    created_date = DateTimeField()
    updated_date = DateTimeField()
    last_login_date = DateTimeField()

    meta = {
        'collection': 'users',
        'strict': False,
        'auto_create_index': False,
        'indexes': [],
        'ordering': ['+id'],
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid.uuid4())
        return super().save(*args, **kwargs)

    async def save_async(self, *args, **kwargs):
        pass
        # save to mongodb async here with motor

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "password": self.password,
            "role": self.role,
            "active": self.active,
            "profile_image": self.profile_image,
            "profile_image_url": self.profile_image_url,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "last_login_date": self.last_login_date,
        }

    @classmethod
    def from_schemas(cls, schema: UserSchema | UserCreateSchema) -> 'User':
        if isinstance(schema, UserSchema):
            return cls.__from_user_schema(schema)
        elif isinstance(schema, UserCreateSchema):
            return cls.__from_user_create_schema(schema)
        else:
            raise TypeError('schema must be User or UserCreate')

    @classmethod
    def __from_user_schema(cls, schema: UserSchema) -> 'User':
        return cls(
            id=schema.id,
            username=schema.username,
            email=schema.email,
            phone=schema.phone,
            firstname=schema.firstname,
            lastname=schema.lastname,
            password=schema.password,
            role=schema.role,
            active=schema.active,
            profile_image=schema.profile_image,
            profile_image_url=schema.profile_image_url,
            created_date=schema.created_date,
            updated_date=schema.updated_date,
            last_login_date=schema.last_login_date,
        )

    @classmethod
    def __from_user_create_schema(cls, schema: UserCreateSchema) -> 'User':
        return cls(
            username=schema.username,
            firstname=schema.firstname,
            lastname=schema.lastname,
            password=schema.password,
            email=schema.email,
            phone=schema.phone,
        )