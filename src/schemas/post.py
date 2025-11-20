from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostRequest(BaseModel):
    content: str

class PostResponse(BaseModel):
    id: str
    content: str
    created_at: datetime
    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None
    category: Optional[str] = None
    category_score: Optional[float] = None
    analyzed_at: Optional[datetime] = None