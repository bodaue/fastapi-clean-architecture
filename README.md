# FastAPI Clean Architecture Template

A modern template for building scalable and maintainable web applications using FastAPI following Clean Architecture
principles.

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688.svg)](https://fastapi.tiangolo.com)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

## 🎯 Features

- **Clean Architecture** design
- **SOLID** principles implementation with focus on Dependency Inversion
- **FastAPI** framework for high-performance API development
- **Session-based authentication** with secure password handling
- **SQLAlchemy** with async support for database operations
- **Dishka** for dependency injection
- **Alembic** for database migrations
- **Poetry** for dependency management
- **Docker** support for containerization
- **Pre-commit hooks** with Ruff for code quality

## 🏗️ Project Structure

```
src/
├── application/          # Application business rules
│   ├── interactors/      # Use cases implementation
│   ├── interfaces/       # Abstract interfaces (ports)
│   └── validators.py     # Validation rules
├── domain/               # Enterprise business rules
│   ├── entities/         # Business entities
│   └── exceptions.py     # Domain exceptions
├── infrastructure/       # External frameworks and tools
│   ├── adapters/         # Implementation of interfaces (adapters)
│   └── database/         # Database related code (SQLAlchemy)
├── main/                 # Application configuration
│   ├── ioc/              # Dependency injection setup
│   └── config.py         # Configuration management
└── presentation/         # Controllers and exception handlers
    └── controllers/      # API endpoints
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Poetry
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-clean-architecture.git
cd fastapi-clean-architecture
```

2. Install dependencies:

```bash
poetry install
```

3. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run migrations:

```bash
poetry run alembic upgrade head
```

### Running the Application

#### Using Poetry:

```bash
poetry run uvicorn src.main.app:create_application --factory
```

#### Using Docker:

```bash
docker-compose up -d
```

## 🔒 Authentication

The template includes session-based authentication with the following features:

- User registration with email and password
- Password validation and secure hashing with bcrypt
- User login with session creation
- Session management (creation, validation, deactivation)
- Integration with request handling

## 📖 API Documentation

Once the application is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔧 Configuration

Configuration is managed through environment variables and pydantic settings. Key configuration options:

- `APPLICATION_TITLE`: Application name
- `APPLICATION_DEBUG`: Debug mode flag
- `SESSION_*`: Session settings
- `POSTGRES_*`: Database connection settings
- `REDIS_*`: Redis connection settings

## 🧪 Architecture

This template strictly adheres to the Clean Architecture principles:

1. **Independence of frameworks**: Business logic is independent of the delivery mechanism (FastAPI)
2. **Testability**: Business rules can be tested without external elements
3. **Independence of UI**: The API can change without changing the business rules
4. **Independence of database**: You can swap SQLAlchemy for another ORM
5. **Independence of external agencies**: Business rules don't know about the outside world

The dependency flow follows the Dependency Inversion Principle:

- Domain layer has no dependencies
- Application layer depends only on the Domain layer
- Infrastructure and Presentation layers depend on the Application layer interfaces