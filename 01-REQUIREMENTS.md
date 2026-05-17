# Task Manager Application - Requirements Document

## Project Overview
A full-stack task management application demonstrating junior software engineering skills.

## Functional Requirements

### User Management
- [FR-01] User can register with username and password
- [FR-02] User can login with existing credentials
- [FR-03] User receives JWT token upon successful login
- [FR-04] User session persists until logout or token expiry

### Task Management
- [FR-05] User can view all their tasks
- [FR-06] User can create a new task with title and description
- [FR-07] User can edit existing task title and description
- [FR-08] User can mark task as complete/incomplete
- [FR-09] User can delete a task
- [FR-10] User cannot see other users' tasks

### UI/UX
- [FR-11] Clean, responsive interface (mobile + desktop)
- [FR-12] Visual feedback for all actions (loading, success, error)
- [FR-13] Form validation before submission

## Non-Functional Requirements

### Performance
- [NFR-01] API response time < 200ms for 95% of requests
- [NFR-02] Page load time < 2 seconds

### Security
- [NFR-03] Passwords never stored in plain text (bcrypt hashing)
- [NFR-04] JWT tokens expire after 24 hours
- [NFR-05] CORS properly configured for frontend origin

### Reliability
- [NFR-06] 99.9% uptime for deployed application
- [NFR-07] Graceful error handling with meaningful messages

### Maintainability
- [NFR-08] Clear code comments and documentation
- [NFR-09] Consistent code style (PEP8 for Python, Airbnb for React)
- [NFR-10] Unit test coverage > 80%

## Technical Constraints
- Backend: Python 3.13+ with Flask
- Frontend: React 18+ with Tailwind CSS
- Database: PostgreSQL 15+
- Authentication: JWT
- Deployment: Docker + AWS ECS/EC2
