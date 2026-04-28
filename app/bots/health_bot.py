import requests
import logging

def run_health_bot():
    logging.info("Health bot iniciado")

    try:
        resp = requests.get("https://google.com", timeout=5)

        if resp.status_code == 200:
            return {
                "status": "success",
                "message": "Site online"
            }

        return {
            "status": "error",
            "message": "Site indisponível"
        }

    except Exception as e:
        logging.error(str(e))

        return {
            "status": "error",
            "message": str(e)
        }