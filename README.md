# HoneyShop

This project is a demo e-commerce site for selling honey built with Django Oscar.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # update values
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Apps

- `landing` – homepage.
- `blog` – simple blog.
- `chat` – integration point for live chat.
- `memberships` – membership logic.
- `loyalty` – loyalty points.

Run tests with:

```bash
pytest
```

## Docker & Docker Compose

1. Copy `.env.example` to `.env` and adjust variables as needed.
   Ensure `USE_POSTGRES=True` so the project connects to PostgreSQL.
2. Build and start the containers:

```bash
docker-compose up --build
```

The `web` service waits for PostgreSQL, runs migrations, collects static files and serves the site on port 8000.

Visit <http://localhost:8000> to view the application. Stop the stack with `docker-compose down`.

To run management commands:

```bash
docker-compose run web python manage.py <command>
```
