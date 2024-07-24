from fastapi import APIRouter

from . import auth, pitch

router = APIRouter(prefix="/companies", tags=["auth"])

router.include_router(auth.router)
router.include_router(pitch.router)
