from pydantic import BaseModel
from typing import Optional
from datetime import date


#Schema for creating or updating a habit

class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str  # e.g. "daily", "weekly"



#Schema for habit responses

class HabitResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    frequency: str
    user_id: int  # owner of the habit

    class Config:
        orm_mode = True  # enable conversion from SQLAlchemy models



#Schema for creating a habit log
# User can send a date or leave it empty (defaults to today)

class HabitLogCreate(BaseModel):
    date: Optional[date] = date.today()



#Schema for returning a habit log

class HabitLogResponse(BaseModel):
    id: int
    habit_id: int
    date: date
    completed: bool

    class Config:
        orm_mode = True
