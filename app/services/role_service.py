from app.models.role import Role
from app.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def list_roles(self, skip: int = 0, limit: int = 100) -> list[Role]:
        return self.repository.get_all(skip=skip, limit=limit)
