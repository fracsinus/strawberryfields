from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from argon2.exceptions import VerificationError
from asyncpg.exceptions import UniqueViolationError

from ..._types import UserType
from ..._types._primordial import SignInData
from ...config import config
from ...utils import generate_access_token, get_user_table
from ...utils.database import get_conn


async def sign_in(user_type: UserType, user_data: SignInData) -> tuple[int, str]:
    """returns access token"""
    table = get_user_table(user_type)

    conn = await get_conn()
    now = datetime.now(timezone.utc)

    select_query = await conn.prepare(
        f"""
        SELECT
            id,
            pw_hash,
            access_token,
            access_token_expires_at
        FROM {table}
        WHERE email = $1
    ;"""
    )

    row = await select_query.fetchrow(user_data.email)

    if not row:
        raise  # TODO

    try:
        PasswordHasher().verify(row["pw_hash"], user_data.password)
    except VerificationError as e:
        raise e  # TODO

    if (
        now - row["access_token_expires_at"]
    ).total_seconds() < config.access_token_lifetime_seconds:
        return (row["id"], row["access_token"])

    else:
        access_token = generate_access_token()
        access_token_expires_at = now + timedelta(
            seconds=config.access_token_lifetime_seconds
        )

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
                        WHERE email = $4
                    ;""",
                    access_token,
                    now,
                    access_token_expires_at,
                    user_data.email,
                )
                return (row["id"], access_token)
            except UniqueViolationError:
                retry_count += 1

    raise  # TODO
