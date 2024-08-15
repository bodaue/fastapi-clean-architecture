from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
