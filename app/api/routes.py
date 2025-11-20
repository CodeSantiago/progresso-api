# Main API router that aggregates all sub-routers
from fastapi import APIRouter

from app.api.auth_routes import router as auth_router
from app.api.habit_routes import router as habit_router
from app.api.habit_log_routes import router as habit_log_router
from app.api.stats_routes import router as stats_router

router = APIRouter()

# Group all routes by prefix and tags for API documentation
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(habit_router, prefix="/habits", tags=["Habits"])
router.include_router(habit_log_router, prefix="/habits", tags=["Habit Logs"])
router.include_router(stats_router, prefix="/habits", tags=["Stats"])
