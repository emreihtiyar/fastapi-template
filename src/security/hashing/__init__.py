from passlib.context import CryptContext
from src.configs import HashingConfigs

class HashHelper:
    """Hashing class to hash and verify passwords"""
    def __init__(self) -> None:
        self.context = CryptContext(
            schemes=HashingConfigs.SCHEMES,
            deprecated="auto",
        )

    def hash(self, password: str) -> str:
        """Hash a password"""
        return self.context.hash(password)

    def verify(self, password: str, hashed_password: str) -> bool:
        """Verify a password"""
        try:
            return self.context.verify(password, hashed_password)
        except ValueError as value_error:
            print(value_error)
            return False
        except TypeError as type_error:
            print(type_error)
            return False
        except Exception as exception:
            print(exception)
            return False

    def to_dict(self) -> dict:
        """Return a dictionary of the class"""
        return self.context.to_dict()