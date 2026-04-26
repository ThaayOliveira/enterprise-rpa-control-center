from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone
from app.database import Base

class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True)
    bot_name = Column(String)
    status = Column(String)
    message = Column(String)
    duration = Column(Float)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))