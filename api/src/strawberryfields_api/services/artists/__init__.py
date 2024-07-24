from .. import _primordial
from ..._types import UserType
from ..._types._primordial import RegisterData, SignInData


async def register(user_data: RegisterData) -> tuple[int, str]:
    try:
        return await _primordial.register(UserType.artist, user_data)
    except:
        raise  # TODO


async def sign_in(user_data: SignInData) -> tuple[int, str]:
    try:
        return await _primordial.sign_in(UserType.artist, user_data)
    except:
        raise  # TODO
