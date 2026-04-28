import time
import requests
import logging

def run_monitor_bot():
    logging.info("MonitorBot iniciado")

    try:
        inicio = time.time()

        resp = requests.get("https://google.com", timeout=5)

        tempo = round(time.time() - inicio, 2)

        if resp.status_code == 200:
            return {
                "status": "success",
                "message": f"Tempo resposta: {tempo}s"
            }

        return {
            "status": "error",
            "message": "Falha no monitoramento"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }