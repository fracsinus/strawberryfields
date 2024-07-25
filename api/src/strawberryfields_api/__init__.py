from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router
from .config import config

origins = config.cors_origin

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(router)
