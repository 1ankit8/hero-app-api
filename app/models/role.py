from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import DateTime, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.associations import UserRole


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[str] =mapped_column(Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user_roles: Mapped[list["UserRole"]] = relationship("UserRole", back_populates="role", foreign_keys="[UserRole.role_id]", uselist=True)
