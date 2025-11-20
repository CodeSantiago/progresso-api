from sqlalchemy.orm import Session
from app.models.user import User
from app.services.auth_service import AuthService

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not AuthService.verify_password(password, user.hashed_password):
        return None
    return user
