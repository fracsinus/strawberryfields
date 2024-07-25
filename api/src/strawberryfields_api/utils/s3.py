from typing import IO
from botocore.response import StreamingBody
import boto3

from .._types import AuthInfo
from ..config import config


def _get_client():
    return  boto3.client(
        "s3",
        aws_access_key_id=config.s3_access_key,
        aws_secret_access_key=config.s3_secret,
    )


def upload(file: IO, checksum: str, artist_id: int, title: str):
    s3 = _get_client()
    file.seek(0)
    s3.upload_fileobj(file, config.s3_bucket, f"artists/{artist_id}/music/{checksum}")


def download_stream(key) -> StreamingBody:
    s3 = _get_client()
    resp = s3.get_object(Bucket=config.s3_bucket, Key=key)
    return resp["Body"]
