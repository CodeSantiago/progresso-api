from sqlalchemy.orm import Session
from datetime import date

from app.models.habit_log import HabitLog

class HabitLogService:

    def mark_completed(self, habit_id: int, log_date: date, db: Session):
        # If no date is provided, default to today's date
        if log_date is None:
            log_date = date.today()

        # Check if a log entry for this habit already exists on this date
        existing = (
            db.query(HabitLog)
            .filter(HabitLog.habit_id == habit_id,
                    HabitLog.date == log_date)
            .first()
        )

        # If the log already exists, return it (prevent duplicates)
        if existing:
            return existing

        # Create a new log entry marking the habit as completed
        new_log = HabitLog(
            habit_id=habit_id,
            date=log_date,
            completed=True
        )

        # Save to database
        db.add(new_log)
        db.commit()
        db.refresh(new_log)

        return new_log

    def get_logs(self, habit_id: int, db: Session):
        # Retrieve all log entries for a specific habit
        return db.query(HabitLog).filter(HabitLog.habit_id == habit_id).all()


# Singleton instance of the service for easy reuse
habit_log_service = HabitLogService()
