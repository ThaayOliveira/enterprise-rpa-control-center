from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = "super-secret-key-change"
ALGORITHM = "HS256"

ACCESS_MINUTES = 15
REFRESH_DAYS = 7

security = HTTPBearer()


def create_token(data: dict, expires_delta):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + expires_delta

    payload.update({"exp": expire})

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_access_token(data: dict):
    return create_token(
        data,
        timedelta(minutes=ACCESS_MINUTES)
    )


def create_refresh_token(data: dict):
    return create_token(
        data,
        timedelta(days=REFRESH_DAYS)
    )


def decode_token(token):
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    return decode_token(token)