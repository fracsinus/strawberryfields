from pydantic import BaseModel

from ..._types import UserType


class AuthResponse(BaseModel):
    user_type: UserType
    id: int
    access_token: str
