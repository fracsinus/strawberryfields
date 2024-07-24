from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from asyncpg.exceptions import UniqueViolationError

from ..._types import UserType
from ..._types._primordial import RegisterData
from ...config import config
from ...utils import generate_access_token, get_user_table
from ...utils.database import get_conn


async def register(user_type: UserType, user_data: RegisterData) -> tuple[int, str]:
    """return access token"""
    table = get_user_table(user_type)

    conn = await get_conn()
    now = datetime.now(timezone.utc)
    access_token = generate_access_token()
    access_token_expires_at = now + timedelta(
        seconds=config.access_token_lifetime_seconds
    )
    pw_hash = PasswordHasher().hash(user_data.password)

    async with conn.transaction():
        try:
            insert_query = await conn.prepare(
                f"""
                INSERT INTO {table} (
                    email,
                    pw_hash,
                    created_at
                ) VALUES ($1, $2, $3)
                RETURNING id
            ;"""
            )
            user_id = (await insert_query.fetchrow(
                user_data.email,
                pw_hash,
                now,
            ))["id"] # type: ignore
        except UniqueViolationError:
            raise  # TODO:

        retry_count = 0
        while retry_count < config.collision_max_retry:
            try:
                await conn.execute(
                    f"""
                        UPDATE {table}
                        SET
                            access_token = $1,
                            access_token_created_at = $2,
                            access_token_expires_at = $3
                        WHERE id = $4
                    ;""",
                    access_token,
                    now,
                    access_token_expires_at,
                    user_id,
                )
                return (user_id, access_token)
            except UniqueViolationError:
                retry_count += 1

        raise  # TODO
