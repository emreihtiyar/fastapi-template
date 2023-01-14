from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from configs import ApiConfigs
from models.schemas import User, Auth


app = FastAPI(
    title=ApiConfigs.title,
    description=ApiConfigs.description,
    version=ApiConfigs.version,
    docs_url=ApiConfigs.api_docs_url,
    redoc_url=ApiConfigs.api_redoc_url,
    openapi_url=ApiConfigs.api_openapi_url,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=ApiConfigs.api_base_url+"/token",
)


@app.get(ApiConfigs.api_base_url+"/")
def get_root():
    return "API is up and running"

@app.post(ApiConfigs.api_base_url+"/")
def post_root():
    return "API is up and running"

@app.post(ApiConfigs.api_base_url+"/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return Auth.OAuthTokenResponse(
        access_token="fake-token",
    )

@app.get(ApiConfigs.api_base_url+"/test")
async def test(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.get(ApiConfigs.api_base_url+"/users/", tags=["users"])
async def get_users():
    return [
        User.UserResponse(
            id=1,
            name="John Doe",
            email="jhon@mail.com",
            role="admin",
            active=True,
            created_date="2021-01-01",
            updated_date="2021-01-01",
            last_password_change="2021-01-01",
        ),
        User.UserResponse(
            id=2,
            name="Jane Doe",
            email="jane@mail.com",
            role="admin",
            active=True,
            created_date="2021-01-01",
            updated_date="2021-01-01",
            last_password_change="2021-01-01",
        ),
    ]

@app.get(ApiConfigs.api_base_url+"/users/{user_id}", tags=["users"])
async def get_user(user_id: int):
    return User.UserResponse(
        id=user_id,
        name="John Doe",
        email="john@mail.com",
        role="admin",
        active=True,
        created_date="2021-01-01",
        updated_date="2021-01-01",
        last_password_change="2021-01-01",
    )