import time
import logging

from app.database import SessionLocal
from app.models import Execution

from app.bots.report_bot import run_report_bot
from app.bots.health_bot import run_health_bot
from app.bots.monitor_bot import run_monitor_bot
from app.bots.reconcile_bot import run_reconcile_bot

# back-end

BOT_REGISTRY = {
    "report": run_report_bot,
    "health": run_health_bot,
    "monitor": run_monitor_bot,
    "reconcile": run_reconcile_bot
}


def run_bot(bot_name):
    db = SessionLocal()
    start = time.time()

    logging.info(f"Solicitação recebida para bot: {bot_name}")

    try:
        bot_function = BOT_REGISTRY.get(bot_name)

        if not bot_function:
            result = {
                "status": "error",
                "message": "Bot não encontrado"
            }

            logging.warning(f"Bot inexistente: {bot_name}")

        else:
            result = bot_function()

        duration = round(time.time() - start, 2)

        execution = Execution(
            bot_name=bot_name,
            status=result.get("status", "error"),
            message=result.get("message", "Sem mensagem"),
            duration=duration
        )

        db.add(execution)
        db.commit()

        logging.info(
            f"Bot {bot_name} finalizado | "
            f"status={execution.status} | "
            f"tempo={duration}s"
        )

        return result

    except Exception as e:
        db.rollback()

        logging.error(f"Erro no bot_service: {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        db.close()