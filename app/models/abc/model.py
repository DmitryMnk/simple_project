from typing import Dict, Any
import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func


class BaseABCModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        attrs = ', '.join(f'{key} = {value}' for key, value in self.to_dict().items())
        return f'{self.__class__.__name__}({attrs})'

    def to_dict(self) -> Dict[str, Any]:
        return {
            field.name: getattr(self, field.name)
            for field in self.__table__.columns #noqa
        }

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=False), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=False), default=func.now(), onupdate=datetime.datetime.now(), nullable=False
    )
