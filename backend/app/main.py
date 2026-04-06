from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import analysis, history, auth

app = FastAPI(title="BiasLens API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(analysis.router, tags=["analysis"])
app.include_router(history.router, tags=["history"])


@app.get("/health")
def health():
    return {"status": "ok"}
