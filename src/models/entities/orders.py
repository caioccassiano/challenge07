from src.models.settings.base import Base
from sqlalchemy import BIGINT, Column, String, ForeignKey, DateTime
from datetime import datetime, timezone

class OrdersTable(Base):
  __tablename__ = "orders"
  id = Column(BIGINT, primary_key=True, autoincrement=True)
  user_id = Column(BIGINT, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  description = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), default=lambda:datetime.now(timezone.utc), nullable=False)

