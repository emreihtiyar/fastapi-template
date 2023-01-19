from fastapi import FastAPI

from src.api.v1.routes import router as v1_router
from src.configs import ApiConfigs

app = FastAPI(
    title=ApiConfigs.title,
    description=ApiConfigs.description,
    version=ApiConfigs.version,
    docs_url=ApiConfigs.api_docs_url,
    redoc_url=ApiConfigs.api_redoc_url,
    openapi_url=ApiConfigs.api_openapi_url,
)

app.include_router(v1_router, prefix="/api")
