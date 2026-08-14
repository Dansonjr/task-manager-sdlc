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
