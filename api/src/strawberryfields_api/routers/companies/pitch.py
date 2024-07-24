from typing import Annotated

from fastapi import APIRouter, Depends

from ..._types import AuthInfo
from ...services.companies import pitch
from ...utils.auth import check_company

router = APIRouter(prefix="/{company_id}/pitch")


@router.get("")
async def list_pitch(auth_info: Annotated[AuthInfo, Depends(check_company)]):
    return await pitch.list_pitch(auth_info.user_id)
