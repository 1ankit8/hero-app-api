from fastapi import APIRouter, Query

from app.api.deps import RoleServiceDep
from app.schemas.role import CreateRole, RoleOut, UpdateRole

router = APIRouter()


@router.get("", response_model=list[RoleOut])
def list_roles(
    service: RoleServiceDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
) -> list[RoleOut]:
    return service.list_roles(skip=skip, limit=limit)

@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: str, service: RoleServiceDep) -> RoleOut | None:
    return service.get_role(role_id=role_id)

@router.post("", response_model=RoleOut, status_code=201)
def create_role(new_role: CreateRole, service: RoleServiceDep) -> RoleOut:
    return service.create_role(new_role=new_role)

@router.patch("/{role_id}", response_model=RoleOut)
def update_role(role_id: str, updated_role: UpdateRole, service: RoleServiceDep) -> RoleOut | None:
    current_role = service.get_role(role_id=role_id)
    return service.update_role(role_id=role_id, updated_role=updated_role, current_role=current_role)

@router.delete("/{role_id}", status_code=204)
def delete_role(role_id: str, service: RoleServiceDep) -> None:
    current_role = service.get_role(role_id=role_id)
    if service.delete_role(role_id=role_id, current_role=current_role):
        return None
    return None