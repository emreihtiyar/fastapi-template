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
    api_docs_url: str = f"{api_base_url}/docs"
    api_redoc_url: str = f"{api_base_url}/redoc"
    api_openapi_url: str = f"{api_base_url}/openapi.json"


@dataclasses.dataclass(frozen=True)
class DatabaseConfigs:
    """Config class to store all the database configurations"""

    # Database configurations
    db_url: str = "sqlite:///./example.db"
    db_echo: bool = False


@dataclasses.dataclass(frozen=True)
class MongoDBConfigs:
    """Config class to store all the MongoDB configurations"""

    # MongoDB configurations
    db_url: str = "mongodb://localhost:27017"
    db_name: str = "example"
    db_echo: bool = False