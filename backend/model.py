from backend.db import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func


class urlmap(Base):
    __tablename__ = "urlmap"
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    url:Mapped[str] = mapped_column(String)
    shortcode: Mapped[str] = mapped_column(String, unique=True, index=True)
    accessCount: Mapped[int] = mapped_column(Integer, default=0)
    createdAt: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now())
    updatedAt: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=func.now())

    def __abs__(self):
        return f"shortcode: {self.shortcode} -> url: {self.url}"