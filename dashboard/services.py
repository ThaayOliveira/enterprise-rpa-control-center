import requests
import os

API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000"
)


def login(username, password):
    return requests.post(
        f"{API_URL}/login",
        json={
            "username": username,
            "password": password
        }
    )


def refresh_token(refresh_token):
    return requests.post(
        f"{API_URL}/refresh",
        json={
            "refresh_token": refresh_token
        }
    )


def executar_bot(bot_name, token):
    return requests.post(
        f"{API_URL}/run/{bot_name}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=120
    )

def get_executions(token):
    return requests.get(
        f"{API_URL}/executions",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )