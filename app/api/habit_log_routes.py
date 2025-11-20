from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app.db.database import get_db
from app.core.security import get_current_user
from app.services.habit_log_service import habit_log_service
from app.schemas.habit_log import HabitLogCreate, HabitLogResponse
from app.models.habit import Habit

router = APIRouter()

@router.post("/{habit_id}/log", response_model=HabitLogResponse)
def mark_completed(
    habit_id: int,
    log: HabitLogCreate,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Mark a habit as completed for a specific date.
    If the date is not provided, the service defaults to today's date.
    """

    # Ensure the habit belongs to the authenticated user
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == user.id
    ).first()

    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")

    # Delegate the creation of the log entry to the service layer
    return habit_log_service.mark_completed(
        habit_id,
        log.date,
        db
    )


@router.get("/{habit_id}/log", response_model=list[HabitLogResponse])
def get_logs(
    habit_id: int,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve all log entries for a habit.
    Only the owner of the habit can access its logs.
    """

    # Ensure the habit belongs to the authenticated user
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == user.id
    ).first()

    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")

    # Fetch all logs through the service layer
    return habit_log_service.get_logs(habit_id, db)
