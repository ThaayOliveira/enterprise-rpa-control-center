import logging

def run_reconcile_bot():
    logging.info("ReconcileBot iniciado")

    try:
        sistema_a = ["cliente1", "cliente2", "cliente3"]
        sistema_b = ["cliente1", "cliente3"]

        faltantes = list(set(sistema_a) - set(sistema_b))

        if faltantes:
            return {
                "status": "success",
                "message": f"Pendências: {faltantes}"
            }

        return {
            "status": "success",
            "message": "Conciliação OK"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }