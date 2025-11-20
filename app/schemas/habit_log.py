from pydantic import BaseModel
from datetime import date
from typing import Optional

class HabitLogCreate(BaseModel):
    date: Optional[date] = None  

class HabitLogResponse(BaseModel):
    id: int
    habit_id: int
    date: date
    completed: bool

    model_config = {"from_attributes": True}
