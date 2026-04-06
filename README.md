# BiasLens 2.0

Full-stack ML system for detecting political bias, sentiment, and narrative framing in text.

The core differentiator is **narrative drift tracking** — monitoring how the same story is framed
differently across sources and over time.

## Stack

| Layer | Tech |
|---|---|
| Backend API | FastAPI + SQLAlchemy + Alembic |
| ML Pipeline | HuggingFace Transformers (PyTorch) |
| Database | PostgreSQL |
| Frontend | Next.js 14 (App Router) + Tailwind CSS + shadcn/ui |
| Browser Extension | Chrome MV3 |
| Infrastructure | Docker Compose |

## Architecture

```
Browser Extension
       │  POST /analyze (text payload)
       ▼
FastAPI Backend ──► services/inference.py ──► ML Pipeline (HuggingFace)
       │
       ▼
  PostgreSQL
       │
       ▼
Next.js Dashboard  (fetches via /history, /analysis/{id})
```

## Quickstart

### 1. Environment

```bash
cp .env.example .env
# Fill in DATABASE_URL, SECRET_KEY, ML_SERVICE_URL, NEWSAPI_KEY, ALLOWED_ORIGINS
```

### 2. Docker (recommended)

```bash
docker compose up --build
```

- API: http://localhost:8000
- Dashboard: http://localhost:3000

### 3. Manual dev setup

**Backend:**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
python -m app.db.seed          # optional: seed dev data
uvicorn app.main:app --reload --port 8000
```

**ML Pipeline:**
```bash
cd ml
# Download model checkpoints — see ml/README.md
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev     # localhost:3000
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/analyze` | Submit text for bias + sentiment analysis |
| GET | `/analysis/{id}` | Fetch a single analysis result |
| GET | `/history` | Paginated analysis history |
| POST | `/login` | Obtain JWT access + refresh tokens |
| POST | `/register` | Create a new user account |
| POST | `/refresh` | Exchange refresh token for new access token |

## What is Narrative Drift?

The drift score is a float `[0, 1]` that measures how differently two sources frame the same story:

- **0** — identical framing
- **1** — maximally opposed framing

It combines cosine distance between bias score vectors, KL divergence between sentiment distributions,
and embedding similarity of the article bodies. Computed in `backend/app/services/narrative.py`.

## Project Layout

```
biaslens/
├── backend/          FastAPI app, ORM models, migrations, tests
├── ml/               HuggingFace model wrappers, training & ingestion scripts
├── frontend/         Next.js dashboard
├── extension/        Chrome MV3 extension
├── docker-compose.yml
└── .env.example
```

See [CLAUDE.md](CLAUDE.md) for full file-level layout and development conventions.

## Known Limitations

- Bias classifier (`cardiffnlp/twitter-roberta-base-sentiment`) was trained on Twitter data and
  degrades on long-form journalism. Fine-tuning is planned.
- Narrative drift currently compares article pairs only. Cross-source trending (3+ sources) is not
  yet implemented.
- Chrome extension has a hard 30s API timeout.
