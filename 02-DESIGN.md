# Task Manager Application - Technical Design

## Architecture Diagram

## Database Schema

### Users Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | SERIAL | PRIMARY KEY |
| username | VARCHAR(80) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(200) | NOT NULL |
| created_at | TIMESTAMP | DEFAULT NOW() |

### Tasks Table
| Column | Type | Constraints |
|--------|------|-------------|
| id | SERIAL | PRIMARY KEY |
| title | VARCHAR(200) | NOT NULL |
| description | VARCHAR(500) | |
| completed | BOOLEAN | DEFAULT FALSE |
| user_id | INTEGER | FOREIGN KEY → users.id |
| created_at | TIMESTAMP | DEFAULT NOW() |
| updated_at | TIMESTAMP | DEFAULT NOW() |

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | /api/register | No | Create new user |
| POST | /api/login | No | Authenticate user |
| GET | /api/tasks | Yes | Get all user tasks |
| POST | /api/tasks | Yes | Create new task |
| PUT | /api/tasks/{id} | Yes | Update task |
| DELETE | /api/tasks/{id} | Yes | Delete task |
| GET | /health | No | Health check |

## Technology Stack

### Backend
- Flask 3.0 - Web framework
- Flask-SQLAlchemy - ORM
- Flask-JWT-Extended - Authentication
- Flask-CORS - Cross-origin requests
- Bcrypt - Password hashing
- Pytest - Testing

### Frontend
- React 18 - UI framework
- Axios - HTTP client
- React Router - Navigation
- Tailwind CSS - Styling
- React Hook Form - Form handling

### DevOps
- Git (feature branch workflow)
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- AWS ECS/EC2 (Deployment)
- PostgreSQL (Production database)
