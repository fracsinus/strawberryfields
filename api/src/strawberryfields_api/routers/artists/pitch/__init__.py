from typing import Annotated

from fastapi import APIRouter, Body, Depends

from ...._types import AuthInfo
from ....services.artists import pitch
from ....utils.auth import check_artist

router = APIRouter(prefix="/{artist_id}/pitch")


@router.get("")
async def list_pitch(auth_info: Annotated[AuthInfo, Depends(check_artist)]):
    return await pitch.list_pitch(auth_info.user_id)


@router.post("")
async def post_pitch(
    auth_info: Annotated[AuthInfo, Depends(check_artist)],
    music_id: Annotated[int, Body()],
    company_id: Annotated[int, Body()],
):
    return await pitch.insert_pitch(auth_info.user_id, music_id, company_id)
