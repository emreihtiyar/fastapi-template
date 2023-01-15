from passlib.hash import bcrypt, bcrypt_sha256, argon2, scrypt
from passlib.context import CryptContext
from configs import HashingConfigs

class Hashing:
    """Hashing class to hash and verify passwords"""
    def __init__(self) -> None:
        self.context = CryptContext(
            schemes=[HashingConfigs.algorithm],
            default=HashingConfigs.algorithm,
            all__vary_rounds=HashingConfigs.rounds,
            all__salt=HashingConfigs.salt,
        )