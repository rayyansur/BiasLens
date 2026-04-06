from datetime import datetime
from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    text: str


class AnalysisResult(BaseModel):
    id: int
    bias: str
    bias_score: float
    sentiment: str
    sentiment_score: float
    created_at: datetime

    model_config = {"from_attributes": True}
