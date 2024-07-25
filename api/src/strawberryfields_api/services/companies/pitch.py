from ...utils.database import get_conn
from ...utils.s3 import download_stream

async def list_pitch(company_id: int):
    conn = await get_conn()
    return await conn.fetch(
        """
            SELECT
                artists.email,
                music.id AS music_id,
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


async def get_pitch(company_id, music_id):
    conn = await get_conn()
    row = await conn.fetchrow(
        """
            SELECT
                music.artist_id,
                music.filename,
                music.checksum
            FROM pitching
                JOIN music
                    ON pitching.music_id = music.id
            WHERE
                pitching.music_id = $1
                AND pitching.company_id = $2
        ;""",
        music_id,
        company_id,
    )

    if not row:
        raise # TODO

    key = "artists/{}/music/{}".format(row["artist_id"], row["checksum"])
    print(key)

    return download_stream(key), row["filename"]
