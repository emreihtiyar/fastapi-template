from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from configs import ApiConfigs

app = FastAPI(
    title=ApiConfigs.title,
    description=ApiConfigs.description,
    version=ApiConfigs.version,
    docs_url=ApiConfigs.api_docs_url,
    redoc_url=ApiConfigs.api_redoc_url,
    openapi_url=ApiConfigs.api_openapi_url,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=ApiConfigs.api_base_url+"/token")


@app.get(ApiConfigs.api_base_url+"/")
def get_root():
    return "API is up and running"

@app.post(ApiConfigs.api_base_url+"/")
def post_root():
    return "API is up and running"

@app.post(ApiConfigs.api_base_url+"/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username+"token"}

@app.get(ApiConfigs.api_base_url+"/test")
async def test(token: str = Depends(oauth2_scheme)):
    return {"token": token}