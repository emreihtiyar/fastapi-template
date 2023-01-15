from fastapi import APIRouter
from .authorization import router as authorization_router
from .users import router as users_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(authorization_router)
router.include_router(users_router)

@router.get("/")
def get_root():
    return "API is UP"