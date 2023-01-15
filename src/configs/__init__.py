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

@dataclasses.dataclass(frozen=True)
class JWTConfigs:
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:str = 30
    REFRESH_TOKEN_EXPIRE_MINUTES:str = 

@dataclasses.dataclass(frozen=True)
class HashingConfigs:
    """Config class to store all the hashing configurations"""

    # Hashing configurations
    algorithm: str = "bcrypt" # bcrypt, argon2, scrypt
    salt: str = "emre" # salt
    rounds: int = 12 # rounds
