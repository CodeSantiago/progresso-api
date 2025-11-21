from pydantic import BaseModel
from typing import Optional
from datetime import date

class HabitLogCreate(BaseModel):
    date: Optional[date] = None

    model_config = {
        "from_attributes": True
    }
