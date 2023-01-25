from fastapi import APIRouter, Depends
from src.models.db.user import (
    User as UserModel,
)
from src.models.schemas.user import (
    User as UserSchema,
)
from src.repository.db import UserOp


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
async def post_users(user: UserSchema):
    """Create a new user."""
    user_model = UserModel.from_schema(user)
    user_id = await UserOp.create(user_model)
    user_db = await UserOp.get(user_id)
    return user_db.to_schema()


@router.get("/")
async def get_users():
    """Get all users."""
    users = await UserOp.get_all()
    return [user.to_schema() for user in users]

@router.get("/{user_id}")
async def get_user(user_id: str):
    """Get a user."""
    user = await UserOp.get(user_id)
    return user.to_schema()

@router.put("/{user_id}")
async def put_user(user_id: str, user: UserSchema):
    """Update a user."""
    user_model = UserModel.from_schema(user)
    user_model = await user_model.update(user_id)
    return user_model.to_schema()

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    """Delete a user."""
    user = await UserOp.delete(user_id)
    return user.to_schema()