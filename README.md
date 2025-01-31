# FastAPI Template

This is a template for a backend API built with FastAPI, SQLAlchemy, Alembic, and PostgreSQL. The project is
containerized using Docker, making it easy to deploy and manage.

## Technologies:

- Python
    - FastAPI
    - SQLAlchemy
    - Alembic
- PostgreSQL
- Docker

## Project Structure

```bash

├── alembic/                 # Alembic configurations and migrations
├── app/
│   ├── api/                 # API routes
│   ├── db/                  # Database session, entities and repositories
│   ├── services/            # Services layer
│   ├── config.py            # Settings
│   ├── main.py              # Main entry point of the application
│   └── __init__.py
├── alembic.ini              # Alembic configuration file
├── docker-compose.yml       # Docker Compose file for setting up the containers
├── Dockerfile               # Dockerfile for building the app's Docker image
├── pyproject.toml           # Poetry configuration file
├── poetry.lock              # Poetry lock file with exact package versions
└── README.md                # This file

```

## Getting Started

- Clone the repository

```bash
  git clone https://github.com/yourusername/fastapi-template.git
  
  cd fastapi-template
```

- Set up environment variables (.env)
    - Rename .env.example to .env
    - Configure it

- Build and run the containers
```bash
  docker-compose up --build
```