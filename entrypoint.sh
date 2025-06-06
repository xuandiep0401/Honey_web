#!/usr/bin/env bash
set -e

DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}

# wait for PostgreSQL
until nc -z "$DB_HOST" "$DB_PORT"; do
  echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
  sleep 1
done

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn honeyshop.wsgi:application --bind 0.0.0.0:8000 --workers 3
