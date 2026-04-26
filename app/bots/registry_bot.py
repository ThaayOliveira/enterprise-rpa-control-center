from app.bots.report_bot import run_report_bot
from app.bots.health_bot import run_health_bot
from app.bots.monitor_bot import run_monitor_bot
from app.bots.reconcile_bot import run_reconcile_bot

BOT_REGISTRY = {
    "report": run_report_bot,
    "health": run_health_bot,
    "monitor": run_monitor_bot,
    "reconcile": run_reconcile_bot
}