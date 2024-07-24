from pydantic import BaseModel

from ..._types import UserType


class SignInData(BaseModel):
    """primordial: to evole/diverge in the future"""
    user_type: UserType
    email: str
    password: str


RegisterData = SignInData


class AuthResponse(BaseModel):
    user_type: UserType
    id: int
    access_token: str
