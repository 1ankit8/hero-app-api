from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, String, func, DateTime, Uuid
from app.db.base import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    firstname: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    avatarURL: Mapped[str | None] = mapped_column(String(255), nullable=True)
    isActive: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
