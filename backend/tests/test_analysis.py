"""Tests for POST /analyze and GET /analysis/{id}."""


def test_analyze_requires_auth(client):
    response = client.post("/analyze", json={"text": "some article text"})
    assert response.status_code == 403
