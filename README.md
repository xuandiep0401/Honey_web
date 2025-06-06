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
