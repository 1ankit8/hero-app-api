from typing import TYPE_CHECKING
from datetime import datetime
from app.db.base import Base
from sqlalchemy import DateTime, ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.role import Role

class UserRole(Base):
    __tablename__ = "user_roles"
    
    user_id: Mapped[str] = mapped_column(Uuid(as_uuid=False), ForeignKey("users.id"), primary_key=True)
    user: Mapped["User"] = relationship("User", back_populates="user_roles", foreign_keys=[user_id])
    role_id: Mapped[str] = mapped_column(Uuid(as_uuid=False), ForeignKey("roles.id"), primary_key=True)
    role: Mapped["Role"] = relationship("Role", back_populates="user_roles", foreign_keys=[role_id])
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default="now()")
    created_by: Mapped[str] = mapped_column(Uuid(as_uuid=False), ForeignKey("users.id"), nullable=False)
    created_by_user: Mapped["User"] = relationship("User", back_populates="created_user_roles", foreign_keys=[created_by])