from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from ..._types import UserType
from ..._types._primordial import RegisterData, SignInData
from ...services import artists
from ...services.artists._types import AuthResponse

router = APIRouter(prefix="/auth")


@router.post("/sign-in")
async def sign_in(body: Annotated[SignInData, Body()]):  # TODO: return type
    # TODO: exception handling
    user_id, access_token = await artists.sign_in(body)
    return AuthResponse(
        user_type=UserType.artist,
        id=user_id,
        access_token=access_token,
    )


@router.post("/register")
async def register(body: Annotated[RegisterData, Body()]):
    # TODO: exception handling
    user_id, access_token = await artists.register(body)
    return AuthResponse(
        user_type=UserType.artist,
        id=user_id,
        access_token=access_token,
    )
