import asyncpg
from ..config import config


async def get_conn() -> asyncpg.Connection:
    return await asyncpg.connect(
        host=config.database_host,
        port=config.database_port,
        user=config.database_user,
        password=config.database_password,
        database=config.database_schema,
    )
