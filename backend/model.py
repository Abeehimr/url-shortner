from backend.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, text
from sqlalchemy.sql import func


class urlmap(Base):
    __tablename__ = "urlmap"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    url = Column(String,nullable=False)
    shortcode = Column(String,nullable=False,unique=True,index=True)
    accessCount = Column(Integer,nullable=False,default=0)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    updatedAt = Column(DateTime, nullable=False, default=func.now())