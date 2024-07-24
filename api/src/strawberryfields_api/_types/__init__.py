from enum import Enum

from pydantic import BaseModel


class UserType(Enum):
    artist = "artists"
    company = "companies"


class AuthInfo(BaseModel):
    user_type: UserType
    user_id: int
    email: str
    access_token: str
