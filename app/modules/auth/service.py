from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.modules.auth.repository import user_repository
from app.modules.auth.schema import UserCreate
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    def create_token(self, user_id: int) -> str:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        return jwt.encode(
            {"sub": str(user_id), "exp": expire},
            settings.SECRET_KEY,
            algorithm="HS256"
        )

    def register(self, db: Session, data: UserCreate):
        existing = user_repository.get_by_email(db, data.email)
        if existing:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "DUPLICATE_EMAIL",
                                  "message": "Email already registered"}}
            )
        hashed = self.hash_password(data.password)
        return user_repository.create(db, data.email, data.full_name, hashed)

    def login(self, db: Session, email: str, password: str):
        user = user_repository.get_by_email(db, email)
        if not user or not self.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=401,
                detail={"error": {"code": "INVALID_CREDENTIALS",
                                  "message": "Invalid email or password"}}
            )
        token = self.create_token(user.id)
        return {"access_token": token, "token_type": "bearer"}

auth_service = AuthService()