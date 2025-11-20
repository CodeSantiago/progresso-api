Progresso API

Progresso API is a REST backend built with FastAPI and PostgreSQL.
It provides user authentication, habit management, daily log tracking, and streak calculations.
The project follows a modular and scalable architecture, suitable for learning or production use.
1. Features
1.1 Authentication

User registration

Login with JWT tokens

Token-based route protection

Secure password hashing with bcrypt

1.2 Habits

Create habits

Update habits

Delete habits

List habits per user

1.3 Habit Logs

Mark a habit as completed for a specific date (or today)

Prevent duplicate logs

Retrieve all logs for a habit

1.4 Streaks

Current streak calculation

Maximum historical streak

Based on consecutive daily completions

2. Project Structure
app/
│── api/          # Route definitions (auth, habits, logs, stats)
│── core/         # JWT, security utilities
│── db/           # Database session and engine
│── models/       # SQLAlchemy ORM models
│── schemas/      # Pydantic input/output schemas
│── services/     # Business logic
│── main.py       # FastAPI application entrypoint


This architecture separates concerns clearly and allows future expansion without rewriting core components.

3. Tech Stack

FastAPI

PostgreSQL

SQLAlchemy ORM

Pydantic

JWT Authentication

bcrypt

Railway (deployment)

4. Local Installation
4.1 Clone the repository
git clone https://github.com/CodeSantiago/progresso-api.git
cd progresso-api

4.2 Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

4.3 Install dependencies
pip install -r requirements.txt

4.4 Create the .env file
DATABASE_URL=postgresql://user:password@localhost:5432/progresso
SECRET_KEY=your_secret_key_here

4.5 Run the API locally
uvicorn app.main:app --reload

5. API Documentation

Once running, visit:

http://localhost:8000/docs


Interactive API documentation is available through Swagger UI.

6. Authentication Flow

User registers with email and password

User logs in and receives an access token

Protected routes require:

Authorization: Bearer <token>

7. Example Requests
7.1 User Registration
POST /auth/register
{
  "email": "user@example.com",
  "password": "example123"
}

7.2 Login
POST /auth/login
{
  "email": "user@example.com",
  "password": "example123"
}

7.3 Create Habit
POST /habits/
Authorization: Bearer <token>
{
  "name": "Read",
  "description": "Read 20 minutes"
}

7.4 Mark Habit Completion
POST /habits/1/log
Authorization: Bearer <token>
{
  "completion_date": "2025-11-20"
}

8. Deployment (Railway)

Progresso API is configured for deployment on Railway. For a successful deployment:

Add the environment variables in Railway:

DATABASE_URL

SECRET_KEY

Include the Procfile at the project root:

web: uvicorn app.main:app --host 0.0.0.0 --port $PORT


Deploy automatically from GitHub on each push.

9. Author

Santiago López
Progresso API was built as a full backend learning project, including architecture, authentication, database design and deployment.

10. License

MIT License.
