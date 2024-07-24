from datetime import datetime, timezone
from typing import IO
import hashlib

from ...utils.database import get_conn
from ...utils.s3 import upload


async def upload_music(
    file: IO,
    artist_id: int,
    title: str,
    filename: str,
):
    h = hashlib.blake2b()
    h.update(file.read())
    checksum = h.hexdigest()
    now = datetime.now(timezone.utc)

    conn = await get_conn()
    try:
        insert_query = await conn.prepare(
            """
                INSERT INTO music (
                    artist_id, checksum, title, filename, created_at
                ) VALUES ($1, $2, $3, $4, $5)
            ;"""
        )
        await insert_query.fetch(artist_id, checksum, title, filename, now)
    except:
        raise # TODO: duplicate (artist_id, checksum) combination

    try:
        upload(file, checksum, artist_id, title)
    except:
        raise # TODO

    # TODO: need to somehow ensure consistency across db and S3

    return


async def list_music(artist_id: int) -> list:
    conn = await get_conn()
    rows = await conn.fetch(
        """
            SELECT id, title, filename, created_at
            FROM music
            WHERE artist_id = $1
        ;""",
        artist_id,
    )

    return rows


async def list_companies(music_id):
    conn = await get_conn()
    select_query = await conn.prepare(
        """
            SELECT
                companies.id,
                companies.email
            FROM companies
                LEFT JOIN pitching
                    ON companies.id  = pitching.company_id
                    AND pitching.music_id = $1
            WHERE pitching.music_id IS NULL
        ;"""
    )
    return await select_query.fetch(music_id)
