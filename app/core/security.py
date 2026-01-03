from datetime import datetime, timedelta, UTC
from typing import Optional, Union
from jose import jwt
from passlib.context import CryptContext
import os

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    SECRET_KEY = os.getenv("SECRET_KEY")
    HASH_ALGO = os.getenv("HASH_ALGO")

    if SECRET_KEY is None:
        raise ValueError("FATAL ERROR: SECRET_KEY environment variable is not set")

    if HASH_ALGO is None:
        raise ValueError("FATAL ERROR: HASH_ALGO environment variable is not set")

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=HASH_ALGO)

    return encoded_jwt