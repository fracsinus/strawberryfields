from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from ..._types import UserType
from ...services import companies
from ...services.companies._types import AuthResponse
from ..._types._primordial import RegisterData, SignInData

router = APIRouter(prefix="/auth")


@router.post("/sign-in")
async def sign_in(body: Annotated[SignInData, Body()]):
    # TODO: exception handling
    user_id, access_token = await companies.sign_in(body)
    return AuthResponse(
        user_type=UserType.company,
        id=user_id,
        access_token=access_token,
    )


@router.post("/register")
async def register(body: Annotated[RegisterData, Body()]):
    # TODO: exception handling
    user_id, access_token = await companies.register(body)
    return AuthResponse(
        user_type=UserType.company,
        id=user_id,
        access_token=access_token,
    )
