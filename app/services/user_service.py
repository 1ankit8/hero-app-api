
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user import CreateUser

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def list_users(self, skip: int = 0, limit: int= 100) -> list[User]:
        return self.repository.get_all(skip=skip, limit=limit)

    def create_user(self, data: CreateUser) -> User:
        user = User(**data.model_dump())
        return self.repository.create(user)
