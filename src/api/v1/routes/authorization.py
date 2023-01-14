from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.schemas import Auth


router = APIRouter(
    prefix="/authorization",
    tags=["authorization"],
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=router.prefix + "/token",
)

@router.get("/")
def get_root():
    return "Authorization Service is UP"

@router.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return Auth.OAuthTokenResponse(
        access_token="fake-token",
    )

@router.get("/test")
async def test(token: str = Depends(oauth2_scheme)):
    return {"token": token}