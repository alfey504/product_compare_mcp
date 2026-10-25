from pydantic import BaseModel
from typing import Literal

UseCase =  Literal["wildlife photography", "portrait photography", "action photography"]

class Product(BaseModel):
    id: int
    name: str
    description: str
    pros: list[str]
    cons: list[str]
    use_case: UseCase
    specification: dict[str, str]
    price: float

