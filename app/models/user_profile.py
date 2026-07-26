from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[str] = mapped_column(Uuid(as_uuid=False), primary_key=True, default=lambda: str(uuid4()))
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(Uuid(as_uuid=False), ForeignKey("users.id"), unique=True, nullable=False, index=True)
    user: Mapped["User"] = relationship(back_populates="profile")
    bio: Mapped[str | None] = mapped_column(nullable=True)
    image_url: Mapped[str | None] = mapped_column(nullable=True)
    # phone_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    address_line1: Mapped[str] = mapped_column(nullable=False)
    address_line2: Mapped[str | None] = mapped_column(nullable=True)
    address_line3: Mapped[str | None] = mapped_column(nullable=True)
    city: Mapped[str] = mapped_column(nullable=False, index=True)
    state: Mapped[str] = mapped_column(nullable=False, index=True)
    country: Mapped[str] = mapped_column(nullable=False, index=True)
    pin_code: Mapped[str] = mapped_column(nullable=False, index=True)