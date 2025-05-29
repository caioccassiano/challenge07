from src.models.settings.base import Base
from sqlalchemy import BIGINT, Column, String

class UserTable(Base):
  __tablename__ = "users"
  id = Column(BIGINT, primary_key=True, autoincrement=True)
  username = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)


