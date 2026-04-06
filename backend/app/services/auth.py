from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from app.core.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7


def _make_token(subject: int, expire: timedelta, token_type: str) -> str:
    payload: dict[str, Any] = {
        "sub": str(subject),
        "type": token_type,
        "exp": datetime.now(timezone.utc) + expire,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def create_access_token(user_id: int) -> str:
    return _make_token(user_id, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), "access")


def create_refresh_token(user_id: int) -> str:
    return _make_token(user_id, timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS), "refresh")


def _decode(token: str, expected_type: str) -> dict | None:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        if payload.get("type") != expected_type:
            return None
        return payload
    except JWTError:
        return None


def decode_access_token(token: str) -> dict | None:
    return _decode(token, "access")


def decode_refresh_token(token: str) -> dict | None:
    return _decode(token, "refresh")
