from datetime import datetime, timezone
from typing import Annotated
import secrets

from fastapi import Header

from .._types import AuthInfo, UserType
from ..config import config
from ..utils import get_user_table
from ..utils.database import get_conn


async def check_auth(user_id: int, user_type: UserType, access_token: str):
    """primordial"""
    now = datetime.now(timezone.utc)
    table = get_user_table(user_type)
    conn = await get_conn()
    select_query = await conn.prepare(f"""
        SELECT
            id,
            email,
            pw_hash,
            access_token,
            access_token_expires_at
        FROM {table}
        WHERE
            id = $1
            AND access_token = $2
    ;""")
    row = await select_query.fetchrow(user_id, access_token)
    if not row:
        raise # TODO

    if not secrets.compare_digest(access_token, row["access_token"]):
        raise # TODO

    if (
        now - row["access_token_expires_at"]
    ).total_seconds() > config.access_token_lifetime_seconds:
        raise

    return AuthInfo(user_type=user_type, user_id=row["id"], email=row["email"], access_token=row["access_token"])



async def check_artist(artist_id: int, Authorization: Annotated[str, Header()]):
    try:
        access_token = Authorization.split(" ")[1]
    except IndexError:
        raise # TODO
    return await check_auth(artist_id, UserType.artist, access_token)


async def check_company(company_id: int, Authorization: Annotated[str, Header()]):
    try:
        access_token = Authorization.split(" ")[1]
    except IndexError:
        raise # TODO
    return await check_auth(company_id, UserType.company, access_token)
