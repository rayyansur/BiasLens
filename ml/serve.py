"""ML inference microservice.

Exposes POST /predict so the FastAPI backend can call it over HTTP.
The pipeline singleton is loaded once at startup — never per request.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel

from ml.models.pipeline import get_pipeline


class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    bias: str
    bias_score: float
    sentiment: str
    sentiment_score: float


_pipeline = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _pipeline
    _pipeline = get_pipeline()  # warm up at startup
    yield


app = FastAPI(title="BiasLens ML Service", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(body: PredictRequest):
    result = _pipeline.run(body.text)
    return result
