from fastapi import APIRouter, Query
from app.api.deps import UserServiceDep
from app.models.user import User
from app.schemas.user import UserOut

router = APIRouter()

@router.get("", response_model=list[UserOut])
def list_users(
    service: UserServiceDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> list[UserOut]:
    return service.list_users(skip=skip, limit=limit)