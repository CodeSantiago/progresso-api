from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    description = Column(String(255), nullable=True)
    frequency = Column(String(50))  # daily / weekly / custom
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="habits")
