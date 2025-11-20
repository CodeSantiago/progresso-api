# Import necessary dependencies for authentication service
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from passlib.context import CryptContext
import bcrypt
from app.services.token_service import create_access_token

# Hash password truncating to 72 bytes (bcrypt limit) and return bcrypt hash
def hash_password_direct(password: str) -> str:
    password_bytes = password.encode('utf-8')[:72]
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password_bytes, salt).decode('utf-8')

# Verify plain password against bcrypt hash, truncating to 72 bytes
def verify_password_direct(plain: str, hashed: str) -> bool:
    plain_bytes = plain.encode('utf-8')[:72]
    hashed_bytes = hashed.encode('utf-8') if isinstance(hashed, str) else hashed
    try:
        return bcrypt.checkpw(plain_bytes, hashed_bytes)
    except (ValueError, TypeError):
        return False


class AuthService:
    # Wrapper for hashing password
    def hash_password(self, password: str) -> str:
        return hash_password_direct(password)

    # Wrapper for verifying password
    def verify_password(self, plain: str, hashed: str) -> bool:
        return verify_password_direct(plain, hashed)

    # Register new user: check if exists, hash password, save to DB
    def register(self, user_data: UserCreate, db: Session) -> UserResponse:
        existing_user = (
            db.query(User)
            .filter(User.email == user_data.email)
            .first()
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_pass = self.hash_password(user_data.password)

        new_user = User(
            email=user_data.email,
            hashed_password=hashed_pass
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return UserResponse.model_validate(new_user)


auth_service = AuthService()

class AuthService:
    # Login: find user, verify password, generate JWT token
    def login(self, email: str, password: str, db: Session):
        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(
                status_code=400,
                detail="Invalid email or password"
            )

        if not self.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=400,
                detail="Invalid email or password"
            )

        access_token = create_access_token({"sub": str(user.id)})

        return {"access_token": access_token, "token_type": "bearer"}
