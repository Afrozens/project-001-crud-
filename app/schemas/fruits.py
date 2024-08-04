from pydantic import UUID4, BaseModel
from datetime import datetime
from typing import Optional


class FruitBase(BaseModel):
    name: str = None
    price: int = None
    description: str = None
    Finish_Line_at: datetime
    place: Optional[datetime]
    featured: bool = False

class FruitCreate(FruitBase):
    pass

class FruitUpdate(FruitBase):
    id: UUID4

class FruitInDbBase(FruitBase):
    id: UUID4

    created_at: datetime
    deleted_at: Optional[datetime]

