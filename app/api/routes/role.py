from fastapi import APIRouter, Query

from app.api.deps import RoleServiceDep
from app.schemas.role import RoleOut

router = APIRouter()


@router.get("", response_model=list[RoleOut])
def list_roles(
    service: RoleServiceDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> list[RoleOut]:
    return service.list_roles(skip=skip, limit=limit)
