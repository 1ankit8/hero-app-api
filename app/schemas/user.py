from pydantic import BaseModel, ConfigDict

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    firstname: str
    lastname: str
    email: str
    avatarURL: str | None