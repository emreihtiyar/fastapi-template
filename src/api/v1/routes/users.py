from fastapi import APIRouter, Depends
from src.models.db.users import (
    User as UserDB,
)
from src.models.schemas.user import UserCreate, User


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

users = []

@router.post("/")
async def post_users(user: UserCreate):
    user = UserDB.from_schemas(user)
    user.save()
    return User.from_models(user)