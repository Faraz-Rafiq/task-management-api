# Task Management API

Production-style REST API built with FastAPI and PostgreSQL.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- JWT Authentication
- Docker

## Setup
1. Clone the repo
2. Copy `.env.example` to `.env` and fill values
3. Run `docker-compose up -d`
4. Run `alembic upgrade head`
5. Run `uvicorn app.main:app --reload`
6. Visit `http://localhost:8000/docs`

## Features
- Task CRUD (create, read, update, delete)
- Filtering by status and priority
- User registration and login
- JWT authentication
- Alembic migrations