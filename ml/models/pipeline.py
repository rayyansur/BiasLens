"""Unified inference pipeline — singleton loaded once at startup."""
from ml.models.bias_classifier import BiasClassifier
from ml.models.sentiment import SentimentModel

MAX_TOKENS = 512


class Pipeline:
    def __init__(self):
        self.bias_classifier = BiasClassifier()
        self.sentiment_model = SentimentModel()

    def run(self, text: str) -> dict:
        """Run bias and sentiment inference on text.

        Args:
            text: Raw article or passage text.

        Returns:
            {"bias": str, "bias_score": float, "sentiment": str, "sentiment_score": float}
        """
        # Preprocessing (truncation) happens here, not in callers.
        truncated = self._truncate(text)

        bias, bias_score = self.bias_classifier.predict(truncated)
        sentiment, sentiment_score = self.sentiment_model.predict(truncated)

        return {
            "bias": bias,
            "bias_score": bias_score,
            "sentiment": sentiment,
            "sentiment_score": sentiment_score,
        }

    @staticmethod
    def _truncate(text: str, max_words: int = MAX_TOKENS) -> str:
        words = text.split()
        return " ".join(words[:max_words])


# Module-level singleton — do not re-initialize per request.
_instance: Pipeline | None = None


def get_pipeline() -> Pipeline:
    global _instance
    if _instance is None:
        _instance = Pipeline()
    return _instance
