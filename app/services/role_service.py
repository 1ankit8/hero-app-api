from app.models.role import Role
from app.schemas.role import CreateRole, UpdateRole
from app.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def list_roles(self, skip: int = 0, limit: int = 100) -> list[Role]:
        return self.repository.get_all(skip=skip, limit=limit)

    def get_role(self, role_id: str) -> Role | None:
        return self.repository.get_by_id(role_id=role_id)
    
    def create_role(self, new_role: CreateRole) -> Role:
        role = Role(**new_role.model_dump())
        return self.repository.create(role)
    
    def update_role(self, role_id: str, updated_role: UpdateRole, current_role: Role) -> Role | None:
        if current_role and current_role.id == role_id:
            for key, value in updated_role.model_dump(exclude_unset=True).items():
                setattr(current_role, key, value)
            return self.repository.update(current_role)
        return None
        
    def delete_role(self, role_id: str, current_role: Role) -> bool:
        if current_role and current_role.id == role_id:
            return self.repository.delete(current_role)
        return False
