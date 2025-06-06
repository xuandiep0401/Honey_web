FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=honeyshop.settings

WORKDIR /app

# install build deps for psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends netcat gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
