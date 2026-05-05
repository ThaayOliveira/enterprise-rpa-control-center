import requests
import time
import os

BASE_URL = os.getenv("API_URL", "http://localhost:8000")

USERNAME = os.getenv("APP_USER")
PASSWORD = os.getenv("APP_PASSWORD")


def test_e2e_report_bot():
    login_resp = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": USERNAME,
            "password": PASSWORD
        }
    )

    assert login_resp.status_code == 200

    data = login_resp.json()
    token = data["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    run_resp = requests.post(
        f"{BASE_URL}/run/report",
        headers=headers
    )

    assert run_resp.status_code == 200
    result = run_resp.json()

    assert result["status"] == "success"

    time.sleep(1)

    exec_resp = requests.get(
        f"{BASE_URL}/executions",
        headers=headers
    )

    assert exec_resp.status_code == 200
    executions = exec_resp.json()

    assert len(executions) > 0
    assert executions[0]["bot_name"] == "report"
    assert executions[0]["status"] == "success"