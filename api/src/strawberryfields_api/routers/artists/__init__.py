from fastapi import APIRouter

from . import auth, music, pitch

router = APIRouter(prefix="/artists")

router.include_router(auth.router)
router.include_router(music.router)
router.include_router(pitch.router)
