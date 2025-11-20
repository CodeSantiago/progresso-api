from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.security import get_current_user
from app.services.stats_service import stats_service
from app.models.habit import Habit

router = APIRouter()


@router.get("/{habit_id}/streak")
def get_streak(
    habit_id: int,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve streak statistics (current streak and max streak)
    for a specific habit.
    
    Only the owner of the habit is allowed to access its statistics.
    """

    # Ensure the habit belongs to the authenticated user
    habit = db.query(Habit).filter(
        Habit.id == habit_id,
        Habit.user_id == user.id
    ).first()

    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")

    # Delegate the streak calculation to the service layer
    return stats_service.get_streak(habit_id, db)
