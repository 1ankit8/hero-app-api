from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    firstname: str
    lastname: str
    email: str
    avatarURL: str | None
    userImage: str | None
    created_at: datetime
    updated_at: datetime

class CreateUser(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=100)
    lastname: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', min_length=5, max_length=100)
    userImage: str | None = None
    
class UserIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    firstname: str
    lastname: str
    email: str
    avatarURL: str | None
    userImage: str | None