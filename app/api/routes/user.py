from fastapi import APIRouter, Query, status
from app.api.deps import UserServiceDep
from app.models.user import User
from app.schemas.user import CreateUser, UserOut

router = APIRouter()

@router.get("", response_model=list[UserOut])
def list_users(
    service: UserServiceDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> list[UserOut]:
    return service.list_users(skip=skip, limit=limit)

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, service: UserServiceDep) -> User:
    return service.create_user(user)