from fastapi import HTTPException

from app.config import (
    APP_USER,
    APP_PASSWORD
)

from app.auth import (
    create_access_token,
    create_refresh_token
)


def authenticate(username, password):

    if (
        username == APP_USER
        and password == APP_PASSWORD
    ):

        payload = {
            "sub": username
        }

        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload),
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=401,
        detail="Credenciais inválidas"
    )