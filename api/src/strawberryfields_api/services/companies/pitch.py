from ...utils.database import get_conn

async def list_pitch(company_id: int):
    conn = await get_conn()
    return await conn.fetch(
        """
            SELECT
                artists.email,
                music.title,
                pitching.created_at
            FROM music
                JOIN pitching
                    ON music.id = pitching.music_id
                JOIN artists
                    ON music.artist_id = artists.id
            WHERE
                pitching.company_id = $1
        ;""",
        company_id,
    )
