from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.models.schemas import auth
from src.security.authorizations import JWTGenerator as JwTGenerator


router = APIRouter(
    prefix="/auth",
    tags=["authorization"],
)


oauth2_scheme = OAuth2PasswordBearer( 
    tokenUrl="/api/v1/auth/token",
)

@router.get("/")
def get_root():
    return "Authorization Service is UP"

@router.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    gen = JwTGenerator(form_data.username)
    return auth.OAuthTokenResponse(
        access_token=gen.generate(),
        token_type="bearer",
        refresh_token=None,
        scope=None
    )

@router.get("/get_token")
async def get_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.post("/verify_token")
async def verify_token(token: str = Depends(oauth2_scheme), user_id: str = "emre"):
    return {"result":JwTGenerator(user_id).verify(token)}