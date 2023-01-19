import datetime

from jose import jwt as jose_jwt
from jose.exceptions import JWSError as JoseJWSError
from jose.exceptions import JWTError as JoseJWTError

from src.configs import JWTConfigs
from src.utils.exceptions import (InvalidJWTException,
                                  InvalidJWTSignatureException)


class JWTGenerator:
    """
    This class is responsible for generating and verifying JWT tokens.
    """
    def __init__(self, user_id: str, **kwargs):
        self.user_id = user_id
        self.iat = kwargs.get("iat", datetime.datetime.utcnow())
        self.expire_in = kwargs.get("expire_in", 
            datetime.timedelta(minutes=JWTConfigs.ACCESS_TOKEN_EXPIRE_MINUTES))
        self.expire = kwargs.get("expire", self.iat + self.expire_in)
        self.payload = self.__generate_payload()
    def __generate_payload(self) -> dict:
        """
        It returns a dictionary with the user_id, iat, and expire values
        :return: A dictionary with the user_id, iat, and expire.
        """
        return {
            "sub": self.user_id,
            "iat": self.iat,
            "exp": self.expire,
        }
    def __generate_token(self) -> str:
        """Generates a JWT token"""
        return jose_jwt.encode(self.payload, JWTConfigs.SECRET_KEY, algorithm=JWTConfigs.ALGORITHM)
    def generate(self) -> str | None:
        """Generates a JWT token for a given user."""
        try:
            return self.__generate_token()
        except JoseJWTError as exp:
            print(exp)
        return None
    def verify(self, token: str) -> bool:
        """Verifies a JWT token and returns a boolean value."""
        try:
            payload = jose_jwt.decode(
                    token,
                    JWTConfigs.SECRET_KEY,
                    algorithms=[JWTConfigs.ALGORITHM]
                )
            if payload.get("sub") == self.user_id and payload.get("exp") > self.iat:
                return True
            return False
        except JoseJWTError as exp:
            print(exp)
            return False

    def generate_refresh_token(self, user_id: int) -> str:
        """Generates a JWT token for a given user."""
        pass

    def refresh(self, token: str) -> str:
        """Refreshes a JWT token and returns a new one."""
        try:
            gen = JWTGenerator.from_token(token)
            if gen.verify(token):
                return gen.generate()
        except JoseJWTError as exp:
            print(exp)
    
    @classmethod
    def from_payload(cls, payload: dict) -> 'JWTGenerator':
        """Generates a JWTGenerator instance from a given payload"""
        payload = payload if isinstance(payload, dict) else dict(payload)
        if not payload.get("sub"):
            raise InvalidJWTException()
        return cls(
            user_id=payload.get("sub"),
            iat=payload.get("iat"),
            expire=payload.get("exp"),
        )
    
    @classmethod
    def from_token(cls, token: str) -> 'JWTGenerator':
        """Generates a JWTGenerator instance from a given token"""
        try:
            payload = jose_jwt.decode(token, JWTConfigs.SECRET_KEY, algorithms=[JWTConfigs.ALGORITHM])
            return cls.from_payload(payload)
        except JoseJWTError as e:
            print(e)
            raise InvalidJWTException()
        except JoseJWSError as e:
            print(e)
            raise InvalidJWTSignatureException()    