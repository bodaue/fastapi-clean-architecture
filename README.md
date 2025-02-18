# FastAPI Clean Architecture Template

A modern template for building scalable and maintainable web applications using FastAPI and Clean Architecture principles.

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-009688.svg)](https://fastapi.tiangolo.com)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

## 🎯 Features

- **Clean Architecture** design following Robert C. Martin's principles
- **FastAPI** framework for high-performance API development
- **SQLAlchemy** with async support for database operations
- **JWT-based** authentication
- **Poetry** for dependency management
- **Alembic** for database migrations
- **Docker** support for containerization
- **Pre-commit hooks** for code quality
- **Ruff** for fast Python linting
- **Dependency Injection** using Dishka

## 🏗️ Project Structure

```
src/
├── application/          # Application business rules
│   ├── interactors/     # Use cases
│   ├── interfaces/      # Abstract interfaces
│   └── validators.py    # Validation rules
├── domain/              # Enterprise business rules
│   ├── entities/        # Business entities
│   └── exceptions.py    # Domain exceptions
├── infrastructure/      # External frameworks and tools
│   ├── adapters/        # Implementation of interfaces
│   └── database/        # Database related code
├── main/               # Application configuration
│   ├── ioc/            # Dependency injection setup
│   └── config.py       # Configuration management
└── presentation/       # Controllers and exception handlers
    └── controllers/    # API endpoints
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
poetry run uvicorn src.main.app:create_application --reload
```

#### Using Docker:
```bash
docker-compose up -d
```

## 🔒 Authentication

The template includes JWT-based authentication with the following features:
- User registration
- User login
- Access token generation
- Password hashing using bcrypt

## 📝 Development

### Code Style

The project uses Ruff for code formatting and linting. Pre-commit hooks are configured to ensure code quality:

```bash
# Install pre-commit hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

### Database Migrations

```bash
# Create a new migration
poetry run alembic revision --autogenerate -m "description"

# Apply migrations
poetry run alembic upgrade head

# Rollback migration
poetry run alembic downgrade -1
```

## 🧪 Testing

```bash
# Run tests
poetry run pytest
```

## 📖 API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔧 Configuration

Configuration is managed through environment variables and pydantic settings. Key configuration options:

- `APPLICATION_TITLE`: Application name
- `APPLICATION_DEBUG`: Debug mode flag
- `JWT_SECRET_KEY`: Secret key for JWT tokens
- `JWT_ALGORITHM`: Algorithm for JWT tokens
- `POSTGRES_*`: Database connection settings
