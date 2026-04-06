"""Tests for the inference service layer (mocks the ML pipeline)."""
from unittest.mock import patch

from app.services.inference import run


def test_run_returns_expected_keys():
    mock_result = {
        "bias": "center",
        "bias_score": 0.5,
        "sentiment": "neutral",
        "sentiment_score": 0.6,
    }
    with patch("app.services.inference._get_pipeline") as mock_get:
        mock_get.return_value.run.return_value = mock_result
        result = run("Some article text here.")

    assert set(result.keys()) == {"bias", "bias_score", "sentiment", "sentiment_score"}
    assert result["bias"] in ("left", "center", "right")
