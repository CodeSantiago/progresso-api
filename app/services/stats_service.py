from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.models.habit_log import HabitLog

class StatsService:

    def get_streak(self, habit_id: int, db: Session):

        # Fetch all logs for the habit, ordered from newest to oldest
        logs = (
            db.query(HabitLog)
            .filter(HabitLog.habit_id == habit_id)
            .order_by(HabitLog.date.desc())
            .all()
        )

        # If the habit has no logs, the streaks are zero
        if not logs:
            return {"current_streak": 0, "max_streak": 0}

        current_streak = 0
        max_streak = 0

        today = date.today()
        expected_day = today

   
        # Count consecutive days starting from today backwards
        for log in logs:
            if log.date == expected_day:
                current_streak += 1
                expected_day -= timedelta(days=1)
            else:
                break

     
        # max streak all-time calculation
     
        max_streak = 1
        streak = 1

        # Check consecutive sequences in the full history
        for i in range(1, len(logs)):
            if logs[i].date == logs[i - 1].date - timedelta(days=1):
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 1

        # Edge case: last streak might be the longest
        max_streak = max(max_streak, streak)

        return {
            "current_streak": current_streak,
            "max_streak": max_streak
        }

# Singleton instance for easy reuse
stats_service = StatsService()
