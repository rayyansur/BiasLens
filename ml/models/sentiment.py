"""Sentiment analysis model wrapper."""
from transformers import pipeline as hf_pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"


class SentimentModel:
    def __init__(self):
        self._pipe = hf_pipeline("text-classification", model=MODEL_NAME, top_k=None)

    def predict(self, text: str) -> tuple[str, float]:
        """Return (sentiment_label, score)."""
        results = self._pipe(text, truncation=True, max_length=512)[0]
        top = max(results, key=lambda r: r["score"])
        label_map = {"LABEL_0": "negative", "LABEL_1": "neutral", "LABEL_2": "positive"}
        label = label_map.get(top["label"], "neutral")
        return label, round(top["score"], 4)
