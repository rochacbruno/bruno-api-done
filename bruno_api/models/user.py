from typing import Optional, List
from pydantic import BaseModel, validator, ValidationError
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False, sa_column_kwargs={"unique": True})
    superuser: bool = False
    password: str


# Serializers

class ValidatePassword(BaseModel):
    @validator('confirm_password', allow_reuse=True, check_fields=False)
    def validate_password(cls, v, values, **kwargs):
        if v != values['password']:
            raise ValueError("Passwords don't match")
        return v


class UserIn(ValidatePassword):
    username: str
    superuser: bool = False
    password: str
    confirm_password: str


class UserPatch(ValidatePassword):
    superuser: Optional[bool]
    password: Optional[str]
    confirm_password: Optional[str]


class UserOut(BaseModel):
    username: str
    superuser: bool


UserOutList = List[UserOut]

