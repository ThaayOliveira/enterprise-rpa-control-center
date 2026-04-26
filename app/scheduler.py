from apscheduler.schedulers.background import BackgroundScheduler
from app.services.bot_service import run_bot

scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(
        lambda: run_bot("report"),
        trigger="interval",
        minutes=5,
        id="report_bot_job",
        replace_existing=True,
        max_instances=1
    )
    scheduler.start()


# encerra scheduler
def stop_scheduler():
    scheduler.shutdown()
