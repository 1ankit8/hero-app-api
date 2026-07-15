from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Role]:
        stmt = select(Role).offset(skip).limit(limit)
        return list(self.db.execute(stmt).scalars().all())
    
    def create(self, role: Role) -> Role:
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role
    
    def get_by_id(self, role_id: int) -> Role | None:
        stmt = select(Role).where(Role.id == role_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def update(self, role_to_update: Role) -> Role:
        self.db.add(role_to_update)
        self.db.commit()
        self.db.refresh(role_to_update)
        return role_to_update
    
    def delete(self, role_to_delete: Role) -> bool:
        if role_to_delete:
            self.db.delete(role_to_delete)
            self.db.commit()
            return True
        return False
