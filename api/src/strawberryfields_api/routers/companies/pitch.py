from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from ..._types import AuthInfo
from ...services.companies import pitch
from ...utils.auth import check_company

router = APIRouter(prefix="/{company_id}/pitch")


@router.get("")
async def list_pitch(auth_info: Annotated[AuthInfo, Depends(check_company)]):
    return await pitch.list_pitch(auth_info.user_id)


@router.get("/{music_id}")
async def get_pitch(auth_info: Annotated[AuthInfo, Depends(check_company)], music_id: int):
    stream, filename = await pitch.get_pitch(auth_info.user_id, music_id)
    def _stream(s):
        yield from s


    return StreamingResponse(
        _stream(stream),
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
