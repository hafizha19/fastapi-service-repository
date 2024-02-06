from datetime import date
from typing import Optional

from pydantic import BaseModel


class Holiday(BaseModel):
    title: str
    code: str
    description: Optional[str] = None
    year: Optional[int] = None
    date: date
