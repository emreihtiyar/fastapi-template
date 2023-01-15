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
    db_url: str = "mongodb+srv://emre:Qy0kYbyI757xvT9A@first.wdqfnt7.mongodb.net/?retryWrites=true&w=majority"
    db_name: str = "first"
    db_echo: bool = False

@dataclasses.dataclass(frozen=True)
class JWTConfigs:
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:str = 30
    REFRESH_TOKEN_EXPIRE_MINUTES:str = 60 * 24 * 7 # 7 days

@dataclasses.dataclass(frozen=True)
class HashingConfigs:
    """Config class to store all the hashing configurations"""
    """
    There are currently four good choices [1] for secure hashing:

    argon2
    bcrypt
    pbkdf2_sha256 / pbkdf2_sha512
    sha256_crypt / sha512_crypt
    """
    # Hashing configurations
    SCHEMES: tuple = ("argon2", "bcrypt", "pbkdf2_sha512", "sha512_crypt")
    SALT: str = "graderthan22characters"
    DEPRECATED: tuple = ("auto", "auto", "auto", "auto")