#!/bin/bash

# Exit on error
set -e

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn server
gunicorn azure_project.wsgi --workers 4 --threads 2 --worker-class sync --worker-tmp-dir /dev/shm --bind 0.0.0.0:8000
