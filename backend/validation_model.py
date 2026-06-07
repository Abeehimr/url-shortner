from pydantic import BaseModel
from datetime import datetime

class LongUrl(BaseModel):
    url: str


class UrlMapBase(BaseModel):
    id: int
    url: str
    shortcode: str
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True

class UrlMapResponse(UrlMapBase):
    pass  # no access_count

class UrlMapStats(UrlMapBase):
    accessCount: int  # only exposed here