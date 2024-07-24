from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
