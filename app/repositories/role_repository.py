from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Role]:
        stmt = select(Role).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())
