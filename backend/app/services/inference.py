import httpx

from app.core.config import settings

# Import mode: used when ML_SERVICE_URL is not configured.
_pipeline = None


def _get_pipeline():
    global _pipeline
    if _pipeline is None:
        from ml.models.pipeline import Pipeline
        _pipeline = Pipeline()
    return _pipeline


def run(text: str) -> dict:
    """Call the ML layer and return a structured result dict.

    Returns:
        {"bias": str, "bias_score": float, "sentiment": str, "sentiment_score": float}
    """
    if settings.ml_service_url:
        response = httpx.post(
            f"{settings.ml_service_url}/predict",
            json={"text": text},
            timeout=30.0,
        )
        response.raise_for_status()
        return response.json()

    return _get_pipeline().run(text)
