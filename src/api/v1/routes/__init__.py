from fastapi import APIRouter
from .authorization import router as authorization_router

router = APIRouter(
    prefix="/v1",
)

router.include_router(authorization_router)

@router.get("/")
def get_root():
    return "API is UP"