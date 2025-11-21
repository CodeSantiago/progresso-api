from pydantic import BaseModel
from typing import Optional
from datetime import date

class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str

class HabitResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    frequency: str
    user_id: int

    class Config:
        orm_mode = True
