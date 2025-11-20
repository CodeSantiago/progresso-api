Progresso API

A habit-tracking REST API built with FastAPI + PostgreSQL + JWT Authentication

Progresso API is a backend system designed to help users create habits, track daily completions, and calculate streaks.
It includes user authentication, secure JWT-based sessions, and a clean service-oriented architecture.

Features
Authentication

User registration

Login with JWT

Protected routes using token-based auth

Secure password hashing with bcrypt

Habits

Create, update, delete habits

List habits owned by the authenticated user

Structured input/output through Pydantic schemas

Habit Logs

Mark a habit as completed for a selected date (or today by default)

Prevent duplicate logs

Retrieve all logs per habit

Streak Calculation

Current streak (today → backwards)

Maximum historical streak

Fully computed server-side

Architecture

Organized in a clean, scalable structure:

app/
│── api/          # Route definitions
│── core/         # Security, auth utilities
│── db/           # Database connection + session
│── models/       # SQLAlchemy ORM models
│── schemas/      # Pydantic models
│── services/     # Business logic
│── main.py       # FastAPI entrypoint

Tech Stack

FastAPI

PostgreSQL

SQLAlchemy

Pydantic

JWT Authentication

bcrypt

Railway Deployment

Installation (Local Development)
1️ Clone the repo
git clone https://github.com/CodeSantiago/progresso-api.git
cd progresso-api

2️ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️ Install dependencies
pip install -r requirements.txt

4️ Set environment variables

Create a .env file:

DATABASE_URL=postgresql://user:password@localhost:5432/progresso
SECRET_KEY=your_secret_key_here

5️ Run FastAPI server
uvicorn app.main:app --reload

Deployment (Railway)

This project is fully configured to deploy on Railway.
You will need:

Procfile with uvicorn start command

Environment variables set in the Railway dashboard

PostgreSQL service connected

Railway automatically builds and deploys on every push to GitHub.

API Documentation

Once running, visit:

http://localhost:8000/docs


or production URL if deployed on Railway.

Authentication Flow

User registers with email + password

User logs in → receives JWT access token

Every protected request sends:

Authorization: Bearer <token>

Example Requests
Register
POST /auth/register
{
  "email": "user@example.com",
  "password": "example123"
}

Login
POST /auth/login
{
  "email": "user@example.com",
  "password": "example123"
}

Create Habit
POST /habits/
Authorization: Bearer <token>
{
  "name": "Read",
  "description": "Read 20 minutes"
}

Mark Completion
POST /habits/1/log
Authorization: Bearer <token>
{
  "completion_date": "2025-11-20"
}

Author

Santiago López
Project built from scratch while learning backend architecture, authentication, and cloud deployment.
Guided step by step with the goal of building production-ready APIs.

Contributions

This project is personal learning, but improvements, suggestions, and pull requests are welcome.

📄 License

MIT License.
