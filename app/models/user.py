# User database model (ORM)
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)  # Unique email for login
    hashed_password = Column(String, nullable=False)  # Bcrypt hash (72 byte limit)

    # Relationship to Habit model: one user has many habits
    habits = relationship("Habit", back_populates="owner", cascade="all, delete")