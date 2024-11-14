import datetime

from sqlalchemy.orm import Mapped, mapped_column

from models import BaseABCModel
from sqlalchemy import String, Date


class Product(BaseABCModel):

    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(String(128), nullable=False)
    sale_date: Mapped[datetime.date] = mapped_column(Date())
