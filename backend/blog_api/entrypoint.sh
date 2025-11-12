#!/bin/bash
set -e

echo "Running migrations..."
alembic upgrade head

echo "Starting gunicorn"
exec gunicorn --bind 0.0.0.0:3838 blog_api.wsgi:app