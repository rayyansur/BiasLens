import numpy as np
from scipy.spatial.distance import cosine
from scipy.special import kl_div


def drift_score(a: dict, b: dict) -> float:
    """Compute narrative drift between two analysis result dicts.

    Args:
        a, b: dicts with keys bias_score, sentiment_score (and optionally an embedding vector).

    Returns:
        float in [0, 1] where 0 = identical framing, 1 = maximally opposed.
    """
    # Cosine distance between bias score vectors
    bias_vec_a = np.array([a["bias_score"]])
    bias_vec_b = np.array([b["bias_score"]])
    bias_dist = cosine(bias_vec_a, bias_vec_b) if np.any(bias_vec_a) and np.any(bias_vec_b) else 0.0

    # KL divergence between sentiment distributions (treat score as a 2-class distribution)
    def sentiment_dist(score: float) -> np.ndarray:
        p = max(min(score, 1 - 1e-9), 1e-9)
        return np.array([p, 1 - p])

    p = sentiment_dist(a["sentiment_score"])
    q = sentiment_dist(b["sentiment_score"])
    kl = float(np.sum(kl_div(p, q)))
    kl_norm = min(kl / 10.0, 1.0)  # normalize to [0, 1]

    # Embedding similarity placeholder (returns 0 until embeddings are wired up)
    embed_dist = 0.0
    if "embedding" in a and "embedding" in b:
        embed_dist = cosine(np.array(a["embedding"]), np.array(b["embedding"]))

    score = (bias_dist * 0.4 + kl_norm * 0.3 + embed_dist * 0.3)
    return float(np.clip(score, 0.0, 1.0))
