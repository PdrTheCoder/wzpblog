from pydantic import BaseModel, Field
from typing import Optional


class BlogValidated(BaseModel):
    title: str
    body: str
    category_id: int


class CategoryValidated(BaseModel):
    name: str