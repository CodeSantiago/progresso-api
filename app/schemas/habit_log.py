from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class HabitLogCreate(BaseModel):
    date: Optional[date] = Field(default_factory=date.today)


class HabitLogResponse(BaseModel):
    id: int
    habit_id: int
    date: date
    completed: bool

    model_config = {
        "from_attributes": True
    }
