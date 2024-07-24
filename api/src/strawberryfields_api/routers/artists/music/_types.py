from pydantic import BaseModel
from fastapi import File, Form, UploadFile


class UploadData(BaseModel):
    title: str
