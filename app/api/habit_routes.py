from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.db.database import get_db
from app.schemas.habit import HabitCreate, HabitResponse
from app.services.habit_service import habit_service
from app.core.security import get_current_user

router = APIRouter()


@router.post("/", response_model=HabitResponse)
def create_habit(
    habit: HabitCreate,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Create a new habit for the authenticated user.
    Delegates the creation logic to the service layer.
    """
    return habit_service.create_habit(habit, user.id, db)


@router.get("/", response_model=list[HabitResponse])
def list_habits(
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Return all habits owned by the authenticated user.
    """
    return habit_service.list_habits(user.id, db)


@router.get("/{habit_id}", response_model=HabitResponse)
def get_habit(
    habit_id: int,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve a single habit by its ID.
    Raises 404 if the habit does not belong to the user
    or does not exist.
    """
    habit = habit_service.get_habit(habit_id, user.id, db)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit


@router.put("/{habit_id}", response_model=HabitResponse)
def update_habit(
    habit_id: int,
    data: HabitCreate,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update an existing habit.
    Only the owner of the habit can modify it.
    """
    updated = habit_service.update_habit(habit_id, user.id, data, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Habit not found")
    return updated


@router.delete("/{habit_id}")
def delete_habit(
    habit_id: int,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete a habit belonging to the authenticated user.
    Returns a success message if deletion is completed.
    """
    deleted = habit_service.delete_habit(habit_id, user.id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Habit not found")

    return {"message": "Habit deleted successfully"}
