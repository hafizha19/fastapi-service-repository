from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Holiday(BaseModel):
    id: str = Field(alias="_id")
    title: str
    code: str
    description: Optional[str] = None
    year: Optional[int] = None
    date: date
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    deletedAt: Optional[datetime] = None
