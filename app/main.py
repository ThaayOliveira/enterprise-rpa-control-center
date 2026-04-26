from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from app.database import Base, engine
from app.scheduler import start_scheduler, stop_scheduler

from app.services.bot_service import run_bot
from app.services.auth_service import authenticate

from app.schemas.auth_schema import LoginRequest

from app.auth import (
    verify_token,
    decode_token,
    create_access_token
)


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    stop_scheduler()


app = FastAPI(
    title="Enterprise RPA API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "status": "ok"
    }


@app.post("/login")
def login(data: LoginRequest):
    return authenticate(
        data.username,
        data.password
    )


@app.post("/refresh")
def refresh(data: dict):

    refresh_token = data.get(
        "refresh_token"
    )

    payload = decode_token(
        refresh_token
    )

    username = payload.get("sub")

    return {
        "access_token": create_access_token(
            {
                "sub": username
            }
        )
    }


@app.post("/run/{bot_name}")
def execute(
    bot_name: str,
    user=Depends(verify_token)
):
    return run_bot(bot_name)