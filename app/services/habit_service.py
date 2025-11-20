from sqlalchemy.orm import Session
from app.models.habit import Habit
from app.schemas.habit import HabitCreate

class HabitService:

    def create_habit(self, habit_data: HabitCreate, user_id: int, db: Session):
        # Create a new habit associated with the current user
        new_habit = Habit(
            user_id=user_id,
            name=habit_data.name,
            description=habit_data.description,
            frequency=habit_data.frequency
        )

        db.add(new_habit)
        db.commit()
        db.refresh(new_habit)
        return new_habit

    def list_habits(self, user_id: int, db: Session):
        # List all habits that belong to the authenticated user
        return db.query(Habit).filter(Habit.user_id == user_id).all()

    def get_habit(self, habit_id: int, user_id: int, db: Session):
        # Retrieve a single habit, ensuring it belongs to the user
        return db.query(Habit).filter(
            Habit.id == habit_id,
            Habit.user_id == user_id
        ).first()

    def update_habit(self, habit_id: int, user_id: int, data: HabitCreate, db: Session):
        # Update an existing habit after verifying ownership
        habit = self.get_habit(habit_id, user_id, db)

        if not habit:
            return None

        habit.name = data.name
        habit.description = data.description
        habit.frequency = data.frequency

        db.commit()
        db.refresh(habit)
        return habit

    def delete_habit(self, habit_id: int, user_id: int, db: Session):
        # Delete a habit only if it exists and belongs to the user
        habit = self.get_habit(habit_id, user_id, db)

        if not habit:
            return None

        db.delete(habit)
        db.commit()
        return True


# Singleton instance of the service
habit_service = HabitService()
