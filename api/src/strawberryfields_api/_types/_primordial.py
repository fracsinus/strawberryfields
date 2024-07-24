"""primordial type definitions, which are to evolve/diverge in the future"""

from pydantic import BaseModel


class SignInData(BaseModel):
    """primordial: to evole/diverge in the future"""
    email: str
    password: str


RegisterData = SignInData
