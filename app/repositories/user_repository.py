from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User


class UserRepository:
    def __init__(self, dbSession: Session):
        self.db = dbSession
    
    def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        stmt = select(User).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())
