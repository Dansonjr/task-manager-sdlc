# Task Manager — SDLC Example

Full-stack Task Manager demonstrating SDLC best practices: Flask backend, React + TypeScript frontend, and PostgreSQL persistence. This repository implements user authentication and task CRUD and is structured as a learning / portfolio project with development and deployment guidance.

## Quick summary
- Purpose: A small, maintainable task-tracking web app intended as an SDLC example (requirements, design, implementation, and project board included).
- Primary users: Developers and reviewers who want a full-stack example using Flask, React and PostgreSQL.

## Features
- User registration and authentication
- Create, read, update, delete tasks
- Task ownership tied to users
- React TypeScript frontend with Tailwind for styling

## Tech stack
- Frontend: React (TypeScript), Tailwind CSS, PostCSS
- Backend: Flask (Python), SQL-backed models (Postgres)
- Dev tooling: npm / node for frontend, Python venv for backend

## Repository layout
```
01-REQUIREMENTS.md                  project requirements
02-DESIGN.md                        architecture and design notes
03-PROJECT-BOARD.md                 planning and board
backend/                            Flask backend
  run.py                            simple app entrypoint
  requirements.txt                  python deps
  app/__init__.py                   application factory / config
  routes/                           HTTP endpoints
    auth.py                         authentication endpoints
    tasks.py                        task CRUD endpoints
  models/                           data models
    user.py                         User model
    task.py                         Task model
frontend/                           React + TypeScript frontend
  package.json                      npm scripts & dependencies
  README.md                         frontend notes
  src/                              React source
    index.tsx                       app entry
    App.tsx                         top-level React component
    components/                     reusable UI components (Auth, TaskList)
    services/                       API client wrappers
```

## Quick start (development)

Prerequisites:
- Python 3.9+ and pip
- Node 16+ and npm (or yarn)
- PostgreSQL running locally or accessible remotely

Backend
```bash
# from repo root
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt

# set environment variables (examples)
export DATABASE_URL="postgresql://user:pass@localhost:5432/taskdb"
export FLASK_ENV=development
export FLASK_APP=backend/run.py

# run the backend
python backend/run.py
```

Frontend
```bash
cd frontend
npm install
npm start
```

Open http://localhost:3000 (frontend) and the React app will connect to the backend API (configure API base URL in frontend/src/services).

## Environment variables / configuration
- DATABASE_URL: PostgreSQL connection string used by the backend (e.g. `postgresql://user:pass@host:5432/dbname`)
- FLASK_ENV / FLASK_APP: standard Flask env vars for development
- SECRET_KEY (recommended): application secret for session signing or token generation (inspect backend/app/__init__.py for exact name)
- FRONTEND_API_BASE (optional): if frontend expects a base URL (check frontend/src/services to confirm)

## Database
This repo currently has models under `backend/models/` (task.py, user.py). I did not find a migrations folder (alembic/) in the repository — add migrations or managed schema scripts before running in production.

Suggested local DB steps:
```bash
# create DB and user in Postgres
createdb taskdb
# run a script / ORM migration to create tables (or use psql and the schema in models)
```

## Tests
- Frontend: App.test.tsx present — frontend unit tests run via `npm test` in `frontend`.
- Backend: no explicit pytest suite found; add tests/ and CI to run them.

## Development & contribution guidance
- Follow the design and requirements docs (01-REQUIREMENTS.md, 02-DESIGN.md) when adding features.
- Add database migrations (Alembic) and document the migration workflow.
- Add unit and integration tests for backend endpoints and model behavior.
- Improve authentication: use hashed passwords (bcrypt) and JWT or session management with proper expiry.
- Add a Dockerfile and docker-compose for local environment parity.

## Roadmap / recommended next steps
1. Add migrations (Alembic) and seed scripts.
2. Harden auth: password hashing, input validation, rate limits, token expiry.
3. Add tests and GitHub Actions CI (lint, tests, build). Use `backend/requirements.txt` and `frontend/package.json` scripts.
4. Add docker-compose for local dev (postgres, backend, frontend) and a production deployment manifest.
5. Add API docs (OpenAPI / Swagger) and front-end API error handling.

## FAQs / pointers
- Where is the API base URL? Check `frontend/src/services` for the client implementation and where the base URL is read (env file / hard-coded).
- Where are migrations? Not present; add Alembic or a SQL schema.
- How to seed data? Add a small `scripts/seed.py` or SQL file.

## License
Specify a license file (e.g., MIT) if you want to make the project open-source and reusable.

## Contact
Repository owner: @Dansonjr

---

If you'd like, I can:
- Commit this README to the repository now.
- Add a docker-compose.yml to simplify local setup.
- Create an Alembic migrations skeleton and an initial migration based on the models.
