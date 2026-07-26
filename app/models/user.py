from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, UniqueConstraint, func, DateTime, Uuid
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user_profile import UserProfile
    from app.models.associations import UserRole

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    email: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    isActive: Mapped[bool] = mapped_column(nullable=False, default=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    profile: Mapped["UserProfile"] = relationship(back_populates="user", uselist=False)
    created_user_roles: Mapped[list["UserRole"]] = relationship("UserRole", back_populates="created_by_user", foreign_keys="[UserRole.created_by]", uselist=True)
    user_roles: Mapped[list["UserRole"]] = relationship("UserRole", back_populates="user", foreign_keys="[UserRole.user_id]", uselist=True)
    
    __table_args__ = (
        # Unique constraint on email and phone_number
        UniqueConstraint('email', 'phone_number', name='uq_user_email_phone'),
    )
