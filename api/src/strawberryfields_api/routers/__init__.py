from fastapi import APIRouter

from . import artists, companies

router = APIRouter()
router.include_router(artists.router)
router.include_router(companies.router)
