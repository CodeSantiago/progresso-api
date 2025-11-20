from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey
from app.db.database import Base

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"))
    date = Column(Date)
    completed = Column(Boolean, default=True)
