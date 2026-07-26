from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    email: str
    phone_number: str
    isActive: bool
    created_at: datetime
    updated_at: datetime

class CreateUser(BaseModel):
    phone_number: str = Field(..., min_length=10, max_length=20)
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', min_length=5, max_length=100)
    
class UserIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phone_number: str
    isActive: bool
    email: str