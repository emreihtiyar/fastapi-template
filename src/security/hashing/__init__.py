from passlib.hash import bcrypt, bcrypt_sha256, argon2, scrypt
from passlib.context import CryptContext
from configs import HashingConfigs

pwd_context = CryptContext(