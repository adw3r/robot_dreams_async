from pydantic import BaseModel, ConfigDict
from pydantic.fields import Field


class Item(BaseModel):
    model_config = ConfigDict(from_attributes=True)


    name: str
    description: str | None = None
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float | None = None