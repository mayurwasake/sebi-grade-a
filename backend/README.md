# Backend

FastAPI service backed by PostgreSQL. Runtime configuration is supplied through environment variables; copy `.env.example` to `.env` and set a strong `POSTGRES_PASSWORD` before starting the database.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
Copy-Item .env.example .env
```

Change the sample password before using this outside local development. Keep `POSTGRES_PASSWORD` and the password in `DATABASE_URL` in sync. Then:

```powershell
docker compose up -d postgres
alembic upgrade head
python -m app.scripts.seed_syllabus
uvicorn app.main:app --reload
```

The PostgreSQL container listens on host port `5433` (container port `5432`) to avoid conflicts with a local PostgreSQL installation. The API docs are available at `/docs`; health is available at `/api/v1/health`. The seeded catalog is available at `GET /api/v1/syllabus/2025/IT`.

## Project layout

- `app/api`: versioned HTTP routes
- `app/core`: configuration and shared settings
- `app/db`: SQLAlchemy setup and session lifecycle
- `app/models`: persistence models
- `app/schemas`: API request and response contracts
- `alembic`: database migration history
- `catalog`: versioned source syllabus data used by the seed command

All persistent application data belongs in PostgreSQL. The frontend must treat the API as the source of truth.
