from fastapi import APIRouter, Depends
from src.models.db import User as UserDB
from src.models.schemas.user import UserCreate
from src.db import db


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

users = []

@router.post("/")
async def post_users(user: UserCreate):
    result = await db.users.insert_one(user.to_dict())
    return print(result)
