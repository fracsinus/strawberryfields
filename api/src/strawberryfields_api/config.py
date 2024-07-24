from dataclasses import dataclass
import os


@dataclass
class Config:
    database_password: str
    s3_bucket: str
    s3_access_key: str
    s3_secret: str
    collision_max_retry: int = 3
    access_token_lifetime_seconds: int = 3600
    database_host: str = "db"
    database_port: int = 5432
    database_user: str = "sbf"
    database_schema: str = "sbf"


DEFAULT_CONFIG = Config(
    database_password=os.environ["POSTGRES_PASSWORD"],
    s3_bucket=os.environ["S3_BUCKET"],
    s3_access_key=os.environ["S3_ACCESS_KEY"],
    s3_secret=os.environ["S3_SECRET"],
)

# TODO: remote config
config = DEFAULT_CONFIG
