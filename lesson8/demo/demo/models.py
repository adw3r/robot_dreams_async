from sqlalchemy.orm import Mapped, mapped_column

from .db import Base

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[float]
    tax: Mapped[float | None]