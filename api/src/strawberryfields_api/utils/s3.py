from typing import IO
import boto3

from .._types import AuthInfo
from ..config import config


def upload(file: IO, checksum: str, artist_id: int, title: str):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=config.s3_access_key,
        aws_secret_access_key=config.s3_secret,
    )
    file.seek(0)
    s3.upload_fileobj(file, config.s3_bucket, f"artists/{artist_id}/music/{checksum}")
