"""HuggingFace model wrapper for political bias classification."""
from transformers import pipeline as hf_pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

LABEL_MAP = {
    "LABEL_0": "left",
    "LABEL_1": "center",
    "LABEL_2": "right",
}


class BiasClassifier:
    def __init__(self):
        self._pipe = hf_pipeline("text-classification", model=MODEL_NAME, top_k=None)

    def predict(self, text: str) -> tuple[str, float]:
        """Return (bias_label, score) for the top predicted class."""
        results = self._pipe(text, truncation=True, max_length=512)[0]
        top = max(results, key=lambda r: r["score"])
        label = LABEL_MAP.get(top["label"], "center")
        return label, round(top["score"], 4)
