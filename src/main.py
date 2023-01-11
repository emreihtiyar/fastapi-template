from fastapi import FastAPI
from configs import ApiConfigs

app = FastAPI(
    title=ApiConfigs.title,
    description=ApiConfigs.description,
    version=ApiConfigs.version,
    docs_url=ApiConfigs.api_docs_url,
    redoc_url=ApiConfigs.api_redoc_url,
    openapi_url=ApiConfigs.api_openapi_url,
)

@app.get(ApiConfigs.api_base_url+"/")
def get_root():
    return "API is up and running"

@app.post(ApiConfigs.api_base_url+"/")
def post_root():
    return "API is up and running"