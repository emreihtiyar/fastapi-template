import dataclasses


@dataclasses.dataclass(frozen=True)
class ApiConfigs:
    """Config class to store all the API configurations"""

    # API configurations
    title: str = "Example API"
    description: str = "Example API description"
    version: str = "0.0.1"
    api_url: str = "/api"
    api_version: str = "1"
    api_base_url: str = f"{api_url}/v{api_version}"
    api_docs_url: str = "/api/docs"
    api_redoc_url: str = "/api/redoc"
    api_openapi_url: str = "/api/openapi.json"