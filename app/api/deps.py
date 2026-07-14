from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repository import UserRepository

from app.services.role_service import RoleService
from app.services.user_service import UserService

DbSession = Annotated[Session, Depends(get_db)]


def get_role_service(db: DbSession) -> RoleService:
    return RoleService(RoleRepository(db))

def get_user_service(db: DbSession) -> UserService:
    return UserService(UserRepository(db))

RoleServiceDep = Annotated[RoleService, Depends(get_role_service)]
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
