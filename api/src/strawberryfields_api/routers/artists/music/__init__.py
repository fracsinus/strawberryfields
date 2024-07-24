from typing import Annotated

from fastapi import APIRouter, Depends, Form, UploadFile

from ...._types import AuthInfo
from ....services.artists import music
from ....utils.auth import check_artist

router = APIRouter(prefix="/{artist_id}/music")


@router.post("")
async def upload_music(
    auth_info: Annotated[AuthInfo, Depends(check_artist)],
    file: UploadFile,
    title: Annotated[str, Form()],
):
    if not file.filename:
        raise # TODO

    # TODO: check asynchronous execution

    return await music.upload_music(file.file, auth_info.user_id, title, file.filename)


@router.get("")
async def list_music(auth_info: Annotated[AuthInfo, Depends(check_artist)]):
    return await music.list_music(auth_info.user_id)


@router.get("/{music_id}/companies")
async def list_companies(
    auth_info: Annotated[AuthInfo, Depends(check_artist)],
    music_id: int,
):
    return await music.list_companies(music_id)
