#!/bin/bash
# Don't exit on error for migrations - app should still start
APP_DIR="$(cd "$(dirname "$0")" && pwd)"

export PYTHONPATH=$APP_DIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=azure_project.settings
cd "$APP_DIR"

# Try to run migrations but don't fail if they don't work
python manage.py migrate --noinput || true

# Now start gunicorn (exit on error here)
exec gunicorn azure_project.wsgi --workers 4 --threads 2 --worker-class sync --bind 0.0.0.0:${PORT:-8000}
