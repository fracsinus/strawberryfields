import secrets
import string

from .._types import UserType
from ..config import config


def get_user_table(user_type: UserType) -> str:
    match user_type:
        case UserType.artist:
            return "artists"
        case UserType.company:
            return "companies"


def generate_access_token():
    space = string.ascii_letters + string.digits
    return "".join(secrets.choice(space) for _ in range(32))
