import pydantic
from typing import Optional
from types import NoneType
from src.configs import JWTConfigs as JWTConfigs

class OAuthBase(pydantic.BaseModel):
    pass

class OAuthTokenRequest(OAuthBase):
    grant_type: str
    client_id: str
    client_secret: str
    username: str
    password: str


class OAuthTokenResponse(OAuthBase):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = JWTConfigs.ACCESS_TOKEN_EXPIRE_MINUTES * 60 # seconds
    refresh_token: str = None
    scope: str = None


class OAuthTokenRefreshRequest(OAuthBase):
    grant_type: str
    client_id: str
    client_secret: str
    refresh_token: str


class OAuthTokenRevokeRequest(OAuthBase):
    token: str
    token_type_hint: Optional[str] = "access_token"


class OAuthTokenIntrospectRequest(OAuthBase):
    token: str
    token_type_hint: Optional[str] = "access_token"