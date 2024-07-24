from datetime import datetime, timezone

from ...utils.database import get_conn


async def list_pitch(artist_id: int):
    conn = await get_conn()
    return await conn.fetch(
        """
            SELECT
                music.title,
                companies.email,
                pitching.created_at
            FROM music
                JOIN pitching
                    ON music.id = music_id
                JOIN companies
                    ON company_id = companies.id
            WHERE
                music.artist_id = $1
        ;""",
        artist_id
    )



async def insert_pitch(artist_id: int, music_id: int, company_id: int):
    now = datetime.now(timezone.utc)
    conn = await get_conn()
    row = await conn.fetchrow(
        """
            SELECT
                count(music.id) AS music,
                count(pitching.company_id) AS company
            FROM music
                LEFT JOIN pitching
                    ON music.id = pitching.music_id
                    AND pitching.company_id = $1
            WHERE
                music.id = $2
                AND music.artist_id = $3
        ;""",
        company_id,
        music_id,
        artist_id,
    )

    if not row:
        raise # unreachable

    if not row["music"]:
        raise # TODO

    if row["company"]:
        raise # TODO

    await conn.execute(
        "INSERT INTO pitching (music_id, company_id, created_at) VALUES ($1, $2, $3);",
        music_id,
        company_id,
        now,
    )
